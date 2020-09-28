import logging
import os


class Config(object):

    # Basic
    SECRET_KEY = 'password'

    # Parameters
    RESPONSE_IMG_NUM = 10
    BATCH_SIZE = 10
    DIM_Z = 128

    # Logging
    LOG_LEVEL = os.environ.get('LOG_LEVEL', logging.DEBUG)