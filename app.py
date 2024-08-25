from flask import Flask, request, jsonify,render_template,redirect,url_for

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/bfhl', methods=['POST','GET'])
def process_data():
    try:
        data = request.get_json()

        if not data or 'data' not in data:
            raise ValueError("Invalid input: 'data' key is missing")

        input_data = data['data']

        user_id = "john_doe_17091999"
        email = "john@xyz.com"
        roll_number = "ABCD123"
        numbers = []
        alphabets = []
        highest_lowercase_alphabet = None

        # Process the input data
        for item in input_data:
            if item.isdigit():
                numbers.append(item)
            elif item.isalpha():
                alphabets.append(item)
                if item.islower() and (highest_lowercase_alphabet is None or item > highest_lowercase_alphabet):
                    highest_lowercase_alphabet = item

        # Prepare the response dictionary
        response = {
            "is_success": True,
            "user_id": user_id,
            "email": email,
            "roll_number": roll_number,
            "numbers": numbers,
            "alphabets": alphabets,
            "highest_lowercase_alphabet": [highest_lowercase_alphabet] if highest_lowercase_alphabet else []
        }

        return jsonify(response), 200

    except ValueError as ve:
        return jsonify({"is_success": False, "error": str(ve)}), 400
    except Exception as e:
        return jsonify({"is_success": False, "error": "An unexpected error occurred: " + str(e)}), 500


@app.route('/bfhl', methods=['GET'])
def get_operation_code():
    # Hardcoded response for GET request
    response = {
        "operation_code": 1
    }
    return jsonify(response), 200

if __name__ == "__main__":
    app.run(debug=True)
