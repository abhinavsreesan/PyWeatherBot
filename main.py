import os
import requests

# Import Environment Variables
WEATHER_API_KEY = os.getenv('WEATHER_API_KEY')
LOCATION = os.getenv('LOCATION')
BOT_API_KEY = os.getenv('BOT_API_KEY')
CHANNEL_NAME = os.getenv('CHANNEL_NAME')

# Weather API URL
weather_url = (f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{LOCATION}"
               f"?unitGroup=us&include=current&key={WEATHER_API_KEY}&contentType=json")


def convert_temp(temp: float) -> float:
    """Converts temperature from Fahrenheit to Celsius
    :param temp: Temperature in Fahrenheit
    :return: Temperature in Celsius
    """
    return round((temp - 32) * 5.0/9.0, 2)


def create_icon(icon: str) -> str:
    """Creates an emoji icon based on the weather condition
    :param icon: str
    :return: Emoji icon
    """
    if icon == 'clear-day':
        return '\U00002600'
    elif icon == 'clear-night':
        return '\U0001F319'
    elif icon == 'rain':
        return '\U00002614'
    elif icon == 'snow':
        return '\U0001F328'
    elif icon == 'sleet':
        return '\U0001F328'
    elif icon == 'wind':
        return '\U0001F32C'
    elif icon == 'fog':
        return '\U0001F32B'
    elif icon == 'cloudy':
        return '\U00002601'
    elif icon == 'partly-cloudy-day':
        return '\U000026C5'
    elif icon == 'partly-cloudy-night':
        return '\U0001F319'
    else:
        return '\U0001F32B'


if __name__ == '__main__':
    try:
        resp = requests.get(weather_url)
        resp.raise_for_status()
    except requests.exceptions.HTTPError as err:
        print(f"Error: {err}")
        exit(1)
    forecast = resp.json()['currentConditions']
    output_str=(f"""
          Todays Weather in {resp.json()['resolvedAddress']} is as follows {create_icon(forecast['icon'])}:
          Temperature: {convert_temp(forecast['temp'])}°C
          Wind Speed: {forecast['windspeed']} mph
          Feels Like: {convert_temp(forecast['feelslike'])} °C
          Humidity: {forecast['humidity']}
          PrecipProb: {forecast['precipprob']}
          Precipitation: {forecast['precip']} inches
          Visibility: {forecast['visibility']} miles
          Cloud Cover: {forecast['cloudcover']} """)
    # print(output_str)
    resp = requests.get(f'https://api.telegram.org/bot{BOT_API_KEY}/sendMessage',
                 params={'chat_id': CHANNEL_NAME,
                         'text': output_str})