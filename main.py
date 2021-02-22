from fastapi import FastAPI
import yfinance as yf


app = FastAPI()


@app.get("/shares/{ticker}")
async def get_price(ticker):

    msft = yf.Ticker(ticker)

    # get historical market data
    hist = msft.history(period="5d")
    industry = msft.info['sector']
    shortName = msft.info['shortName']
    regularMarketPrice = msft.info['regularMarketPrice']
    # See all available metrics
    print(hist)
    return {"industry": industry, "Name": shortName, "Regular Market price": regularMarketPrice}
