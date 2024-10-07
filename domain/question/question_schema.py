import datetime

from pydantic import BaseModel

# question 스키마 생성
class Question(BaseModel):
    id: int
    subject: str
    content: str
    create_date: datetime.datetime