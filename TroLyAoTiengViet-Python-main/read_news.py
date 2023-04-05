from TroLyAo import speak, get_text
import requests
import webbrowser
def read_news():
    
    speak("Bạn muốn đọc báo về gì")
    
    queue = get_text()
    params = {
        'apiKey': '9007bba8aca54b379ccba2964abac887',
        'q': queue,
    }
    api_result = requests.get('http://newsapi.org/v2/top-headlines?', params)
    api_response = api_result.json()
    if len(api_response['articles']) != 0:
        print("Tin tức")
        for number, result in enumerate(api_response['articles'], start=1):
            print(f"""Tin {number}:\nTiêu đề: {result['title']}\nTrích dẫn: {result['description']}\nLink: {result['url']}\nNội dung: {result['content']}
        """)
            if number <= 3:
                webbrowser.open(result['url'])
    else: print("Không tìm thấy tin tức liên quan")
    
read_news()