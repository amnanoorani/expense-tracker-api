
from fastapi import HTTPException
from database import get_connection
from psycopg2.extras import RealDictCursor
from models import ExpenseCreate, ExpenseUpdate

def add_expense_handler(expense: ExpenseCreate):
    expense_date = expense.date or date_type.today()

    conn = get_connection()
    try:
        cur = conn.cursor(cursor_factory=RealDictCursor)
        cur.execute(
            "INSERT INTO expenses (description, amount, date) VALUES (%s, %s, %s) RETURNING id, description, amount, date",
            (expense.description, expense.amount, expense_date)
        )
        new_expense = cur.fetchone()
        conn.commit()
        cur.close()
        return new_expense
    except Exception as e:
        conn.rollback()
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        conn.close()

def get_all_expenses_handler():
    conn = get_connection()
    try:
        cur = conn.cursor(cursor_factory=RealDictCursor)
        cur.execute("SELECT id, description, amount, date FROM expenses ORDER BY id")
        rows = cur.fetchall()
        cur.close()
        return rows
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        conn.close()


def get_summary_handler():
    conn = get_connection()
    try:
        cur = conn.cursor(cursor_factory=RealDictCursor)
        cur.execute("SELECT amount FROM expenses")
        rows = cur.fetchall()
        cur.close()

        if len(rows) == 0:
            return {"total_expenses": 0, "total_amount": 0, "average": 0}

        total = sum(float(r["amount"]) for r in rows)
        count = len(rows)
        average = total / count

        return {
            "total_expenses": count,
            "total_amount": round(total, 2),
            "average": round(average, 2)
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        conn.close()        


def get_monthly_summary_handler(month: int):
    if month < 1 or month > 12:
        raise HTTPException(status_code=400, detail="Month must be between 1 and 12")

    conn = get_connection()
    try:
        cur = conn.cursor(cursor_factory=RealDictCursor)
        cur.execute(
            "SELECT description, amount, date FROM expenses WHERE EXTRACT(MONTH FROM date) = %s ORDER BY date",
            (month,)
        )
        rows = cur.fetchall()
        cur.close()

        if len(rows) == 0:
            return {"month": month, "count": 0, "total": 0, "average": 0, "expenses": []}

        total = sum(float(r["amount"]) for r in rows)
        count = len(rows)

        return {
            "month": month,
            "count": count,
            "total": round(total, 2),
            "average": round(total / count, 2),
            "expenses": rows
        }
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        conn.close()



def get_expense_handler(expense_id: int):
    conn = get_connection()
    try:
        cur = conn.cursor(cursor_factory=RealDictCursor)
        cur.execute(
            "SELECT id, description, amount, date FROM expenses WHERE id = %s",
            (expense_id,)
        )
        row = cur.fetchone()
        cur.close()

        if row is None:
            raise HTTPException(status_code=404, detail="Expense not found")

        return row
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        conn.close()


def update_expense_handler(expense_id: int, expense: ExpenseUpdate):
    conn = get_connection()
    try:
        cur = conn.cursor(cursor_factory=RealDictCursor)

        
        cur.execute("SELECT id, description, amount, date FROM expenses WHERE id = %s", (expense_id,))
        existing = cur.fetchone()

        if existing is None:
            cur.close()
            raise HTTPException(status_code=404, detail="Expense not found")

        
        new_description = expense.description if expense.description is not None else existing["description"]
        new_amount = expense.amount if expense.amount is not None else existing["amount"]
        new_date = expense.date if expense.date is not None else existing["date"]

        cur.execute(
            "UPDATE expenses SET description = %s, amount = %s, date = %s WHERE id = %s RETURNING id, description, amount, date",
            (new_description, new_amount, new_date, expense_id)
        )
        updated = cur.fetchone()
        conn.commit()
        cur.close()
        return updated

    except HTTPException:
        raise
    except Exception as e:
        conn.rollback()
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        conn.close()        



def delete_expense_handler(expense_id: int):
    conn = get_connection()
    try:
        cur = conn.cursor(cursor_factory=RealDictCursor)

        cur.execute("SELECT description FROM expenses WHERE id = %s", (expense_id,))
        existing = cur.fetchone()

        if existing is None:
            cur.close()
            raise HTTPException(status_code=404, detail="Expense not found")

        cur.execute("DELETE FROM expenses WHERE id = %s", (expense_id,))
        conn.commit()
        cur.close()

        return {"message": f"Expense '{existing['description']}' deleted successfully"}

    except HTTPException:
        raise
    except Exception as e:
        conn.rollback()
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        conn.close()      