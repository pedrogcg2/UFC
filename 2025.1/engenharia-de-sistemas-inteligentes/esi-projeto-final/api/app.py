from flask import Flask, request, jsonify
from model_service import ModelService

app = Flask(__name__)
model_path = "model-bird_classifier.pkl"
encoder_path = "encoder-bird_classifier.npy"

model_service = ModelService(model_path, encoder_path)


@app.route('/predict', methods=['POST'])
def predict():
    try:
        print(request)
        print(request.files)

        image = request.files["bird"]
        if image:
            prediction = model_service.predict(image)
            return jsonify({"result": prediction}), 200
    except (TypeError, ValueError) as e:
        return jsonify({'error': str(e)}), 400
            
if __name__ == '__main__':
    app.run(debug=True)


