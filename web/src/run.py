import logging

from flask import Flask
from flask_bootstrap import Bootstrap

from config import Config

app = Flask(__name__)
app.config.from_object(Config)
bootstrap = Bootstrap(app)

app.logger.setLevel(app.config['LOG_LEVEL'])

from controller import *