import csv
import matplotlib.pyplot as plt
from collections import defaultdict


def main():
     ...


def read_expenses(file_name):
    expenses_by_category = defaultdict(float)
    dates = []
    amounts = []

    try:
        with open(file_name, mode='r') as csv_file:
            reader = csv.reader(csv_file)
            next(reader)  # Skip header
            for row in reader:
                if row:
                    date, category, amount = row
                    amounts.append(float(amount))
                    dates.append(date)
                    expenses_by_category[category] += float(amount)

        return dates, amounts, expenses_by_category
    except FileNotFoundError:
        print(f"File {file_name} not found.")
        return [], [], {}

def visualize_expenses(file_name, n):
    dates, amounts, expenses_by_category = read_expenses(file_name)

    if not dates or not expenses_by_category:
        print("No expenses to visualize.")
        return

    try:
        if n == '1':
           bar_chart(dates, amounts)
        elif n == '2':
            pie_chart(expenses_by_category)
        elif n == '3':
            bar_chart(dates, amounts)
            pie_chart(expenses_by_category)

    except:
        print("Invalid Input")


def bar_chart(dates, amounts):
     # Bar Chart for daily expenses
            plt.figure(figsize=(4.5, 6))
            plt.bar(dates, amounts, color='blue')
            plt.xlabel('Date')
            plt.ylabel('Amount (₹)')
            plt.title('Daily Expenses')
            plt.xticks(rotation=0, ha="right")
            plt.tight_layout()  # Adjust layout to fit labels
            plt.show()

def pie_chart(expenses_by_category):
     # Pie Chart for expenses by category
            categories = list(expenses_by_category.keys())
            amounts_by_category = list(expenses_by_category.values())

            plt.figure(figsize=(5, 3))
            plt.pie(amounts_by_category, labels=categories, autopct='%1.1f%%', startangle=140)
            plt.title('Expenses by Category')
            plt.show()


if __name__ =="__main__":
     main()