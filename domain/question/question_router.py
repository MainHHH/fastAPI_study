from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from domain.question import question_schema

from database import get_db
from models import Question

router = APIRouter(
    prefix="/api/question",
)

# with문으로 자동화
# @router.get("/list")
# def question_list():
#     with get_db() as db:
#         _question_list = db.query(Question).order_by(Question.create_date.desc()).all()
#     return _question_list


# Depends으로 자동화
@router.get("/list", response_model=list[question_schema.Question])
def question_list(db: Session = Depends(get_db)):
    _question_list = db.query(Question).order_by(Question.create_date.desc()).all()
    return _question_list