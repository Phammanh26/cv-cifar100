import numpy as np 
import json
from flask import Flask, render_template , request
from tensorflow.keras.models import load_model
from image_process import ImageDataset
from numpyEncoder import  NpEncoder
from rsloggin import ResultLog
app = Flask(__name__)          
model  = load_model('./model/restnet50/cifar1001.h5')
rslog = ResultLog(path = 'log_results.txt')
@app.route("/")
def home():
	return render_template("home.html")

@app.route('/test' , methods=['POST'])
def preidct():
	
	## file request
	img_file = request.files['image']

	image = ImageDataset(target_size= (224, 224))
	image.save(img_file, folder='./image')
	image_readed = image.read()
	image_processing = image.processing(image_readed)

	## predict
	prediction = model.predict(image_processing)
	label = np.argmax(prediction, axis=-1)[0]
	
	##log results
	rslog.add({
		'path': image.path,
		'prediction': prediction,
		'label': label
	})
	return json.dumps(label, cls=NpEncoder)





def run_server_api():
    app.run(debug = True, host='0.0.0.0', port="5050")
  
if __name__ == "__main__":     
    run_server_api()