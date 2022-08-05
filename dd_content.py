import csv
import json
import random
import datetime
from urllib import request


def get_random_quote(quotes_file='quotes.csv'):
    try:
        with open(quotes_file) as csv_file:
            quotes = [{'author': line[0], 'quote': line[1]} for line in csv.reader(csv_file, delimiter='|')]
    except Exception as e:
        quotes = [{'author': 'Eric Idle', 'quote': 'Always look on the bright side of life'}]

    return random.choice(quotes)


def get_weather_forecast(coords={'lat': 28.4717, 'lon': -80.5378}):
    try:
        api_key = 'ed2dcc3c7ccf72b5199ea6954b60a337'
        url = f'https://api.openweathermap.org/data/2.5/forecast?units=metric&lat={coords["lat"]}&lon={coords["lon"]}&appid={api_key}'
        data = json.load(request.urlopen(url))

        forecast = {'city': data['city']['name'],
                    'country': data['city']['country'],
                    'periods': list()}

        for period in data['list'][0:9]:
            forecast['periods'].append({'timestamp': datetime.datetime.fromtimestamp(period['dt']),
                                        'temp': round(period['main']['temp']),
                                        'description': period['weather'][0]['description'].title(),
                                        'icon': f'https://openweathermap.org/img/wn/{period["weather"]}'})

        return forecast

    except Exception as e:
        print(e)


def get_wikipedia_article():
    try:
        data = json.load(request.urlopen('https://en.wikipedia.org/api/rest_v1/page/random/summary'))

        return {'title': data['title'],
                'extract': data['extract'],
                'url': data['content_urls']['desktop']['page']}
    except Exception as e:
        print(e)


if __name__ == '__main__':
    """test get_random_quote()"""
    quote = get_random_quote()
    print(quote)

    """test get_weather_forecast()"""
    test_forecast = get_weather_forecast()
    if test_forecast:
        print(f'\nWeather forecast for {test_forecast["city"]}, {test_forecast["country"]} is:')

        for test_period in test_forecast['periods']:
            print(f' - {test_period["timestamp"]} | {test_period["temp"]} | {test_period["description"]}')

    general_toshevo = {'lat': 43.7017, 'lon': 28.0396}
    test_forecast = get_weather_forecast(general_toshevo)
    if test_forecast:
        print(f'\nWeather forecast for {test_forecast["city"]}, {test_forecast["country"]} is:')

        for test_period in test_forecast['periods']:
            print(f' - {test_period["timestamp"]} | {test_period["temp"]} | {test_period["description"]}')

    invalid = {'lat': 33343.7017, 'lon': 28.0396}
    test_forecast = get_weather_forecast(invalid)
    if test_forecast:
        print(f'\nWeather forecast for {test_forecast["city"]}, {test_forecast["country"]} is:')

        for test_period in test_forecast['periods']:
            print(f' - {test_period["timestamp"]} | {test_period["temp"]} | {test_period["description"]}')
    else:
        print('Invalid coords')

    """test get_wikipedia_article()"""
    article = get_wikipedia_article()
    print(f'\nTitle: {article["title"]}\nSummary: {article["extract"]}\nURL: {article["url"]}')
