"""This Module controls the application Emotion Detector"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def detect_emotion():
    """This function detects the emotion based on AI and given test of a user"""
    text_to_analyze = request.args.get('textToAnalyze')
    result =  emotion_detector(text_to_analyze)
    string_to_return = f'''For the given statement, the system response is
    'anger': {result['anger']}, 
    'disgust': {result['disgust']}, 
    'fear': {result['fear']}, 
    'joy': {result['joy']} 
    and 'sadness': {result['sadness']}. 
    The dominant emotion is {result['dominant_emotion']}.    
    '''
    if result['dominant_emotion'] is None:
        return "Invalid text! Please try again!"
    return string_to_return
@app.route("/")
def show_homepage():
    """This function renders the homepage"""
    return render_template("index.html")
if __name__ == "__main__":
    app.run("0.0.0.0", port = 5000)
