from app import db


class Colleger(db.Model):
    __tablename__ = "colleger"

    id = db.Column(db.Integer, unique=True, primary_key=True, nullable=False)
    identity_number = db.Column(db.String(255), nullable=False)
    name = db.Column(db.String(255), nullable=False)
    collegers_take = db.relationship('TakeCourse', backref='colleger', lazy='dynamic')

    def __init__(self, identity_number, name):
        self.identity_number = identity_number
        self.name = name

    def __repr__(self):
        return "<Name: {}>".format(self.name)

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @staticmethod
    def getAll():
        collegers = Colleger.query.all()
        result = list()
        for colleger in collegers:
            obj = {
                "id": colleger.id,
                "identity_number": colleger.identity_number,
                "name": colleger.name
            }
            result.append(obj)
        return result

    @staticmethod
    def getById(id):
        colleger = Colleger.findById(id)
        result = {
            "id": colleger.id,
            "identity_number": colleger.identity_number,
            "name": colleger.name
        }
        return result

    @staticmethod
    def findById(id):
        return Colleger.query.filter_by(id=id).first()
