from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from ..models.food_model import Food
from .. import db

food_bp = Blueprint("food", __name__)

@food_bp.route("/foods", methods=["POST"])
@jwt_required()
def add_food():

    data = request.json

    food = Food(
        food_name=data["food_name"],
        quantity=data["quantity"],
        location=data["location"],
        expiry_time=data["expiry_time"]
    )

    db.session.add(food)
    db.session.commit()

    return {"message": "Food added"}

@food_bp.route("/foods", methods=["GET"])
def get_foods():

    foods = Food.query.all()

    result = []

    for f in foods:
        result.append({
            "id": f.id,
            "food": f.food_name,
            "quantity": f.quantity,
            "location": f.location
        })

    return jsonify(result)