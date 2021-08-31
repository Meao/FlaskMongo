from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Shop home page"

@app.route('/phones/', methods=['POST'])
def create_phone():
    return "Under development"

@app.route('/phones/', methods=['GET'])
def read_phone():
    return "Under development"

@app.route('/phones/', methods=['PUT'])
def update_phone():
    return "Under development"

@app.route('/phones/', methods=['DELETE'])
def delete_phone():
    return "Under development"

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)