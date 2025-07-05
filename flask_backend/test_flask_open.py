# test_flask_open.py
from flask import Flask

app = Flask(__name__)

@app.route('/test', methods=['GET'])
def test():
    return {"message": "API working!"}, 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
