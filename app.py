from flask import (
    Flask,
    render_template,
    request,
    url_for,
    redirect
)

from user import UserManager

manager = UserManager()

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]

        is_login_valid = manager.validade_login(email, password)
        if is_login_valid:
            return redirect(url_for("session"))

        return redirect(url_for("login"))

    return render_template("index.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        first_name = request.form["first_name"]
        last_name = request.form["last_name"]
        email = request.form["email"]
        password = request.form["password"]

        sucessful = manager.create_user(first_name, last_name, email, password)
        print(sucessful)
        if sucessful:
            return redirect(url_for("login"))

        return redirect(url_for("register"))

    return render_template("register.html")

@app.route("/session")
def session():
    return render_template("session.html")

if __name__ == "__main__":
	app.run(debug=True)