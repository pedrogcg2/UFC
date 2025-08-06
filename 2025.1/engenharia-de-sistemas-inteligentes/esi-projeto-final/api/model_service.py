import pickle
from PIL import Image
import tensorflow as tf
import numpy as np
from sklearn.preprocessing import LabelEncoder

class ModelService:
    def __init__(self, model_path: str, encoder_path):
        self.model = pickle.load(open(model_path, 'rb'))
        self.encoder = LabelEncoder()
        self.encoder.classes_ = np.load(encoder_path)


    def predict(self, bird_image) -> str:
        image_pixels = Image.open(bird_image.stream)
        img_constant = tf.constant(image_pixels)
        img_constant = img_constant[None, ...]
        if (len(img_constant.shape) < 3):
            img_constant = img_constant[..., tf.newaxis]
            img_constant = tf.image.grayscale_to_rgb(img_constant)
   
        img_constant = tf.image.central_crop(img_constant, 0.8)
   
        img_resized = tf.image.resize(img_constant, (128, 128))
        prediction = self.model.predict(img_resized,batch_size=128, verbose=2).argmax()
        return self.encoder.classes_[prediction] 
