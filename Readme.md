# Create a Simple Telegram Bot to deliver Weather Updates

## Introduction
This is a simple Telegram Bot that delivers weather updates to users. 
The bot is built using Python and the visualcrossing API. The bot is hosted on RPI.

## Requirements
- Python 3.12 or higher
- Visualcrossing API key 
  - Sign up for a free account at https://www.visualcrossing.com/weather-api
  - Get the API key
- Telegram Bot Token
  - Create a new bot using BotFather and get the token
  - Add the bot to a channel or group
  - Send a message to the bot in the channel or group
  - Get the chat_id by visiting `https://api.telegram.org/bot<YourBOTToken>/getUpdates`

## Installation
1. Clone the repository
2. Install the required packages using `pip install -r requirements.txt`
3. Create a `.env` file and add the following variables:
  ```
  API_KEY=<Your Visualcrossing API Key
  BOT_TOKEN=<Your
  CHAT_ID=<Your Chat ID>
  ```
4. Run the bot using `python main.py` to test locally
5. Move the script to RPI in a folder and run the script using `python3 main.py` to test the bot
6. Set up a cron job to run the script every hour by:
  - Running `crontab -e`
  - Adding the following line to the file:
    ```
    0 * * * * python3 ~/path/to/main.py
    ```
    - Save the file and exit
7. The bot will now send weather updates every hour

 