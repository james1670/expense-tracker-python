import csv
from datetime import datetime
from tabulate import tabulate
import project

def main():
    ...

def check_file_exist(file_name):
    try:
        with open(file_name, mode='r'):
            return True  
    except FileNotFoundError:
        return False
    

def log_expense(file_name, date, category, amount):

    file_exists = check_file_exist(file_name)

    with open(file_name, mode='a', newline='') as csv_file:
        writer = csv.writer(csv_file)

        if not file_exists:
            writer.writerow(['Date', 'Category', 'Amount'])

        writer.writerow([date, category, amount])


def retrieve_expenses(file_name):
    try:
        with open(file_name, mode='r') as csv_file:
            reader = csv.reader(csv_file)
            # Skip the header
            next(reader)
            expenses = [[row[0], row[1].capitalize(), f"₹ {row[2]}"] for row in reader]
            expenses.sort(key=lambda x: datetime.strptime(x[0], '%Y-%m-%d'))
            if expenses:
                title = "\nEXPENSES RETRIEVED"
                print(title)
                print(tabulate(expenses, headers=['Date', 'Category', 'Amount(₹)'], tablefmt='rounded_outline'),"\n")
            else:
                print("No expenses found.")
    except FileNotFoundError:
        print("The file does not exist.")


def check_budget(file_name, budget_limit=10000):
    total_expenses = 0

    try:
        with open(file_name, mode='r') as csv_file:
            reader = csv.reader(csv_file)
            next(reader)
            for row in reader:
                if row:  
                    total_expenses += float(row[2])  

        if total_expenses > budget_limit:
            opt = [
                ["Total Budget", f"₹{budget_limit:.2f}"],
                ["Total Expenses", f"₹{total_expenses:.2f}"],
                ["Exceeds ", f"₹{round(total_expenses - budget_limit, 2)}"]
            ]
        else:
            opt = [
                ["Total Budget", f"₹{budget_limit:.2f}"],
                ["Total Expenses", f"₹{total_expenses:.2f}"],
                ["Surplus", f"₹{round(budget_limit - total_expenses, 2)}"]
            ]

        print("\nBUDGET TABLE")
        print(tabulate(opt, headers=["Category", "Amount(₹)"], tablefmt='rounded_outline'),"\n")
    except FileNotFoundError:
        print("The file does not exist.\n")





def edit_or_delete_expense(file_name, action):
    if not check_file_exist(file_name):
        print("The file does not exist.")
        return

    with open(file_name, mode='r') as csv_file:
        reader = csv.reader(csv_file)
        rows = list(reader)

    if len(rows) == 1:
        print("No expenses found.")
        return

    # Display current expenses
    expenses = [[i, row[0], row[1].capitalize(), f"₹ {row[2]}"] for i, row in enumerate(rows[1:], start=1)]
    print(tabulate(expenses, headers=['ID', 'Date', 'Category', 'Amount(₹)'], tablefmt='rounded_outline'))

    try:
        row_id = int(input(f"Enter the ID to {action}: "))

        if row_id < 1 or row_id >= len(rows):
            print("Invalid ID.")
            return

        if action == "edit":
            # Get new values from the user
            date = input("Enter new date (YYYY-MM-DD): ")
            if not project.validate_input(date, "date"):
                print("\nInvalid DATE\n")
                return 

            category = input("Enter new category: ")
            if not project.validate_input(category, "category"):
                print("\nInvalid CATEGORY\n")
                return

            # Validate amount input
            amount = input("Enter new amount: ")
            if not project.validate_input(amount, "amount"):
                print("\nInvalid AMOUNT\n")
                return

            rows[row_id] = [date, category, amount]

        elif action == "delete":
            rows.pop(row_id)

        # Write it
        with open(file_name, mode='w', newline='') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerows(rows)

        print(f"Expense {action}ed successfully.")

    except ValueError:
        print("Invalid input.")

if __name__ == "__main__":
    main()