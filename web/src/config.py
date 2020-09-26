import logging
import os


class Config(object):

    # Basic
    SECRET_KEY = 'password'

    # Path
    TAG_JSON_PATH = 'tag.json'

    # Logging
    LOG_LEVEL = os.environ.get('LOG_LEVEL', logging.DEBUG)