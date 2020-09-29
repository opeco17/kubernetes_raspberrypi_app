import json

from flask import request, Response

from config import Config
from model import get_encode_imgs
from run import app


@app.route('/', methods=['GET'])
def index():
    return 'This is api!'


@app.route('/img_bytes', methods=['GET'])
def img_bytes():
    app.logger.info('API: index called.')
    label = request.get_json().get('label')
    img_bytes = get_encode_imgs(label, Config.RESPONSE_IMG_NUM)
    response_body = {'img_bytes': img_bytes}
    response = Response(
        response=json.dumps(response_body),
        mimetype='application/json',
        status= 200
    )
    return response