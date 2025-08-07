# Monitoreo Web con Alerta por Telegram

Este proyecto permite monitorear la disponibilidad de una página web y enviar alertas a un chat de Telegram si la página no responde correctamente.

## Características

- Verifica periódicamente el estado de una URL.
- Envía notificaciones automáticas a Telegram si la web no está disponible.
- Configuración sencilla mediante archivo `.env`.

## Requisitos

- Python 3.x
- Paquetes: `requests`, `python-dotenv`

## Instalación

1. Clona este repositorio o descarga los archivos.
2. Instala las dependencias:
```bash
pip install -r requirements.txt
```

## Uso

1. Crea un archivo `.env` basado en el archivo `.env.example`.
2. Edita el archivo `.env` y configura tus preferencias:
   - `URL_TO_MONITOR`: La URL de la página que deseas monitorear.
   - `TELEGRAM_CHAT_ID`: Tu ID de chat de Telegram.
   - `TELEGRAM_BOT_TOKEN`: El token de tu bot de Telegram.
3. Ejecuta el script principal:
```bash
python conf.py
```

## Contribuciones

Las contribuciones son bienvenidas. Por favor, sigue estos pasos:

1. Haz un fork del repositorio.
2. Crea una nueva rama (`git checkout -b feature/nueva-caracteristica`).
3. Realiza tus cambios y haz commit (`git commit -am 'Agrega nueva característica'`).
4. Haz push a la rama (`git push origin feature/nueva-caracteristica`).
5. Crea un nuevo Pull Request.
