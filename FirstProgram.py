import sqlite3

# Connecting to SQLite database
conn = sqlite3.connect('expenses.db')
c = conn.cursor()

# Creating expenses table
c.execute('''CREATE TABLE IF NOT EXISTS expenses (
             id INTEGER PRIMARY KEY,
             date TEXT,
             amount REAL,
             category TEXT,
             description TEXT
             )''')
conn.commit()

def add_expense(date, amount, category, description):
    #adding expenses to the database
    c.execute('''INSERT INTO expenses (date, amount, category, description)
                 VALUES (?, ?, ?, ?)''', (date, amount, category, description))
    conn.commit()

def get_total_expenses():
    #retrieving total expenses from the database
    c.execute('SELECT SUM(amount) FROM expenses')
    total = c.fetchone()[0]
    return total if total else 0

def get_expenses_by_category():
    #retrieving expenses grouped by category
    c.execute('''SELECT category, SUM(amount) FROM expenses
                 GROUP BY category''')
    return c.fetchall()

def main():
    while True:
        print("1. Add Expense")
        print("2. View Total Expenses")
        print("3. View Expenses by Category")
        print("4. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            #input expense details
            date = input("Enter date (YYYY-MM-DD): ")
            amount = float(input("Enter amount: "))
            category = input("Enter category: ")
            description = input("Enter description: ")
            add_expense(date, amount, category, description)
            print("Expense added successfully!")
        elif choice == '2':
            #to view total expenses
            total = get_total_expenses()
            print(f"Total Expenses: ${total:.2f}")
        elif choice == '3':
            #viewing expenses grouped by category
            expenses_by_category = get_expenses_by_category()
            print("Expenses by Category:")
            for category, amount in expenses_by_category:
                print(f"{category}: ${amount:.2f}")
        elif choice == '4':
            #exit the program
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

# Close database connection
conn.close()
