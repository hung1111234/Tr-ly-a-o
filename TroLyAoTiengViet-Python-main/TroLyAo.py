# -*- coding: utf-8 -*-

import os
import playsound
import speech_recognition as sr
import time
import ctypes
import wikipedia
import datetime
import json
import re
import ctypes
import random
import urllib.request
import sys
import webbrowser
import smtplib
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from time import strftime
from gtts import gTTS
import youtubesearchpython
from youtube_search import YoutubeSearch
from email.mime.multipart import MIMEMultipart
from youtubesearchpython import VideosSearch
import pyttsx3
from googlesearch import search
# from newspaper import Article

#%% ngon ngu
wikipedia.set_lang('vi')
language = 'vi'
path = ChromeDriverManager().install()

#%%
def speak(text):
    print("Trợ lý ảo: {}".format(text))
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.say(text)
    engine.runAndWait()

#%%
def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Tôi: ", end='')
        audio = r.record(source, duration=5)
        try:
            text = r.recognize_google(audio, language="vi-VN")
            print(text)
            return text
        except:
            print("...")
            return None

#%%
def stop():
    speak("Hẹn gặp lại bạn sau!")
    
#%%
def get_text():
    for i in range(3):
        text = get_audio()
        if text:
            return text.lower()
        elif i < 2:
            speak("Tôi không nghe rõ. Bạn nói lại được không!")
    time.sleep(2)
    stop()
    return None

def search_google():
    query = "python programming"
    search_results = list(search(query, num_results=10))
    # Lấy ngẫu nhiên một đường link trong danh sách kết quả tìm kiếm
    random_link = random.choice(search_results)
    webbrowser.open(random_link)

#%%
def hello(name):
    day_time = int(strftime('%H'))
    if day_time < 12:
        speak("Chào buổi sáng bạn {}. Chúc bạn một ngày tốt lành.".format(name))
    elif 12 <= day_time < 18:
        speak("Chào buổi chiều bạn {}. Bạn đã dự định gì cho chiều nay chưa.".format(name))
    else:
        speak("Chào buổi tối bạn {}. Bạn đã ăn tối chưa nhỉ.".format(name))
        
#%%
def get_time(text):
    now = datetime.datetime.now()
    if "giờ" in text:
        speak('Bây giờ là %d giờ %d phút' % (now.hour, now.minute))
    elif "ngày" in text:
        speak("Hôm nay là ngày %d tháng %d năm %d" %
              (now.day, now.month, now.year))
    else:
        speak("Tôi chưa hiểu ý của bạn. Bạn nói lại được không?")

def search_youtube():
    text = get_text()
    search = VideosSearch(text)

    # Lấy kết quả tìm kiếm
    results = search.result()

    # Lấy một liên kết video ngẫu nhiên từ danh sách kết quả
    if len(results['result']) > 0:
        video_links = [result['link'] for result in results['result']]
        random_link = random.choice(video_links)
        webbrowser.open(random_link)
    else:
        print("Không tìm thấy kết quả phù hợp trên YouTube")

#%%
def open_application(text):
    if "google" in text:
        speak("Mở Google Chrome")
        os.startfile(
            r'C:\Program Files\Google\Chrome\Application\chrome.exe')
    elif "word" in text:
        speak("Mở Microsoft Word")
        os.startfile(
            r'C:\Program Files (x86)\Microsoft Office\root\Office16\WINWORD.EXE')
    elif "excel" in text:
        speak("Mở Microsoft Excel")
        os.startfile(
            r'C:\Program Files (x86)\Microsoft Office\root\Office16\EXCEL.EXE')
    elif "powerpoint" in text or "thuyết trình" in text:
        speak("Mở PowerPoint")
        os.startfile(
            r'C:\Program Files (x86)\Microsoft Office\root\Office16\POWERPNT.EXE')     
    else:
        speak("Ứng dụng chưa được cài đặt. Bạn hãy thử lại!")
        
#%%
def open_website(text):
    reg_ex = re.search('mở (.+)', text)
    if reg_ex:
        domain = reg_ex.group(1)
        url = 'https://www.' + domain
        webbrowser.open(url)
        speak("Trang web bạn yêu cầu đã được mở.")
        return True
    else:
        return False
    
#%%
def open_google_and_search(text):
    query = text
    # Tìm kiếm trên Google và lưu trữ các kết quả trong danh sách 'search_results'
    search_results = list(search(query, num_results=10))
    # Lấy ngẫu nhiên một đường link trong danh sách kết quả tìm kiếm
    random_link = random.choice(search_results)
    webbrowser.open(random_link)
    
#%%
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

#%%
def read_news():
    
    speak("Bạn muốn đọc báo về gì")
    
    queue = get_text()
    #queue = "Trump"
    params = {
        'apiKey': '9007bba8aca54b379ccba2964abac887',
        'q': queue,
    }
    api_result = requests.get('http://newsapi.org/v2/top-headlines?', params)
    api_response = api_result.json()
    print("Tin tức")

    for number, result in enumerate(api_response['articles'], start=1):
        print(f"""Tin {number}:\nTiêu đề: {result['title']}\nTrích dẫn: {result['description']}\nLink: {result['url']}\nNội dung: {result['content']}
    """)
        if number <= 3:
            webbrowser.open(result['url'])

#%%
def tell_me_about():
    try:
        speak("Bạn muốn nghe về gì ạ")
        time.sleep(2)
        text = get_text()
        contents = wikipedia.summary(text).split('\n')
        speak(contents[0])
        time.sleep(30)
        for content in contents[1:]:
            speak("Bạn muốn nghe thêm không")
            ans = get_text()
            if "có" not in ans:
                break    
            speak(content)
            time.sleep(30)
        time.sleep(3)
        speak('Cảm ơn bạn đã lắng nghe!!!')
    except:
        speak("Tôi không định nghĩa được thuật ngữ của bạn. Xin mời bạn nói lại")
        
#%%
def help_me():
    speak("""Tôi có thể giúp bạn thực hiện các câu lệnh sau đây:
    1. Chào hỏi
    2. Hiển thị giờ
    3. Mở website, application
    4. Tìm kiếm trên Google
    5. Dự báo thời tiết
    6. Mở video trên youtube
    7. Đọc báo hôm nay
    8. Kể bạn biết về thế giới""")
    time.sleep(22)

#%%
def assistant():
    speak("Xin chào, bạn tên là gì nhỉ?")
    time.sleep(2)
    s = get_text().split()
    name = s[-1]
    if name:
        speak("Chào bạn {}".format(name))
        time.sleep(2)
        speak("Bạn cần tôi giúp gì ạ?")
        while True:
            time.sleep(3)
            text = get_text()
            if not text:
                break
            elif "dừng" in text or "tạm biệt" in text or "tạm biệt robot" in text or "ngủ thôi" in text:
                stop()
                break
            elif "có thể làm gì" in text or 'làm được gì' in text:
                help_me()
            elif "chào trợ lý ảo" in text or "Xin chào" in text:
                hello(name)
            elif "hiện tại" in text or "mấy giờ" in text:
                get_time(text)
            elif "mở" in text:
                if 'mở google và tìm kiếm' in text:
                    open_google_and_search(text)
                elif "." in text:
                    open_website(text)
                elif "youtube" in text or "bài hát" in text:
                    search_youtube()
                else:
                    open_application(text)
            elif "youtube" in text:
                search_youtube(text)
            elif "thời tiết" in text:
                current_weather()
            elif "đọc báo" in text:
                read_news()
            elif "định nghĩa" in text or "cho tôi biết" in text or "tôi muốn biết" in text:
                tell_me_about()
            else:
                speak("Bạn cần tôi giúp gì ạ?")
#%%
assistant()