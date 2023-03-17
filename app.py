import pandas as pd
import numpy as np
import boto3

# Defining function for the aws lambda which takes json objects and saves the extracted data to s3 bucket
def lambda_handler(event, context):
    # TODO implement
    # Extracting roll, pitch and yaw data from the payload coming from data streaming app
    roll = [i['values']['roll'] for i in event['payload']]
    pitch = [i['values']['pitch'] for i in event['payload']]
    yaw = [i['values']['yaw'] for i in event['payload']]

    # Creating pandas dataframe from the given values
    df = pd.DataFrame({'roll':roll, 'pitch':pitch, 'yaw':yaw})

    # print(event)
    # Saving the dataframe in the local directory
    csv_loc = '/tmp/' + str(event['messageId']) + '.csv'
    df.to_csv(csv_loc)

    # Uploading the locally saved data to the s3 bucket
    bucket_name = 'imu-streaming-data'
    csv_object = event['deviceId'] + '/' + \
        event['sessionId'] + '/' + str(event['messageId']) + '.csv'
    s3 = boto3.resource('s3')    
    s3.Bucket(bucket_name).upload_file(csv_loc, csv_object)

    return {
        'statusCode': 200
    }