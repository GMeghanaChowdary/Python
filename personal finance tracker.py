def personal_finance_tracker():
    income = float(input("Enter your income: "))
    expenses = float(input("Enter your expenses: "))
    savings = income - expenses
    print(f"Your savings: {savings}")
personal_finance_tracker()
