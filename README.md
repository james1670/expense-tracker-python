

# **Expenses Tracker**  

#### Video Demo:  <https://youtu.be/Znkmp1zumVA?si=7Y6HTPe9Fsakx598>

---

## **Overview**  

**Expenses Tracker** is a Python-based command-line application designed to help users efficiently track, manage, and visualize their daily expenses. This intuitive tool allows users to easily log expenses, summarize their spending, check budget status, and generate visual reports to better understand their financial habits.  

---

## **Key Features**  

🔹 **Log Expenses**:  
Easily add your expenses by specifying details like the **date**, **category**, and **amount**. The categories include common types like Food, Transport, Entertainment, etc.  

🔹 **Summarize Expenses**:  
Retrieve all your logged expenses in a clear, tabulated format, sorted by date.  

🔹 **Check Budget**:  
Keep track of your total expenses and compare them against a predefined budget limit. The app will notify you if your spending exceeds your budget or if you have savings left.  

🔹 **Visualize Expenses**:  
Create insightful visualizations using **Bar Charts** and **Pie Charts** that give a graphical representation of your spending patterns.  

🔹 **Edit/Delete Expenses**:  
Modify or remove any logged expense seamlessly. 

---

## **Technology & Libraries**  

- **Python**: The core language used for all functionalities.
- **CSV**: Data persistence is achieved using CSV files, making the storage of logged data lightweight and portable.
- **Matplotlib**: Used for generating the visual charts (Bar & Pie charts).
- **Tabulate**: For generating beautiful tables in the command-line interface, giving a clear and structured view of data.
- **Pytest**: For running unit tests and ensuring the integrity of the application.

---

## **Installation Instructions**  

To install and get the project running on your local machine, follow the steps below:

### 1. **Clone the Repository**  
Run the following command to clone the repository to your local system:
```bash
git clone https://github.com/james1669/ExpensesTracker.git
cd ExpensesTracker
```

### 2. **Install Dependencies**  
Install the required packages using the `requirements.txt` file:
```bash
pip install -r requirements.txt
```

---

## **How to Use the Application**  

### **Running the Application**  
After installation, simply run the main script to launch the expense tracker:
```bash
python project.py
```

### **Using the Menu**  
Once the application starts, you will be greeted with a menu. Simply follow the on-screen instructions to:

- **Log new expenses**: Add a new expense by entering the date, category, and amount.
- **Summarize your expenses**: Get a detailed overview of all your logged expenses.
- **Check if you're staying within budget**: Compare your total expenses against a set budget.
- **Visualize expenses**: View your expenses through graphical representations, such as bar and pie charts.
- **Edit previous entries**: Modify any existing expense by selecting the entry you want to change and updating its details (date, category, amount).
- **Delete previous entries**: Remove an expense entirely by selecting the entry you wish to delete.

Each feature is mapped to a distinct menu option for ease of navigation.


---

## **File Structure**  

The project consists of several Python modules, each handling a specific functionality:

- **`project.py`**:  
  The main interface of the application. Handles user input and navigates between different features.
  
- **`data_handler.py`**:  
  Manages all data operations such as logging expenses, retrieving saved data, and editing or deleting existing records.
  
- **`visualize.py`**:  
  Contains functions that create visual representations of the data using bar and pie charts.
  
- **`test_project.py`**:  
  Unit tests to ensure the various parts of the application are functioning correctly.
  
- **`requirements.txt`**:  
  Contains the list of dependencies to ensure the application runs smoothly on any system.

---

## **Requirements**  

- **Python 3.x**  
- Libraries:  
  - `tabulate` (for table display)  
  - `pytest` (for testing)  
  - `matplotlib` (for charts)  

---

## **Testing the Application**  

To ensure the code is working correctly, the application comes with a set of unit tests. You can run them using the following command:
```bash
pytest test_project.py
```

---

## **Future Enhancements**  

- **Advanced Reporting**:  
  Add detailed weekly/monthly summaries to provide deeper financial insights.
  
- **Multiple Budget Support**:  
  Allow users to define budgets for different categories or time periods.
  
- **Database Integration**:  
  Migrate from CSV to an SQLite or PostgreSQL database for better data management and scalability.

---

## **Author**  

This project was developed by **James Bright**.  
For any queries or contributions, feel free to visit my GitHub profile:  
[GitHub Profile](https://github.com/james1669)

---


