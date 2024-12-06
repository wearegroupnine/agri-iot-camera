import cv2
from flask import Flask, jsonify
from lib.camera import capture
app = Flask(__name__)

@app.route('/takephoto', methods=['GET'])
def takephoto():
    img = capture()
    response = {"img":img.tolist()}
    return jsonify(response), 200

@app.route('/strawberry', methods=['GET'])
def strawberry():
    img = cv2.imread("strawberry.png")
    response = {"img":img.tolist()}
    return jsonify(response), 200

if __name__ == "__main__":
    app.run(debug=True, port=6665)
