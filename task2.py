def track_portfolio():
    # Hardcoded stock prices
    stock_prices = {
        "AAPL": 180,
        "TSLA": 250,
        "GOOGL": 140,
        "AMZN": 145,
        "MSFT": 330
    }

    portfolio = {}
    total_investment = 0

    print("Welcome to the Stock Portfolio Tracker!")
    print("Available stocks:", ", ".join(stock_prices.keys()))
    print("Enter 'done' as the stock name when you're finished.\n")

    while True:
        stock_name = input("Enter stock name: ").upper()

        if stock_name == "DONE":
            break

        if stock_name not in stock_prices:
            print("Stock not found in our list. Please choose from:", ", ".join(stock_prices.keys()))
            continue

        try:
            quantity = int(input(f"Enter quantity of {stock_name}: "))
        except ValueError:
            print("Please enter a valid number for quantity.")
            continue

        if quantity <= 0:
            print("Quantity must be greater than zero.")
            continue

        cost = stock_prices[stock_name] * quantity
        total_investment += cost

        if stock_name in portfolio:
            portfolio[stock_name] += quantity
        else:
            portfolio[stock_name] = quantity

        print(f"Added {quantity} share(s) of {stock_name} at ${stock_prices[stock_name]} each = ${cost}\n")

    # Display summary
    print("\n----- Portfolio Summary -----")
    if not portfolio:
        print("No stocks were added.")
    else:
        for stock, qty in portfolio.items():
            price = stock_prices[stock]
            value = price * qty
            print(f"{stock}: {qty} share(s) x ${price} = ${value}")
        print(f"\nTotal Investment Value: ${total_investment}")

        # Optional: save to file
        save_choice = input("\nDo you want to save this summary to a file? (yes/no): ").lower()
        if save_choice == "yes":
            with open("portfolio_summary.txt", "w") as f:
                f.write("----- Portfolio Summary -----\n")
                for stock, qty in portfolio.items():
                    price = stock_prices[stock]
                    value = price * qty
                    f.write(f"{stock}: {qty} share(s) x ${price} = ${value}\n")
                f.write(f"\nTotal Investment Value: ${total_investment}\n")
            print("Summary saved to 'portfolio_summary.txt'")


if __name__ == "__main__":
    track_portfolio()