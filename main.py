#-*- coding: utf-8 -*-

from flask import Flask
from flask import render_template

app = Flask(__name__)
app.debug=True

# blueprints
from docs.blueprint import docs
app.register_blueprint(docs)

app.run()
