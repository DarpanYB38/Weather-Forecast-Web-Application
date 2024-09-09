from flask import Flask, render_template, request
import requests
import datetime

app = Flask(__name__)

API_KEY = 'ad28d833fae6f220c2ff6192a039bfc7'  # Your actual API key

@app.route('/', methods=['GET','POST'])
def index():
    city = 'Bengaluru' # Default city
    if request.method == 'POST':
        city = request.form.get('city')

    weather_data = get_weather(city)
    
    if weather_data:
        return render_template('index.html', weather_data=weather_data)
    else:
        # Still render the template, but pass weather_data=None
        return render_template('index.html', weather_data=None)

def get_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)

    print(response.status_code, response.text)

    if response.status_code == 200:
        data = response.json()

         # Get current time based on timezone
        timezone_offset = data['timezone']  # Timezone offset in seconds
        utc_now = datetime.datetime.utcnow()  # Current UTC time
        local_time = utc_now + datetime.timedelta(seconds=timezone_offset)  # Local time in the city

        # Convert sunrise and sunset from UNIX timestamp to human-readable time
        sunrise = datetime.datetime.utcfromtimestamp(data['sys']['sunrise'] + timezone_offset).strftime('%H:%M:%S')
        sunset = datetime.datetime.utcfromtimestamp(data['sys']['sunset'] + timezone_offset).strftime('%H:%M:%S')


        weather = {
            'city': city,
            'temperature': data['main']['temp'],
            'description': data['weather'][0]['description'],
            'icon': data['weather'][0]['icon'],
            'humidity': data['main']['humidity'],  # Additional data: Humidity
            'wind_speed': data['wind']['speed'],  # Additional data: Wind Speed
            'sunrise': sunrise,  # Sunrise time
            'sunset': sunset,    # Sunset time
            'local_time': local_time.strftime('%Y-%m-%d %H:%M:%S')
        }
        return weather
    else:
        print("Error fetching weather data:", response.text)
        return None

if __name__ == '__main__':
    app.run(debug=True)
