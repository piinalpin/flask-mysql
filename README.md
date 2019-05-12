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
  |    |    |--- CollegerController.py
  |    |    |--- CoursesController.py
  |    |    |--- Main.py
  |    |    |--- TakeCourseController.py
  |    |--- model/
  |    |    |--- CollegerModel.py
  |    |    |--- CoursesModel.py
  |    |    |--- TakeCourseModel.py
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
4. Install MySQL database if you don't have, but if you have MySQL you can skip this step
5. Create user and grant privilege for user was created
```mysql
mysql> CREATE USER 'newuser'@'localhost' IDENTIFIED BY 'password';
mysql> GRANT ALL PRIVILEGES ON * . * TO 'newuser'@'localhost';
mysql> FLUSH PRIVILEGES;
```
6. Create database on MySQL
```mysql
mysql> CREATE DATABASE YOUR_DATABASE_NAME
```
7. Create `project_name/run.py` directory inside flask-project according the above structure
```python
from app import app


if __name__ == "__main__":
    app.run(host="localhost", port=5000, debug=True)
```
8. Create `project_name/app/config/Database.py` to create configuration for database
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
9. Create `project_name/app/__init__.py` inside app directory according the above structure `project_name/app/`. This step will setup for SQLAlchemy config.
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
10. Define colleger model to application and create database migration, create python file on `app/model/` you can see defined model on [here](https://github.com/piinalpin/flask-mysql/tree/master/app/model)
11. Update `app/__init__.py` should like as follows
```python
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
```
12. Run migration with flask-migrate, type in terminal as below
```
flask db init
flask db migrate
flask db upgrade
```
13. The structure of database should like as follows
![Sample Database](https://raw.githubusercontent.com/piinalpin/flask-mysql/master/docs/dbdiagram.png)

14. Create controller to application, create python file on `app/controller/` you can see defined controller [here](https://github.com/piinalpin/flask-mysql/tree/master/app/controller)
15. Update `app/__init__.py` add this import into end line of file, this step to import the controller
```python
from app.controller.Main import *
from app.controller.CollegerController import *
from app.controller.CoursesController import *
from app.controller.TakeCourseController import *
```
16. Create templates to application on `app/templates/` you can see defined templates [here](https://github.com/piinalpin/flask-mysql/tree/master/app/templates)
17. Then, you can run this application by terminal
```
python run.py
```
18. Homepage

![Sample Homepage](https://raw.githubusercontent.com/piinalpin/flask-mysql/master/docs/homepage.png)

19. Colleger Page
![Sample Colleger](https://raw.githubusercontent.com/piinalpin/flask-mysql/master/docs/colleger.png)

20. Courses Page
![Sample Courses](https://raw.githubusercontent.com/piinalpin/flask-mysql/master/docs/courses.png)

21. Take Course Page
![Sample Take Course](https://raw.githubusercontent.com/piinalpin/flask-mysql/master/docs/take_courses.png)

## Built With

* [Python 3](https://www.python.org/download/releases/3.0/) - The language programming used
* [Flask](http://flask.pocoo.org/) - The web framework used
* [Flask Migrate](https://pypi.org/project/Flask-Migrate/) - The database migration
* [Virtualenv](https://virtualenv.pypa.io/en/latest/) - The virtual environment used
* [SQL Alchemy](https://www.sqlalchemy.org/) - The database library
* [Flask-SQLAlchemy](http://flask-sqlalchemy.pocoo.org/2.3/) - Flask and SQL Alchemy connector
* [MySQL Connector Python](https://pypi.org/project/mysql-connector-python/) - Connector MySQL for Python
* [MySQL](https://www.mysql.com/) - MySQL Database

## Clone or Download

You can clone or download this project
```
> Clone : git clone https://github.com/piinalpin/flask-mysql.git
```

## Authors

* **Alvinditya Saputra** - [LinkedIn](https://linkedin.com/in/piinalpin) [Instagram](https://www.instagram.com/piinalpin) [Twitter](https://www.twitter.com/piinalpin)
