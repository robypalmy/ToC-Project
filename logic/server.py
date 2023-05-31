from flask import Flask, request, jsonify, make_response, send_file
from flask import send_from_directory
from logic import logic_sat
from flask_cors import CORS
from graph_printer import graphPrinter
from graph_generator import * # Import your logic function from logic.
import os
import matplotlib
matplotlib.use('Agg')

app = Flask(__name__)
CORS(app)

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

        # Read the contents of the solution file
        with open(solution_filepath, 'r') as f:
            file_contents = f.read()
        

        print(image_path)
        # Prepare the response data
        response_data = {
            'image_path': '/api/image/' + os.path.basename(image_path),
            'file_contents': file_contents
        }

        return jsonify(response_data)


@app.route('/api/generate', methods=['POST'])
def generate():
    # if 'fileName' in request.files:

    data = request.get_json()
    
    # print("request", request.files.keys())
    file_name = data['fileName']
    nodes = data['nodes']
    edges = data['edges']
    hamiltonian = data['hamiltonian']
    random = data['random']
    print("file_name", file_name)
    print("nodes", nodes)
    print("edges", edges)
    print("hamiltonian", hamiltonian)
    print("random", random)

    file_path = "../graphs/" + file_name
    if random:
        generate_undirected_graph(nodes, edges, file_path)
    elif hamiltonian:
        generate_graph_with_hamiltonian_cycle(nodes, edges, file_path)

    solution_filepath = logic_sat(file_path)

    print("sat result", solution_filepath)

    image_path = graphPrinter(file_path, solution_filepath)
    print("image_path", image_path)
    
    with open(solution_filepath, 'r') as f:
        file_contents = f.read()

    response_data = {
        'image_path': '/api/image/' + os.path.basename(image_path),
        'file_contents': file_contents
    }

    return jsonify(response_data)


@app.route('/api/image/<filename>', methods=['GET'])
def send_image(filename):
    directory = os.path.abspath("./images")  # The directory where you store the images
    return send_from_directory(directory, filename)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001)
