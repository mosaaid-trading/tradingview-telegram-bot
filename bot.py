import requests
from flask import Flask, request

app = Flask(__name__)

TELEGRAM_TOKEN = "ضع التوكن هنا"
CHAT_ID = "ضع معرف القناة أو المستخدم هنا"

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    message = data.get('message', 'تنبيه جديد من TradingView')
    send_telegram_message(message)
    return 'OK'

def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": message}
    requests.post(url, json=payload)

if __name__ == '__main__':
    app.run()
