import json
import logging
import os


class Config(object):

    # Basic
    SECRET_KEY = 'password'

    # Path
    TAG_JSON_PATH = 'tag.json'

    # URI
    API_URI = 'http://api:80/img_bytes'

    # Parameters
    with open(TAG_JSON_PATH, 'r') as f:
        tag_json = json.load(f)
    HAIR_COLORS = [(hair_color, hair_color[:-5].capitalize()) for hair_color in tag_json.get('hair_color')]

    # Logging
    LOG_LEVEL = os.environ.get('LOG_LEVEL', logging.DEBUG)
