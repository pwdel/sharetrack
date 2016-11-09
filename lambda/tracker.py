from __future__ import print_function

import json, boto3,time
from boto3.dynamodb.conditions import Key, Attr

#from boto3.dynamodb import Table
print('Loading function')

def get_current_user(): 
    return 12

def push_location(dynamo, gps_coords, ignore, test_mode):
    lat = gps_coords.split(',')[0]
    lon = gps_coords.split(',')[1]
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
    coords = [( x["time"], x["lat"], x["lon"]) for x in values["Items"]]
    coords.sort(key=lambda x: x[0])
    return {
            "type": "Feature",
            "properties": {},
            "geometry": {
                "type": "LineString",
                "coordinates": [[x[2], x[1]] for x in coords]
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
    
