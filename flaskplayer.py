from flask import Flask, request
app = Flask(__name__)

@app.route('/')
def splash_page():
    return 'Welcome to The Seminal Apocalypse. Entrench!'