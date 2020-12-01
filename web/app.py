from flask import Flask, jsonify
app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")



@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        file = request.files['file']
        img_bytes = file.read()
        class_id, class_name = get_predicition(image_bytes=img_bytes)
        return jsonify({'class_id': class_id, 'class_name': class_name})

   return imagenet_class_index[predicted_idx]
