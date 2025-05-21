''' This script initiates the Flask web application for emotion detection.
    It runs on localhost:8000 and provides two main routes:
    - '/' for rendering the main HTML page.
    - '/emotionDetector' for processing text and returning emotion analysis.
'''
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_detector():
    '''
    This function handles the '/emotionDetector' route.
    It retrieves the text from the 'textToAnalyze' query parameter,
    sends it to the emotion_detector function for analysis,
    and formats the response to be displayed to the user.
    It also includes basic error handling for invalid input text.
    '''
    text_to_analyze = request.args.get("textToAnalyze")
    response = emotion_detector(text_to_analyze)
    anger = response["anger"]
    disgust = response["disgust"]
    fear = response["fear"]
    joy = response["joy"]
    sadness = response["sadness"]
    dominant_emotion = response["dominant_emotion"]
    if dominant_emotion is None:
        return "Invalid text! Please try again!"
    return (f"For the given statement, the system response is "
        f"'anger': {anger}, 'disgust': {disgust}, 'fear': {fear}, "
        f"'joy': {joy}, 'sadness': {sadness}. "
        f"The dominant emotion is {dominant_emotion}.")

@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page (index.html) over the Flask channel.
    '''
    return render_template("index.html")

if __name__ == "__main__":
    # This function executes the Flask app and deploys it on localhost:8000
    app.run(host="0.0.0.0", port=8000, debug=True)
