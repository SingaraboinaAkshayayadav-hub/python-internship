from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory database
users = [
    {"id": 1, "name": "Akshaya", "age": 20},
    {"id": 2, "name": "Rahul", "age": 22}
]

# GET - Fetch all users
@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users), 200

# GET - Fetch user by ID
@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    for user in users:
        if user["id"] == user_id:
            return jsonify(user), 200
    return jsonify({"message": "User not found"}), 404

# POST - Add new user
@app.route('/users', methods=['POST'])
def add_user():
    data = request.json

    new_user = {
        "id": len(users) + 1,
        "name": data["name"],
        "age": data["age"]
    }

    users.append(new_user)
    return jsonify(new_user), 201

# PUT - Update user
@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.json

    for user in users:
        if user["id"] == user_id:
            user["name"] = data.get("name", user["name"])
            user["age"] = data.get("age", user["age"])
            return jsonify(user), 200

    return jsonify({"message": "User not found"}), 404

# DELETE - Remove user
@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    for user in users:
        if user["id"] == user_id:
            users.remove(user)
            return jsonify({"message": "User deleted"}), 200

    return jsonify({"message": "User not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)