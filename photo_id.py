import requests
import os

TOKEN = os.environ['TOKEN']

def photo_id(chat_id:str, photo:str):
    url = f'https://api.telegram.org/bot{TOKEN}/sendPhoto'
    param = {
        'chat_id':chat_id,
        'photo':photo
    }

    r = requests.get(url=url, params=param)
    r.json()

chat_id = '996172963'

photos_id = 'AgACAgIAAxkBAAMnY7ezjNMhfqkXJVOM8XxpgB8LoSEAAu3BMRvK3LlJTc69b5lsz8EBAAMCAAN5AAMtBA'

photo_id(chat_id, photos_id)