import boto3

def lambda_handler(event, context):
    try:
        input_text = event['sessionState']['intent']['slots']['text']['value']['interpretedValue'].strip()
        language_slot = event['sessionState']['intent']['slots']['language']['value']['interpretedValue']

        if not input_text : 
            raise  ValueError("Input is Empty")
        
        languages_codes = {
            'French': 'fr',
            'Japanese': 'ja',
            'Chinese': 'zh',
            'Spanish': 'es',
            'German': 'de',
            'Norwegian': 'no'
        }

        if language_slot not in languages_codes:
            raise ValueError(f"Unsupported language: {language_slot}")
        
        target_language_code = languages_codes[language_slot]

        #Initialise Amazon Translate client
        translate_client = boto3.client("translate")

        #Perform the translation 
        response = translate_client.translate_text(
            Text = input_text,
            SourceLanguageCode = 'auto',
            TargetLanguageCode = target_language_code
        )

        translated_text = response['TranslatedText']

        lex_response = {
            "sessionState": {
              "dialogAction": {
                  "type" : "Close"
              },
              "intent" : {
                "name" : "TranslateIntent", #Add your Intent Name
                "state" : "Fulfilled"
              }
            },
            "messages": [
                {
                    "contentType": "PlainText",
                    "content": translated_text
                }
            ]
        }

        return lex_response


    except Exception as error :
        error_message = "Lambda execution error: " + str(error)
        print(error_message)
        lex_error_response = {
            "sessionState": {
              "dialogAction": {
                  "type" : "Close"
              },
              "intent" : {
                "name" : "TranslateIntent",
                "state" : "Fulfilled"
              }
            },
            "messages": [
                {
                    "contentType": "PlainText",
                    "content": error_message
                }
            ]
        }

        return lex_error_response