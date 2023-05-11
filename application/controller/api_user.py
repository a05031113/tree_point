from flask import *
from application.model import *

user_api = Blueprint('user_api', __name__)


@user_api.route("/api/user/add", methods=["POST"])
def api_register():
    data = request.get_json()["data"]
    username = data["username"]
    try:
        # check is user exist
        search_result = rds().check_user(username)
        if len(search_result) > 0:
            return jsonify({"error": True, "message": "user already exist"}), 400
        else:
            # create user
            insert_result = rds().add_user(username)
            if insert_result:
                return jsonify({"register": True, "message": "register success"}), 200
    except:
        return jsonify({"error": True, "message": SyntaxError}), 500
