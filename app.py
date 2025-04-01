from flask import Flask, request, jsonify
from googletrans import Translator  # Para traducción
import openai  # Para generar preguntas, si deseas usar GPT-4 u OpenAI

app = Flask(__name__)

# Inicialización del traductor de Google
translator = Translator()

# Ruta resumen
@app.route('/resumen', methods=['GET'])
def resumen():
    # Esto puede ser dinámico si lo deseas, por ejemplo, leer desde un archivo o base de datos
    return jsonify({"resumen": "Este es un resumen de un texto o actividad."})

# Ruta pregunta
@app.route('/pregunta', methods=['POST'])
def pregunta():
    # Asumimos que recibimos una pregunta en el cuerpo del POST
    data = request.get_json()
    question = data.get('question')
    
    # Respuesta simulada (aquí podrías integrar un modelo de IA o lógica para responder)
    response = "Esta es la respuesta a tu pregunta: " + question
    return jsonify({"response": response})

# Ruta generar_preguntas
@app.route('/generar_preguntas', methods=['POST'])
def generar_preguntas():
    # Recibe un texto del cual se generarán preguntas
    data = request.get_json()
    text = data.get('text')

    # Aquí puedes integrar una lógica de generación de preguntas, usando OpenAI o similar.
    # Para simplificar, generaremos preguntas sencillas.
    questions = [
        "¿Qué es el texto sobre el cual se basa este resumen?",
        "¿Cuáles son los puntos clave de este texto?"
    ]
    
    return jsonify({"questions": questions})

# Ruta traducir
@app.route('/traducir', methods=['POST'])
def traducir():
    data = request.get_json()
    text = data.get('text')
    target_lang = data.get('target_lang', 'en')  # Idioma por defecto es inglés
    
    # Usamos googletrans para la traducción
    translated = translator.translate(text, dest=target_lang)
    
    return jsonify({"translated_text": translated.text})

if __name__ == '__main__':
    app.run(debug=True)
