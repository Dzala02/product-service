import os

from dotenv import load_dotenv
from flask import Flask, jsonify
from flask_cors import CORS

# Factor 3: load optional .env; real environment variables take precedence
load_dotenv()

app = Flask(__name__)

# Same as the Rust version: allow GET requests from any origin
CORS(app, resources={r"/products": {"origins": "*", "methods": ["GET"]}})

PRODUCTS = [
    {"id": 1, "name": "Dog Food", "price": 19.99},
    {"id": 2, "name": "Cat Food", "price": 34.99},
    {"id": 3, "name": "Bird Seeds", "price": 10.99},
]


@app.route("/products", methods=["GET"])
def get_products():
    return jsonify(PRODUCTS)


if __name__ == "__main__":
    # Local runs only; on Azure, gunicorn starts the app
    port = int(os.getenv("PORT", "3030"))
    app.run(host="0.0.0.0", port=port)
