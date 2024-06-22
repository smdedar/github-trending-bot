from flask import Flask
import sqlite3
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

# Function to fetch current trending repositories
def fetch_trending_repos():
    result = requests.get("https://github.com/trending")
    src = result.content
    soup = BeautifulSoup(src, 'lxml')
    featured_challenges = soup.find_all('h1', attrs={'class': 'lh-condensed'})
    
    current_trend = []
    for featured_challenge in featured_challenges:
        url = 'https://github.com' + featured_challenge.a.attrs['href']
        current_trend.append(url)
    
    return current_trend

# Function to track new trending repositories
def track_new_trends(current_trend):
    conn = sqlite3.connect('github.db')
    cursor = conn.cursor()
    cursor.execute('''SELECT * FROM github''')
    results = cursor.fetchall()
    previous_trend = [result[1] for result in results]
    unique_trend = set(current_trend) - set(previous_trend)
    
    return unique_trend

# Function to track repository URL in the database
def track(trendurl):
    conn = sqlite3.connect('github.db')
    cursor = conn.cursor()
    cursor.execute('''INSERT INTO github(url) VALUES (?)''', (trendurl,))
    conn.commit()
    conn.close()

# Function to publish repository URL to Telegram
def publish(trendurl):
    bot_token = ''  # Add your bot token here
    channel_id = ''  # Add your channel ID here
    publish_url = f"https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={channel_id}&text={trendurl}"
    requests.get(publish_url)

# Endpoint to run the trending repositories tracking and publishing logic
@app.route('/track_trends', methods=['GET'])
def track_trends():
    current_trend = fetch_trending_repos()
    unique_trend = track_new_trends(current_trend)
    
    for trendurl in unique_trend:
        track(trendurl)
        publish(trendurl)
    
    return "Tracked and published new trends", 200

if __name__ == '__main__':
    app.run()
