import requests
import os

TOKEN = os.environ['TOKEN']

def img(chat_id:str, photo:str):
    URl = f'https://api.telegram.org/bot{TOKEN}/sendPhoto'
    param = {
        'chat_id':chat_id
    }
    files = {
        'photo':photo
    }

    r = requests.post(url=URl, params=param, files=files)
    r.json()

photo = open('logo.jpg', 'rb').read()

chat_id = '996172963'

img(chat_id, photo)