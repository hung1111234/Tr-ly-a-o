from TroLyAo import speak
import os
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
