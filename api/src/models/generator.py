import base64
import sys
from typing import List
sys.path.append('..')

import cv2
import numpy as np
from PIL import Image
import torch

from config import Config
from models.model import ResNetGenerator
from models.sampler import Sampler


def pil2cv(image):
    new_image = np.array(image, dtype=np.uint8)
    if new_image.ndim == 2:
        pass
    elif new_image.shape[2] == 3:
        new_image = cv2.cvtColor(new_image, cv2.COLOR_RGB2BGR)
    elif new_image.shape[2] == 4:
        new_image = cv2.cvtColor(new_image, cv2.COLOR_RGBA2BGRA)
    return new_image


def generate(label):
    hair_colors = ['pink', 'blue', 'brown', 'silver', 'blonde', 'red', 'black', 'white', 'purple']
    hair_colors_index_mapper =  {hair_color: index  for index, hair_color in enumerate(hair_colors)}

    gen = ResNetGenerator(num_classes=len(hair_colors))
    gen.load_state_dict(torch.load('./gen_parameter.pth', map_location=torch.device('cpu')))
    gen.eval()


    # APIを想定
    label = 'pink'
    index = hair_colors_index_mapper.get(label)

    fake_img, _ = Sampler.sample_from_gen(num_classes=len(hair_colors), batch_size=Config.BATCH_SIZE, dim_z=Config.DIM_Z, label=index, device='cpu', gen=gen)

    img_bytes = []

    for i in range(Config.BATCH_SIZE):
        fake = (fake_img[i] * 255).astype(np.uint8)
        fake = Image.fromarray(fake)
        _, encimg = cv2.imencode(".png", pil2cv(fake))
        img_str = encimg.tostring()
        img_byte = base64.b64encode(img_str).decode("utf-8")
        img_bytes.append(img_byte)
        
    return img_bytes