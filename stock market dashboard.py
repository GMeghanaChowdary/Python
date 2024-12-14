import yfinance as yf
def stock_dashboard():
    stock_symbol = input("Enter stock symbol: ")
    stock_data = yf.Ticker(stock_symbol)
    print(stock_data.history(period="1d"))
stock_dashboard()
