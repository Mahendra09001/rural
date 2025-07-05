from flask import Flask, request, jsonify
from flask_cors import CORS
from db import db
from models.person_model import format_person

app = Flask(__name__)
CORS(app)  # Allow cross-origin requests

@app.route('/submit-person', methods=['POST'])
def submit_person():
    data = request.get_json()
    if not data or 'id' not in data:
        return jsonify({"error": "Invalid data"}), 400

    # Update if person with same 'id' exists
    existing = db.persons.find_one({"id": data["id"]})
    if existing:
        db.persons.update_one({"id": data["id"]}, {"$set": data})
        return jsonify({"message": "Person data updated"}), 200
    else:
        db.persons.insert_one(data)
        return jsonify({"message": "Person data saved"}), 201

@app.route('/persons', methods=['GET'])
def get_all_persons():
    persons = db.persons.find()
    return jsonify([format_person(p) for p in persons]), 200

@app.route('/person/<string:person_id>', methods=['DELETE'])
def delete_person(person_id):
    result = db.persons.delete_one({"id": person_id})
    if result.deleted_count == 0:
        return jsonify({"error": "Person not found"}), 404
    return jsonify({"message": "Person deleted"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
