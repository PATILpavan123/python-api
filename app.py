from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# In-memory data store
data_store = []

@app.route('/')
def index():
    return render_template('index.html', data=data_store)

@app.route('/add_data', methods=['POST'])
def add_data():
    try:
        # Get data from the form
        email = request.form.get('email')
        role = request.form.get('role')

        # Create a new data entry
        new_entry = {'email': email, 'role': role}

        # Append to the data store
        data_store.append(new_entry)

        return jsonify({'message': 'Data added successfully'})
    except Exception as e:
        return jsonify({'error': str(e)})

@app.route('/get_data', methods=['GET'])
def get_data():
    return jsonify(data_store)

@app.route('/delete_data/<int:index>', methods=['DELETE'])
def delete_data(index):
    try:
        # Check if the index is within bounds
        if 0 <= index < len(data_store):
            # Remove the data entry at the specified index
            deleted_entry = data_store.pop(index)
            return jsonify({'message': f'Data deleted successfully: {deleted_entry}'})
        else:
            return jsonify({'error': 'Invalid index'})
    except Exception as e:
        return jsonify({'error': str(e)})

@app.route('/delete_data', methods=['DELETE'])
def delete_data_from_form():
    try:
        index = int(request.form.get('deleteIndex'))
        # Check if the index is within bounds
        if 0 <= index < len(data_store):
            # Remove the data entry at the specified index
            deleted_entry = data_store.pop(index)
            return jsonify({'message': f'Data deleted successfully: {deleted_entry}'})
        else:
            return jsonify({'error': 'Invalid index'})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
