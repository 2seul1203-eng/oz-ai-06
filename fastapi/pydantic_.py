# Pydantic
# 데이터 검증/파싱을 담당하는 라이브러리

from pydantic import BaseModel

class Item(BaseModel):
    name: str
    price: int

class Item2:
    def __init__(self, name, price):
        self.name = name
        self.price = price

# 상품 등록 요청 시 클라이언트가 보내야 하는 데이터 형식
class ItemRegisterRequest(BaseModel):
    name: str
    price: int

# 서버가 응답할 때 사용하는 데이터 형식
class ItemResponse(BaseModel):
    id: int
    name: str
    price: int

