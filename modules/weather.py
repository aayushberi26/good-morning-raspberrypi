import requests
import json

def request_weather(url, location_code, api_key):
    '''
    Makes a request to the openweathermap forecast api and returns data for todays forcast.
    Returns a string with the day's high and low temperature, average wind speed, and weather
    conditions
    '''
    try:
        r = requests.get(url + str(location_code) + '?apikey=' + api_key)
        data = r.json()
        print(data)
        data = data['DailyForecasts'][0]
        low = data['Temperature']['Minimum']['Value']
        high = data['Temperature']['Maximum']['Value']
        day = data['Day']['IconPhrase']
        night = data['Night']['IconPhrase']
        return 'High: ' + str(high) + ', Low: ' + str(low) + ', Day: ' + day + ', Night: ' + night
    except:
        return None

if __name__ == '__main__':
    url = 'http://dataservice.accuweather.com/forecasts/v1/daily/1day/'
    location_code = '2102599'
    api_key = 'D7APbGqGf38GnNIAs1vPGgQkumgdAWZw'
    print(request_weather(url, api_key, location_code))
