from flask import Blueprint, request
from flask_jwt_extended import create_access_token
from ..models.user_model import User
from .. import db

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/register", methods=["POST"])
def register():

    data = request.json

    user = User(
        name=data["name"],
        email=data["email"],
        password=data["password"],
        role=data["role"]
    )

    db.session.add(user)
    db.session.commit()

    return {"message": "User registered"}

@auth_bp.route("/login", methods=["POST"])
def login():

    data = request.json

    user = User.query.filter_by(email=data["email"]).first()

    if user and user.password == data["password"]:
        token = create_access_token(identity=str(user.id))
        return {"token": token}

    return {"message": "Invalid credentials"}