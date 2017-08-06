import requests

def request_weather(url, location_code, api_key):
    '''
    Makes a request to the openweathermap forecast api and returns data for todays forcast.
    Returns a string with the day's high and low temperature, average wind speed, and weather
    conditions
    '''
    try:
        r = requests.get(url + str(location_code) + '?apikey=' + api_key)
        data = r.json()
        data = data['DailyForecasts'][0]
        low = data['Temperature']['Minimum']['Value']
        high = data['Temperature']['Maximum']['Value']
        day = data['Day']['IconPhrase']
        night = data['Night']['IconPhrase']
        return 'Temp: ' + str(high) + ' - ' + str(low) + ', Day: ' + day + ', Night: ' + night
    except:
        return None
