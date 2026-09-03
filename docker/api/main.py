from fastapi import FastAPI, Body


app = FastAPI()

@app.post(
    "/generate",
    summary="Llama 응답 생성 API",
)

def generate_chat_handler(
    user_input: str = Body(..., embed=True)
):
    Llama 추론 작업 요청 -> Queue에 쌓기
    return ...