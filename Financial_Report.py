company = "X company"
revenue = 1500000
expenses = 900000
profit = revenue - expenses

print(f"📊 financial statement  {company}:")
print(f"revenue: {revenue:,} $")
print(f"expenses: {expenses:,} $")
print(f"net profit : {profit:,} $ ({profit/revenue:.1%} from profit)")