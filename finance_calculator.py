monthly_income = input("Enter your monthly income: ")
monthly_expenses =  input("Enter your total monthly expenses: ")
monthly_savings = float(monthly_income) - float(monthly_expenses)
monthly_savings = int(monthly_savings)
projected_savings = int(monthly_savings * 12 * 1.05)

print(f"Your monthly savings are ${monthly_savings}.")
print(f"Projected savings after one year, with interest, is: ${projected_savings}.")