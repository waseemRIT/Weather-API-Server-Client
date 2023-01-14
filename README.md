# Weather Data Server and Client

This project provides a server that fetches and provides weather data for a given city using the OpenWeatherMap API. It also includes a client that makes requests to the server to fetch the list of cities and weather data for a selected city.

## Server
The server is built using Flask, a lightweight web framework for Python. It uses the ThreadingMixIn class to handle multiple clients simultaneously by creating a new thread for each incoming request. The server retrieves the API key from an environment variable, and has two routes:

* /weather/<city>: returns the weather data for the given city in JSON format.
* /cities: returns the list of cities in JSON format.

## Client
The client is built using the requests library in Python. It makes GET requests to the server's routes to fetch the list of cities and weather data for a selected city, and then parses the JSON response and prints the data.

## Future Work
* Implement user authentication and authorization for the server
* Add the ability for the client to input a new city to fetch the weather for
* Add more data points to the weather data such as the city's name, and time of the data
* Build a UI for the client application
* Implement caching mechanism for weather data
* Add support for more weather APIs

## Note
The code is provided as an example and will not work as is. You will need to sign up for an API key from OpenWeatherMap to run the code.


## Installation
To run this project, you will need to have Python 3 and pip installed on your machine. Follow these steps to set up the project:

* Clone the repository by running git clonehttps://github.com/waseemRIT/WeatherApi.git
* Navigate to the project directory by running cd WeatherApi
* Create a virtual environment by running python -m venv venv
* Activate the virtual environment by running source venv/bin/activate (on Linux/macOS) or venv\Scripts\activate (on Windows)
* Install the required dependencies by running pip install -r requirements.txt
* You will also need to sign up for an API key from OpenWeatherMap and set it as an environment variable named "WEATHERAPI" on your machine.
* Make sure that you are in the project directory before running the above commands.

## Running the Server and Client
To run the server, navigate to the project directory in the command line and run python server.py.
To run the client, navigate to the project directory in the command line and run python client.py.

## Contribution
If you would like to contribute to this project, please fork the repository, make your changes and submit a pull request.

## Acknowledgments
This project uses the OpenWeatherMap API to fetch weather data. More information about the API and its usage can be found here:
https://openweathermap.org/api

## Support
If you have any questions or issues, please open an issue on the repository, reach out to me directly via my linkedin, Waseem Qaffaf, (https://www.linkedin.com/in/waseem-qaffaf/) or email me at realwaseemqaffaf@gmail.com.
