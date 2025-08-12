def calculate_npv(cashflows, discount_rate):
    """
    Net Present Value (NPV)
    cashflows:
    discount_rate:
    """
    npv = 0
    for year, cf in enumerate(cashflows):
        npv += cf / (1 + discount_rate)**year
    return npv

#Example
cashflows = [-1000, 350, 400, 500]  #  initial investment is: 1000-
print(f"NPV: {calculate_npv(cashflows, 0.1):.2f}")