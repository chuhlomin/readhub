from readhub.server import app
import os
import logging
from logging.handlers import RotatingFileHandler

handler = RotatingFileHandler('foo.log', maxBytes=10000, backupCount=1)
handler.setLevel(logging.INFO)
app.logger.addHandler(handler)
app.run(host="0.0.0.0", port=int(os.environ.get('PORT', 8000)), debug=True)
