from app import app
import os
from flask import jsonify

@app.route("/")
def index():
    app_name = os.getenv("APP_NAME")

    return jsonify(
        app_name=app_name,
        name='Brent',
    )
