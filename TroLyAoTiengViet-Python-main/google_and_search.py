from TroLyAo import speak, get_text
from googlesearch import search
import random
import webbrowser

def open_google_and_search():
    # if flag == 1: speak("Vui lòng nói từ khóa tìm kiếm:")
    # if flag == 2: speak("Vui lòng nhập từ khóa tìm kiếm:")
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
