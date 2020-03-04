from flask import Flask, request, jsonify

app = Flask(__name__)
from image_detection import *



@app.route('/detect', methods=['POST'])
def image_recognisition():
    request_data = request.get_json()
    if "file_path" in request_data.keys():
        dt = detect(request_data['file_path'])
        label,Image=dt.recognise()


        if status:
            return jsonify("success ")
        else:
            return jsonify("Not Success")
    else:
        return jsonify("FilePath Not Given")


if __name__ == '__main__':
    app.run(debug=True)
