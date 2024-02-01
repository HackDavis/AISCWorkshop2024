from flask import Flask, jsonify, send_file
from flask_cors import CORS
from algorithm import run_algorithm
from flask_restful import Api, Resource

app = Flask(__name__)

CORS(app, resources={
    r"/*": {
        "origins": ["https://aisc-workshop2024-kten-66z8uhjsc-win-chengs-projects.vercel.app"],
        "methods": ["GET", "POST", "PUT", "DELETE", "OPTIONS"],
        "allow_headers": ["Content-Type", "Authorization", "X-Requested-With"]
    }
})

api = Api(app)


@app.route("/", methods=['GET'])
def return_home():
    return jsonify({
        'message': "Hello world!",
        'people': ["Aa", "Bb", "Cc"]
    })

@app.route('/first_image')
def get_image():
    result = run_algorithm()
    return send_file('first_graph.png', mimetype='image/png')

@app.route('/models')
def get_models():
    result = run_algorithm()
    # print("xgb", result['XGBoost'])
    return jsonify({
        'models': result
    })

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