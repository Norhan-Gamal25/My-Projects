import os

from cs50 import SQL
from flask import Flask, redirect, render_template, request, session, url_for
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash
from helpers import apology, textToaudio, login_required, convert_is_correct

app = Flask(__name__)

app.jinja_env.filters['convert_is_correct'] = convert_is_correct

# Configure session to use filesystem (instead of signed cookies)
app.secret_key = os.environ.get("SECRET_KEY") or os.urandom(24)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///braille.db")

@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 400)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 400)

        # Query database for username
        rows = db.execute(
            "SELECT * FROM users WHERE username = ?", request.form.get("username")
        )

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(
            rows[0]["hash"], request.form.get("password")
        ):
            return apology("invalid username and/or password", 400)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")
    
@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    if request.method == "GET":
        return render_template("register.html")
    if request.method == "POST":
        password = request.form.get("password")
        password_confirm = request.form.get("confirmation")
        if not password:
            return apology("Must provide password", 400)
        if not password_confirm:
            return apology("Must provide password confirmation", 400)
        user_name = request.form.get("username")
        if not user_name:
            return apology("Must provide user name", 400)
        if password != password_confirm:
            return apology("Passwords don't match", 400)
        hashed_password = generate_password_hash(password, method='scrypt')
        try:
            db.execute("INSERT INTO USERS (username, hash) VALUES (?, ?)",
                        user_name, hashed_password)
        except:
            return apology("Username already exists", 400)
        user_id = db.execute("SELECT id FROM users WHERE username = ?", user_name)
        session["user_id"] = user_id[0]["id"]
        return redirect("/login")
            
@app.route("/")
def index():
    return render_template("index.html")
 
@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")

@app.route("/lessons")
@login_required 
def lessons():
    """Show lessons page"""
    return render_template("lessons.html")

@app.route("/quizzes", methods=["GET", "POST"]) 
@login_required 
def quizzes():  
    """Show quizzes page"""
    if request.method == "GET":
        section = request.args.get("section")
        alphabetAndnumbers = db.execute("SELECT * FROM braille_quizzes where lesson = 'Alphabet' or lesson = 'Numbers'")
        punctuation = db.execute("SELECT * FROM braille_quizzes where lesson = 'Punctuation'")
        contractions = db.execute("SELECT * FROM braille_quizzes where lesson = 'Contractions'")
        return render_template("quizzes.html", section=section, alphabetAndnumbers=alphabetAndnumbers, punctuation=punctuation, contractions=contractions)
    if request.method == "POST":
        section = request.form.get("section")
        quiz_id = request.form.get("quiz_id")
        user_id = session["user_id"]
        userans = request.form.get("answer")
        if not userans:
            return apology("Must provide an answer", 400)
        answer = db.execute("SELECT correct_answer FROM braille_quizzes WHERE id = ?", quiz_id)
        correct_answer = answer[0]["correct_answer"]
        if userans.lower() == correct_answer.lower():
            db.execute("INSERT INTO quiz_attempts (user_id, quiz_id, is_correct, answered_at) VALUES (?, ?, ?, CURRENT_TIMESTAMP)", user_id, quiz_id, 1)
            textToaudio("Correct! Excellent work, you're learning fast!")
        else:
            db.execute("INSERT INTO quiz_attempts (user_id, quiz_id, is_correct, answered_at) VALUES (?, ?, ?, CURRENT_TIMESTAMP)", user_id, quiz_id, 0)
            textToaudio(f"Not quite, but don't worry. The correct answer is {correct_answer}. You'll get it next time!")
        return redirect(url_for("quizzes", section=section))

@app.route("/progress", methods=["GET"])
@login_required
def progress():
    """Show user's progress"""
    if request.method == "GET":
        user_id = session["user_id"]
        progress_data = db.execute("SELECT question, is_correct, answered_at FROM quiz_attempts qa JOIN braille_quizzes bq ON qa.quiz_id = bq.id WHERE qa.user_id = ?", user_id)
        return render_template("progress.html", progress_data=progress_data)