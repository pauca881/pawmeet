import tensorflow as tf
import numpy as np
from tensorflow.keras.preprocessing import image
from tensorflow.keras.models import load_model
from PIL import Image
import logging

model = None

# def load_model():
#     MODEL_PATH = './IA_deteccion_perrosgatos.h5'
#     global model
#     # Carguem el model nomes si no esta cargat.
#     if model is None:
#         model = tf.keras.models.load_model(MODEL_PATH)

def preprocess_image(img):
    logging.critical("tl_models - preprocess_image1")
    # Redimensionem la imatge.
    img = image.load_img(img, target_size=(256, 256))
    logging.critical("tl_models - preprocess_image2")
    img_array = image.img_to_array(img)  # Convertim la imatge a un vector numpy.
    logging.critical("tl_models - preprocess_image3")
    img_array = np.array(img) / 255.0 # Normalitzem la imatge.
    logging.critical("tl_models - preprocess_image4")
    img_array = np.expand_dims(img_array, axis=0)  # Dimensio batch
    logging.critical("tl_models - preprocess_image5")
    return img_array

def predict_image(image_path):
    logging.critical("tl_models - predict_image1")
    model = load_model("./IA_deteccion_perrosgatos.h5")
    logging.critical("tl_models - predict_image2")
    model.summary()
    logging.critical("tl_models - predict_image3")
    image = preprocess_image("mascotas/gato_gafas.jpg")  # Processem la imatge.
    prediction = model.predict(image)
    return prediction[0][0] == 0