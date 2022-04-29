import numpy as np
from keras.preprocessing import image
from tensorflow.keras.applications.resnet50 import preprocess_input
from werkzeug.utils import secure_filename
import os
class ImageDataset:
    def __init__(self, target_size = (224, 224)):
        self.path = None
        self.target_size = target_size
        pass
    def read(self):
        if self.path != None:
            img = image.load_img(self.path, target_size = self.target_size)
            return img
        ##log
        print("ERROR: Can't read file")
        return None

    def save(self, request_file, folder):
        ## storage file from server
        filename = secure_filename(request_file.filename)
        path = os.path.join(folder, filename)
        request_file.save(path)
        self.path = path
        ##log
        print("SUCCESS: save done!!!")
        return None
    def batch_inputs(self, img_array):
        img_batch = np.expand_dims(img_array, axis=0)
        img_preprocessed = preprocess_input(img_batch)
        # print(img_preprocessed.shape)
        return img_preprocessed
    def processing(self, img_file):
        ## processing image
        img_array = image.img_to_array(img_file)
        img_preprocessed = self.batch_inputs(img_array)
        return img_preprocessed