from flask import Blueprint, jsonify, request

from App.Services.user_dao import create_user, get_all, password_matches, update_balance, get_balance

user_bp = Blueprint('user', __name__)

@user_bp.route('/get-all')
def get_all_users():
    try:
        users = get_all()
        users_dicts = [user.to_dict() for user in users]
        return jsonify(users_dicts), 200 #Basically retruning a tuple of the response and the status code.
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
@user_bp.route('/add-user', methods = ['POST'])
def add_user():
    try:
        data = request.get_json()
        create_user(data.get('username'), data.get('password'), data.get('balance'))
        return jsonify('OK'), 200
    except Exception as e:
        return jsonify({"message": f"Failed to create a new user {str(e)}"}), 500
    
@user_bp.route('/authenticate-user/<string:username>/<string:password>')
def authenticate_user(username: str, password:str):
    try:
        user = password_matches(username, password)
        return jsonify(user.to_dict()), 200
    except Exception as e:
        return jsonify ({"message": f"Failed to authenticate user {username}: {str(e)}"}), 500

@user_bp.route('/update-balance/<int:user_id>', methods=['PUT'])
def update_user_balance(user_id):
    try:
        data = request.get_json()
        new_balance = data.get('balance')
        if new_balance is None:
            return jsonify({"message": "Balance is required"}), 400
        user = update_balance(user_id, float(new_balance))
        return jsonify({
            "message": "Balance updated successfully",
            "new_balance": user.balance
        }), 200
    except QueryException as e:
        return jsonify({"message": str(e)}), 404
    except Exception as e:
        return jsonify({"message": str(e)}), 500
    
@user_bp.route('/get-balance/<int:user_id>', methods=['GET'])
def get_user_balance(user_id):
    try:
        balance = get_balance(user_id)
        return jsonify({'balance': balance}), 200
    except QueryException as e:
        return jsonify({'message': str(e)}), 404
    except Exception as e:
        return jsonify({'message': str(e)}), 500