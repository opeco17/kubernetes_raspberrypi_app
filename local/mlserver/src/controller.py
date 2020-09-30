import json

from flask import request, Response

from config import Config
from models.generator import generate
from run import app, hair_colors, hair_colors_index_mapper, gen


@app.route('/', methods=['GET'])
def index():
    return 'This is api!'


@app.route('/img_bytes', methods=['GET'])
def img_bytes():
    app.logger.info('API: index called.')
    label = request.get_json().get('label')
    img_bytes = generate(label, gen, hair_colors, hair_colors_index_mapper)
    response_body = {'img_bytes': img_bytes}
    response = Response(
        response=json.dumps(response_body),
        mimetype='application/json',
        status= 200
    )
    return response
