from __future__ import print_function

import json, boto3,time
from boto3.dynamodb.conditions import Key, Attr

#from boto3.dynamodb import Table
print('Loading function')

def get_current_user(): 
    return 12

def push_location(dynamo, lat, lon, test_mode):
    if test_mode=='true': 
        return "{'status': 'success'}"
    else:
        dynamo.put_item(Item={'lat':lat,
        'lon':lon, 
        'time':(int(time.time())), 
        'user': get_current_user(),
        'test_mode': int(test_mode)})

def get_location_history(dynamo, test_mode):
    values = dynamo.scan(FilterExpression=Attr('test_mode').eq(int(test_mode)))
    #return values
    return {
            "type": "Feature",
            "properties": {},
            "geometry": {
                "type": "LineString",
                "coordinates": [[x["lon"], x["lat"]] for x in values["Items"]]
        }}

def lambda_handler(event, context):
    query_string = event['queryParams']
    #Table needs to be manually created!!! Primary key is "number" time
    dynamo = boto3.resource('dynamodb').Table('Locations')
    #Table('Locations')
    #dynamo.put_item(Item={'test':1, 'time':(int(time.time()))})
    if query_string['operation'] == 'push_location':
        return push_location(dynamo,
            query_string['lat'], 
            query_string['lon'], 
            query_string['testMode'])
    elif query_string['operation'] == 'get_location_history':
        return get_location_history(dynamo, query_string['testMode'])
    elif query_string['operation'] == 'release':
        #return release()
        pass
    elif query_string['operation'] == 'acquire':
        pass
