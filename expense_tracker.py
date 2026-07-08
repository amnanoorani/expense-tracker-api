import datetime

expenses = []

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

    expense = [description, amount, date]
    expenses.append(expense)

    print(f"Expense added: {description} - {amount}")

def view_expenses():
    if len(expenses) == 0:
        print("\nNo expenses found!")
        return

    print("\nALL EXPENSES")
    print("#   Date        Description          Amount")

    total = 0
    try:
        for i in range(len(expenses)):
            expense = expenses[i]
            print(f"{i+1}   {expense[2]}   {expense[0]}   {expense[1]}")
            total = total + expense[1]
    except Exception as e:
        print(f"Error while showing expenses: {e}")
        return

    print(f"TOTAL: {total}")

def update_expense():
    if len(expenses) == 0:
        print("\nNo expenses to update!")
        return

    view_expenses()

    try:
        index = int(input("\nEnter expense number to update: ")) - 1
    except ValueError:
        print("Please enter a valid number!")
        return
    except Exception as e:
        print(f"Error: {e}")
        return

    if index < 0 or index >= len(expenses):
        print("Invalid number!")
        return

    try:
        expense = expenses[index]
        print(f"\nUpdating: {expense[0]} - {expense[1]}")
        print("Press Enter to keep current value")

        new_desc = input(f"New description (current: {expense[0]}): ")
        if new_desc != "":
            expense[0] = new_desc

        new_amount = input(f"New amount (current: {expense[1]}): ")
        if new_amount != "":
            try:
                amount = float(new_amount)
                if amount > 0:
                    expense[1] = amount
                else:
                    print("Amount must be positive! Keeping old value.")
            except ValueError:
                print("Invalid amount! Keeping old value.")

        new_date = input(f"New date (current: {expense[2]}): ")
        if new_date != "":
            try:
                datetime.datetime.strptime(new_date, "%Y-%m-%d")
                expense[2] = new_date
            except ValueError as e:
                print(f"Error while reading date: {e}")
                print("Keeping old date.")

        print("Expense updated successfully!")

    except Exception as e:
        print(f"Error while updating expense: {e}")

def delete_expense():
    if len(expenses) == 0:
        print("\nNo expenses to delete!")
        return

    view_expenses()

    try:
        index = int(input("\nEnter expense number to delete: ")) - 1
    except ValueError:
        print("Please enter a valid number!")
        return
    except Exception as e:
        print(f"Error: {e}")
        return

    if index < 0 or index >= len(expenses):
        print("Invalid number!")
        return

    try:
        expense = expenses[index]
        confirm = input(f"Delete '{expense[0]}'? (y/n): ")

        if confirm.lower() == "y":
            expenses.pop(index)
            print("Expense deleted!")
        else:
            print("Deletion cancelled.")

    except Exception as e:
        print(f"Error while deleting expense: {e}")

def view_summary():
    if len(expenses) == 0:
        print("\nNo expenses to summarize!")
        return

    try:
        total = 0
        for expense in expenses:
            total = total + expense[1]

        average = total / len(expenses)

        print("\nEXPENSE SUMMARY")
        print(f"Total Expenses: {len(expenses)}")
        print(f"Total Amount:   {total}")
        print(f"Average:        {average}")
    except Exception as e:
        print(f"Error while calculating summary: {e}")

def view_monthly_summary():
    if len(expenses) == 0:
        print("\nNo expenses to summarize!")
        return

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

    month_expenses = []
    total = 0

    try:
        for expense in expenses:
            date_parts = expense[2].split("-")
            if len(date_parts) >= 2:
                try:
                    expense_month = int(date_parts[1])
                except ValueError:
                    continue
                if expense_month == month:
                    month_expenses.append(expense)
                    total = total + expense[1]
    except Exception as e:
        print(f"Error while reading expense dates: {e}")
        return

    if len(month_expenses) == 0:
        print(f"\nNo expenses found for month {month}")
        return

    print(f"\nSUMMARY FOR MONTH {month}")
    print(f"Number of expenses: {len(month_expenses)}")
    print(f"Total: {total}")
    print(f"Average: {total / len(month_expenses)}")

    print("\nDetails:")
    for expense in month_expenses:
        print(f"{expense[2]} - {expense[0]}: {expense[1]}")

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