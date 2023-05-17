from flask import Flask, jsonify, request

from flask_cors import CORS

app = Flask(__name__)
CORS(app, supports_credentials=True)


@app.route('/get/no-cors', methods=['GET'])
def get_no_cors():
    data = {
        'message': 'Hello, World!',
        'count': 42
    }
    return jsonify(data)


@app.route('/get-and-options/no-cors-with-credentials', methods=['OPTIONS', 'GET'])
def get_and_options_no_cors_with_credentials():
    if request.method == 'OPTIONS':
        return ('', 200)
    
    # Handle the GET request
    data = {
        'message': 'Hello, World!',
        'count': 42
    }
    response = jsonify(data)
    response.headers.add('Access-Control-Allow-Credentials', 'true')
    return jsonify(data)

@app.route('/get-and-options/no-cors', methods=['OPTIONS', 'GET'])
def get_and_options_no_cors():
    if request.method == 'OPTIONS':
        return ('', 200)
    
    # Handle the GET request
    data = {
        'message': 'Hello, World!',
        'count': 42
    }
    return jsonify(data)

@app.route('/get-and-options/with-cors', methods=['OPTIONS', 'GET'])
def get_and_options_with_cors():
    if request.method == 'OPTIONS':
        response = app.response_class(
            response='',
            status=200,
            mimetype='application/json'
        )
        response.headers.add('Access-Control-Allow-Origin', '*')
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
        response.headers.add('Access-Control-Allow-Methods', 'GET, OPTIONS')
        return response

    # Handle the GET request
    data = {
        'message': 'Hello, World!',
        'count': 42
    }
    response = jsonify(data)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/get-and-options-and-credentials/with-cors', methods=['OPTIONS', 'GET'])
def get_and_options_and_credentials_with_cors():
    if request.method == 'OPTIONS':
        response = app.response_class(
            response='',
            status=200,
            mimetype='application/json'
        )
        response.headers.add('Access-Control-Allow-Origin', 'https://3000-bpmct-corstests-paqeobhjskm.ws-us97.gitpod.io')
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
        response.headers.add('Access-Control-Allow-Methods', 'GET, OPTIONS')
        response.headers.add('Access-Control-Allow-Credentials', 'true')
        return response

    # Handle the GET request
    data = {
        'message': 'Hello, World!',
        'count': 42
    }
    response = jsonify(data)
    response.headers.add('Access-Control-Allow-Origin', 'https://3000-bpmct-corstests-paqeobhjskm.ws-us97.gitpod.io')
    response.headers.add('Access-Control-Allow-Credentials', 'true')
    return response

@app.route('/')
def home():
    route_names = {
        '/get/no-cors': 'Route without CORS',
        '/get-and-options/no-cors-with-credentials': 'Route without CORS but with credentials',
        '/get-and-options/no-cors': 'Route without CORS',
        '/get-and-options/with-cors': 'Route with CORS',
        '/get-and-options-and-credentials/with-cors': 'Route with CORS and credentials'
    }
    return '<h2>' + route_names[request.path] + '</h2>'

