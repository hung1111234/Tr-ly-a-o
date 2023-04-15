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

flag = True
def assistant(text, current_chat_content):
    flag = False
    # tạo một cửa sổ mới
    new_window = Tk()
    new_window.title("Nhóm 2")
    new_window.configure(width=600, height=600, bg=BG_COLOR)
    head_lable = Label(new_window, bg=BG_COLOR, fg=TEXT_COLOR, text="Welcome", font=FONT_BOLD, pady=10)
    head_lable.place(relheight=1)

    line = Label(new_window, width=450, bg=BG_GRAY)
    line.place(relwidth=1, rely=0.07, relheight=0.012)

    text_widget = Text(new_window, width=20, height=2, bg=BG_COLOR, fg=TEXT_COLOR, font=FONT_BOLD, padx=5, pady=5)
    text_widget.place(relheight=0.745, relwidth=1, rely=0.08)

    text_widget.configure(cursor="arrow", state=NORMAL)
    text_widget.insert(1.0, current_chat_content)

    scrollbar = Scrollbar(text_widget)
    scrollbar.place(relheight=1, relx=0.974)
    scrollbar.configure(command=text_widget.yview)

    bottom_label = Label(new_window, bg=BG_GRAY, height=80)
    bottom_label.place(relwidth=1, rely=(0.825))

    msg_entry = Entry(bottom_label, bg="#2C3E50", fg=TEXT_COLOR, font=FONT)
    msg_entry.place(relwidth=0.74, relheight=0.06, rely=0.008, relx=0.011)
    msg_entry.focus()
    msg_entry.bind("<Return>", lambda event: _on_enter_pressed(event))

    send_button = Button(bottom_label, text="Send", font=FONT_BOLD, width=20, bg=BG_GRAY, command=lambda: message())
    send_button.place(relx=0.77, rely=0.008, relheight=0.06, relwidth=0.22)

    record_button = Button(bottom_label, text="Record", font=FONT_BOLD, width=20, bg=BG_GRAY, command=lambda: say())
    record_button.place(relx=0.54, rely=0.008, relheight=0.06, relwidth=0.22)
    def message():
        global current_chat_content
        current_chat_content = text_widget.get(1.0, END)
        set_text(current_chat_content)
        new_window.destroy()
    def say():
        new_window.destroy()
    
    width = window.winfo_width()
    height = window.winfo_height()
    x = window.winfo_x()
    y = window.winfo_y()

    new_window.geometry(f"{width}x{height}+{x}+{y}")
    new_window.lift(window)
    flag = True

def You_say(text, text_widget):
    text_widget.configure(state=NORMAL)
    text_widget.insert(END, f"Tôi: {text}\n\n")
    text_widget.see(END)
    # text_widget.configure(state=DISABLED)
    current_chat_content = text_widget.get(1.0, END)
    if flag == True: assistant(text.lower(), current_chat_content)

def set_text(current_chat_content):
    global text_widget
    text_widget.config(state=NORMAL)
    text_widget.delete(1.0, END)
    text_widget.insert(1.0, current_chat_content)

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
current_chat_content = text_widget.get(1.0, END)

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
