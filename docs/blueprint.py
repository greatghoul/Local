#-*- coding:utf-8 -*-
import logging
logger = logging.getLogger(__name__)

from flask import Blueprint
from flask import render_template
from flask import url_for, redirect, send_file, request
from flask import abort
from models import Doc
from database import db_session
import os

HOME_PAGES = ['index.html', 'index.htm', 'default.html', 'default.htm']

docs = Blueprint('docs', __name__, url_prefix='/docs' , \
                                   template_folder='templates',
                                   static_folder='static')

@docs.route('/', methods=['GET'])
def index():
    docs = Doc.query.all()
    return render_template('docs/index.html', docs=docs)

@docs.route('/update/<doc_id>', methods=['GET', 'POST'])
def update(doc_id):
    doc = db_session.query(Doc).get(doc_id)

    if request.method == 'GET':
        return render_template('docs/update.html', doc=doc)
    else:
        doc.name = request.form.get('name')
        doc.slug = request.form.get('slug')
        doc.path = request.form.get('path')
        db_session.commit()
        return redirect(url_for('.index'))

@docs.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'GET':
        return render_template('docs/create.html')
    else:
        name = request.form.get('name')
        slug = request.form.get('slug')
        path = request.form.get('path')
        doc = Doc(name, path, slug)
        db_session.add(doc)
        db_session.commit()
        return redirect(url_for('.index'))

@docs.route('/delete/<doc_id>/', methods='DELETE')
def delete(doc_id):
    return redirect(url_for('index'))

@docs.route('/doc/<slug>/')
@docs.route('/doc/<slug>/<path:filename>')
def view(slug, filename=''):
    doc = db_session.query(Doc).filter_by(slug=slug).first()
    if doc:
        doc_file = os.path.join(doc.path, filename)
        if os.path.isfile(doc_file):
            return send_file(doc_file)
        elif os.path.isdir(doc_file):
            if filename and not filename.endswith('/'):
                return redirect(url_for('.view', slug=slug, filename=filename+'/'))
            else:
                for page in HOME_PAGES:
                    if os.path.exists(os.path.join(doc_file, page)):
                        return redirect(url_for('.view', slug=slug, filename=filename + page))
    abort(404)

@docs.teardown_request
def shutdown_session(exception=None):
    db_session.remove()