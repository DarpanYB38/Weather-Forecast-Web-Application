# Weather-Forecast-Web-Application
A weather forecast web application built with Flask and OpenWeatherMap API. This application allows users to input a city name and retrieve real-time weather data, including temperature, description, humidity, wind speed, sunrise, sunset, and the current local time.

## Features 
- City Selection : Input any city name to get the weather forecast.
- Current Weather: Display temperature, description, weather icon, humidity, wind speed.
- Sunrise and Sunset : Show sunrise and sunset times in the city.
- Local Time : Show the current local time based on the city's timezone.

## Technologies Used 
- Python : Programmig language used for backend logic.
- Flask : Web framework used to build the web application.
- OpenWeatherMap API: Provides real-time weather data.
- Bootstrap: Framework used for responsive and stylish UI.
- HTML/CSS: Markup and styling for the web pages.

## Installation

1. **Clone the repository**:

    ```bash
    git clone https://github.com/yourusername/weather-forecast-app.git
    ```

2. **Navigate to the project directory**:

    ```bash
    cd weather-forecast-app
    ```

3. **Set up a virtual environment**:

    ```bash
    python3 -m venv venv
    ```

4. **Activate the virtual environment**:

    - On Windows:

        ```bash
        venv\Scripts\activate
        ```

    - On macOS/Linux:

        ```bash
        source venv/bin/activate
        ```

5. **Install the required dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

6. **Set your OpenWeatherMap API key**:

    Create a `.env` file in the root directory and add your API key:

    ```bash
    API_KEY=your_openweathermap_api_key
    ```

7. **Run the application**:

    ```bash
    python app.py
    ```

8. **Open your web browser** and go to `http://127.0.0.1:5000/` to see the application in action.


## Usage 
1. Enter a city name into the input field on the homepage.
2. Click "Get Weather" to retrieve the weather data for the entered city.
3. View the weather details including temperature, description, local time, humidity, wind speed, sunrise, and     
   sunset times.
   
## Contributing
Feel free to fork the repository and submit pull requests. For any issues or feature requests, please open an issue in the GitHub repository.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Contact

For any questions or feedback, you can reach me at darpanbrahma@gmail.com.

