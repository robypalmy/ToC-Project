from flask import Flask, request, jsonify, make_response
from logic import * # Import your logic function from logic.py
from graph_printer import * # Import your logic function from logic.py

app = Flask(__name__)

@app.route('/api/upload', methods=['POST'])
def upload():
    if 'file' in request.files:
        
        file = request.files['file']
        print("file.filename", file.filename)
        print("file", file)

        file_path = "../graphs/" + file.filename
        file.save(file_path)
    
        solution_filepath = logic_sat(file_path)

        print("sat result", solution_filepath)

        image_path = graphPrinter(file_path, solution_filepath)
        print("image_path", image_path)

        return 0
    else:
        return "No file in request", 400



if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001)
