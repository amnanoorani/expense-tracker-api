import datetime
import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()

DB_NAME = os.environ.get("DB_NAME")
DB_USER = os.environ.get("DB_USER")
DB_PASSWORD = os.environ.get("DB_PASSWORD")
DB_HOST = os.environ.get("DB_HOST")
DB_PORT = os.environ.get("DB_PORT")

def get_connection():
    try:
        conn = psycopg2.connect(
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD,
            host=DB_HOST,
            port=DB_PORT
        )
        return conn
    except Exception as e:
        print(f"Could not connect to database: {e}")
        return None


def show_menu():
    print("\nEXPENSE TRACKER")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. Update Expense")
    print("4. Delete Expense")
    print("5. View Summary")
    print("6. View Monthly Summary")
    print("7. Exit")


def add_expense():
    print("\n--- Add New Expense ---")

    description = input("Enter description: ")

    while True:
        try:
            amount = float(input("Enter amount: "))
            if amount <= 0:
                print("Amount must be greater than 0!")
                continue
            break
        except ValueError:
            print("Please enter a valid number! (e.g. 500 or 500.50)")
        except Exception as e:
            print(f"Error while reading amount: {e}")

    while True:
        date = input("Enter date (YYYY-MM-DD) or press Enter for today: ")
        if date == "":
            date = str(datetime.date.today())
            break
        try:
            datetime.datetime.strptime(date, "%Y-%m-%d")
            break
        except ValueError as e:
            print(f"Error while reading date: {e}")
            print("Please enter the date in YYYY-MM-DD format (e.g. 2026-07-05)")

    conn = get_connection()
    if conn is None:
        return

    try:
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO expenses (description, amount, date) VALUES (%s, %s, %s)",
            (description, amount, date)
        )
        conn.commit()
        cur.close()
        print(f"Expense added: {description} - {amount}")
    except Exception as e:
        print(f"Error while saving expense: {e}")
    finally:
        conn.close()


def view_expenses():
    conn = get_connection()
    if conn is None:
        return

    try:
        cur = conn.cursor()
        cur.execute("SELECT id, description, amount, date FROM expenses ORDER BY id")
        rows = cur.fetchall()
        cur.close()
    except Exception as e:
        print(f"Error while fetching expenses: {e}")
        conn.close()
        return

    conn.close()

    if len(rows) == 0:
        print("\nNo expenses found!")
        return

    print("\nALL EXPENSES")
    print("#   Date        Description          Amount")

    total = 0
    for row in rows:
        expense_id, description, amount, date = row
        print(f"{expense_id}   {date}   {description}   {amount}")
        total = total + float(amount)

    print(f"TOTAL: {total}")


def update_expense():
    view_expenses()

    try:
        expense_id = int(input("\nEnter expense # to update: "))
    except ValueError:
        print("Please enter a valid number!")
        return
    except Exception as e:
        print(f"Error: {e}")
        return

    conn = get_connection()
    if conn is None:
        return

    try:
        cur = conn.cursor()
        cur.execute("SELECT description, amount, date FROM expenses WHERE id = %s", (expense_id,))
        row = cur.fetchone()

        if row is None:
            print("Invalid expense number!")
            cur.close()
            conn.close()
            return

        description, amount, date = row
        print(f"\nUpdating: {description} - {amount}")
        print("Press Enter to keep current value")

        new_desc = input(f"New description (current: {description}): ")
        if new_desc == "":
            new_desc = description

        new_amount_input = input(f"New amount (current: {amount}): ")
        if new_amount_input == "":
            new_amount = amount
        else:
            try:
                new_amount = float(new_amount_input)
                if new_amount <= 0:
                    print("Amount must be positive! Keeping old value.")
                    new_amount = amount
            except ValueError:
                print("Invalid amount! Keeping old value.")
                new_amount = amount

        new_date_input = input(f"New date (current: {date}): ")
        if new_date_input == "":
            new_date = date
        else:
            try:
                datetime.datetime.strptime(new_date_input, "%Y-%m-%d")
                new_date = new_date_input
            except ValueError as e:
                print(f"Error while reading date: {e}")
                print("Keeping old date.")
                new_date = date

        cur.execute(
            "UPDATE expenses SET description = %s, amount = %s, date = %s WHERE id = %s",
            (new_desc, new_amount, new_date, expense_id)
        )
        conn.commit()
        cur.close()
        print("Expense updated successfully!")

    except Exception as e:
        print(f"Error while updating expense: {e}")
    finally:
        conn.close()


def delete_expense():
    view_expenses()

    try:
        expense_id = int(input("\nEnter expense # to delete: "))
    except ValueError:
        print("Please enter a valid number!")
        return
    except Exception as e:
        print(f"Error: {e}")
        return

    conn = get_connection()
    if conn is None:
        return

    try:
        cur = conn.cursor()
        cur.execute("SELECT description FROM expenses WHERE id = %s", (expense_id,))
        row = cur.fetchone()

        if row is None:
            print("Invalid expense number!")
            cur.close()
            conn.close()
            return

        description = row[0]
        confirm = input(f"Delete '{description}'? (y/n): ")

        if confirm.lower() == "y":
            cur.execute("DELETE FROM expenses WHERE id = %s", (expense_id,))
            conn.commit()
            print("Expense deleted!")
        else:
            print("Deletion cancelled.")

        cur.close()

    except Exception as e:
        print(f"Error while deleting expense: {e}")
    finally:
        conn.close()


def view_summary():
    conn = get_connection()
    if conn is None:
        return

    try:
        cur = conn.cursor()
        cur.execute("SELECT amount FROM expenses")
        rows = cur.fetchall()
        cur.close()
    except Exception as e:
        print(f"Error while calculating summary: {e}")
        conn.close()
        return

    conn.close()

    if len(rows) == 0:
        print("\nNo expenses to summarize!")
        return

    total = sum(float(r[0]) for r in rows)
    average = total / len(rows)

    print("\nEXPENSE SUMMARY")
    print(f"Total Expenses: {len(rows)}")
    print(f"Total Amount:   {total}")
    print(f"Average:        {average}")


def view_monthly_summary():
    try:
        month = int(input("Enter month (1-12): "))
        if month < 1 or month > 12:
            print("Invalid month! Must be 1-12.")
            return
    except ValueError:
        print("Please enter a valid number!")
        return
    except Exception as e:
        print(f"Error: {e}")
        return

    conn = get_connection()
    if conn is None:
        return

    try:
        cur = conn.cursor()
        cur.execute(
            "SELECT description, amount, date FROM expenses WHERE EXTRACT(MONTH FROM date) = %s ORDER BY date",
            (month,)
        )
        rows = cur.fetchall()
        cur.close()
    except Exception as e:
        print(f"Error while reading expense dates: {e}")
        conn.close()
        return

    conn.close()

    if len(rows) == 0:
        print(f"\nNo expenses found for month {month}")
        return

    total = sum(float(r[1]) for r in rows)

    print(f"\nSUMMARY FOR MONTH {month}")
    print(f"Number of expenses: {len(rows)}")
    print(f"Total: {total}")
    print(f"Average: {total / len(rows)}")

    print("\nDetails:")
    for description, amount, date in rows:
        print(f"{date} - {description}: {amount}")


def main():
    while True:
        try:
            show_menu()
            choice = input("Enter your choice (1-7): ")

            if choice == "1":
                add_expense()
            elif choice == "2":
                view_expenses()
            elif choice == "3":
                update_expense()
            elif choice == "4":
                delete_expense()
            elif choice == "5":
                view_summary()
            elif choice == "6":
                view_monthly_summary()
            elif choice == "7":
                print("\nGoodbye!")
                break
            else:
                print("Invalid choice!")

        except Exception as e:
            print(f"\nOops! Something unexpected happened: {e}")

        input("\nPress Enter to continue...")


main()