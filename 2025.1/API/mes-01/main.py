from flask import Flask, jsonify, make_response, request
from flask_jwt_extended import create_access_token
from models.user import User
app = Flask(__name__)

users = list()

@app.route("/users", methods=['POST', "GET"])
def users_endpoint():
    if request.method == "POST":
        return create_user(request)
    return [user.to_dict() for user in users]

def create_user(request):
    body = request.get_json()
    login = body['login']
    password = body['password']

    if (not is_user_available(login)):
        return make_response("Login not available", 400)

    user = User(login, password)
    users.append(user)
    return make_response(user.to_dict(), 201)

@app.route("/login", methods=['POST'])
def login():
    body = request.get_json()
    login = body['login']
    password = body['password']
    userCandidate = [user for user in users if user.login == login]
    if len(userCandidate) == 0:
        return make_response("User not found", 401)
    print(userCandidate[0].login)

    is_password_correct = userCandidate[0].compare_password(password)

    if not is_password_correct:
        return make_response("Password does not match", 401)
    return make_response(jsonify(create_access_token(identity=login), 200))


def is_user_available(login):
    for user in users:
        if (user.login == login):
            return False
    return True
