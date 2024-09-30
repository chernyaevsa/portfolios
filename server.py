from flask import Flask, render_template, request
from waitress import serve
from dotenv import load_dotenv
import os

import db

load_dotenv() 

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

if __name__ == "__main__":
    ddd = db.Database()
    ddd.get_profile_info()
    print("\n===Portfolio server===\n")
    host = os.getenv("HOST")
    port = os.getenv("PORT")
    print(f"Host: {host}")
    print(f"Port: {port}")
    print("\n===\n")
    serve(app, host=host, port=port)