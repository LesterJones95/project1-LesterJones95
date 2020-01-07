import os

from flask import Flask, session, render_template, request
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

app = Flask(__name__)

# Check for environment variable
if not os.getenv("DATABASE_URL"):
    raise RuntimeError("DATABASE_URL is not set")

# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Set up database
engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))

db_loc = scoped_session(sessionmaker(bind=create_engine("postgres://postgres:root@localhost:5432/bookreview_project1")))

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/sign_up")
def sign_up():

    return render_template("sign_up.html")

@app.route("/personal_page", methods=["POST"])
def personal_page():
    """Log Existing User in"""
    users = db_loc.execute("SELECT * FROM users").fetchall()

    username = request.form.get("username")
    password = request.form.get("password")

    if db_loc.execute("SELECT * FROM users WHERE username = :username AND password =:password", {"username": username, "password":password}).rowcount == 0:
        return render_template("error.html", message="No such user.")

    return render_template("personal_page.html")

@app.route("/register", methods=["POST"])
def register():
    """Log Existing User in"""
    users = db_loc.execute("SELECT * FROM users").fetchall()

    username = request.form.get("username")
    password = request.form.get("password")

    if db_loc.execute("SELECT * FROM users WHERE username = :username", {"username": username}).rowcount == 1:
        return render_template("error.html", message="Username taken")


    db_loc.execute("INSERT INTO users (username, password) VALUES (:username, :password)",
            {"username": username, "password": password})
    db_loc.commit()
    return render_template("success.html")
