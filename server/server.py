from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
# from algorithm import run_algorithm
from main import run_algorithm
from eda import analysis
from flask_restful import Api, Resource

app = Flask(__name__)

CORS(app)
api = Api(app)

all_models = ['logistic_regression', 'k_nearest_neighbors', 'support_vector_machine', 'decision_tree', 'random_forest', 'gradient_boosting', 'naive_bayes', 'neural_network', 'ada_boost', 'xg_boost']
@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
    return response

@app.route("/", methods=['GET'])
def return_home():
    return jsonify({
        'message': "Hello world!",
        'people': ["Aa", "Bb", "Cc"]
    })

@app.route('/first_image', methods = ['GET'])
def get_image():
    result = run_algorithm(all_models)
    return send_file('first_graph.png', mimetype='image/png')

@app.route('/analysis', methods = ['GET'])
def analyse():
    # analysis()
    return send_file('analysis.png', mimetype='image/png')

@app.route('/models', methods = ['GET', 'POST'])
def get_models():
    if request.method == 'GET':
        result = run_algorithm(all_models)  
        return jsonify({
            'models': result
        })

    if request.method == 'POST':
        try:
            data = request.json
            models_to_run = data.get('models')
            result = run_algorithm(models_to_run)
            return jsonify({
                'models': result
            }), 200
        except Exception as e:
                return jsonify({
                    'error': 'Invalid request',
                    'details': str(e)
                }), 400
    

# @app.route('/download_first_graph')
# def download_first_graph():
#     run_algorithm()  # Generate the graphs
#     return send_file('first_graph.png', as_attachment=True)

# @app.route('/download_second_graph')
# def download_second_graph():
#     run_algorithm()  # Generate the graphs
#     return send_file('second_graph.png', as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True, port=8080)

# def create_app():
#     return app