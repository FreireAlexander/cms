from flask import Flask, render_template
from settings import general_settings

app = Flask('')


@app.route("/")
def helloWorld():
    return render_template("admin/index.html")


@app.route("/admin")
def adminPage():
    return render_template("admin.html")


if __name__ == "__main__":
    app.run(debug=True)