from flask import Flask, jsonify
from flask_jwt_extended import JWTManager, jwt_required, get_jwt_identity
from config import Config
from models import db, User
from auth import auth_bp

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
jwt = JWTManager(app)

app.register_blueprint(auth_bp)

@app.before_first_request
def create_tables():
    db.create_all()

@app.route("/")
def home():
    return jsonify({"message": "User Management System Running"})

@app.route("/profile")
@jwt_required()
def profile():
    current_user = get_jwt_identity()
    return jsonify(current_user)

@app.route("/users")
@jwt_required()
def get_users():
    current_user = get_jwt_identity()
    if current_user["role"] != "admin":
        return jsonify({"message": "Admin access required"}), 403

    users = User.query.all()
    return jsonify([{"username": u.username, "role": u.role} for u in users])

if __name__ == "__main__":
    app.run(debug=True)
