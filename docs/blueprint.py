#-*- coding:utf-8 -*-
from flask import Blueprint
from flask import render_template
from flask import url_for
docs = Blueprint('docs', __name__, url_prefix='/docs',
        template_folder='templates', static_folder='static')

@docs.route('/')
def index():
    return render_template('docs/index.html')
