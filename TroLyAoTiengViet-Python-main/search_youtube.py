from TroLyAo import get_text, speak
from youtubesearchpython import VideosSearch
import webbrowser
import random
def search_youtube():
    # if flag == 1: speak("Vui lòng nói từ khóa tìm kiếm:")
    # if flag == 2: speak("Vui lòng nhập từ khóa tìm kiếm:")
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

search_youtube()