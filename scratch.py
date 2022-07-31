import requests
from bs4 import BeautifulSoup

response = requests.get(YOUTUBE_TRENDING_URL)

print('Status Code: ',response.status_code)

with open('trending.html','w') as f:
  f.write(response.text)

doc = BeautifulSoup(response.text,'html.parser')
print('Page Title: ',doc.title.text)

#Find all video div
video_div = doc.find_all('div',class_='style-scope ytd-shelf-renderer')
print(f'Found {len(video_div)} videos')