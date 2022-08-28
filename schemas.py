from typing import List, Optional, Generic, TypeVar
from pydantic import BaseModel, Field
from pydantic.generics import GenericModel


#schema=데이터베이스의 자료구조, 자료간의 관계 정립
#일종의 drf 시리얼라이저 같은 역할인듯??

T= TypeVar('T')

class BookSchema(BaseModel):
    id: Optional[int]= None
    title: Optional[str]= None
    description:Optional[str]=None

    class Config:
        orm_mode = True


class RequestBook(BaseModel):
    parameter: BookSchema = Field(...)


class Response(GenericModel, Generic[T]):
    code: str
    status: str
    message: str
    result: Optional[T]
