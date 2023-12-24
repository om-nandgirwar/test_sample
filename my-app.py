from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Placeholder for the inventory (you might use a database in a real application)
inventory = []


# Render the form to add items
@app.route('/')
def add_item_form():
    return render_template('index.html')


# Add item to the inventory
@app.route('/add_item', methods=['POST'])
def add_item():
    data = request.form
    name = data['name']
    quantity = int(data['quantity'])

    # Create a dictionary for the new item
    new_item = {'name': name, 'quantity': quantity}

    # Add the item to the inventory
    inventory.append(new_item)

    return jsonify({'message': 'Item added successfully'})


# Retrieve all items from the inventory
@app.route('/list_inventory')
def list_inventory():
    return render_template('list_inventory.html', inventory=inventory)


if __name__ == '__main__':
    app.run(debug=True)
