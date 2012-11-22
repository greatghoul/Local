#-*- coding:utf-8 -*-
import logging
logger = logging.getLogger(__name__)

from flask import Blueprint, redirect, url_for, send_file, \
                  render_template, flash, request, current_app
from extensions import db
from models.docs import Doc
from forms.docs import DocForm
import os

HOME_PAGES = ['index.html', 'index.htm', 'default.html', 'default.htm']

docs = Blueprint('docs', __name__)

@docs.route('/', methods=['GET'])
def index():
    keyword = request.args.get('q', None)
    page = int(request.args.get('page', '1'))
    logger.info('Keyworkd %s', keyword)
    query = keyword and Doc.query.filter(Doc.name.like(u'%%%s%%' % keyword)) or Doc.query
    pagination = query.paginate(page, per_page=current_app.config.get('PAGE_SIZE', 20))
    # docs = pagination.items
    return render_template('docs/index.html', pagination=pagination)

@docs.route('/create', methods=['GET', 'POST'])
def create():
    form = DocForm(csrf_enabled=False)
    if form.validate_on_submit():
        doc = Doc()
        logger.info(form.populate_obj(doc))
        db.session.add(doc)
        flash('Document created successfully.', 'success')
        return redirect('.index')
    else:
        return render_template('docs/create.html', form=form)

@docs.route('/update/<slug>/', methods=['GET', 'POST'])
def update(slug):
    doc = Doc.query.filter_by(slug=slug).first()
    if doc is None:
        flash('Document <strong>%s</strong> is missing.', 'error')
        return redirect('.index')

    form = DocForm(csrf_enabled=False)
    if form.validate_on_submit():
        form.populate_obj(doc)
        flash('Document updated successfully.', 'success')
        return redirect('.index')
    else:
        not form.errors and form.process(obj=doc)
        return render_template('docs/create.html', form=form)

@docs.route('/destroy/<slug>/')
def destroy(slug):
    doc = Doc.query.filter_by(slug=slug).first()
    flash(u'Document <storng>%s</strong> deleted successfully.' % slug, 'success') 
    db.session.delete(doc)
    return redirect(url_for('.index'))

@docs.route('/doc/<slug>/')
@docs.route('/doc/<slug>/<path:filename>')
def view(slug, filename=''):
    doc = Doc.query.filter_by(slug=slug).first_or_404()
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
