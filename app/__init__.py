from .site.routes import site
from flask import Flask


app = Flask(__name__)

app.register_blueprint(site)

