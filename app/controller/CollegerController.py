from app import app
from flask import request, render_template, redirect
from app.model.CollegerModel import Colleger


@app.route("/colleger", methods=["GET"])
def getColleger():
    collegers = Colleger.getAll()
    return render_template("colleger.html", data=enumerate(collegers, 1))


@app.route("/colleger", methods=["POST"])
def createColleger():
    identityNumber = request.form["identityNumber"]
    name = request.form["name"]
    colleger = Colleger(identity_number=identityNumber, name=name)
    colleger.save()
    return redirect("/colleger")


@app.route("/colleger/<int:id>/edit", methods=["GET"])
def updateCollegerForm(id):
    colleger = Colleger.getById(id)
    return render_template("colleger_update.html", data=colleger)


@app.route("/colleger/<int:id>/edit", methods=["POST"])
def updateColleger(id):
    colleger = Colleger.findById(id)

    identityNumber = request.form["identityNumber"]
    name = request.form["name"]

    colleger.identity_number = identityNumber
    colleger.name = name
    colleger.save()
    return redirect("/colleger")


@app.route("/colleger/<int:id>/delete", methods=["GET"])
def deleteColleger(id):
    colleger = Colleger.findById(id)
    colleger.delete()
    return redirect("/colleger")
