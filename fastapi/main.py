# # HTTP 요청
# # 1) 행위(Action) -> Method
# # 2) 자원(Resource) -> URL

# # GET /hello 요청 -> hello() -> {"msg": "hello"} 응답
# @app.get("/hello")
# def hello_handler():
#     return{"msg": "hello"}

# def add(n1, n2):
#     return n1 + n2

# # /hello/world 경로에 GET 요청을 보냈을 때, 
# # # {"mas": ["hello", "world"]}가 출력 되도록 hello_handler 함수를 수정

# @app.get("/hello/world")
# def hello_handler():
#     return{"mas": ["hello", "world"]}

from fastapi import FastAPI, Path, Query, Body, HTTPException

from pydantic import BaseModel
from pydantic_ import ItemRegisterRequest, ItemResponse
from connection import SessionFactory
from sqlalchemy import select
from model import Item

app = FastAPI()

all_items = []

@app.get(
    "/items",
    summary="전체 상품 조회 API",
    response_model=list[ItemResponse]
)
def get_all_items_handler():
    with SessionFactory() as session:
        stmt = select(Item)
        result = session.execute(stmt)
        items: list[Item] = result.scalars().all()
        return items

# GET /items/search?query=apple
@app.get("/items/search",
         summary="상품 검색 API",
         response_model=list[ItemResponse]
)
def search_item_handler(
    query: str = Query(..., min_length=2)
):
    Session = SessionFactory()
    # 이름에 query 문자열을 포함하고 있는 상품 조회
    try:
        stmt = select(Item).where(Item.name.contains(query))
        result = Session.execute(stmt)
        items = result.scalars().all # 0 ~ N 개
        return items
    finally:
        Session.close()

# Path Parameter
# 1. 다수의 경로를 한 번에 처리하는 API를 만들 때 사용
# 2. 같은 이름의 변수를 핸들러 함수 안으로 전달할 수 있다
# 3. 핸들러 함수로 전달되는 값에 대해서 타입을 지정할 수 있다

# 함수의 매개변수에 기본값을 미리 채워놓을 수 있다
# -> 실제 값이 전달되면, 덮어쓰기
@app.get(
        "/items/{item_id}",
        summary="단일 상품 조회 API",
        response_model=ItemResponse,
) # 경로에 특정 부분을 공통으로 묶어줌
def get_item_handler(
    item_id: int = Path(..., ge=1) # 1 이상인지 검사
):
    with SessionFactory() as session:
        stmt = select(Item).where(Item.id == item_id)
        result = session.execute(stmt)
        item: Item | None = result.scalar() # 0~1개


    if item is None:
        raise HTTPException(
            status_code=404,
            detail="아이템을 찾을 수 없습니다."
    )

# Query Parameter
# ?key = value
# GET /user?name=kim


# 서버에서 요구하는  Item 등록 방식 
class ItemRegisterRequest(BaseModel):
    name: str
    price: int

# 서버에서 응답하기로 약속한 데이터 형식
class ItemRegisterResponse(BaseModel):
    name: str
    price: int


# 전체 상품 조회 API
@app.get(
        "/items",
        summary="전체 상품 조회 API",
         response_model=list[ItemResponse]
)

def get_all_items_handler():
    session = SessionFactory() # 데이터베이스와 연결 유지
    try:

        stmt = select(Item)
        result = session.execute(stmt) # SQL문 실행
        items: list[Item] = result.scalars().all()
        return items
    finally:
        session.close()

# 상품 등록 API
@app.post(
    "/items",
    summary="상품 등록 API",
    response_model=ItemResponse,
)
def register_item_handler(
    # 요청 본문의 형식이 ItemRegisterRequest랑 일치해야 된다
    # 클라이언트는 ItemRegisterRequest에 맞는 데이터를 보내야된다
    body: ItemRegisterRequest
):
    new_item = Item(name=body.name, price=body.price)

    with SessionFactory() as session:
        session.add(new_item) # 메모리의 session 안에 기록
        session.commit() # DB 저장(INSERT INTO...)
        return new_item

class ItemUpdateRequest(BaseModel):
    name: str | None = None
    price: int| None = None

@app.patch(
    "/items/{item_id}",
    summary="상품 수정 API",
    response_model=ItemResponse,
)
def update_item_handler(
    item_id: int = Path(..., ge=1),
    body: ItemUpdateRequest = Body(...),
):
    with SessionFactory() as session:
        stmt = select(Item).where(Item.id == item_id)
        result = session.execute(stmt)
        item: Item | None = result.scalar()

        if item is None:
            raise HTTPException(
                status_code=404,
                detail="아이템을 찾을 수 없습니다."
            )

        # 데이터 수정
        if body.name:
            item.name = body.name

        if body.price:
            item.price = body.price

        session.commit() # UPDATE 쿼리 발생
        return item

@app.delete(
    "/items/{item_id}",
    summary="상품 삭제 API",
    status_code=204,
    response_model=None,
)
def delete_item_handler(
    item_id: int = Path(..., ge=1),
):
    for item in all_items:
        if item["item_id"] == item_id:
            all_items.remove(item)
            return

    raise HTTPException(
        status_code=404,
        detail="아이템을 찾을 수 없습니다."
    )