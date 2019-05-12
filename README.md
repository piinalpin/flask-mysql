# Flask MySQL Application With Database Migration Using Flask-Migrate and SQLAlchemy

This project will create CRUD application with Object Relational Mapping on MySQL using flask and sqlalchemy.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

Make sure you have installed Python 3 on your device

### Project structure
```
* flask-mysql/
  |--- app/
  |    |--- config/
  |    |    |--- __init__.py
  |    |    |--- Database.py
  |    |--- controller/
  |    |    |--- __init__.py
  |    |    |--- controller.py
  |    |--- model/
  |    |    |--- Colleger.py
  |    |    |--- Courses.py
  |    |    |--- TakeCourse.py
  |    |--- templates/
  |    |--- __init__.py
  |--- run.py
```

### Step to create this project

A step by step series of examples that tell you how to get a development env running

1. Install virtual environment if you dont have virtual environment
```
pip install virtualenv
```
2. Create virtual environment and activate inside your flask-rest-api directory according the above structure
```
virtualenv venv
> On windows -> venv\Scripts\activate
> On linux -> . env/bin/activate
```
3. Install some third party libraries on your virtual environment with pip
```
pip install flask flask-sqlalchemy flask-migrate mysql-connector-python
```
4. Create `project_name/run.py` directory inside flask-project according the above structure
```python
from app import app


if __name__ == "__main__":
    app.run(host="localhost", port=5000, debug=True)
```
5. Create `project_name/app/config/Database.py` to create configuration for database
```python
class DbConfig:
    def __init__(self):
        self.DB_USERNAME = "<YOUR_USERNAME>"
        self.DB_PASSWORD = "<YOUR_PASSWORD>"
        self.DB_HOST = "localhost"
        self.DB_PORT = 3306
        self.DB_NAME = "<YOUR_DATABASE_NAME>"

    def getUri(self):
        return "mysql+mysqlconnector://{}:{}@{}:{}/{}".format(self.DB_USERNAME, self.DB_PASSWORD, self.DB_HOST,
                                                              self.DB_PORT, self.DB_NAME)

```
6. Create `project_name/app/__init__.py` inside app directory according the above structure `project_name/app/`. This step will setup for SQLAlchemy config.
```python
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from app.config.Database import DbConfig

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = DbConfig().getUri()
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

migrate = Migrate(app, db)

```
7. Define model to application and create database migration, you should create `project_name/app/model/Colleger.py`
```python
from app import db


class Colleger(db.Model):
    __tablename__ = "colleger"

    id = db.Column(db.Integer, unique=True, primary_key=True, nullable=False)
    identity_number = db.Column(db.String(255), nullable=False)
    name = db.Column(db.String(255), nullable=False)
    take_courses = db.relationship("take_courses", backref="colleger", lazy="dynamic")

    def __init__(self, identityNumber, name):
        self.identity_number = identityNumber
        self.name = name

    def __repr__(self):
        return "<Name: {}>".format(self.name)

```
12. Run migration with flask-migrate, type in terminal as below
```
flask db init
flask db migrate
flask db upgrade
```
13. The structure of database should like as follows

Mahasiswa  |
------------- |
`id (Integer, PK, Autoincrement, NOT NULL)`  |
`name (String, NOT NULL)`  |
`nim (String, NOT NULL)`  |


### Want to demo online?
#### [Backend Flask REST API](https://flask-rest-api-maverick.herokuapp.com/)

## Built With

* [Python 3](https://www.python.org/download/releases/3.0/) - The language programming used
* [Flask](http://flask.pocoo.org/) - The web framework used
* [Flask Migrate](https://pypi.org/project/Flask-Migrate/) - The database migration
* [Virtualenv](https://virtualenv.pypa.io/en/latest/) - The virtual environment used
* [SQL Alchemy](https://www.sqlalchemy.org/) - The database library
* [Flask-SQLAlchemy](http://flask-sqlalchemy.pocoo.org/2.3/) - Flask and SQL Alchemy connector

## Clone or Download

You can clone or download this project
```
> Clone : git clone https://github.com/piinalpin/flask-rest-api.git
```

## Authors

* **Alvinditya Saputra** - *Initial work* - [DSS Consulting](https://dssconsulting.id/) - [LinkedIn](https://linkedin.com/in/piinalpin) [Instagram](https://www.instagram.com/piinalpin) [Twitter](https://www.twitter.com/piinalpin)
