{python}
from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample data to simulate a database
pets = [
    {'id': 1, 'name': 'Buddy', 'type': 'Dog', 'age': 5},
    {'id': 2, 'name': 'Mittens', 'type': 'Cat', 'age': 3},
]

# Get all pets
@app.route('/pets', methods=['GET'])
def get_pets():
    return jsonify(pets)

# Get a pet by ID
@app.route('/pets/<int:pet_id>', methods=['GET'])
def get_pet(pet_id):
    pet = next((pet for pet in pets if pet['id'] == pet_id), None)
    return jsonify(pet) if pet else ('', 404)

# Add a new pet
@app.route('/pets', methods=['POST'])
def add_pet():
    new_pet = request.get_json()
    new_pet['id'] = len(pets) + 1
    pets.append(new_pet)
    return jsonify(new_pet), 201

# Update a pet by ID
@app.route('/pets/<int:pet_id>', methods=['PUT'])
def update_pet(pet_id):
    pet = next((pet for pet in pets if pet['id'] == pet_id), None)
    if pet is None:
        return ('', 404)
    
    data = request.get_json()
    pet.update(data)
    return jsonify(pet)

# Delete a pet by ID
@app.route('/pets/<int:pet_id>', methods=['DELETE'])
def delete_pet(pet_id):
    global pets
    pets = [pet for pet in pets if pet['id'] != pet_id]
    return ('', 204)

if __name__ == '__main__':
    app.run(debug=True)
