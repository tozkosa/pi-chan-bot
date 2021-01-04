""" import pya3rt

def talk_ai(word):
    apikey = "DZZc3U3GHk8ST7wZfcaRxFCyh20heP90"
    client = pya3rt.TalkClient(apikey)
    reply_message = client.talk(word)
    print(reply_message['results'][0]['reply'])

talk_ai("好きな食べ物は？")

 """