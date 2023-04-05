from time import strftime
from TroLyAo import speak

def hello_name(name):
    day_time = int(strftime('%H'))
    if day_time < 12:
        return speak("Chào buổi sáng bạn {}. Chúc bạn một ngày tốt lành.".format(name))
    elif 12 <= day_time < 18:
        return speak("Chào buổi chiều bạn {}. Bạn đã dự định gì cho chiều nay chưa.".format(name))
    else:
        return speak("Chào buổi tối bạn {}. Bạn đã ăn tối chưa nhỉ.".format(name))
