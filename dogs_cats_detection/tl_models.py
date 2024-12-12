import tensorflow as tf
import numpy as np
from tensorflow.keras.preprocessing import image
from PIL import Image

model = None

def load_model():
    MODEL_PATH = 'IA_deteccion_perrosgatos.h5'
    global model
    # Carguem el model nomes si no esta cargat. 
    if model is None:
        model = tf.keras.models.load_model(MODEL_PATH)



def preprocess_image(img):
    # Redimensionem la imatge. 
    img = image.load_img(img, target_size=(224, 224))
    img_array = image.img_to_array(img)  # Convertim la imatge a un vector numpy.
    img_array = np.array(img) / 255.0 # Normalitzem la imatge.
    img_array = np.expand_dims(img_array, axis=0)  # Dimensio batch
    return img_array

def predict_image(image_path):
    load_model()  # Carguem el model.
    image = preprocess_image(image_path)  # Processem la imatge.
    prediction = model.predict(image)
    return prediction[0][0] == 0 