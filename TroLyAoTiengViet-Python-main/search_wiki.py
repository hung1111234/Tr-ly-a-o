from TroLyAo import speak, get_text
import time
import wikipedia
wikipedia.set_lang('vi')

def tell_me_about():
    try:
        speak("Bạn muốn nghe về gì ạ")
        time.sleep(2)
        text = get_text()
        contents = wikipedia.summary(text).split('\n')
        speak(contents[0])
        time.sleep(3)
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

tell_me_about()