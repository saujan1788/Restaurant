from flask import Flask, request, render_template
import requests
from dotenv import load_dotenv
import os

#Load environment variables from .env file
load_dotenv()

app = Flask(__name__)
api_key = os.getenv('OPENWEATHER_API_KEY') #Get API Key from environment variable

@app.route('/')
def home():
    city = request.args.get('city','Dublin')
    weather_data = get_weather(city)
    return render_template('index.html',weather=weather_data, city = city)

def get_weather(city):
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    response = requests.get(url)
    return response.json()

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000)






