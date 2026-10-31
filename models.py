from pydantic import BaseModel, Field
from datetime import date as date_type

class ExpenseCreate(BaseModel):
    model_config = {"extra": "forbid"}
    description: str
    amount: float = Field(gt=0)
    date: date_type | None = None

class ExpenseUpdate(BaseModel):
    model_config = {"extra": "forbid"}
    description: str | None = None
    amount: float | None = Field(default=None, gt=0)
    date: date_type | None = None

class ExpenseOut(BaseModel):
    id: int
    description: str
    amount: float
    date: date_type


    