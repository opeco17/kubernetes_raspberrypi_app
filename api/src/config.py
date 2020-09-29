import logging
import os


class Config(object):

    # Basic
    SECRET_KEY = 'password'

    # URI
    ML_API_URI = '192.168.3.11:3031/img_bytes'

    # Parameters
    RESPONSE_IMG_NUM = 10
    BATCH_SIZE = 10
    DIM_Z = 128

    # Logging
    LOG_LEVEL = os.environ.get('LOG_LEVEL', logging.DEBUG)