#-*- coding: utf-8 -*-

from flask.ext import wtf
from forms import RedirectForm

class DocForm(RedirectForm):
    name = wtf.TextField('Name', validators=[ \
            wtf.Required('Missing document name') ])
    path = wtf.TextField('Path', validators=[ \
            wtf.Required('Missing document path') ])
    slug = wtf.TextField('Slug', validators=[ \
            wtf.Required('Missing document slug') ])
