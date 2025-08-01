from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
import json
import os
import google.generativeai as genai
from dotenv import load_dotenv

# Configuración del modelo (igual que en Script.py)
SYSTEM_INSTRUCTION = """
Eres 'DJ Kore', un asistente de IA de élite y coach de carrera para DJs...
"""

MODEL_NAME = 'gemini-1.5-pro-latest'
GENERATION_CONFIG = {
    "temperature": 0.6,
    "max_output_tokens": 2048,
}

# Configurar API
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")
if api_key:
    genai.configure(api_key=api_key)

# Inicializar modelo
model = genai.GenerativeModel(
    model_name=MODEL_NAME,
    system_instruction=SYSTEM_INSTRUCTION,
    generation_config=GENERATION_CONFIG
)

@csrf_exempt
@require_http_methods(["POST"])
def chat_api(request):
    try:
        data = json.loads(request.body)
        prompt = data.get('prompt', '')
        
        if not prompt:
            return JsonResponse({'error': 'No prompt provided'}, status=400)
        
        # Crear nueva sesión de chat para cada request
        chat = model.start_chat(history=[])
        response = chat.send_message(prompt)
        
        return JsonResponse({
            'respuesta': response.text,
            'status': 'success'
        })
        
    except Exception as e:
        return JsonResponse({
            'error': f'Error procesando request: {str(e)}',
            'status': 'error'
        }, status=500)

def index(request):
    return render(request, 'chat/index.html')
# Create your views here.
