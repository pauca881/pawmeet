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

        respuestas_error = [
  "Lo siento, no entendí esa pregunta. ¿Podrías ser más específico?",
  "Perdón, no estoy seguro de haber entendido. ¿Podrías aclararlo?",
  "Disculpa, no comprendo bien la pregunta. ¿Podrías darme más detalles?",
  "No estoy seguro de haber captado lo que necesitas. ¿Podrías reformular la pregunta?",
  "Lo siento, no logro entender lo que me estás preguntando. ¿Puedes explicarlo de otra manera?",
  "No entiendo del todo. ¿Podrías ser más claro?",
  "Perdón, no sé si he entendido tu pregunta. ¿Podrías especificar un poco más?",
  "No estoy seguro de haber entendido correctamente. ¿Podrías volver a intentarlo con más detalles?",
  "Lo siento, no comprendo lo que intentas preguntar. ¿Puedes ser un poco más específico?",
  "No estoy seguro de lo que estás preguntando. ¿Podrías explicarlo mejor?"
];
        # Si no hay coincidencia, devolver mensaje random del array
        return random.choice(respuestas_error)

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
