from flask import Flask, render_template, request, Response
import requests
import json
import os

SERVER = 'https://bunkie-backend-foja2uwzca-ey.a.run.app'
TOKEN = ""
IMAGE_FOLDER = os.path.join('static', 'img')

app = Flask(__name__)
app.config['SERVER'] = SERVER
app.config['TOKEN'] = TOKEN
app.config['IMAGE_FOLDER'] = IMAGE_FOLDER

@app.route('/')
def index():
    icon_filename = os.path.join(app.config['IMAGE_FOLDER'], 'icon.png')
    logo_filename = os.path.join(app.config['IMAGE_FOLDER'], 'logo.png')
    return render_template("index.html", icon=icon_filename, logo=logo_filename)

@app.route('/login', methods=['POST'])
def login():
    email = request.form['admin-email']
    password = request.form['admin-pw']
    headers = {'Access-Control-Allow-Origin': '*',
            'Content-Type': 'application/json; charset=UTF-8'}
    response = requests.post(
        app.config['SERVER']+'/users/admin/login',
        json={"username_or_email": email, "password": password},
        headers=headers)
    if response.status_code == 200:
        app.config['TOKEN'] = dict(json.loads(response.text))['token']
        icon_filename = os.path.join(app.config['IMAGE_FOLDER'], 'icon.png')
        logo_filename = os.path.join(app.config['IMAGE_FOLDER'], 'logo.png')
        return render_template("console.html", icon=icon_filename, logo=logo_filename)
    else:
        return None, response.status_code, headers

@app.route('/get_users', methods=['POST'])
def get_user():
    username = request.form['uname']
    headers = {'Access-Control-Allow-Origin': '*',
            'Content-Type': 'application/json; charset=UTF-8'}
    response = requests.post(
        app.config['SERVER']+'/users/admin/get_users',
        json={"token": app.config['TOKEN']},
        headers=headers)
    print(response)

if __name__ == "__main__":
    app.run()