
**Code (expense_tracker.py)**  
```python
import csv
import os

FILE = "expenses.csv"

def init_file():
    if not os.path.exists(FILE):
        with open(FILE, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["Description", "Amount"])

def add_expense():
    desc = input("Enter description: ")
    amt = input("Enter amount: ")
    with open(FILE, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([desc, amt])
    print("Expense added.")

def view_expenses():
    with open(FILE, "r") as f:
        reader = list(csv.reader(f))
        for i, row in enumerate(reader[1:], start=1):
            print(f"{i}. {row[0]} - ₹{row[1]}")

def delete_expense():
    view_expenses()
    idx = int(input("Enter expense number to delete: "))
    with open(FILE, "r") as f:
        rows = list(csv.reader(f))
    rows.pop(idx)
    with open(FILE, "w", newline="") as f:
        csv.writer(f).writerows(rows)
    print("Expense deleted.")

init_file()

while True:
    print("\n1. Add  2. View  3. Delete  4. Exit")
    choice = input("Choose: ")
    if choice == "1": add_expense()
    elif choice == "2": view_expenses()
    elif choice == "3": delete_expense()
    else: break
