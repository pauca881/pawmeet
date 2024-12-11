import tensorflow as tf
import numpy as np
from tensorflow.keras.preprocessing import image

def load_model():
    path = 'IA_deteccion_perrosgatos.h5'
    model = tf.keras.models.load_model(path)
    return model

def preprocess_image(img):
    # Redimensionamos la imagen al tamaño que espera el modelo (e.g., 224x224 para VGG16)
    img = image.load_img(img, target_size=(224, 224))
    img_array = image.img_to_array(img)  # Convertimos la imagen a un array de Numpy
    img_array = np.expand_dims(img_array, axis=0)  # Añadimos la dimensión del batch
    img_array /= 255.0  # Normalizamos si el modelo fue entrenado de esta manera
    return img_array

def predict(image_path):
    model = load_model()  # Load the model
    # Preprocess the image before passing it to the model
    image = preprocess_image(image_path)  # Apply preprocessing
    result = model.predict(image)
    return result