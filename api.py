# Creating a rest APi Using flask to manage user data 

# Imported libraries Flask ,request and jsonify
from flask import Flask, request, jsonify, send_from_directory
import os

app = Flask(__name__)

# Creating a dictionary 
users = {}


@app.route("/")
def home():
    return jsonify({"Message": "WELCOME TO OUR USER MANAGEMENT API"})


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(
        os.path.join(app.root_path),
        'favicon.ico',
        mimetype='image/vnd.microsoft.icon'
    )



# GET all users
@app.route("/users", methods=["GET"])
def get_users():
    return jsonify(users)




# GET a single user ID 
@app.route("/users/<int:user_id>", methods=["GET"])
def get_user(user_id):
    if user_id in users:
        return jsonify(users[user_id])
    return jsonify({"error": "User not found"}), 404




# POST : Add a new user 
@app.route("/users", methods=["POST"])
def create_user():
    data = request.get_json()  # Gives u the json data
    if not data or "name" not in data or "email" not in data:
        return jsonify({"error": "Invalid data"}), 400
    

    user_id = len(users) + 1
    users[user_id] = {
        "name": data["name"],
        "email": data["email"]
    }
    return jsonify({"message" : "User created", "User": users[user_id]}), 201





# PUT: Update user by ID
@app.route("/users/<int:user_id>", methods=["PUT"])
def update_user(user_id):
     if user_id in users: 
        data = request.get_json() 
        users[user_id].update(data) 
        return jsonify({"message": "User updated", "user": users[user_id]}) 
     return jsonify({"error": "User not found"}), 404





# DELETE : Remove user by ID 
@app.route("/users/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    if user_id in users:
        del users[user_id]
        return jsonify({"message": "User deleted"})
    return jsonify({"error": "User not found"}), 404




# Running the flask app 
if __name__ == "__main__":
    app.run(debug=True)




