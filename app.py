from flask import Flask, request, jsonify

app = Flask(__name__)

def validate_input(args) -> tuple:
    try:
        x = float(args.get('x'))
        y = float(args.get('y'))
    except TypeError:
        return (False, jsonify({"error": "Missing x or y"}), 400)
    except ValueError:
        return (False, jsonify({"error": "x and y must be numbers"}), 400)

    return (True, "Valid", 200)


@app.route("/")
@app.route("/test")
def home():
    return "Local Server Is Operational"


@app.route('/add', methods=['GET'])
def add_numbers():

    valid, reason, status_code = validate_input(request.args)
    
    if not valid:
        return reason, status_code
    
    x = float(request.args.get('x'))
    y = float(request.args.get('y'))
    result = x + y
    return jsonify({"result": result})

@app.route('/subtract', methods=['GET'])
def subtract_numbers():

    valid, reason, status_code = validate_input(request.args)
    
    if not valid:
        return reason, status_code
    
    x = float(request.args.get('x'))
    y = float(request.args.get('y'))
    result = x - y
    return jsonify({"result": result})

@app.route('/multiply', methods=['GET'])
def multiply_numbers():

    valid, reason, status_code = validate_input(request.args)
    
    if not valid:
        return reason, status_code
    
    x = float(request.args.get('x'))
    y = float(request.args.get('y'))
    result = x * y
    return jsonify({"result": result})

@app.route('/divide', methods=['GET'])
def divide_numbers():

    valid, reason, status_code = validate_input(request.args)
    
    if not valid:
        return reason, status_code
    
    x = float(request.args.get('x'))
    y = float(request.args.get('y'))
    result = x / y
    return jsonify({"result": result})


if __name__ == '__main__':
    app.run()
