monthly_income = int(input("Enter your monthly income: "))
monthly_expenses =  int(input("Enter your total monthly expenses: "))
#monthly_savings = int(monthly_income) - int(monthly_expenses)
monthly_savings =  monthly_income - monthly_expenses
annual_savings = int(monthly_savings * 12 * 1.05)
print(f"Your monthly savings are ${str(int(monthly_savings))}.")
print(f"Projected savings after one year, with interest, is: ${str(annual_savings)}.")
