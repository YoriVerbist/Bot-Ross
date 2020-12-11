# app.py

import os

from flask import Flask, request, make_response, jsonify, render_template
from werkzeug.utils import secure_filename
from fastai.vision.all import *
from fastai.data.external import *

# Place where files are stored
UPLOAD_FOLDER = 'static/uploads/'

# codeblock below is needed for Windows path #############
import pathlib
temp = pathlib.PosixPath
#pathlib.PosixPath = pathlib.WindowsPath
##########################################################

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

learner = load_learner('export.pkl')

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/')
def home():
    return render_template("index.html")

@app.route('/predict', methods=['POST', 'GET'])
def predict():
    if request.method == "POST":
        if 'image' not in request.files:
            return {'error': 'no image found, in request.'}, 400

        file = request.files['image'] 
        if file.filename == '':
            return {'error': 'no image found. Empty'}, 400
    
        if file and allowed_file(file.filename): 
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            img = PILImage.create(file)
            pred = learner.predict(img)
            print(pred)
            index = pred[1].item()
            certainty = pred[2][index].item()
            print(certainty)
            # if you want a json reply, together with class probabilities:
            #return jsonify(str(pred))
            # or if you just want the result
            return render_template("predict.html", pred = pred[0], filename = 'uploads/' + filename, certainty = certainty)

        return {'error': 'something went wrong.'}, 500

def display_image(filename):
	#print('display_image filename: ' + filename)
	return redirect(url_for('static', filename='uploads/' + filename), code=301)
        


if __name__ == '__main__':
    port = os.getenv('PORT',5000)
    app.run(debug=True, host='0.0.0.0', port=port) 
