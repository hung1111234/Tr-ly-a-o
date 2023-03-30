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
from gtts import gTTS

#%% ngon ngu
wikipedia.set_lang('vi')
language = 'vi'
path = ChromeDriverManager().install()
flag = 1

print("Trợ lý ảo: Tôi có thể giao tiếp với bạn qua 2 cách sau:")
print("Chọn 1: Tôi sẽ giao tiếp với bạn qua giọng nói")
print("Chọn 2: Tôi sẽ giao tiếp với bạn qua tin nhắn")
print("Vui lòng nhập: ", end='')
while True:
    flag = int(input())
    if flag != 1 and flag != 2:
        print("Bạn đã nhập sai, vui lòng nhập lại: ", end='')
    else: break

#%%
def speak(text):
    print("Trợ lý ảo: {}".format(text))
    if flag == 1:
        tts = gTTS(text = text,lang='vi')
        tts.save("sound.mp3")
        playsound.playsound("sound.mp3")
        os.remove("sound.mp3")
        # engine = pyttsx3.init()
        # voices = engine.getProperty('voices')
        # engine.setProperty('voice', voices[1].id)
        # engine.say(text)
        # engine.runAndWait()


#%%
def get_audio():
    if flag == 1:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Tôi: ", end='')
            audio = r.record(source, duration=5)
            try:
                text = r.recognize_google(audio, language="vi-VN")
                print(text)
                return text
            except:
                print()
                speak("Nếu bạn không tiện nói bạn có thể nhập")
                text = input("Tôi: ")
                return text
    else:
        print("Tôi: ", end='')
        text = input()
        return text

#%%
def stop():
    speak("Hẹn gặp lại bạn sau!")
    
#%%
def get_text():
    for i in range(10000):
        text = get_audio()
        if text:
            return text.lower()
        # elif flag == 1:
        #     speak("Tôi không nghe rõ. Bạn nói lại được không!")
        elif flag == 2:
            speak("Bạn đã nhập sai, vui lòng nhập lại:")
    time.sleep(2)
    stop()
    return None   

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
    if flag == 1: speak("Vui lòng nói từ khóa tìm kiếm:")
    if flag == 2: speak("Vui lòng nhập từ khóa tìm kiếm:")
    text = get_text()
    search = VideosSearch(text)

    # Lấy kết quả tìm kiếm
    results = search.result()

    # Lấy một liên kết video ngẫu nhiên từ danh sách kết quả
    if len(results['result']) > 0:
        video_links = [result['link'] for result in results['result']]
        random_link = random.choice(video_links)
        webbrowser.open(random_link)
        speak("Video đã mở thành công")
    else:
        print("Không tìm thấy kết quả phù hợp trên YouTube")

#%%
def open_application(text):
    if "google" in text:
        speak("Mở Google Chrome")
        os.startfile(r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe")
    elif "zalo" in text:
        speak("Mở Zalo")
        os.startfile(r'C:\Users\ADMIN\AppData\Local\Programs\Zalo\Zalo.exe')
    elif "word" in text:
        speak("Mở Microsoft Word")
        os.startfile(r"C:\Program Files\Microsoft Office\root\Office16\WINWORD.EXE")
    elif "excel" in text:
        speak("Mở Microsoft Excel")
        os.startfile(r"C:\Program Files\Microsoft Office\root\Office16\EXCEL.EXE")
    elif "powerpoint" in text or "thuyết trình" in text:
        speak("Mở PowerPoint")
        os.startfile(r"C:\Program Files\Microsoft Office\root\Office16\POWERPNT.EXE")     
    elif "zoom" in text:
        speak("Mở Zoom")
        os.startfile(r"C:\Users\ADMIN\AppData\Roaming\Zoom\bin\Zoom.exe")     
    elif "c++" in text:
        speak("Mở Dev C++")
        os.startfile(r"C:\Program Files (x86)\Dev-Cpp\devcpp.exe")     
    elif "java" in text:
        speak("Mở Apache NetBeans")
        os.startfile(r"C:\Program Files\NetBeans-15\netbeans\bin\netbeans64.exe")
    else:
        speak("Ứng dụng chưa được cài đặt. Bạn hãy thử lại!")
    
#%%
def open_google_and_search():
    if flag == 1: speak("Vui lòng nói từ khóa tìm kiếm:")
    if flag == 2: speak("Vui lòng nhập từ khóa tìm kiếm:")
    query = get_text()
    # Tìm kiếm trên Google và lưu trữ các kết quả trong danh sách 'search_results'
    try:
        search_results = list(search(query, num_results=10))
        # Lấy ngẫu nhiên một đường link trong danh sách kết quả tìm kiếm
        if len(search_results) > 0:
            random_link = random.choice(search_results)
            webbrowser.open(random_link)
            speak("Trang web đã mở thành công")
    except: speak("Tôi không tìm thấy kết quả này trên google")
    
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
        time.sleep(10)
        for content in contents[1:]:
            speak("Bạn muốn nghe thêm không")
            ans = get_text()
            if "có" not in ans:
                break    
            speak(content)
            time.sleep(10)
        time.sleep(3)
        speak('Cảm ơn bạn đã lắng nghe!!!')
    except:
        speak("Tôi không định nghĩa được thuật ngữ của bạn. Xin mời bạn thực hiện lại thao tác")
        
#%%
def help_me():
    speak("Tôi có thể giúp bạn thực hiện các câu lệnh sau đây:")
    print("""
    1. Chào hỏi
    2. Hiển thị giờ
    3. Mở Application
    4. Tìm kiếm trên Google
    5. Dự báo thời tiết
    6. Mở video trên youtube
    7. Đọc báo hôm nay
    8. Tìm thông tin của một thuật ngữ, một người""")
    time.sleep(2)

#%%
def assistant():
    speak("Xin chào, bạn tên là gì nhỉ?")
    time.sleep(1)
    s = get_text().split()
    name = s[-1]
    if name:
        speak("Chào bạn {}".format(name[0:1].upper() + name[1:]))
        time.sleep(2)
        speak("Bạn cần tôi giúp gì ạ?")
        while True:
            time.sleep(3)
            text = get_text()
            if not text:
                break
            elif "dừng" in text or "stop" in text or "tạm biệt" in text or "ngủ thôi" in text:
                stop()
                break
            elif "làm gì" in text or 'làm được gì' in text:
                help_me()
            elif "chào trợ lý ảo" in text or "Xin chào" in text:
                hello(name)
            elif "hiện tại" in text or "mấy giờ" in text:
                get_time(text)
            elif "tìm kiếm" in text or "trên google" in text:
                open_google_and_search()
            elif "youtube" in text or "video" in text or "bài hát" in text or "nhạc" in text or "nghe" in text:
                search_youtube()
            elif "mở" in text or "ứng dụng" in text:
                open_application(text)
            elif "thời tiết" in text:
                current_weather()
            elif "đọc báo" in text:
                read_news()
            elif "thuật ngữ" in text or "cho tôi biết" in text or "tôi muốn biết" in text or "thông tin" in text:
                tell_me_about()
            else:
                speak("Bạn cần tôi giúp gì ạ?")
                help_me()
#%%
assistant()
