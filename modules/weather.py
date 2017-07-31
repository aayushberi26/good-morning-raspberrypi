import requests
import json

def request_weather(url, key, zip_code, units='imperial'):
    '''
    Makes a request to the openweathermap forecast api and returns data for todays forcast.
    Returns a string with the day's high and low temperature, average wind speed, and weather
    conditions
    '''
    r = requests.get(url + str(zip_code) + '&appid=' + key + '&units=' + units)
    response = r.json()

    # response has weather in 3 hour segments for 5 days, want only todays weather
    todays_forecast = response["list"][0:7]
    min_temp = 125.0
    max_temp = -25.0
    wind = 0
    conditions = {}

    for time_segment in todays_forecast:
        wind += time_segment['wind']['speed']
        if time_segment['main']['temp_min'] < min_temp:
            min_temp = time_segment['main']['temp_min']
        if time_segment['main']['temp_max'] > max_temp:
            max_temp = time_segment['main']['temp_min']
        for subsegment in time_segment['weather']:
            # keep track of the time_segments each condition occurs in
            if subsegment['description'] not in conditions:
                conditions[subsegment['description']] = [convert_military_time(time_segment['dt_txt'].split(' ')[1][0:5])]
            else:
                conditions[subsegment['description']].append(convert_military_time(time_segment['dt_txt'].split(' ')[1][0:5]))
    
    avg_wind = float(wind) / len(todays_forecast)
    
    parsed_response = "Today's forecast: high %.2f, low %.2f, average wind %.2f MPH. Conditions: " %(max_temp, min_temp, avg_wind)
    if len(conditions) == 1:
        parsed_response += conditions.keys[0]
    else:
        for condition in conditions:
            parsed_response += condition + ': '
            for time_interval in conditions[condition]:
                parsed_response += time_interval + ', '
            parsed_response = parsed_response[:-2] + ' '

    return parsed_response

def convert_military_time(time):
    hour = int(time[0:2])
    if hour == 0:
        hour = 12
    if hour <= 12:
        return time + ' AM'
    else:
        return str(hour - 12) + ':00 PM'