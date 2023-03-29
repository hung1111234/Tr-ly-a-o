import random
from googlesearch import search

# Từ khóa cần tìm kiếm
query = "python programming"

# Tìm kiếm trên Google và lưu trữ các kết quả trong danh sách 'search_results'
search_results = list(search(query, num_results=10))

# Lấy ngẫu nhiên một đường link trong danh sách kết quả tìm kiếm
random_link = random.choice(search_results)

print(random_link)