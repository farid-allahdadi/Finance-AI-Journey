# recieving input
symbol = input("symbol (for example AAPL): ").strip().upper()
price = float(input("Stock Price: "))


report = f"""
📈 report:
symbpl : {symbol}
price: {price:,.0f} $
situation: {"📉 loss" if price < 1000 else "📈 profit"}
"""

print(report)