import yfinance as yf
company=yf.Ticker('MSFT')
stock_deatils=company.history(period='2mo')
print(stock_deatils)