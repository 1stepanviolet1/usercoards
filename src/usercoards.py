from flask import (
    Flask, 
    render_template,
    request,
    flash
)

from dbapi import (
    connect_to_db,
    close_db,
    get_id_by_username,
    insert_data,
    get_all
)


from config import (
    host,
    port,
    debug
)


app = Flask(__name__)
app.config["SECRET_KEY"] = "ks76dgsKJHsfg76JHdusvb7s7gdf"


data_for_index = {
    "title": "usercoards"
}


def render_reg(**values):
    return render_template(
        'reg.html',
        title="reg",
        msg="Авторизация",
        **values
    )

def render_index(**values):
    return render_template(
        'index.html',
        title="usercoards",
        **values
    )


@app.route("/")
def index():
    users = get_all(DB)
    return render_index(users=[user.items() for user in users])


@app.route("/reg", methods=["GET", "POST"])
def reg():
    if request.method == "GET":
        return render_reg()

    _username = request.form["username"]
    _pwd = request.form["pwd"]

    try:
        int(_username)
    except ValueError:
        ...
    else:
        flash("Bad username: full numbers", category="error")
        return render_reg(
            username=_username,
            pwd=_pwd
        )
    
    if len(_username) < 4:
        flash("Bad username: minimal length - 4", category="error")
        return render_reg(
            username=_username,
            pwd=_pwd
        )
    
    if len(_pwd) < 3:
        flash("Bad password: minimal length - 3", category="error")
        return render_reg(
            username=_username,
            pwd=_pwd
        )
    
    if len(_username) > 255:
        flash("Maximal username length - 255", category="error")
        return render_reg(
            username=_username,
            pwd=_pwd
        )
    
    if len(_username) > 255:
        flash("Maximal password length - 255", category="error")
        return render_reg(
            username=_username,
            pwd=_pwd
        )
    

    userid = get_id_by_username(DB, _username)

    if userid:
        flash("This user already exists", category="error")
        return render_reg(
            username=_username,
            pwd=_pwd
        )
    
    insert_data(DB, _username, _pwd)
    flash("Success", category="message")

    return render_reg()


if __name__ == '__main__':
    DB = connect_to_db()
    app.run(host, port, debug)
    close_db(DB)
