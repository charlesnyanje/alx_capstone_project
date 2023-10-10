from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY']="myscecegdhdfkjfjfkjffjkffkjfjk"

from flaskblog import routes