from flask import Flask
from flask.ext.admin import Admin

app = Flask(__name__)

admin = Admin(app)
# Add administrative views here

app.run(host='0.0.0.0')
