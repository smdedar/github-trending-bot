# GitHub Trending Repositories Tracker

## Overview
This project is a Flask-based web application designed to track trending repositories on GitHub and publish new trends to a specified Telegram channel. It regularly scrapes the GitHub trending page, stores new trending repositories in a SQLite database, and uses the Telegram Bot API to notify users of these trends.

## Description
The GitHub Trending Repositories Tracker is an automated system that keeps users informed about the latest trending repositories on GitHub. By utilizing web scraping techniques and a scheduled cron job, the application continuously monitors and updates the list of trending repositories, ensuring that users receive timely notifications via Telegram.

## How it Works
1. **Web Scraping**: The application scrapes the GitHub trending page to fetch the latest trending repositories.
2. **Database Storage**: It checks the fetched repositories against a SQLite database to identify new trends.
3. **Notification**: New trending repositories are stored in the database and published to a specified Telegram channel using the Telegram Bot API.
4. **Scheduled Execution**: A cron job periodically triggers the tracking and notification process, ensuring the application runs at regular intervals.

## Features
- **Automated Tracking**: Automatically tracks and updates the list of trending GitHub repositories.
- **Telegram Notifications**: Publishes new trending repositories to a specified Telegram channel.
- **Database Storage**: Uses SQLite to store and manage the list of tracked repositories.
- **Scheduled Execution**: Employs cron jobs to run the tracking process at regular intervals.

## Technologies Used
- **Python**: The core programming language used for the application.
- **Flask**: A lightweight WSGI web application framework used to build the web application.
- **SQLite**: A lightweight, disk-based database used to store the list of tracked repositories.
- **BeautifulSoup**: A library used for web scraping to parse the GitHub trending page.
- **Requests**: A library used to make HTTP requests to GitHub and the Telegram API.
- **Telegram Bot API**: Used to send notifications to a Telegram channel.
- **Cron**: A time-based job scheduler used to run the tracking script at regular intervals.