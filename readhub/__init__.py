import os, logging
from flask import Flask


app = Flask(__name__, static_url_path='/static')
app.config.from_object(os.environ.get('SETTINGS'))

if not app.debug:
    app.logger.addHandler(logging.StreamHandler())
    app.logger.setLevel(logging.INFO)

app.logger.info("\nConfiguration\n%s\n" % app.config)

from flask.ext.sqlalchemy import SQLAlchemy

db = SQLAlchemy(app)

# govuk_template asset path
@app.context_processor
def asset_path_context_processor():
    return {'asset_path': '/static/'}