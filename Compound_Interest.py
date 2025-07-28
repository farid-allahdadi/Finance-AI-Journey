principal = float(input("💰 initial equity ($): "))
rate = float(input("📈 anuual rate (%): ")) / 100
years = int(input("⏳ time of investment (year): "))

final_amount = principal * (1 + rate) ** years
print(f"✅ final amount after  {years} years: {final_amount:,.0f} $")