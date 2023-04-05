import os
import sys
import playsound
import speech_recognition as sr
import ctypes
import re
import urllib.request
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from gtts import gTTS
import pyttsx3
from googlesearch import search
from gtts import gTTS
from hello import hello_name
from get_time import get_time
from tkinter import*
import tkinter as tk
import time
from time import strftime
path = ChromeDriverManager().install()
flag = 1

# print("Trợ lý ảo: Tôi có thể giao tiếp với bạn qua 2 cách sau:")
# print("Chọn 1: Tôi sẽ giao tiếp với bạn qua giọng nói")
# print("Chọn 2: Tôi sẽ giao tiếp với bạn qua tin nhắn")
# print("Vui lòng nhập: ", end='')
# while True:
#     flag = int(input())
#     if flag != 1 and flag != 2:
#         print("Bạn đã nhập sai, vui lòng nhập lại: ", end='')
#     else: break
    
def get_response(text):
    if "chào" in text:
        return hello_name("Hùng")
    elif "dừng" in text or "stop" in text or "tạm biệt" in text or "ngủ thôi" in text:
        return stop()
    elif "làm gì" in text or 'làm được gì' in text:
        return help_me()
    elif "hiện tại" in text or "mấy giờ" in text:
        return get_time(text)
    # elif "tìm kiếm" in text or "trên google" in text or "web" in text:
    #     open_google_and_search()
    # elif "youtube" in text or "video" in text or "bài hát" in text or "nhạc" in text or "nghe" in text:
    #     search_youtube()
    # elif "mở" in text:
    #     text1 = get_text()
    #     open_application(text1)
    # elif "thời tiết" in text:
    #     current_weather()
    # elif "đọc báo" in text:
    #     read_news()
    # elif "thuật ngữ" in text or "cho tôi biết" in text or "tôi muốn biết" in text or "thông tin" in text:
    #     tell_me_about()
    # else:
    #     speak("Bạn cần tôi giúp gì ạ?")
    #     help_me()
#     return f"Trợ lý ảo: {text}"
# %%
def speak(text):
    # print("Trợ lý ảo: {}".format(text))
    if flag == 1:
        tts = gTTS(text = text,lang='vi')
        tts.save("sound.mp3")
        playsound.playsound("sound.mp3")
        os.remove("sound.mp3")
    return text


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
    return speak("Hẹn gặp lại bạn sau!")
    
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
def help_me():
    speak("Tôi có thể giúp bạn thực hiện các câu lệnh sau đây:")
    print("""
    1. Chào hỏi
    2. Hiển thị giờ
    3. Mở ứng dụng
    4. Tìm kiếm trên Google
    5. Dự báo thời tiết
    6. Mở video trên youtube
    7. Đọc báo hôm nay
    8. Tìm thông tin của một thuật ngữ, một người""")

# #%%
def assistant():
    speak("Xin chào, bạn tên là gì nhỉ?")
    time.sleep(1)
    s = get_text().split()
    name = s[-1]
    if name:
        speak("Chào bạn {}".format(name[0:1].upper() + name[1:]))
        time.sleep(2)
        speak("Bạn cần tôi giúp gì ạ?")

BG_GRAY="#ABB2B9"
BG_COLOR="#17202A"
TEXT_COLOR = "#EAECEE"

FONT = "Helvetica 14"
FONT_BOLD = "Helvetica 13 bold"


def create_chat_application():
    window = Tk()
    window.title("A+ Python")
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
    msg_entry.bind("<Return>", lambda event: _on_enter_pressed(event, msg_entry, text_widget))

    #send button
    send_button = Button(bottom_label, text="Send", font=FONT_BOLD, width=20, bg=BG_GRAY, command=lambda: _on_enter_pressed(None, msg_entry, text_widget))
    send_button.place(relx=0.77, rely=0.008, relheight=0.06, relwidth=0.22)

    window.mainloop()

def _on_enter_pressed(event, msg_entry, text_widget):
    msg = msg_entry.get()
    msg_entry.delete(0, END)
    msg1 = f"You: {msg}\n\n"
    text_widget.configure(state=NORMAL)
    text_widget.insert(END, msg1)
    text_widget.configure(state=DISABLED)

    msg2 = f"Trợ lý ảo: {get_response(msg)}\n\n"
    text_widget.configure(state=NORMAL)
    text_widget.insert(END, msg2)
    text_widget.configure(state=DISABLED)
    text_widget.see(END)

create_chat_application()