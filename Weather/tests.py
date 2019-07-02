
from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/weather', methods=['POST'])
def temperature():
    zipcode = request.form['zip']
    r = requests.get('http://api.openweathermap.org/data/2.5/weather?zip='+zipcode+',us&units=imperial&mode=html&appid=bf357a3c897f482670e76847febb1cb5')
    return zipcode


    #return render_template('weather.html')
    

@app.route('/')
def home():
    return render_template('home.html')


if __name == '__main__':
    app.run(debug=True)

# Create your tests here.
