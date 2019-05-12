from app import db
from app.model.CollegerModel import Colleger
from app.model.CoursesModel import Courses


class TakeCourse(db.Model):
    __tablename__ = "take_courses"

    id = db.Column(db.Integer, unique=True, primary_key=True, nullable=False)
    colleger_id = db.Column(db.Integer, db.ForeignKey("colleger.id"), nullable=False)
    courses_id = db.Column(db.Integer, db.ForeignKey("courses.id"), nullable=False)
    value = db.Column(db.Float, nullable=True)

    def __repr__(self):
        return "<Colleger Id: {}>".format(self.colleger_id)

    def __init__(self, colleger_id, courses_id):
        self.colleger_id = Colleger.findById(colleger_id).id
        self.courses_id = Courses.findById(courses_id).id

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @staticmethod
    def getAll():
        data = TakeCourse.query.all()
        result = list()
        for value in data:
            obj = {
                "id": value.id,
                "colleger": Colleger.getById(value.colleger_id),
                "courses": Courses.getById(value.courses.id),
                "value": value.value
            }
            result.append(obj)
        return result

    @staticmethod
    def getById(id):
        data = TakeCourse.findById(id)
        result = {
            "id": data.id,
            "colleger": Colleger.getById(data.colleger_id),
            "courses": Courses.getById(data.courses.id),
            "value": data.value
        }
        return result

    @staticmethod
    def findById(id):
        return TakeCourse.query.filter_by(id=id).first()

    @staticmethod
    def findByCollegerIdAndCoursesId(colleger_id, courses_id):
        return TakeCourse.query.filter_by(colleger_id=colleger_id, courses_id=courses_id).first()
