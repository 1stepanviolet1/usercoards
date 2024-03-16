from flask import Flask, render_template

from config import (
    host,
    port,
    debug
)


app = Flask(__name__)

data_for_index = {
    "title": "TestFlask",
    "msg": "List of int:",
    "arr": [12, 34, 56],
}

data_for_reg = {
    "title": "Reg",
    "msg": "Авторизация",
}


@app.route("/")
def index():
    return render_template(
        'index.html',
        **data_for_index
    )


@app.route("/reg")
def reg():
    return render_template(
        'reg.html',
        **data_for_reg
    )


if __name__ == '__main__':
    app.run(host, port, debug)
