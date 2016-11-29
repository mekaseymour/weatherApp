from flask import Flask, render_template, request #this is the request object in Flask, not to be confused with the requests library
import requests #need this library to call APIs

app = Flask(__name__)

@app.route('/temperature', methods=['POST'])
def temperature():
    zipcode = request.form['zip']
    # next step is to call the API
    # the response will be 'r'
    r = requests.get('http://api.openweathermap.org/data/2.5/weather?zip='+zipcode+',us&appid=e3a4f9f6b0e0a983ba5b78cb1c724f81')
    # use the below line just to display the text --
    # json_object = r.text
    # use the below line to parse the json
    json_object = r.json()
    # the temperature we want to display is burried two layers deep in the JSON
    temp_k = float(json_object['main']['temp'])
    # convert temp_k to temperature in Fahrenheit
    temp_f = (temp_k - 273.15) * 1.8 + 32
    return render_template('temperature.html', temp=temp_f)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
