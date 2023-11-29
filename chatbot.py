import openai
# import os
from config import API_KEY
# API_KEY = os.environ.get("API_KEY")
openai.api_key = API_KEY

def generar_respuesta(pregunta):
    respuesta = openai.completions.create(
        model = "text-davinci-003",
        prompt= pregunta,
        max_tokens= 60,
        temperature= 0.5
    )
    return respuesta.choices[0].text.strip()    #la respuesta q devolvera el api


def main():
    print("Bienvenido al Chatbot de OpenAI")

    while True:
        pregunta = input("Escribe tu pregunta (o 'salir' para finalizar): ")

        if pregunta.lower() == 'salir':
            print("¡Hasta luego!")
            break

        respuesta = generar_respuesta(pregunta)
        print("Respuesta:", respuesta)

if __name__ == "__main__":  #cuando ejecuto chatbot se ejecuta la funcion main (se hace arriba)
    main()
   
#falta conectarme con openai, se hace arriba de main