import requests
import os

TOKEN = os.environ['TOKEN']

def photo_url(chat_id:str, photo:str):
    url = f'https://api.telegram.org/bot{TOKEN}/sendPhoto'
    param = {
        'chat_id': chat_id,
        'photo':photo
    }
    
    r = requests.get(url=url, params=param)

    r.json()

    pass

photo_url = 'https://random.dog/eb002f57-e511-4c9d-894e-10a3a3326193.jpg'

chat_id = '996172963'

photo_url(chat_id, photo_url)
