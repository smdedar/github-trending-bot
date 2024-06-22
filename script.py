import sqlite3
import requests
from bs4 import BeautifulSoup

result = requests.get("https://github.com/trending")
src = result.content
soup = BeautifulSoup(src, 'lxml')
featured_challenges = soup.find_all('h1', attrs={'class': 'lh-condensed'})

current_trend = []
for featured_challenge in featured_challenges:
    url = 'https://github.com'+ featured_challenge.a.attrs['href']
    current_trend.append(url)
    

conn = sqlite3.connect('github.db')
cursor = conn.cursor()
cursor.execute('''SELECT * from github''')
results = cursor.fetchall();


previous_trend = []
for result in results:
    previous_trend.append(result[1])
    
    
unique_trend = set(current_trend) - set(previous_trend)



def track(trendurl):
    conn = sqlite3.connect('github.db')
    cursor = conn.cursor()
    cursor.execute(f'''INSERT INTO github(url) VALUES ('{trendurl}')''')
    conn.commit()

def publish(trendurl):
    bot_token = ''
    channel_id = ''
    publish = requests.get(f"https://api.telegram.org/{bot_token}/sendMessage?chat_id={channel_id}&text={trendurl}")

for trendurl in unique_trend:
    track(trendurl)
    publish(trendurl)