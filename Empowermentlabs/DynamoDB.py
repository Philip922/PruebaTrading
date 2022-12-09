from botocore.exceptions import ClientError
from boto3.dynamodb.conditions import Key, Attr
import boto3
import logging

def add_Symbol(boto_resource, Identifier:int, Symbol:str, Description:str)->None:
    """
    Adds a Symbol to the table.
    :param boto_resource: Boto 3 reourde of the dynamo db
    :param Identifier: The database ID of the stock
    :param Symbol: The database Symbol of the stock
    :param Description: The database Description of the stock
    """
    try:
        table=boto_resource.Table('TradeSymbols')
        table.put_item(
            Item={
                'Identifier': Identifier,
                'Symbol': Symbol,
                'Description': Description})
    except ClientError as err:
        logging.logger.error(
            "Couldn't add symbol %s to table %s. Here's why: %s: %s",
            Identifier, table.name,
            err.response['Error']['Code'], err.response['Error']['Message'])
        raise

def get_all_Symbol(boto_resource)->dict:
    """
    Retrieves all avaliable symbols
    :param boto_resource: Boto 3 reourde of the dynamo db
    """
    try:
        table=boto_resource.Table('TradeSymbols')
        response=table.scan(
            FilterExpression=Attr('Identifier').gte(0)
        )
        return response
    except ClientError as err:
        logging.logger.error(
            "Couldn't add symbol %s to table %s. Here's why: %s: %s",
            Identifier, table.name,
            err.response['Error']['Code'], err.response['Error']['Message'])
        raise

def get_user_data(boto_resource, user_id:int)->dict:
    """
    retrieves the data from a given user
    :param boto_resource: Boto 3 reourde of the dynamo db
    """
    try:
        table=boto_resource.Table('UserFavs')
        response=table.scan(
            FilterExpression=Attr('UserID').eq(user_id)
        )
        return response["Items"]
    except ClientError as err:
        logging.logger.error(
            "Couldn't add symbol %s to table %s. Here's why: %s: %s",
            Identifier, table.name,
            err.response['Error']['Code'], err.response['Error']['Message'])
        raise

def set_user_data(boto_resource, userID:int, Name:str, Favorites:list)->dict:
    """
    Sets user data
    :param boto_resource: Boto 3 reourde of the dynamo db
    :param userID: the user ID to modify
    :param Name: The person name
    :Param Favorites: a list of the favorite markets
    """
    try:
        table=boto_resource.Table('UserFavs')
        table.put_item(
            Item={
                'UserID': userID,
                'Name': Name,
                'Favorites': Favorites})
    except ClientError as err:
        logging.logger.error(
            "Couldn't add symbol %s to table %s. Here's why: %s: %s",
            Identifier, table.name,
            err.response['Error']['Code'], err.response['Error']['Message'])
        raise

#Usage examples
#dynamodb = boto3.resource('dynamodb')
#add_Symbol(dynamodb, 2, 'CPNG', 'Coupang, Inc.')
#symbols=get_all_Symbol(dynamodb)
#favs=get_user_data(dynamodb,1)
#set_user_data(dynamodb, 2, "Penny Rose", ["META", "HON"])