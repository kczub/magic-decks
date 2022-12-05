import os
import requests
from PIL import Image
from io import BytesIO

card_id = '3d24036e-075f-4991-a740-a9d943722ad2'

class ApiClient:
    base_url = 'https://api.scryfall.com/cards'
    
    def card_data(self, data):
        return {
            'name': data.get('name'),
            'mana_cost': data.get('mana_cost'),
            'type': data.get('type_line'),
            'text': data.get('oracle_text'),
            'power': data.get('power'),
            'toughness': data.get('toughness'),
            'colors': data.get('colors'),
            'color_identity': data.get('color_identity'),
            'card_faces': data.get('card_faces'),
            'rarity': data.get('rarity'),
            'booster': data.get('booster'),
            'story_spotlight': data.get('story_spotlight'),
            'img_url': data.get('image_uris').get('large'),
        }

    def get_card_by_id(self, card_id):
        url = f'{self.base_url}/{card_id}'
        r = requests.get(url)

        data = r.json()
        card = self.card_data(data)
        
        return card

    def get_image(self, card_id, save=False):
        url = f'{self.base_url}/{card_id}'
        base_dir = os.path.dirname(os.path.abspath(__file__))
        img_path = os.path.join(base_dir, "image.png")
        params = {'format': 'image', 'version': 'png'}
        r_img = requests.get(url, params=params)
        img = Image.open(BytesIO(r_img.content))

        if save:
            img.save(img_path)
            print("saved")

        return img.show()


    def search(self, query):
        url = f'{self.base_url}/search'
        params = {'q': query, 'unique': 'unique'}
        r = requests.get(url, params=params)
        
        # search always returns a list
        data = r.json().get('data')[0]
        card = self.card_data(data)
        
        return card

