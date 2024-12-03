# chatbot/views.py
from django.http import JsonResponse
from django.shortcuts import render
import json
import re
import random
import nltk
import time

nltk.download('punkt')

from nltk.chat.util import Chat, reflections

# Cargar el archivo JSON con preguntas y respuestas
with open('chatbot/data/intents.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Convertir las preguntas y respuestas en patrones y respuestas
def crear_patrones_respuestas(data):
    patrones = []

    # Recorremos el JSON para crear los patrones
    for categoria, info in data.items():
        for pregunta in info['preguntas']:
            # Crear un patrón regex más flexible
            patron = f".*{re.escape(pregunta.lower())}.*"
            # Cambiar la respuesta a una lista de respuestas posibles
            respuestas = info['respuesta']
            patrones.append((patron, respuestas))

    return patrones

# Crear los patrones de preguntas y respuestas
patrones = crear_patrones_respuestas(data)

# Crear el chatbot usando NLTK
class MiChatbot(Chat):
    def __init__(self, patrones, reflejos):
        super().__init__(patrones, reflejos)

    def respond(self, mensaje):
        # Convertir el mensaje a minúsculas para mayor flexibilidad
        mensaje = mensaje.lower()

        # Buscar coincidencias
        for (patron, respuestas) in self._pairs:
            match = re.match(patron, mensaje)
            if match:
                # Seleccionar una respuesta aleatoria
                return random.choice(respuestas)

        # Si no hay coincidencia, devolver mensaje predeterminado
        return "Lo siento, no entendí esa pregunta. ¿Podrías ser más específico?"

# Instanciar el chatbot
chatbot = MiChatbot(patrones, reflections)

def chatbot_response(request):
    if request.method == 'POST':
        user_message = request.POST.get('message', '')
        time.sleep(1)

        response = chatbot.respond(user_message)
        return JsonResponse({'response': response})

    return JsonResponse({'response': "Método no permitido"}, status=405)

def chatbot_interface(request):
    return render(request, 'chatbot.html')
