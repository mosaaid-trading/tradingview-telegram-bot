import os

def handler(request):
    return {
        "statusCode": 200,
        "headers": { "Content-Type": "text/plain" },
        "body": "TradingView Telegram bot is working!"
    }
