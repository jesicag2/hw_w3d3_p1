# HW1_P3: Python Loops and Tuples in Analytical Applications

# Task 1: Stock Market Data Analysis
'''
You have been provided with stock market data, where each data point is 
a tuple containing a company's stock symbol, the date, and the closing price. 
Your task is to analyze this data to find the average closing price of a 
specified stock over a given period.

- Create a function to calculate the average closing price of a specific stock symbol over all dates.
- Ensure your solution handles cases where the stock symbol does not exist in the data.
'''

stock_data = [
    ("AAPL", "2021-01-01", 130.0),
    ("AAPL", "2021-01-02", 132.0),
    ("MSFT", "2021-01-01", 220.0),
]
def avg_closing_price(symbol):
    closing_prices = []
    for info in stock_data:
        stock, date, closing_price = info
        if stock == symbol:
            closing_prices.append(closing_price)
        else:
            print (f"{symbol} is not in our database.")
    if closing_price:
        avg_price = sum(closing_prices) / len(closing_prices)
        print(f"Average closing price for {symbol} is {avg_price}")


avg_closing_price("GOOG")
avg_closing_price("AAPL")
