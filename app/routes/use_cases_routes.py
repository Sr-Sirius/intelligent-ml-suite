from flask import Blueprint, render_template

use_cases = Blueprint("use_cases", __name__)

@use_cases.route("/")
def menu():
    return render_template("use_cases/menu.html")

@use_cases.route("/case1")
def case1():
    return render_template("use_cases/case1.html")

@use_cases.route("/case2")
def case2():
    return render_template("use_cases/case2.html")

@use_cases.route("/case3")
def case3():
    return render_template("use_cases/case3.html")

@use_cases.route("/case4")
def case4():
    return render_template("use_cases/case4.html")