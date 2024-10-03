from flask import Flask, render_template, request, redirect
from waitress import serve
from dotenv import load_dotenv
import os

import controllers.profile as profile


load_dotenv() 

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/profile')
def profile_by_id():
    id = request.args.get('id')
    if id == None : return redirect("/", code=302)
    return render_template('profile.html', 
                           profile=profile.get_profile_info(id),
                           achievements=profile.get_profile_achievements(id))

if __name__ == "__main__":
    print("\n===Portfolio server===\n")
    host = os.getenv("HOST")
    port = os.getenv("PORT")
    print(f"Host: {host}")
    print(f"Port: {port}")
    print("\n===\n")
    serve(app, host=host, port=port)