from flask import Flask, redirect, url_for, render_template, Blueprint, session, flash

views = Blueprint("views", __name__)

@views.route("/")
def index():
    return render_template("index.html")

@views.route("/profile")
def profile():
    return render_template("profile.html")