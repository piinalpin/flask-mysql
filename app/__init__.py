from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from app.config.Database import DbConfig

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = DbConfig().getUri()
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

from app.model import CoursesModel, CollegerModel, TakeCourseModel

migrate = Migrate(app, db)

from app.controller.Main import *
from app.controller.CollegerController import *
from app.controller.CoursesController import *
from app.controller.TakeCourseController import *