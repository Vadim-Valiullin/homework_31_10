from flask import Flask

# Это уже знакомое callable WSGI-приложение
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'I will do my best'
