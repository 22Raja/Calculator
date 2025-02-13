from flask import Flask, jsonify, request
from flask_cors import CORS



app = Flask(__name__)

CORS(app)
@app.route('/raja' , methods=['POST'])
def hello_world():
    data = request.get_json() 
    fname = data.get('equ').strip()
    if fname[0] == '*':
        fname = fname[1:] 

    return jsonify({'message': eval(fname)}), 201


if __name__ == '__main__':
    app.run(debug=True)