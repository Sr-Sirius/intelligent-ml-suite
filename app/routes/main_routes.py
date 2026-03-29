from flask import Blueprint, render_template

main_bp = Blueprint(
    "main",
    __name__,
    template_folder="../templates"
)

@main_bp.route("/")
def home():
    return render_template("home.html", theme="ml")


@main_bp.route("/ml")
def ml_menu():
    return render_template("ml/menu.html", theme="ml")