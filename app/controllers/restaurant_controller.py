from flask import Blueprint, jsonify, request

from models.restauran_model import Animal
from utils.decorators import jwt_required, roles_required
from views.restaurant_view import render_animal_detail, render_animal_list

animal_bp = Blueprint("restaurant", __name__)


@animal_bp.route("/restaurant", methods=["GET"])
@jwt_required
@roles_required(roles=["admin", "user"])
def get_restaurant():
    restaurant = Animal.get_all()
    return jsonify(render_animal_list(restaurant))


@animal_bp.route("/restaurant/<int:id>", methods=["GET"])
@jwt_required
@roles_required(roles=["admin", "user"])
def get_animal(id):
    animal = Animal.get_by_id(id)
    if animal:
        return jsonify(render_animal_detail(animal))
    return jsonify({"error": "Animal no encontrado"}), 404


@animal_bp.route("/restaurant", methods=["POST"])
@jwt_required
@roles_required(roles=["admin"])
def create_animal():
    data = request.json
    user_id = data.get("user_id")
    reservation_id = data.get("reservation_id")
    reservation_date = data.get("reservation_date")

    if not user_id or not reservation_id or reservation_date is None:
        return jsonify({"error": "Faltan datos requeridos"}), 400

    animal = Animal(user_id=user_id, reservation_id=reservation_id, reservation_date=reservation_date)
    animal.save()

    return jsonify(render_animal_detail(animal)), 201


@animal_bp.route("/restaurant/<int:id>", methods=["PUT"])
@jwt_required
@roles_required(roles=["admin"])
def update_animal(id):
    animal = Animal.get_by_id(id)

    if not animal:
        return jsonify({"error": "restaurant no encontrado"}), 404

    data = request.json
    user_id = data.get("user_id")
    reservation_id = data.get("reservation_id")
    reservation_date = data.get("reservation_date")

    animal.update(user_id=user_id, reservation_id=reservation_id, reservation_date=reservation_date)

    return jsonify(render_animal_detail(animal))


@animal_bp.route("/restaurant/<int:id>", methods=["DELETE"])
@jwt_required
@roles_required(roles=["admin"])
def delete_animal(id):
    animal = Animal.get_by_id(id)

    if not animal:
        return jsonify({"error": "Animal no encontrado"}), 404

    animal.delete()

    return "", 204
