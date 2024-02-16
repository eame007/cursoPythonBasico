import requests

def contar_palabras_url(url):
    
    try:
        respuesta = requests.get(url)
        if respuesta.status_code == 200:
                contenido = respuesta.text
                palabras = contenido.split()
                numero_palabras = len(palabras)
                print(f"El número de palabras en el archivo es: {numero_palabras}")
        else:
            print("No se pudo acceder al archivo. Código de estado:", respuesta.status_code)
    except requests.RequestException as e:
        print("Error al realizar la solicitud:", e)
        
        
url_archivo = "https://www.facebook.com"

# Llamar a la función para contar las palabras en la URL proporcionada
contar_palabras_url(url_archivo)