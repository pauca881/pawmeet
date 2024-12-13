# Aquest apartat es per validar les imatges penjades (Signals de Django).
# Validarem la imatge just despres de que es cargui.

from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import Mascota
from dogs_cats_detection.tl_models import predict_image
from PIL import Image
import logging
import cv2

@receiver(pre_save, sender = Mascota)
def validation_pic_pet(sender, instance, **kwargs):
    try:
        image = cv2.imread("mascotas/gato_gafas.jpg")
        is_a_pet = predict_image(image)
        if not is_a_pet:
            raise ValueError("La imagen subida no es valida.")
        instance.is_a_pet = True

    except Exception as e:
        raise ValueError(f"Error al validar la imagen.")