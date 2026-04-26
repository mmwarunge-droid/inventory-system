from flask import Flask, request, jsonify
from inventory import inventory
from services.openfoodfacts import fetch_product

app = Flask(__name__)

@app.route("/")
def home():
    return {"message": "Inventory API Running"}

@app.route("/favicon.ico")
def favicon():
    return "", 204

# GET ALL
@app.route("/inventory", methods=["GET"])
def get_inventory():
    return jsonify(inventory), 200


# GET ONE
@app.route("/inventory/<int:id>", methods=["GET"])
def get_item(id):
    item = next((x for x in inventory if x["id"] == id), None)

    if item:
        return jsonify(item), 200

    return jsonify({"error": "Item not found"}), 404


# POST
@app.route("/inventory", methods=["POST"])
def add_item():
    data = request.json

    new_item = {
        "id": len(inventory) + 1,
        "product_name": data["product_name"],
        "brands": data["brands"],
        "price": data["price"],
        "stock": data["stock"],
        "barcode": data["barcode"]
    }

    inventory.append(new_item)

    return jsonify(new_item), 201


# PATCH
@app.route("/inventory/<int:id>", methods=["PATCH"])
def update_item(id):
    item = next((x for x in inventory if x["id"] == id), None)

    if not item:
        return jsonify({"error": "Item not found"}), 404

    data = request.json

    item.update(data)

    return jsonify(item), 200


# DELETE
@app.route("/inventory/<int:id>", methods=["DELETE"])
def delete_item(id):
    item = next((x for x in inventory if x["id"] == id), None)

    if not item:
        return jsonify({"error": "Item not found"}), 404

    inventory.remove(item)

    return jsonify({"message": "Deleted"}), 200


# SEARCH EXTERNAL API
@app.route("/search/<barcode>", methods=["GET"])
def search_product(barcode):
    product = fetch_product(barcode)
    return jsonify(product)


if __name__ == "__main__":
    app.run(debug=True)