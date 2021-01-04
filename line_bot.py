from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage
import pya3rt
#from flask_ngrok import run_with_ngrok

app = Flask(__name__)
#run_with_ngrok(app)

linebot_api = LineBotApi('uxn6DE0iHNkb4GtWlOTSclWXY+2pjzOp9DjvaV0pW5px6hTQDxQQAIRKj6ebIX3bjx62vW2ZD9Icy/PhHYPcFSSMDEEGePmJaDdimrnHi1p8hBCttEhZlF5KBDBXBXaXLKR+QhMFq6QVXpMNZf5n+QdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('a0053246627ae928a2f35b5806a07fc3')

# @app.route('/')
# def hello_world():
#     return "Hello World!" 


@app.route('/callback', methods=['POST'])
def callback():
    # リクエストがLINE Platformから送られてきたかを確認
    signature = request.headers["X-Line-Signature"]
    body = request.get_data(as_text=True)

    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    
    return 'OK'

@handler.add(MessageEvent, message=TextMessage) # メッセージが送られてきたときに返信するため。メッセージの種類
def handle_message(event):
    ai_message = talk_ai(event.message.text)
    linebot_api.reply_message(event.reply_token, TextSendMessage(text=ai_message)) # line_bot_api

def talk_ai(word):
    apikey = "DZZc3U3GHk8ST7wZfcaRxFCyh20heP90"
    client = pya3rt.TalkClient(apikey)
    reply_message = client.talk(word)
    return reply_message['results'][0]['reply']

if __name__ == '__main__':
    app.run()


