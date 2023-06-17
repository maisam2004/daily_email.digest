import csv,random

from urllib import request
import json
import datetime
import tweepy

#openweathermap.org




def get_random_quote(quotes_file='quotes.csv'):
    try:
        with open(quotes_file , '+r')as quotes_csv:

            csv_file =  csv.reader(quotes_csv,delimiter='|',)
            quotes = [{'author':row[0],'quote':row[1]} for row in csv_file]
    except Exception as e:
        quotes = [{'author': 'Eric Idle',
                    'quote': 'Always Look on the Bright Side of Life.'}]
    return random.choice(quotes)

def get_weather_forecast(coords=None):

    if coords is None:
        coords = {'lat': 28.4717, 'lon': -80.5378}
    try: # retrieve forecast for specified coordinates
        api_key = 'YOUR OPENWEATHERMAP API KEY GOES HERE' # replace with your own OpenWeatherMap API key
        url = f'https://api.openweathermap.org/data/2.5/forecast?lat={coords["lat"]}&lon={coords["lon"]}&appid={api_key}&units=metric'
        data = json.load(request.urlopen(url))

        forecast = {'city': data['city']['name'], # city name
                    'country': data['city']['country'], # country name
                    'periods': list()} # list to hold forecast data for future periods

        for period in data['list'][0:9]: # populate list with next 9 forecast periods 
            forecast['periods'].append({'timestamp': datetime.datetime.fromtimestamp(period['dt']),
                                        'temp': round(period['main']['temp']),
                                        'description': period['weather'][0]['description'].title(),
                                        'icon': f'http://openweathermap.org/img/wn/{period["weather"][0]["icon"]}.png'})
        return forecast
    except Exception as e:
        print(e)

def get_twitter_trends():#tweepy
    try: # retrieve Twitter trends for specified location
        api_key = 'YOUR TWITTER API KEY GOES HERE' # replace with your own Twitter API key
        api_secret_key = 'YOUR TWITTER API SECRET KEY GOES HERE' # replace with your own Twitter API secret key
        auth = tweepy.AppAuthHandler(api_key, api_secret_key)
        return tweepy.API(auth).trends_place(woeid)[0]['trends'] # NOTE: Tweepy 4.0.0 renamed the 'trends_place' method to 'get_place_trends'

    except Exception as e:
        print(e)

def get_wikipedia_article():
    try:
        data = json.load(request.urlopen('https://en.wikipedia.org/api/rest_v1/page/random/summary'))
        return{'title':data['title'],'extract':data['extract'],'url':data['content_urls']['desktop']['page']}
    except Exception as e:
        print(e)
    
if __name__ =='__main__':

    qoute =get_random_quote()
    print(f'randome author > {qoute["author"]} + and qoute>> {qoute["quote"]}')

    qoute = get_random_quote(quotes_file=None)
    print(f'randome author > {qoute["author"]} + and qoute>> {qoute["quote"]}')


    forecast = get_weather_forecast() # get forecast for default location
    if forecast:
        print(f'\nWeather forecast for {forecast["city"]}, {forecast["country"]} is...')
        for period in forecast['periods']:
            print(f' - {period["timestamp"]} | {period["temp"]}°C | {period["description"]}')

    austin = {'lat': 30.2748,'lon': -97.7404} # coordinates for Texas State Capitol
    forecast = get_weather_forecast(coords = austin) # get Austin, TX forecast
    if forecast:
        print(f'\nWeather forecast for {forecast["city"]}, {forecast["country"]} is...')
        for period in forecast['periods']:
            print(f' - {period["timestamp"]} | {period["temp"]}°C | {period["description"]}')

    invalid = {'lat': 1234.5678 ,'lon': 1234.5678} # invalid coordinates
    forecast = get_weather_forecast(coords = invalid) # get forecast for invalid location
    if forecast is None:
        print('Weather forecast for invalid coordinates returned None')

    ##### test get_twitter_trends() #####
    print('\nTesting Twitter trends retrieval...')

    trends = get_twitter_trends() # get trends for default location of United States
    if trends:
        print('\nTop 10 Twitter trends in the United States are...')
        for trend in trends[0:10]: # show top ten
            print(f' - {trend["name"]}: {trend["url"]}')

    trends = get_twitter_trends(woeid = 44418) # get trends for London
    if trends:
        print('\nTop 10 Twitter trends in London are...')
        for trend in trends[0:10]: # show top ten
            print(f' - {trend["name"]}: {trend["url"]}')

    trends = get_twitter_trends(woeid = -1) # invalid WOEID
    if trends is None:
        print('Twitter trends for invalid WOEID returned None')

    ##### test wikipedia () #####
    article = get_wikipedia_article()
    if article:
        print(f'\n{article["title"]}\n<{article["url"]}>\n{article["extract"]}')