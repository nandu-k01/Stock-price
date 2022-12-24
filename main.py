import yfinance as yf
from forex_python.converter import CurrencyRates
cr = CurrencyRates()


def get_price(tkr):
    company = yf.Ticker(tkr)
    current_price = company.info["regularMarketPrice"]
    current_price_inr = cr.convert("USD", "INR", current_price)
    company_name = company.info["shortName"]
    company_bs = company.balance_sheet

    print("Current stock price of", company_name, "is", current_price, "USD")
    print("Current stock price of", company_name, "in INR is", current_price_inr,
          "(Approx = ", int(current_price_inr), ")")
    print("\n")
    print(company_bs)


ticker = input("Enter the ticker symbol of desired company: ").upper()
get_price(ticker)


