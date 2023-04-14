import os
import threading
import playsound
import speech_recognition as sr
import time
import wikipedia
import datetime
import json
import re
import random
import urllib.request
import sys
import webbrowser
import requests
from time import strftime
from gtts import gTTS
from youtubesearchpython import VideosSearch
import pyttsx3
from googlesearch import search
from gtts import gTTS
from tkinter import *
# import a
#%% ngon ngu
wikipedia.set_lang('vi')
language = 'vi'
flag = True

def say():
    # Ghi âm giọng nói và chuyển đổi thành văn bản
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.record(source, duration=5)
    try:
        text = r.recognize_google(audio, language="vi-VN")
        You_say(text, text_widget)
        return text
    except Exception:
        You_say("...", text_widget)
        return "..."
#%%
def hello():
    speak("Xin chào bạn, bạn tên là gì ạ!")
    while True:
        text = say()
        if text == '...': 
            speak("Tôi không nghe rõ, bạn có thể nói lại được không")
        else: break
    name = text.split()[-1]
    day_time = int(strftime('%H'))
    if day_time < 12:
        speak("Chào buổi sáng bạn {}. Chúc bạn một ngày tốt lành.".format(name))
    elif 12 <= day_time < 18:
        speak("Chào buổi chiều bạn {}. Bạn đã dự định gì cho chiều nay chưa.".format(name))
    else:
        speak("Chào buổi tối bạn {}. Chúc bạn một buổi tối vui vẻ.".format(name))
    speak("Bạn có khỏe không?")
    while True:
        text = say()
        if text == '...': 
            speak("Tôi không nghe rõ, bạn có thể nói lại được không")
        else: break
    

#%%
def get_time(text):
    now = datetime.datetime.now()
    if "giờ" in text:
        speak('Bây giờ là %d giờ %d phút' % (now.hour, now.minute))
    elif "ngày" in text:
        speak("Hôm nay là ngày %d tháng %d năm %d" %
              (now.day, now.month, now.year))
    else:
        speak("Tôi không hiểu ý của bạn. Bạn nói lại được không?")

def search_youtube():
    speak("Vui lòng nói từ khóa tìm kiếm mà bạn muốn xem")
    while True:
        text = say()
        if text == '...': 
            speak("Tôi không nghe rõ, bạn có thể nói lại được không")
        else: break
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
        speak("Không tìm thấy kết quả phù hợp trên YouTube")

#%%
def open_application(text):
    if "google" in text: 
        os.startfile(r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe")
        speak("Đã mở Google Chrome")
    
    elif "zalo" in text:    
        os.startfile(r'C:\Users\ADMIN\AppData\Local\Programs\Zalo\Zalo.exe')
        speak("Đã mở Zalo")
    
    elif "word" in text:
        os.startfile(r"C:\Program Files\Microsoft Office\root\Office16\WINWORD.EXE")
        speak("Đã mở Microsoft Word")
    
    elif "excel" in text:
        os.startfile(r"C:\Program Files\Microsoft Office\root\Office16\EXCEL.EXE")
        speak("Đã mở Microsoft Excel")
    
    elif "powerpoint" in text or "thuyết trình" in text:
        os.startfile(r"C:\Program Files\Microsoft Office\root\Office16\POWERPNT.EXE")     
        speak("Đã mở PowerPoint")
    
    elif "zoom" in text:    
        os.startfile(r"C:\Users\ADMIN\AppData\Roaming\Zoom\bin\Zoom.exe")     
        speak("Đã mở Zoom")
    elif "c++" in text:
        os.startfile(r"C:\Program Files (x86)\Dev-Cpp\devcpp.exe")     
        speak("Đã mở Dev C++")
    elif "java" in text:      
        os.startfile(r"C:\Program Files\NetBeans-15\netbeans\bin\netbeans64.exe")
        speak("Đã mở Apache NetBeans")
    else:
        speak("Ứng dụng chưa được cài đặt hoặc tôi chưa hiểu ý bạn. Bạn hãy thử lại!")

    
#%%
def open_google_and_search():
    speak("Vui lòng nói từ khóa tìm kiếm trên google:")
    while True:
        text = say()
        if text == '...': 
            speak("Tôi không nghe rõ, bạn có thể nói lại được không")
        else: break
    # Tìm kiếm trên Google và lưu trữ các kết quả trong danh sách 'search_results'
    try:
        search_results = list(search(text, num_results=10))
        # Lấy ngẫu nhiên một đường link trong danh sách kết quả tìm kiếm
        if len(search_results) > 0:
            random_link = search_results[0]
            webbrowser.open(random_link)
            speak("Trang web đã mở thành công")
    except: speak("Tôi không tìm thấy kết quả này trên google")
    
#%%
def current_weather():
    speak("Bạn muốn xem thời tiết ở đâu ạ.")
    while True:
        city = say()
        if city == '...': 
            speak("Tôi không nghe rõ, bạn có thể nói lại được không")
        else: break
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
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

    else:
        speak("Tôi không tìm thấy địa chỉ nơi bạn muốn biết thời tiết")

#%%
def read_news():
    
    speak("Bạn muốn đọc báo về gì")

    while True:
        queue = say()
        if queue == '...': 
            speak("Tôi không nghe rõ, bạn có thể nói lại được không")
        else: break
    text_widget.insert(END, "\n\n")
    params = {
        'apiKey': '9007bba8aca54b379ccba2964abac887',
        'q': queue,
    }
    api_result = requests.get('http://newsapi.org/v2/top-headlines?', params)
    api_response = api_result.json()
    speak("Tin tức")

    for number, result in enumerate(api_response['articles'], start=1):
        print(f"""Tin {number}:\nTiêu đề: {result['title']}\nTrích dẫn: {result['description']}\nLink: {result['url']}\nNội dung: {result['content']}
    """)
        if number <= 3:
            webbrowser.open(result['url'])

#%%
def tell_me_about():
    try:
        speak("Bạn muốn nghe về gì ạ")
        while True:
            text = say()
            if text == '...': 
                speak("Tôi không nghe rõ, bạn có thể nói lại được không")
            else: break
        contents = wikipedia.summary(text).split('\n')
        speak(contents[0])
        for content in contents[1:]:
            speak("Bạn muốn nghe thêm không")
            while True:
                text = say()
                if text == '...': 
                    speak("Tôi không nghe rõ, bạn có thể nói lại được không")
                else: break
            if "có" not in text:
                break    
            speak(content)

        speak('Cảm ơn bạn đã lắng nghe!!!')
    except:
        speak("Tôi không tìm thấy thông tin của thuật ngữ mà bạn cần.")
        
#%%
def help_me():

    speak("""Tôi có thể giúp bạn thực hiện các chức năng sau đây:
        1. Chào hỏi
        2. Hiển thị ngày hoặc giờ
        3. Mở ứng dụng
        4. Mở google và tìm kiếm
        5. Dự báo thời tiết
        6. Xem video, nghe nhạc trên youtube
        7. Đọc báo hôm nay
        8. Tìm thông tin của một thuật ngữ hoặc một người""")

#%%
def assistant(text):
    global flag
    flag = False
    ok = 0
    if "làm gì" in text or 'làm được gì' in text:
        help_me()
        ok = 1
    elif "chào" in text or "hello" in text:
        hello()
        ok = 1
    elif "hiện tại" in text or "giờ" in text or "ngày" in text:
        get_time(text)
        ok = 1
    elif "tìm kiếm" in text or "trên google" in text or "web" in text:
        open_google_and_search()
        ok = 1
    elif "mở" in text or "open" in text or "ứng dụng" in text:
        open_application(text)
        ok = 1
    elif "youtube" in text or "nhạc" in text or "video" in text or "bài hát" in text or "xem" in text:
        search_youtube()
        ok = 1
    elif "thời tiết" in text:
        current_weather()
        ok = 1
    elif "đọc báo" in text:
        read_news()
        ok = 1
    elif "định nghĩa" in text or "cho tôi biết" in text or "tôi muốn biết" in text or "thông tin" in text:
        tell_me_about()
        ok = 1
    time.sleep(2)
    if ok:
        speak("Bạn cần tôi giúp gì nữa không ạ?")
    else: 
        speak("Tôi chưa hiểu ý của bạn, bạn có thể nói lại giúp tôi được không?")
            
    text_widget.configure(state=DISABLED)
    flag = True
                

def speak(text):
    tts = gTTS(text = text,lang='vi')
    tts.save("sound.mp3")
    playsound.playsound("sound.mp3")
    os.remove("sound.mp3")
    Bot_say(text, text_widget)

def Bot_say(text, text_widget):
    text_widget.configure(state=NORMAL)
    text_widget.insert(END, f"Trợ lý ảo: {text}\n\n")
    text_widget.configure(state=DISABLED)
    text_widget.see(END)

def You_say(text, text_widget):
    text_widget.configure(state=NORMAL)
    text_widget.insert(END, f"Tôi: {text}\n\n")
    text_widget.see(END)
    # text_widget.configure(state=DISABLED)
    if flag == True: assistant(text.lower())
    
def _on_enter_pressed(event):
    msg = msg_entry.get()
    msg_entry.delete(0, END)
    You_say(msg, text_widget)

def start_recording():
    record_button.config(text="Listening...", state=DISABLED)
    t = threading.Thread(target=record)
    t.start()

def record():
    # Ghi âm giọng nói và chuyển đổi thành văn bản
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.record(source, duration=5)
    try:
        text = r.recognize_google(audio, language="vi-VN")
        You_say(text, text_widget)
    except Exception:
        You_say("...", text_widget)
    finally:
        # Sau khi ghi âm hoàn thành, chuyển đổi trạng thái của nút Record trở lại
        record_button.config(text="Record", state=NORMAL)

BG_GRAY="#ABB2B9"
BG_COLOR="#17202A"
TEXT_COLOR = "#EAECEE"

FONT = "Helvetica 14"
FONT_BOLD = "Helvetica 13 bold"
window = Tk()
window.title("Nhóm 2")
window.configure(width=600, height=600, bg=BG_COLOR)
# head label
head_lable = Label(window, bg=BG_COLOR, fg=TEXT_COLOR, text="Welcome", font=FONT_BOLD, pady=10)
head_lable.place(relheight=1)

#tiny divider
line = Label(window, width=450, bg=BG_GRAY)
line.place(relwidth=1, rely=0.07, relheight=0.012)

#text widget
text_widget = Text(window, width=20, height=2, bg=BG_COLOR, fg=TEXT_COLOR, font=FONT_BOLD, padx=5, pady=5)
text_widget.place(relheight=0.745, relwidth=1, rely=0.08)

text_widget.configure(cursor="arrow", state=DISABLED)

# scroll bar
scrollbar = Scrollbar(text_widget)
scrollbar.place(relheight=1, relx=0.974)
scrollbar.configure(command=text_widget.yview)

#bottom label 
bottom_label = Label(window, bg=BG_GRAY, height=80)
bottom_label.place(relwidth=1, rely=(0.825))

# message entry box
msg_entry = Entry(bottom_label, bg="#2C3E50", fg=TEXT_COLOR, font=FONT)
msg_entry.place(relwidth=0.74, relheight=0.06, rely=0.008, relx=0.011)
msg_entry.focus()
msg_entry.bind("<Return>", lambda event: _on_enter_pressed(event))

#send button
send_button = Button(bottom_label, text="Send", font=FONT_BOLD, width=20, bg=BG_GRAY, command=lambda: _on_enter_pressed(None))
send_button.place(relx=0.77, rely=0.008, relheight=0.06, relwidth=0.22)

# record button
record_button = Button(bottom_label, text="Record", font=FONT_BOLD, width=20, bg=BG_GRAY, command=lambda: start_recording())
record_button.place(relx=0.54, rely=0.008, relheight=0.06, relwidth=0.22)   

window.mainloop()
