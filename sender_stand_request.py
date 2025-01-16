# sender_stand_request.py
import configuration
import requests
import data
from data import kit_body


def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,  # inserta la dirección URL completa
                         json=body,  # inserta el cuerpo de solicitud
                         headers=data.headers)  # inserta los encabezados


def get_kit_body():
    return requests.get(configuration.URL_SERVICE + configuration.KITS_PATH,
                         json=kit_body, # Datos a enviar en la solicitud.
                         headers=data.headers)


def post_new_client_kit(kit_body):
    headers = data.headers.copy()
    token = post_new_user(data.user_body).json()["authToken"]
    headers["Authorization"] = token
    return requests.post(configuration.URL_SERVICE + configuration.KITS_PATH,
                         json=kit_body, # Datos a enviar en la solicitud.
                         headers=headers) # Encabezados de solicitud.