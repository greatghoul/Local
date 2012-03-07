#-*- coding: utf-8 -*-

from flask import Flask
from flask import render_template
from sqlalchemy import create_engine

app = Flask(__name__)
app.debug=True

# blueprints
from docs.blueprint import docs
app.register_blueprint(docs)

app.run(host='local.g2w.me', port=80, debug=True)
