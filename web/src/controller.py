from flask import render_template, request
import requests

from config import Config
from forms import TagSelectForm
from run import app


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    app.logger.info('Web: index called.')
    tag_select_form = TagSelectForm()
    if request.method == 'GET':
        return render_template('index.html', form=tag_select_form)
    elif request.method == 'POST':
        if tag_select_form.validate_on_submit():
            hair_color = tag_select_form.hair_color.data
            app.logger.info(hair_color)
            headers = {'Content-Type': 'application/json'}
            data = {'label': hair_color[:-5]}
            response = requests.get(Config.API_URI, headers=headers, json=data)
            img_bytes = response.json().get('img_bytes')
            imgs = [f"data:image/png;base64,{img_byte}" for img_byte in img_bytes]
            return render_template('result.html', imgs1=imgs[:5], imgs2=imgs[5:])
        else:
            return render_template('index.html', form=tag_select_form)