import json
import uuid
from fastapi import FastAPI, Body
from fastapi.responses import StreamingResponse
from redis import asyncio as aredis


redis_client = aredis.Redis.from_url(
    "redis://redis:6379",
    decode_responses=True
)

app = FastAPI()

@app.post(
    "/generate",
    summary="Llama 응답 생성 API",
)
async def generate_chat_handler(
    user_input: str = Body(..., embed=True)
):
    # 채널 ID 발급
    channel_id = str(uuid.uuid4())

    pubsub = redis_client.pubsub()
    await pubsub.subscribe(channel_id)  # 채널 구독

    # Llama 추론 작업 요청 -> Queue 작업 추가
    task = {
        "channel_id": channel_id,  # 결과를 돌려받을 채널 ID
        "user_prompt": user_input,  # 사용자의 질문
    }
    await redis_client.lpush("task_queue", json.dumps(task))

    # =====================
    # 제너레이터 객체: 값을 여러번 반환하는 함수
    async def event_generator():
        async for message in pubsub.listen():
            if message["type"] == "message":
                token = message["data"]
                # 더 이상 수신할 토큰이 없기 때문에 listen 종료
                if token == "[DONE]":
                    break
                yield token

        await pubsub.unsubscribe(channel_id)  # 채널 구독 해제
        await pubsub.close()  # pubsub 연결 종료



    return StreamingResponse(

      event_generator(),
        media_type="text/event-stream"
    )
