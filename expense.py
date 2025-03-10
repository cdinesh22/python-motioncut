import json
import os
class ExpenseTracker:
    def __init__(self, filename="expenses.json"):
        self.filename = filename
        self.expenses = self.load_expenses()
    def load_expenses(self):
        if os.path.exists(self.filename):
            with open(self.filename, "r") as file:
                return json.load(file)
        return []
    def save_expenses(self):
        with open(self.filename, "w") as file:
            json.dump(self.expenses, file, indent=4)
    def add_expense(self, amount, category, description):
        try:
            amount = float(amount)
            expense = {"amount": amount, "category": category, "description": description}
            self.expenses.append(expense)
            self.save_expenses()
            print("Expense added successfully.")
        except ValueError:
            print("Invalid amount. Please enter a numeric value.")
    def view_expenses(self):
        if not self.expenses:
            print("No expenses recorded yet.")
        else:
            for idx, expense in enumerate(self.expenses, start=1):
                print(f"{idx}. ${expense['amount']} - {expense['category']} - {expense['description']}")
    def generate_report(self):
        summary = {}
        for expense in self.expenses:
            category = expense["category"]
            summary[category] = summary.get(category, 0) + expense["amount"]
        print("\nExpense Report:")
        for category, total in summary.items():
            print(f"{category}: ${total:.2f}")
    def run(self):
        while True:
            print("\nExpense Tracker Menu:")
            print("1.Add Expense")
            print("2.View Expenses")
            print("3.Generate Report")
            print("4.Exit")
            choice = input("Select an option: ")
            if choice == "1":
                amount = input("Enter amount: ")
                category = input("Enter category (Food, Transport, etc.): ")
                description = input("Enter description: ")
                self.add_expense(amount, category, description)
            elif choice == "2":
                self.view_expenses()
            elif choice == "3":
                self.generate_report()
            elif choice == "4":
                print("Exitinging Expense Tracker.........Goodbye!")
                break
            else:
                print("Invalid choice. Please try again!!!!!!!!")
tracker = ExpenseTracker()
tracker.run()
