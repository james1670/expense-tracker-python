import sys, data_handler, visualize, re
from tabulate import tabulate

# Main function
def main():
    take_action()



def take_action():
    while True:

        options = {"1": "Log an expense", 
           "2": "Summarize expenses", 
           "3": "Check budget", 
           "4": "Visualize expenses",
           "5": "Edit expense",
           "6": "Delete expense", 
           "0": "Exit"}

        options_list = [[key, value] for key, value in options.items()]

        # Print with tablw along with title
        table = tabulate(options_list, headers=["ID", "Option"], tablefmt='rounded_outline')
        title = "EXPENSE TRACKER MENU"
        table_width = len(table.splitlines()[0])
        print(title.center(table_width))
        print(table)

        choice = input("Enter your choice: ")

        if choice == "1":
            try:
                date, category, amount = take_input()
                data_handler.log_expense("Expenses.csv", date, category, amount)
                print("Expense Logged.\n")
            except:
                pass
        elif choice == "2":
            try:
                data_handler.retrieve_expenses("Expenses.csv")
            except:
                print("Failed Retrieval")
        elif choice == "3":
            data_handler.check_budget("Expenses.csv")
        elif choice == "4":
            options_prompt = [["1. Bar Chart"], ["2. Pie Chart"], ["3. Both Charts"]]
            print(tabulate(options_prompt, headers=["Enter Options"], tablefmt='rounded_outline'))
            n = input(": ")
            visualize.visualize_expenses("Expenses.csv", n)

        elif choice == "5":
            data_handler.edit_or_delete_expense("Expenses.csv", "edit")

        elif choice == "6":
            data_handler.edit_or_delete_expense("Expenses.csv", "delete")

        elif choice == "0" or choice.lower() == "exit":
            break
        else:
            print("Invalid choice. Please try again.\n")


def take_input():
    while True:
        
        # Get date input
        options_prompt = [["Date - (YYYY-MM-DD)"], ["Exit - 'exit'"]]
        print(tabulate(options_prompt, headers=["Enter Options"], tablefmt='rounded_outline'))
        date = input(": ")
        if date.lower() == 'exit':
            sys.exit("\nExiting...")
        else:
            if not validate_input(date, "date"):
                print("\nInvalid DATE\n")
                break
                

        # Get category input
        options_prompt = [["Food"], ["Transport"], ["Entertainment"], ["Groceries"], ["Clothing"], ["Exit - 'exit'"]]
        print(tabulate(options_prompt, headers=["Enter Options"], tablefmt='rounded_outline'))
        category = input(": ")
        if category.lower() == 'exit':
            sys.exit("\nExiting...")
        else:
            if not validate_input(category, "category"):
                print("\nInvalid CATEGORY\n")
                break


        # Get amount input
        options_prompt = [["Amount - (₹)"], ["Exit - 'exit'"]]
        print(tabulate(options_prompt, headers=["Enter Options"], tablefmt='rounded_outline'))
        amount = input(": ")
        if amount.lower() == 'exit':
            sys.exit("\nExiting...")
        else:
            if not validate_input(amount, "amount"):
                print("\nInvalid AMOUNT\n")
                break
        
        return date, category, amount



def validate_input(value, input_type):
    if input_type == "date":
        pattern = r'^\d{4}-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])$'
        return re.match(pattern, value) is not None

    elif input_type == "category":
        return value.isalpha() and value.lower() in ["food", "transport", "entertainment", "clothing", "groceries"]

    elif input_type == "amount":
        try:
            amount = float(value)
            return amount >= 0
        except ValueError:
            return False

    return False


if __name__ == "__main__":
    main()
