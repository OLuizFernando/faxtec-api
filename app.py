import os
from datetime import datetime
from dotenv import load_dotenv
from flask import Flask, redirect, request, jsonify
from flask_cors import CORS
from flask_restful import Api, Resource
from flask_sqlalchemy import SQLAlchemy

load_dotenv()

app = Flask(__name__)
CORS(app)
api = Api(app)

app.config["SQLALCHEMY_DATABASE_URI"] = f"postgresql://{os.getenv("PGUSER")}:{os.getenv("PGPASSWORD")}@{os.getenv("PGHOST")}/{os.getenv("PGDATABASE")}?sslmode=require"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class Messages(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    message = db.Column(db.Text, nullable=False)
    date = db.Column(db.String, default=datetime.now().isoformat()[:-3] + "Z") # YYYY-MM-DDTHH:MM:SS.sssZ
    addressee = db.Column(db.String(100), nullable=False)


    def to_dict(self):
        return {
            "id": self.id,
            "message": self.message,
            "date": self.date,
            "addressee": self.addressee
        }


with app.app_context():
    db.create_all()


@app.route("/")
def index():
    return redirect("/messages")


@app.route("/messages", methods=["GET"])
def get_messages():
    messages = Messages.query.all()
    return jsonify([message.to_dict() for message in messages])


@app.route("/messages", methods=["POST"])
def create_message():
    data = request.get_json()

    if "message" not in data or "addressee" not in data:
        return jsonify({"error": "Missing data"}), 400
    
    new_message = Messages(message=data["message"], addressee=data["addressee"])
    db.session.add(new_message)
    db.session.commit()

    return jsonify(new_message.to_dict()), 201


@app.errorhandler(404)
def page_not_found(error):
    return jsonify({"error": "Route not found"}), 404


@app.errorhandler(405)
def method_not_allowed(error):
    return jsonify({"error": "Method not allowed"}), 405


@app.errorhandler(500)
def internal_server_error(error):
    return jsonify({"error": "Internal server error"}), 500


if __name__ == "__main__":
    app.run(debug=True)