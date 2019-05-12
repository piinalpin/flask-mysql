from app import app
from flask import request, render_template, redirect
from app.model.CollegerModel import Colleger
from app.model.CoursesModel import Courses
from app.model.TakeCourseModel import TakeCourse


@app.route("/take-courses", methods=["GET"])
def getTakeCourses():
    collegers = Colleger.getAll()
    courses = Courses.getAll()
    takeCourses = TakeCourse.getAll()
    if "message" in request.args:
        message = request.args["message"]
    else:
        message = ""
    return render_template("take_courses.html", collegers=collegers, courses=courses, data=enumerate(takeCourses, 1),
                           message=message)


@app.route("/take-courses", methods=["POST"])
def createTakeCourse():
    collegerId = request.form["collegerId"]
    courseId = request.form["coursesId"]
    findExisting = TakeCourse.findByCollegerIdAndCoursesId(colleger_id=collegerId, courses_id=courseId)
    if findExisting is not None:
        return redirect("/take-courses?message=Failed! Duplicate Data.")
    else:
        takeCourses = TakeCourse(courses_id=courseId, colleger_id=collegerId)
        takeCourses.save()
        return redirect("/take-courses")


@app.route("/take-courses/<int:id>/add-value", methods=["GET"])
def updateValueForm(id):
    takeCourses = TakeCourse.getById(id)
    return render_template("take_courses_update.html", data=takeCourses)


@app.route("/take-courses/<int:id>/add-value", methods=["POST"])
def updateValue(id):
    takeCourses = TakeCourse.findById(id)

    value = float(request.form["value"])

    takeCourses.value = value
    takeCourses.save()
    return redirect("/take-courses")


@app.route("/take-courses/<int:id>/delete")
def deleteTakeCourses(id):
    takeCourses = TakeCourse.findById(id)
    takeCourses.delete()
    return redirect("/take-courses")
