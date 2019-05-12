from app import db


class Courses(db.Model):
    __tablename__ = "courses"

    id = db.Column(db.Integer, unique=True, primary_key=True, nullable=False)
    name = db.Column(db.String(255), nullable=False)
    sks = db.Column(db.Integer, nullable=False)
    semester = db.Column(db.Integer, nullable=False)
    courses_take = db.relationship('TakeCourse', backref='courses', lazy='dynamic')

    def __init__(self, name, sks, semester):
        self.name = name
        self.sks = sks
        self.semester = semester

    def __repr__(self):
        return "<Name: {}, SKS: {}>".format(self.name, self.sks, self.semester)

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @staticmethod
    def getAll():
        courses = Courses.query.all()
        result = list()
        for course in courses:
            obj = {
                "id": course.id,
                "name": course.name,
                "sks": course.sks,
                "semester": course.semester
            }
            result.append(obj)
        return result

    @staticmethod
    def getById(id):
        course = Courses.findById(id)
        result = {
            "id": course.id,
            "name": course.name,
            "sks": course.sks,
            "semester": course.semester
        }
        return result

    @staticmethod
    def findById(id):
        return Courses.query.filter_by(id=id).first()
