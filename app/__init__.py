from flask import Flask

from . import config

app = config.app

from .login import login
app.register_blueprint(login)

