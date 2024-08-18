from flask import Flask, jsonify
from flasgger import Swagger

app = Flask(__name__)
swagger = Swagger(app)

@app.route('/hello', methods=['GET'])
def hello_world():
    """
    Example endpoint returning a hello world
    ---
    responses:
      200:
        description: A simple API to return Hello World
    """
    return jsonify({"message": "Hello World"})

if __name__ == '__main__':
    app.run(debug=True)
