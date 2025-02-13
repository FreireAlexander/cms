from flask import render_template
from jinja2 import FileSystemLoader, Environment

from app import create_app

app = create_app()

print("Appp creada")

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login')
def update_page():
    return render_template('login.html')

@app.route('/generate')
def generate():
    env = Environment(
            loader=FileSystemLoader("app/templates"),
            trim_blocks=True,
            lstrip_blocks=True
        )
    template = env.get_template("home.html")
    with open("index.html", "w", encoding="utf-8") as archivo:
        archivo.write(template.render())
    
    return render_template("success.html")