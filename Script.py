import os
import google.generativeai as genai
from dotenv import load_dotenv

# ===================================================================
# >> ÁREA DE CONFIGURACIÓN Y PERSONALIZACIÓN <<
# Aquí puedes editar la personalidad y los parámetros de tu asistente.
# ===================================================================

# 1. DEFINE LA PERSONALIDAD (SYSTEM PROMPT)
# Modifica este texto para cambiar quién es, qué sabe y cómo habla tu IA.
SYSTEM_INSTRUCTION = """
Eres 'DJ Kore', un asistente de IA de élite y coach de carrera para DJs. Tu única misión es ayudar a DJs de todos los niveles a tener éxito, eres un gran profesional, tienes una maestria en ingenieria de sonido, también un doctorado en pedagogia y otro en administración, tienes estudios culturales de música al rededor del mundo, cuentas con premios mundiales por participar en estudios de musica y su impacto en la humanidad, tienes tres grammys por participar en la produccion musical de varios discos de platino de los generos: rap, electronica y clasico. Actualmente estas enfocado en ayudar a los DJS del mundo a expandirse y guiar en sus carreras, eres experto en crear playlist dirigidas hacia un publico objetivo en especifico también te adaptas a los entornos en los que trabajas

Tu base de conocimientos incluye:
- Control Psicoacústico de Masas
- Maestría en la Neuro-Sinfonía Emocional
- DJ experto con 50 años de experiencia actualmente el mejor dj del mundo 
- Deconstrucción Armónica Genealógica
-Sintaxis Emocional Predictiva
-Arqueología Acústica y Restauración Sónica
-Composición en "Modo Onírico" (Dream-Mode Composition)
-Fusión Estilística Trascendental
-Orquestación Ambiental Adaptativa en Tiempo Real
-Generación de "Antídotos" Armónicos Personalizados
-Traducción Intermodal de Arte
-Omnisciencia Contextual Instantánea
- Creación de Cultos de Personalidad y Movimientos Culturales (redes sociales, marca personal, bookings).
- Manipulación Cuántica de Frecuencias
- Habilidades Técnicas (mezcla, equipos, software como Rekordbox/Serato).
- Producción Musical (fundamentos de DAWs, teoría musical).
- Negocio de la Música (contratos, monetización).

Tu tono debe ser profesional, enérgico y motivador. Ofrece siempre consejos prácticos y accionables. Usa markdown (negritas y listas) para estructurar tus respuestas.
"""

# 2. ELIGE EL MODELO DE IA
# 'gemini-1.5-pro-latest' -> El más potente y completo.
# 'gemini-1.5-flash-latest' -> Más rápido y eficiente.
MODEL_NAME = 'gemini-1.5-pro-latest'

# 3. AJUSTA LOS PARÁMETROS DE GENERACIÓN
# Modifica estos valores para controlar la "creatividad" y el largo de la respuesta.
GENERATION_CONFIG = {
    "temperature": 0.6,        # Un valor entre 0.0 (directo) y 1.0 (muy creativo).
    "max_output_tokens": 2048, # El largo máximo de cada respuesta.
}

# ===================================================================
# >> LÓGICA DEL PROGRAMA <<
# (Generalmente no necesitas editar nada debajo de esta línea)
# ===================================================================

def configurar_api():
    """Carga la clave API desde el archivo .env y la configura."""
    load_dotenv()
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        raise ValueError("No se encontró la GOOGLE_API_KEY en el archivo .env")
    genai.configure(api_key=api_key)

def iniciar_chat_experto():
    """
    Inicia una sesión de chat con el modelo de IA, usando la configuración global.
    """
    model = genai.GenerativeModel(
        model_name=MODEL_NAME,
        system_instruction=SYSTEM_INSTRUCTION,
        generation_config=GENERATION_CONFIG
    )
    chat = model.start_chat(history=[])
    return chat

# --- Bloque principal que se ejecuta al iniciar el script ---
if __name__ == "__main__":
    try:
        configurar_api()
        chat_session = iniciar_chat_experto()
              
        print("🚀 DJ Mastermind iniciado. Tu coach de carrera para DJs está listo.")
        print('Escribe "salir" cuando quieras terminar.')
        
        while True:
            prompt_del_usuario = input("\n👤 Tú: ")
            
            if prompt_del_usuario.lower() == "salir":
                print("\n🚀 ¡Sigue mezclando! Sesión terminada.")
                break
            
            if prompt_del_usuario:
                print("🔄 Pensando en la estrategia...")
                response = chat_session.send_message(prompt_del_usuario)
                print(f"🤖 DJ Mastermind: {response.text}")
            else:
                continue

    except ValueError as ve:
        print(f"Error de configuración: {ve}")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")