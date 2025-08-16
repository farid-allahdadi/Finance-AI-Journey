def portfolio_analysis(*stocks, **metrics):
    """
    Analyzes a stock portfolio with flexible parameters
    :param stocks: Positional args (stock symbols)
    :param metrics: Keyword args (analysis metrics)
    """
    print("\n=== PORTFOLIO ANALYSIS ===")

    # Handle positional arguments
    print("Stocks to analyze:")
    for i, stock in enumerate(stocks, 1):
        print(f"{i}. {stock}")

    # Handle keyword arguments
    print("\nAnalysis Metrics:")
    for metric, value in metrics.items():
        print(f"{metric}: {value}")

    # Calculate default metric if not provided
    risk_level = metrics.get('risk', 'Medium')
    print(f"\nRisk Level: {risk_level}")


# Example usage with mixed arguments
portfolio_analysis(
    "AAPL",
    "TSLA",
    "NVDA",
    pe_ratio=25.3,
    dividend_yield=1.8,
    beta=1.2
)
