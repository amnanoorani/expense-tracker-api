from fastapi import FastAPI
from models import ExpenseCreate, ExpenseUpdate, ExpenseOut
from handlers import (
    add_expense_handler,
    get_all_expenses_handler,
    get_summary_handler,
    get_monthly_summary_handler,
    get_expense_handler,
    update_expense_handler,
    delete_expense_handler,
)

app = FastAPI(title="Expense Tracker API")


@app.post("/expenses", response_model=ExpenseOut, status_code=201)
def add_expense(expense: ExpenseCreate):
    return add_expense_handler(expense)


@app.get("/expenses", response_model=list[ExpenseOut])
def get_all_expenses():
    return get_all_expenses_handler()


@app.get("/expenses/summary")
def get_summary():
    return get_summary_handler()


@app.get("/expenses/summary/monthly/{month}")
def get_monthly_summary(month: int):
    return get_monthly_summary_handler(month)


@app.get("/expenses/{expense_id}", response_model=ExpenseOut)
def get_expense(expense_id: int):
    return get_expense_handler(expense_id)


@app.put("/expenses/{expense_id}", response_model=ExpenseOut)
def update_expense(expense_id: int, expense: ExpenseUpdate):
    return update_expense_handler(expense_id, expense)


@app.delete("/expenses/{expense_id}")
def delete_expense(expense_id: int):
    return delete_expense_handler(expense_id)