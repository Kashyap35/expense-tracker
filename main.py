import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt
from charts import plot_monthly_expenses, plot_category_expenses




CSV_FILE = 'expenses.csv'

# Function to add an expense
def add_expense():
    date = input("Enter date (YYYY-MM-DD) or leave blank for today: ")
    if not date:
        date = datetime.today().strftime('%Y-%m-%d')
    category = input("Enter category (Food, Rent, Travel, etc.): ")
    amount = float(input("Enter amount: "))
    description = input("Enter description: ")

    new_expense = pd.DataFrame([[date, category, amount, description]], 
                               columns=['Date', 'Category', 'Amount', 'Description'])
    
    try:
        df = pd.read_csv(CSV_FILE)
        df = pd.concat([df, new_expense], ignore_index=True)
    except FileNotFoundError:
        df = new_expense
    
    df.to_csv(CSV_FILE, index=False)
    print("Expense added successfully!")

# Function to view all expenses
def view_expenses():
    try:
        df = pd.read_csv(CSV_FILE)
        print("\n--- All Expenses ---")
        print(df)
    except FileNotFoundError:
        print("No expenses recorded yet.")

# Function to summarize expenses by month
def monthly_summary():
    try:
        df = pd.read_csv(CSV_FILE)
        df['Date'] = pd.to_datetime(df['Date'])
        df['Month'] = df['Date'].dt.to_period('M')
        summary = df.groupby('Month')['Amount'].sum()
        print("\n--- Monthly Expense Summary ---")
        print(summary)
    except FileNotFoundError:
        print("No expenses recorded yet.")

# Function to summarize expenses by category
def category_summary():
    try:
        df = pd.read_csv(CSV_FILE)
        summary = df.groupby('Category')['Amount'].sum()
        print("\n--- Expense by Category ---")
        print(summary)
    except FileNotFoundError:
        print("No expenses recorded yet.")

def plot_monthly_expenses():
    try:
        df = pd.read_csv(CSV_FILE)
        df['Date'] = pd.to_datetime(df['Date'])
        df['Month'] = df['Date'].dt.to_period('M')
        summary = df.groupby('Month')['Amount'].sum()
        
        summary.plot(kind='bar', title='Monthly Expenses')
        plt.xlabel('Month')
        plt.ylabel('Total Amount')
        plt.tight_layout()
        plt.show()
    except FileNotFoundError:
        print("No expenses recorded yet.")


def plot_category_expenses():
    try:
        df = pd.read_csv(CSV_FILE)
        summary = df.groupby('Category')['Amount'].sum()
        
        summary.plot(kind='pie', autopct='%1.1f%%', title='Expenses by Category')
        plt.ylabel('')
        plt.tight_layout()
        plt.show()
    except FileNotFoundError:
        print("No expenses recorded yet.")



# Main menu
def main():
    while True:
        print("\n--- Personal Expense Tracker ---")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Monthly Summary")
        print("4. Category Summary")
        print("5. Plot Monthly Expenses")
        print("6. Plot Category Expenses")
        print("7. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            add_expense()
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            monthly_summary()
        elif choice == '4':
            category_summary()
        elif choice == '5':
            plot_monthly_expenses()
        elif choice == '6':
            plot_category_expenses()
        elif choice == '7':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
