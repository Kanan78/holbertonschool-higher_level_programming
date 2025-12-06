#!/usr/bin/python3
"""This module is about the importance of API security"""

from flask import Flask, jsonify,request
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity

app = Flask(__name__)

app.config["JWT_SECRET_KEY"] = "secret12345"
jwt = JWTManager(app)
auth = HTTPBasicAuth()

users = {
    "user1": {
        "username": "user1",
        "password": generate_password_hash("password"),
        "role": "user"
    },
    "admin1": {
        "username": "admin1",
        "password": generate_password_hash("password"),
        "role": "admin"
    }
}

@auth.verify_password
def verify_password(username, password):
    if username in users and check_password_hash(users[username]["password"],  password):
        return username
    return None


@app.route("/basic-protected")
@auth.login_required
def protected():
    return jsonify({"message": "Basic Auth: Access Granted"}), 200


@app.route("/login", methods=["POST"])
def login():
    data = request.get_json(silent=True)

    if data is None:
        return jsonify({"error": "Invalid JSON"}), 400

    username = data.get("username")
    password = data.get("password")

    if username in users and check_password_hash(users[username]["password"], password):
        access_token = create_access_token(identity={
            "username": username,
            "role": users[username]["role"]})
        return jsonify({"access_token": access_token}), 200
    return jsonify({"error": "Invalid credentials"}), 401

@app.route("/jwt-protected", methods=["GET"])
@jwt_required()
def jwt_required():
    return jsonify({"message": "JWT Auth: Access Granted"}), 200

def admin_required():
    @wraps(fn)
    @jwt_required()
    def wrapper(*args, **kwargs):
        identity = get_jwt_identity()
        if identity["role"] != "admin":
            return jsonify({"error": "Admin access required"}), 403
        return fn(*args, **kwargs)
    return wrapper

@app.route("/admin-only", methods=["GET"])
@admin_required
def admin_only():
    return jsonify({"message": "Admin Access: Granted"}), 200

@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    return jsonify({"error": "Missing or invalid token"}), 401


@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    return jsonify({"error": "Invalid token"}), 401


@jwt.expired_token_loader
def handle_expired_token_error(err):
    return jsonify({"error": "Token has expired"}), 401


@jwt.revoked_token_loader
def handle_revoked_token_error(err):
    return jsonify({"error": "Token has been revoked"}), 401


@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(err):
    return jsonify({"error": "Fresh token required"}), 401

if __name__ == "__main__":
    app.run()
