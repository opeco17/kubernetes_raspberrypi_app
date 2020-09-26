from flask import render_template

from forms import TagSelectForm
from run import app

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    app.logger.info('Web: index called.')
    tag_select_form = TagSelectForm()
    if tag_select_form.validate_on_submit():
        hair_color = tag_select_form.hair_color.data
        eye_color = tag_select_form.eye_color.data
        return 'OK'
    else:
        return render_template('index.html', form=tag_select_form)