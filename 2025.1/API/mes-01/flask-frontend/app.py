from flask import Flask, jsonify, make_response, request, render_template, redirect, url_for, session
from flask_jwt_extended import JWTManager, create_access_token
import os

# Import User model - assuming it's in a models directory
from models.user import User

app = Flask(__name__)
app.secret_key = os.urandom(24)  # For session management
app.config['JWT_SECRET_KEY'] = os.urandom(24)  # For JWT
jwt = JWTManager(app)

users = list()

@app.route("/api/users", methods=['POST', "GET"])
def users_endpoint():
    if request.method == "POST":
        return create_user(request)
    return jsonify([user.to_dict() for user in users])

def create_user(request):
    body = request.get_json()
    login = body['login']
    password = body['password']

    if (not is_user_available(login)):
        return make_response("Login not available", 400)

    user = User(login, password)
    users.append(user)
    return make_response(jsonify(user.to_dict()), 201)

@app.route("/api/login", methods=['POST'])
def api_login():
    body = request.get_json()
    login = body['login']
    password = body['password']
    userCandidate = [user for user in users if user.login == login]
    if len(userCandidate) == 0:
        return make_response("User not found", 401)

    is_password_correct = userCandidate[0].compare_password(password)

    if not is_password_correct:
        return make_response("Password does not match", 401)
    token = create_access_token(identity=login)
    return make_response(jsonify({"token": token}), 200)

def is_user_available(login):
    for user in users:
        if (user.login == login):
            return False
    return True

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    error = None
    if request.method == "POST":
        login = request.form.get("login")
        password = request.form.get("password")

        if login is not str or password is not str:
            error = "Paramaters incorrect"

        elif not is_user_available(login):

            error = "Login not available"
        else:
            user = User(login, password)
            users.append(user)
            return redirect(url_for("login"))

    return render_template("register.html", error=error)

@app.route("/login", methods=["GET", "POST"])
def login():
    error = None
    if request.method == "POST":
        login = request.form.get("login")
        password = request.form.get("password")

        userCandidate = [user for user in users if user.login == login]
        if len(userCandidate) == 0:
            error = "User not found"
        else:
            is_password_correct = userCandidate[0].compare_password(password)
            if not is_password_correct:
                error = "Password does not match"
            else:
                session["user"] = login
                return redirect(url_for("dashboard"))

    return render_template("login.html", error=error)

@app.route("/dashboard")
def dashboard():
    if "user" not in session:
        return redirect(url_for("login"))

    return render_template("dashboard.html", username=session["user"], users=users)

@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(debug=True)
