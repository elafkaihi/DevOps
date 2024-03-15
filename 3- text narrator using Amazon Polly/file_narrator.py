import boto3
from io import BytesIO
import time

def text_narrator(event, context):
    try:
        #Extract text input from the event
        text = event['text']

        #Initialize Polly and S3 clients
        s3_client = boto3.client('s3')
        polly_client = boto3.client('polly')

        #Parameters for Polly
        params = {
            'Text' : text,
            'OutputFormat' : 'mp3',
            'VoiceId' : 'Joanna'
        }

        #Generate Speech
        reponse = polly.synthesize_speech(**params)
        audio_stream = response['AudioStream'].read()

        #Generate a unique key for the audio file 
        key = f"audio-{int(time.time())}.mp3"

        #Parameters for S3
        s3_params = {
            'Bucket': 'your-bucket-name',
            'Key': key,
            'Body': audio_stream,
            'ContentType': 'audio/mpeg'
        }
        # Upload audio file to S3
        s3.upload_fileobj(BytesIO(audio_stream), s3_params['Bucket'], s3_params['Key'], ExtraArgs={'ContentType': s3_params['ContentType']})

        output_message = f"The audio file has been successfully stored in the S3 bucket by the name {key}"

        return {
            'statusCode': 200,
            'body': {'message': output_message}
        }

    except Exception as e :
        print(f'Error: {e}')
        return {
            'statusCode': 500,
            'body': {'message': 'Internal server error'}
        }