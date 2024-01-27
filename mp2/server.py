from flask import Flask, request, jsonify

PORT = 80

app = Flask(__name__)

# Initialize seed value
seed_value = 0

@app.route("/", methods=["POST"])
def update_seed():
    global seed_value
    data = request.get_json()
    if "num" in data:
        seed_value = data["num"]
        return jsonify({"message": "Seed updated successfully"})
    else:
        return jsonify({"error": "Invalid request body"}), 400

@app.route("/", methods=["GET"])
def get_seed():
    return str(seed_value)

if __name__ == "__main__":
    # Run the app on a specific port
    app.run(host="0.0.0.0", port=80)