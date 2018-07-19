# -*- coding:utf-8 -*-
from flask import Flask
from app.home import home
from app.admin import admin

app = Flask(__name__)


app.register_blueprint(home)
app.register_blueprint(admin, url_prefix="/admin")
