from flask import Flask, request, jsonify
import speech_recognition as sr
import pyttsx3
import google.generativeai as genai

app = Flask(__name__)

recognizer = sr.Recognizer()
genai.configure(api_key='AIzaSyBPJoPtPj-sZTTAkmOOzdeYtuxqib3UvNg')  

@app.route('/process_audio', methods=['POST'])
def process_audio():
    data = request.json
    listen = data.get('audio')

    if listen:
        try:
            txt = recognize_speech(listen)
            generated_text = generate_content(txt)
            return jsonify({'text': generated_text}), 200
        except Exception as e:
            return jsonify({'error': str(e)}), 500
    else:
        return jsonify({'error': 'No audio provided'}), 400

def recognize_speech(audio):
    with sr.AudioFile(audio) as source:
        audio_data = recognizer.record(source)
        txt = recognizer.recognize_google(audio_data)
        return txt

def generate_content(listen):
    if listen:
        model = genai.GenerativeModel('gemini-pro')
        response = model.generate_content(listen)
        return response.text
    else:
        return "Sorry, Could not understand audio, Please repeat"

if __name__ == '__main__':
    app.run(debug=True)
