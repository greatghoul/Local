#-*- coding: utf-8 -*-
import sys, logging, filters
logger = logging.getLogger(__name__)

from flask import Flask, url_for, abort
from extensions import db

def make_application():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_pyfile('config.py')
    logging.basicConfig(level=app.config['LOGGER_LEVEL'], \
                        format=app.config['LOGGER_FORMAT'])

    # Setup sqlalchemy
    db.init_app(app)

    @app.after_request
    def after_request(response):
        try:
            db.session.commit()
        except Exception:
            db.session.rollback()
            abort(500)
        return response

    # blueprints
    from views import docs
    app.register_blueprint(docs, url_prefix='/docs')

    # Config jinjia global variables
    app.jinja_env.filters['error_class'] = filters.error_class
    app.jinja_env.filters['error_text'] = filters.error_text
    app.jinja_env.filters['dateformat'] = filters.dateformat
    app.jinja_env.filters['empty'] = filters.empty
    app.jinja_env.globals['static'] = (
        lambda filename: url_for('static', filename=filename))

    return app

def runserver():
    app = make_application()
    app.run(app.config['HOST'], app.config['PORT'], app.config['DEBUG'])

def initdb():
    app = make_application()
    db.app = app
    db.drop_all()
    db.create_all()
    logger.info('Database reseted')

if __name__ == '__main__':
    if len(sys.argv) == 1:
        print 'Usage: python main.py <command>'
    else:
        command = sys.argv[1]
        command_action = globals().get(command)
        if callable(command_action):
            command_action()
        else:
            print 'Command "%s" is not avaiable' % command
