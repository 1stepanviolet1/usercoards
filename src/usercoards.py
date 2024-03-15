from flask import Flask, render_template

from config import (
    host,
    port,
    debug
)


app = Flask(__name__)

title = "TestFlask"
msg = "This is cool!"
arr = [12, 34, 56]


@app.route("/")
def index():
    return render_template(
        'index.html',
        title=title,
        msg=msg,
        arr=arr
    )


if __name__ == '__main__':
    app.run(host, port, debug)
