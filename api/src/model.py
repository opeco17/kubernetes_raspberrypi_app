import base64

import glob
import requests

from config import Config


def get_encode_imgs(label, num):
    img_paths = glob.glob(f'./raw_images/{label}/*.png')[:num]

    img_bytes = []
    for img_path in img_paths:
        with open(img_path, 'rb') as f:
            img = f.read()
        img_byte = base64.b64encode(img).decode('utf-8')
        img_bytes.append(img_byte)
    return img_bytes
        

def get_encode_imgs_external(label):
    response = requests.post(Config.ML_API_URI, )
    headers = {'Content-Type': 'application/json'}
    data = {'label': label}
    response = requests.get(Config.ML_API_URI, headers=headers, json=data)
    img_bytes = response.json().get('img_bytes')
    return img_bytes
