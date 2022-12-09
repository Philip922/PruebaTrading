from polygon import RESTClient
from typing import cast
from urllib3 import HTTPResponse
import pandas as pd
import json
import boto3
import DynamoDB

def view_avaliable_symbols()->None:
    """
    Prints all the avaliable user symbols that can be viewed with the app
    """
    response=DynamoDB.get_all_Symbol(dynamodb)
    markets=response['Items']
    print('All avaliable symbols')
    for x in markets:
        print(x['Symbol']+" - "+x['Description'])

def view_favorite_symbol(userid:int)->None:
    """
    Prints all the favorite user symbols that can be viewed with the app
    """
    userData=DynamoDB.get_user_data(dynamodb,userid)
    favs=userData[0]['Favorites']
    print("Your Favorite Symbols")
    for fav in favs:
        print(fav)

  
def get_market_movements(market:str, datefrom:str, dateto:str, timespan:str)->pd.DataFrame:
    """
    Returns the market movements in aperior of time from Polygon.io
    """
    aggs = cast(
        HTTPResponse,
        polygon_client.get_aggs(
            market,
            1,
            timespan,
            datefrom,
            dateto,
            raw=True,
        ),
    )
    #print(aggs.geturl())
    #print(aggs.status)
    string = aggs.data.decode('utf-8')
    json_obj = json.loads(string)
    df=pd.DataFrame(json_obj['results'])
    return df

def save_market_CSV(market:str)->None:
    """
    Saves a CSV with the hourly data of a given market
    """
    Marketdata=get_market_movements('AAPL',"2022-12-06","2022-12-07","hour")
    filename='market_'+market+".csv"
    Marketdata.to_csv(filename, index=False)  
    print("Success")

def view_market(market:str,startdate:str,finishdate:str)->None:
    """
    Displays the selected market in a daily timespan
    """
    Marketdata=get_market_movements(market,startdate,finishdate,"day")
    print(Marketdata)

dynamodb = boto3.resource('dynamodb')
polygon_client=RESTClient('KEicNKiVm9dFmY8TbGtX7tOnBXFfJGCD')