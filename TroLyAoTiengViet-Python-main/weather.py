from TroLyAo import speak, get_text
import time
import datetime
import requests
def current_weather():
    speak("Bạn muốn xem thời tiết ở đâu ạ.")
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    time.sleep(2)
    city = get_text()
    if not city:
        pass
    api_key = "5f9242d740d1e6278e390d5fd21a3881"
    call_url = base_url + "appid=" + api_key + "&q=" + city 
    response = requests.get(call_url)
    data = response.json()
    if data["cod"] != "404":
        city_res = data["main"]
        current_temperature = city_res["temp"]
        current_pressure = city_res["pressure"]
        current_humidity = city_res["humidity"]
        
        wthr = data["weather"]
        weather_description = wthr[0]["description"]
        now = datetime.datetime.now()
        content = """
        Hôm nay là ngày {day} tháng {month} năm {year}
        Nhiệt độ trung bình là {temp} độ Kelvin
        Áp suất không khí là {pressure} héc tơ Pascal
        Độ ẩm là {humidity}%
        Trời hôm nay quang mây. Dự báo mưa rải rác ở một số nơi.""".format(day = now.day,month = now.month, year= now.year, 
                                                                           temp = current_temperature, pressure = current_pressure, humidity = current_humidity)
        speak(content)
        time.sleep(20)
    else:
        speak("Tôi không tìm thấy địa chỉ nơi bạn muốn biết thời tiết")
current_weather()