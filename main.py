#-*- coding: utf-8 -*-
import logging
logging.basicConfig(level=logging.INFO)

from flask import Flask, url_for
from sqlalchemy import create_engine

app = Flask(__name__)
app.debug=True

# blueprints
from docs.blueprint import docs
app.register_blueprint(docs)

app.run(host='local.g2w.me', port=80, debug=True)