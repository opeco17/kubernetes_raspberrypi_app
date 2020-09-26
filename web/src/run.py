import json
import logging

from flask import Flask
from flask_bootstrap import Bootstrap

from config import Config

app = Flask(__name__)
app.config.from_object(Config)
bootstrap = Bootstrap(app)

app.logger.setLevel(app.config['LOG_LEVEL'])

with open(Config.TAG_JSON_PATH, 'r') as f:
    tag_json = json.load(f)

hair_colors = [(hair_color, hair_color[:-5].capitalize()) for hair_color in tag_json['hair_color']]
eye_colors = [(eye_color, eye_color[:-5].capitalize()) for eye_color in tag_json['eye_color']]

from controller import *