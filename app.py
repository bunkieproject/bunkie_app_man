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
        return render_template("console.html", icon=icon_filename, logo=logo_filename, user_id="")
    
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

    icon_filename = os.path.join(app.config['IMAGE_FOLDER'], 'icon.png')
    logo_filename = os.path.join(app.config['IMAGE_FOLDER'], 'logo.png')

    for account in response.json()["result"]:
        if account["username"] == username:
            return render_template("console.html", icon=icon_filename, logo=logo_filename, user_id=account["user_id"])

    return render_template("console.html", icon=icon_filename, logo=logo_filename, user_id="")

@app.route('/warn_user', methods=['POST'])
def warn_user():
    user_id = request.form['userid']
    headers = {'Access-Control-Allow-Origin': '*',
            'Content-Type': 'application/json; charset=UTF-8'}

    response = requests.post(
        app.config['SERVER'] + '/users/admin/warn_user',
        json={"token": app.config['TOKEN'], "user_id": user_id},
        headers=headers)

    if response.status_code == 200:
        icon_filename = os.path.join(app.config['IMAGE_FOLDER'], 'icon.png')
        logo_filename = os.path.join(app.config['IMAGE_FOLDER'], 'logo.png')
        return render_template("console.html", icon=icon_filename, logo=logo_filename, user_id="")
    else:
        return None, response.status_code, headers

@app.route('/ban_user', methods=['POST'])
def ban_user():
    user_id = request.form['userid']
    headers = {'Access-Control-Allow-Origin': '*',
            'Content-Type': 'application/json; charset=UTF-8'}

    response = requests.post(
        app.config['SERVER'] + '/users/admin/ban_user',
        json={"token": app.config['TOKEN'], "user_id": user_id},
        headers=headers)

    if response.status_code == 200:
        icon_filename = os.path.join(app.config['IMAGE_FOLDER'], 'icon.png')
        logo_filename = os.path.join(app.config['IMAGE_FOLDER'], 'logo.png')
        return render_template("console.html", icon=icon_filename, logo=logo_filename, user_id="")
    else:
        return None, response.status_code, headers

@app.route('/unban_user', methods=['POST'])
def unban_user():
    user_id = request.form['userid']
    headers = {'Access-Control-Allow-Origin': '*',
            'Content-Type': 'application/json; charset=UTF-8'}

    response = requests.post(
        app.config['SERVER'] + '/users/admin/unban_user',
        json={"token": app.config['TOKEN'], "user_id": user_id},
        headers=headers)

    if response.status_code == 200:
        icon_filename = os.path.join(app.config['IMAGE_FOLDER'], 'icon.png')
        logo_filename = os.path.join(app.config['IMAGE_FOLDER'], 'logo.png')
        return render_template("console.html", icon=icon_filename, logo=logo_filename, user_id="")
    else:
        return None, response.status_code, headers

@app.route('/delete_user', methods=['POST'])
def delete_user():
    user_id = request.form['userid']
    headers = {'Access-Control-Allow-Origin': '*',
            'Content-Type': 'application/json; charset=UTF-8'}

    response = requests.post(
        app.config['SERVER'] + '/users/admin/delete_user',
        json={"token": app.config['TOKEN'], "user_id": user_id},
        headers=headers)

    if response.status_code == 200:
        icon_filename = os.path.join(app.config['IMAGE_FOLDER'], 'icon.png')
        logo_filename = os.path.join(app.config['IMAGE_FOLDER'], 'logo.png')
        return render_template("console.html", icon=icon_filename, logo=logo_filename, user_id="")
    else:
        return None, response.status_code, headers

if __name__ == "__main__":
    app.run()