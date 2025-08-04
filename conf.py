import requests
import time
from dotenv import load_dotenv
import os

load_dotenv()

tele_token = os.getenv("TELE_TOKEN")
chat_id = os.getenv("CHAT_ID")
url = os.getenv("URL")
intervalo = 5

def enviar_mensaje_telegram(mensaje):
    url_telegram = f"https://api.telegram.org/bot{tele_token}/sendMessage"
    data = {
        'chat_id' : chat_id,
        'text' : mensaje
    }
    try:
        response = requests.post(url_telegram, data=data)
        if response.status_code != 200:
            print("Error , no se ha podido enviar el mensaje por telegram")
    except Exception as e:
        print(f"Error, fallo en Telegram: {e}")
    
def verificar_url(url):
    try:
        respuesta = requests.get(url, timeout=10)
        if respuesta.status_code == 200:
            print(f"{url} está disponible")
        else:
            mensaje = f"Alerta: {url} no está disponible. Código de estado: {respuesta.status_code}"
            print(mensaje)
            enviar_mensaje_telegram(mensaje)
    except Exception as e:
        mensaje = f"No se pudo acceder a {url}. Error: {e}"
        print(mensaje)
        enviar_mensaje_telegram(mensaje)

if __name__ == "__main__":
    while True:
        verificar_url(url)
        time.sleep(intervalo)
