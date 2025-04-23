from flask import Flask, request, jsonify
from database.db import get_connection
from core.engine import CoreEngine

app = Flask(__name__)
db_conn = get_connection()
engine = CoreEngine(db_conn)

@app.route("/users", methods=["GET"])
def get_users():
    return jsonify(engine.fetch_all_users())

@app.route("/users", methods=["POST"])
def add_user():
    data = request.get_json()
    return jsonify(engine.add_user(data["name"], data["email"]))

if __name__ == "__main__":
    app.run(port=8080)
