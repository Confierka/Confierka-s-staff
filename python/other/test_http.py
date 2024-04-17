import requests
import time
week_days=[
    "Понедельник",
    "Вторник",
    "Среда",
    "Четверг",
    "Пятница",
    "Суббота",
    "Воскресенье"
]



def get_weather():
    result = requests.get('https://api.open-meteo.com/v1/forecast?latitude=55.75&longitude=37.62&hourly=temperature_2m')




    temp = result.json()['hourly']['temperature_2m']
    times = result.json()['hourly']['time']
    zipped = list(zip(times,temp))

    response=[]

    for t, tmp in zipped:
        parsed=(time.strptime(t,"%Y-%m-%dT%H:%M")) 

        if parsed.tm_hour==12:
            response.append((parsed.tm_wday,tmp))