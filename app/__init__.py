from flask import Flask
from app.config import Config

app = Flask(__name__)

app.config.from_object(Config)

# blueprints register
from app.resources import (
    oauth, index
)
app.register_blueprint(oauth.bp)
app.register_blueprint(index.bp)