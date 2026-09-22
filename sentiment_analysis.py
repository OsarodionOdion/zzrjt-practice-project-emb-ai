# Function for running sentiment analysis using the Watson NLP BERT Sentiment Analysis function.

'''
URL, headers and input JSON format for accessing the BERT based Sentiment Analysis function of the Watson NLP Library

URL: 'https://sn-watson-sentiment-bert.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/SentimentPredict'
Headers: {"grpc-metadata-mm-model-id": "sentiment_aggregated-bert-workflow_lang_multi_stock"}
Input json: { "raw_document": { "text": text_to_analyse } }

'''

def sentiment_analyzer(text_to_analyse):
    
    url = 'https://sn-watson-sentiment-bert.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/SentimentPredict'
    header = {"grpc-metadata-mm-model-id": "sentiment_aggregated-bert-workflow_lang_multi_stock"}
    myobj = { "raw_document": { "text": text_to_analyse } }
    response = requests.post(url, json = myobj, headers=header)

    return response.text