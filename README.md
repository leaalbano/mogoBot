# Reddit Trading Bot for Monopoly Go Stickers

This Python script is designed to run a trading bot on the Reddit platform, specifically targeting the MonopolyGoTrading subreddit. The bot monitors new submissions to the subreddit and searches for specific keywords indicating trade requests for Monopoly Go stickers. It then matches these requests with other submissions containing potential trading opportunities and replies to the original submission with the matching trades.

## Requirements
- Python 3.x
- PRAW (Python Reddit API Wrapper)

## Installation
1. Install Python 3.x from the [official website](https://www.python.org/downloads/).
2. Install PRAW using pip:
```pip install praw```
3. Clone or download the script file (`mogoBot.py`) from this repository.

## Configuration
Before running the script, you need to provide the following configuration parameters in the script file:
- `client_id`: Your Reddit API client ID.
- `client_secret`: Your Reddit API client secret.
- `user_agent`: A unique user agent string for your bot.
- `username`: Your Reddit username.
- `password`: Your Reddit password.

## Usage
To run the script:
1. Open a terminal or command prompt.
2. Navigate to the directory containing the script file.
3. Run the script using Python:
```python3 mogoBot.py```

## Features
- Monitors new submissions on the MonopolyGoTrading subreddit.
- Searches for trade requests containing specific keywords (e.g., "LF" or "HAVE").
- Matches trade requests with potential trading opportunities based on specified criteria.
- Replies to the original submission with the matching trades.



