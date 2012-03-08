#!-*- coding: utf-8 -*-
from database import init_db
from database import db_session
from models import Doc
import random

def init_database():
    print 'init db ...',
    init_db()
    print '[done]'

def init_docs():
    print 'add a doc'
    doc = Doc("Flask's Documentation",
        r'/home/greatghoul/Workspaces//python/libs/Flask-0.8/flask-docs',
        'flask')
    db_session.add(doc)
    db_session.commit()
    db_session.remove()

def show_docs():
    for doc in Doc.query.all():
        print doc

if __name__ == '__main__':
    init_database()
    init_docs()
    show_docs()
