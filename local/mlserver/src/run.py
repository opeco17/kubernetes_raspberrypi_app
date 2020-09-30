import json

from flask import Flask
import torch

from config import Config
from models.generator import ResNetGenerator


app = Flask(__name__)
app.config.from_object(Config)

app.logger.setLevel(app.config['LOG_LEVEL'])

hair_colors = ['pink', 'blue', 'brown', 'silver', 'blonde', 'red', 'black', 'white', 'purple']
hair_colors_index_mapper =  {hair_color: index  for index, hair_color in enumerate(hair_colors)}

gen = ResNetGenerator(num_classes=len(hair_colors))
gen.load_state_dict(torch.load('./models/gen_parameter.pth', map_location=torch.device('cpu')))
gen.eval()

from controller import *
