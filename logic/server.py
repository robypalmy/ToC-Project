from flask import Flask, request, jsonify, make_response
from logic import * # Import your logic function from logic.py
from graph_printer import * # Import your logic function from logic.py

app = Flask(__name__)

@app.route('/api/upload', methods=['POST'])
def upload():
    if 'file' in request.files:
        
        file = request.files['file']
        print(file.filename)
        
        filename = "../graphs/" + file.filename

        print(filename)

        logic_result = logic(filename)

        print(logic_result)

        function(filename)

        return logic_result
    else:
        return "No file in request", 400



if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001)
