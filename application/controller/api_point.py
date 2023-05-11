from flask import *
from application.model import *

point_api = Blueprint('point_api', __name__)


@point_api.route("/api/point/received", methods=["POST"])
def api_received():
    data = request.get_json()["data"]
    username = data["username"]
    received = data["received"]
    try:
        check_result = rds().check_user(username)
        user_id = check_result[0]["id"]
        # check is user exist
        if len(check_result) == 0:
            return jsonify({"error": True, "message": "user not exist"}), 400
        # give user points
        result = rds().received_or_used_point(user_id, received)
        if result:
            return jsonify({"success": True, "received points": received}), 200
    except:
        return jsonify({"error": True, "message": SyntaxError}), 500


@point_api.route("/api/point/used", methods=["POST"])
def api_used():
    data = request.get_json()["data"]
    username = data["username"]
    used = -data["used"]
    try:
        check_result = rds().total_point(username)
        user_id = check_result[0]["id"]
        rest_point = check_result[0]["total_points"]
        # check is user exist
        if not user_id:
            return jsonify({"error": True, "message": "user not exist"}), 400
        # check is enough points
        if used + rest_point < 0:
            return jsonify({"error": True, "message": "not enough points"}), 400
        # used points
        result = rds().received_or_used_point(user_id, used)
        if result:
            return jsonify({"success": True, "used points": -used}), 200
    except:
        return jsonify({"error": True, "message": SyntaxError}), 500


@point_api.route("/api/point/", methods=["GET"])
def api_count():
    data = request.get_json()["data"]
    username = data["username"]
    try:
        result = rds().total_point(username)
        user_id = result[0]["id"]
        total_points = result[0]["total_points"]
        # check user exist
        if not user_id:
            return jsonify({"error": True, "message": "user not exist"}), 400
        # return total points
        return jsonify({"success": True, "total points": total_points}), 200
    except:
        return jsonify({"error": True, "message": SyntaxError}), 500
