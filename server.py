import os

from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "Hello from David"


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5002))
    app.run(host='0.0.0.0', port=port)