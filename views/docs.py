#-*- coding:utf-8 -*-
import logging
logger = logging.getLogger(__name__)

from flask import Blueprint, redirect, abort, \
        url_for, send_file, render_template, flash
from extensions import db
from models.docs import Doc
from forms.docs import DocForm
import os

HOME_PAGES = ['index.html', 'index.htm', 'default.html', 'default.htm']

docs = Blueprint('docs', __name__)

@docs.route('/', methods=['GET'])
def index():
    docs = Doc.query.all()
    return render_template('docs/index.html', docs=docs)

@docs.route('/save', methods=['POST'])
def save():
    form = DocForm(csrf_enabled=False)
    if form.validate_on_submit():
        doc = Doc()
        doc.name = form.data['name']
        doc.slug = form.data['slug']
        doc.path = form.data['path']
        db.session.add(doc)
        flash('Document created successfully.', 'success')
        return form.redirect('doc.index')
    else:
        flash('Failed while creating doc.', 'error')
        return render_template('docs/new.html', form=form)

@docs.route('/new')
def new():
    form = DocForm(csrf_enabled=False)
    return render_template('docs/new.html', form=form)

@docs.route('/delete/<doc_id>/', methods='DELETE')
def delete(doc_id):
    return redirect(url_for('index'))

@docs.route('/doc/<slug>/')
@docs.route('/doc/<slug>/<path:filename>')
def view(slug, filename=''):
    doc = Doc.query.filter_by(slug=slug).first()
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
