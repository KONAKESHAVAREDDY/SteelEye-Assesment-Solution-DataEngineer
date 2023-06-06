#import necessary libraries 
from typing import List
import datetime as dt
from pydantic import BaseModel, Field
from fastapi import FastAPI, Form, Query
from starlette.responses import RedirectResponse
from fastapi_pagination import add_pagination, paginate,Page
import enum
import uvicorn
from typing import Optional


# Sample Pydantic Model
class TradeDetails(BaseModel):
    buySellIndicator: str = Field(description="A value of BUY for buys, SELL for sells.")

    price: float = Field(description="The price of the Trade.")

    quantity: int = Field(description="The amount of units traded.")

class Trade(BaseModel):
    asset_class: Optional[str] = Field(alias="assetClass", default=None, description="The asset class of the instrument traded. E.g. Bond, Equity, FX...etc")

    counterparty: Optional[str] = Field(default=None, description="The counterparty the trade was executed with. May not always be available")

    instrument_id: str = Field(alias="instrumentId", description="The ISIN/ID of the instrument traded. E.g. TSLA, AAPL, AMZN...etc")

    instrument_name: str = Field(alias="instrumentName", description="The name of the instrument traded.")

    trade_date_time: dt.datetime = Field(alias="tradeDateTime", description="The date-time the Trade was executed")

    trade_details: TradeDetails = Field(alias="tradeDetails", description="The details of the trade, i.e. price, quantity")

    trading_id: str = Field(alias="tradeId", default=None, description="The unique ID of the trade")

    trader: str = Field(description="The name of the Trader")

# Rough Database
Data_Base= [
    {
    "assetClass": "America",
    "counterparty": "USSR",
    "instrumentId": "ABCD",
    "instrumentName": "Debts",
    "tradeDateTime": "2026-05-04 00:03:34.525321",
    "tradeDetails": {
        "buySellIndicator": "BUY",
        "price": 15.36,
        "quantity": 18
    },
    "tradeId": "h0ded2dg-h4b5-2942-kid5-70hg9gj3j4b0",
    "trader": "Jones"
    },
    {
        "assetClass": "America",
        "counterparty": "USA",
        "instrumentId": "EFGH",
        "instrumentName": "Debts",
        "tradeDateTime": "2024-02-03 00:06:15.525231",
        "tradeDetails": {
            "buySellIndicator": "SELL",
            "price": 7.2,
            "quantity": 6
        },
        "tradeId": "jwhfb3jr-j3b4-9473-fhi9-92uyj3m4h9",
        "trader": "smith"
    },
    {
        "assetClass": "France",
        "counterparty": "UAE",
        "instrumentId": "IJKL",
        "instrumentName": "Shares",
        "tradeDateTime": "2012-12-03 00:04:25.525631",
        "tradeDetails": {
            "buySellIndicator": "BUY",
            "price": 24.36,
            "quantity": 21
        },
        "tradeId": "jdhft4jf-j3f5-9474-hfu8-98fhu2j9h8",
        "trader": "Kona"
    },
    {
        "assetClass": "France",
        "counterparty": "UFC",
        "instrumentId": "MNOP",
        "instrumentName": "Stocks",
        "tradeDateTime": "2003-10-02 00:07:45.525321",
        "tradeDetails": {
            "buySellIndicator": "SELL",
            "price": 53.36,
            "quantity": 18
        },
        "tradeId": "hfbfj8gd-u3u8-8383-jkh9-37ryu4y7g8",
        "trader": "Jhon"
    },
    {
        "assetClass": "Germany",
        "counterparty": "UFC",
        "instrumentId": "WXYA",
        "instrumentName": "Stocks",
        "tradeDateTime": "2003-11-02 00:07:45.528321",
        "tradeDetails": {
            "buySellIndicator": "SELL",
            "price": 33.36,
            "quantity": 11
        },
        "tradeId": "webfj8es-g3u8-8343-jkr9-47rhu4y5r8",
        "trader": "Wick"
    },
      
]
app = FastAPI()
class sortChoice(str, enum.Enum):
    asc = "asc"
    desc = "desc"

@app.get("/")
def main():
    return RedirectResponse(url="/docs/")

# 1 Fetch all list of tradings
@app.get("/tradings/", status_code=200, response_model=Page[Trade])
def fetch_all_tradings(*,assetClassSort: sortChoice = Query(None), counterpartySort: sortChoice = Query(None), instrumentIdSort: sortChoice = Query(None), instrumentNameSort: sortChoice = Query(None), tradeDateTimeSort: sortChoice = Query(None), buySellIndicatorSort: sortChoice = Query(None), priceSort: sortChoice = Query(None), quantitySort: sortChoice = Query(None),tradeIdSort: sortChoice = Query(None), traderSort: sortChoice = Query(None)) -> list:
    """
    Fetching the list of tradings
    """
    res = Data_Base
    if assetClassSort == "asc":
        res = sorted(Data_Base, key=lambda trade: trade['assetClass']) 
    
    if assetClassSort == "desc":
        res = sorted(Data_Base, key=lambda trade: trade['assetClass'], reverse=True)
    
    if counterpartySort == "asc":
        res = sorted(res, key=lambda trade: trade['counterparty']) 
    
    if counterpartySort == "desc":
        res = sorted(res, key=lambda trade: trade['counterparty'], reverse=True)

    if instrumentIdSort == "asc":
        res = sorted(res, key=lambda trade: trade['instrumentId']) 
    
    if instrumentIdSort == "desc":
        res = sorted(res, key=lambda trade: trade['instrumentId'], reverse=True)
    
    if instrumentNameSort == "asc":
        res = sorted(res, key=lambda trade: trade['instrumentName']) 
    
    if instrumentNameSort == "desc":
        res = sorted(res, key=lambda trade: trade['instrumentName'], reverse=True)

    if tradeDateTimeSort == "asc":
        res = sorted(res, key=lambda trade: trade['tradeDateTime']) 
    
    if tradeDateTimeSort == "desc":
        res = sorted(res, key=lambda trade: trade['tradeDateTime'], reverse=True)

    if buySellIndicatorSort == "asc":
        res = sorted(res, key=lambda trade: trade['tradeDetails']['buySellIndicator']) 
    
    if buySellIndicatorSort == "desc":
        res = sorted(res, key=lambda trade: trade['tradeDetails']['buySellIndicator'], reverse=True)
    
    if quantitySort == "asc":
        res = sorted(res, key=lambda trade: trade['tradeDetails']['quantity']) 
    
    if quantitySort == "desc":
        res = sorted(res, key=lambda trade: trade['tradeDetails']['quantity'], reverse=True)
    
    if traderSort == "asc":
        res = sorted(res, key=lambda trade: trade['trader']) 
    
    if traderSort == "desc":
        res = sorted(res, key=lambda trade: trade['trader'], reverse=True)

    if tradeIdSort == "asc":
        res = sorted(res, key=lambda trade: trade['tradeId']) 
    
    if tradeIdSort == "desc":
        res = sorted(res, key=lambda trade: trade['tradeId'], reverse=True)
    
    if priceSort == "asc":
        res = sorted(res, key=lambda trade: trade['tradeDetails']['price']) 
    
    if priceSort == "desc":
        res = sorted(res, key=lambda trade: trade['tradeDetails']['price'], reverse=True)

    return paginate(res)

# 2 Fetch a trade by ID
@app.get("/tradings/{trading_id}", status_code=200, response_model=Trade)
def fetch_trade_by(*, trading_id: str) -> dict:
    """
    Fetch a trade by ID
    """

    result = [trade for trade in Data_Base if trade["tradeId"] == trading_id]
    if result:
        return result[0]

# 3 Fetch a list of tradings will searching for tradings through counterparty, instrumentId, instrumentName and trader.
@app.get("/tradings", status_code=200, response_model=Page[Trade])
def search_trade(*, search: str = Query(None)) -> list:
    """
    Fetch a list of tradings will searching for tradings through counterparty, instrumentId, instrumentName and trader.
    """
    results = []
    for trade in Data_Base:
        if search.lower() in trade["counterparty"].lower() or search.lower() in trade["instrumentId"].lower() or search.lower() in trade["instrumentName"].lower() or search.lower() in trade["trader"].lower():
            results.append(trade)

    return paginate(results)

# 4 Fetch a list of tradings will searching for tradings through assetClass, end, maxPrice, minPrice, start and tradeType.
@app.get("/tradings", status_code=200, response_model=Page[Trade])
def advance_search_trade(*, assetClass: str = Query(None), maxPrice: float = Query(None), minPrice: float = Query(None), tradeType: str = Query(None), end: dt.datetime = Query(None), start: dt.datetime = Query(None)) -> list:
    """
    Fetch a list of tradings will searching for tradings through assetClass, end, maxPrice, minPrice, start and tradeType.
    """
    results = []
    for trade in Data_Base:
        flagAssetClass = True
        flagTradeType = True
        flagMinPrice = True
        flagMaxPrice = True
        flagStart = True
        flagEnd = True

        if assetClass != None:
            flagAssetClass = False
        if tradeType != None:
            flagTradeType = False
        if minPrice != None:
            flagMinPrice = False
        if maxPrice != None:
            flagMaxPrice = False
        if start != None:
            flagStart = False
        if end != None:
            flagEnd = False

        if assetClass != None:
            if assetClass.lower() in trade["assetClass"].lower():
                flagAssetClass = True
        if tradeType != None:
            if tradeType.lower() in trade["tradeDetails"]["buySellIndicator"].lower():
                flagTradeType = True

        if minPrice != None:
            if trade["tradeDetails"]["price"] >= minPrice:
                flagMinPrice = True
        
        if maxPrice != None:
            if maxPrice != None:
                if trade["tradeDetails"]["price"] <= maxPrice:
                    flagMaxPrice = True

        if start != None:
            if str(start) >= trade["tradeDateTime"]:
                flagStart = True
        if end != None:
            if str(end) <= trade["tradeDateTime"]:
                flagEnd = True

        if flagAssetClass and flagTradeType and flagMinPrice and flagMaxPrice and flagStart and flagEnd:
            results.append(trade)

    return paginate(results)

add_pagination(app)

if __name__ == "__main__":
    uvicorn.run("app:app", port=8000, reload=True)
