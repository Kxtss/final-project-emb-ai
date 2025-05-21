import requests
import json

def emotion_detector(text_to_analyse):
    URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    my_obj = { "raw_document": { "text": text_to_analyse } }
    response = requests.post(url = URL, json = my_obj, headers = header)
    if response.status_code == 200:
        formatted_response = json.loads(response.text)
        emotion_scores = {
            "anger": formatted_response["emotionPredictions"][0]["emotion"]["anger"],
            "disgust": formatted_response["emotionPredictions"][0]["emotion"]["disgust"],
            "fear": formatted_response["emotionPredictions"][0]["emotion"]["fear"],
            "joy": formatted_response["emotionPredictions"][0]["emotion"]["joy"],
            "sadness": formatted_response["emotionPredictions"][0]["emotion"]["sadness"]
        }
        dominant_emotion = max(emotion_scores, key = emotion_scores.get)
        return {
            "anger": emotion_scores["anger"],
            "disgust": emotion_scores["disgust"],
            "fear": emotion_scores["fear"],
            "joy": emotion_scores["joy"],
            "sadness": emotion_scores["sadness"],
            "dominant_emotion": dominant_emotion
            }
    elif response.status_code == 400:
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None
        }
    return {
        "anger": None,
        "disgust": None,
        "fear": None,
        "joy": None,
        "sadness": None,
        "dominant_emotion": None
    }
