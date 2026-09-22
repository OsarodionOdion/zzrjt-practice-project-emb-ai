# Function for running sentiment analysis using the Watson NLP BERT Sentiment Analysis function.

'''
URL, headers and input JSON format for accessing the BERT based Sentiment Analysis function of the Watson NLP Library

URL: 'https://sn-watson-sentiment-bert.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/SentimentPredict'
Headers: {"grpc-metadata-mm-model-id": "sentiment_aggregated-bert-workflow_lang_multi_stock"}
Input json: { "raw_document": { "text": text_to_analyse } }

'''

import requests

def sentiment_analyzer(text_to_analyse):

    """ Function for running sentiment analysis using the Watson NLP BERT Sentiment Analysis function.
    
    Args:
        text_to_analyse (str): text to be analyzed

    returns:
        str: text attribute of the BERT model response object on the analyzed text

    """
    # URL of the sentiment analysis service
    url = 'https://sn-watson-sentiment-bert.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/SentimentPredict'
    
    # header required for the API request
    header = {"grpc-metadata-mm-model-id": "sentiment_aggregated-bert-workflow_lang_multi_stock"}
    
    # dictionary with the text to be analyzed
    myobj = { "raw_document": { "text": text_to_analyse } }

    # send POST request to the API with the text and headers
    response = requests.post(url, json = myobj, headers=header)

    return response.text