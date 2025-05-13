from contextlib import contextmanager

import allure
import requests
import random
import string

from urls import URL

class CouriersMethods:

    @staticmethod
    # генерация случайной строки из букв нижнего регистра
    def generate_random_string(length=10):
        return ''.join(random.choice(string.ascii_lowercase) for _ in range(length))

    # создать курьера с рандомными данными
    @allure.step('создать нового курьера')
    def create_courier(self, login=None, password=None, first_name=None):
        payload = {
            "login": login,
            "password": password,
            "firstName": first_name
        }

        response = requests.post(URL.CREATE_COURIER, data=payload)

        return {
            "login": payload["login"],
            "password": payload["password"],
            "first_name": payload["firstName"],
            "response": response
        }


    # создание курьера с заданными данными
    @allure.step('метод создает курьера с заданными данными')
    def given_register_new_courier(self, login, password, first_name):
        # создаём список, чтобы метод мог его вернуть
        login_pass = []
        # собираем тело запроса
        payload = {
            "login": login,
            "password": password,
            "firstName": first_name
        }
        # отправляем запрос на регистрацию курьера и сохраняем ответ в переменную response
        response = requests.post(URL.CREATE_COURIER, data=payload)
        # если регистрация прошла успешно (код ответа 201), добавляем в список логин и пароль курьера
        if response.status_code == 201:
            login_pass.extend([login, password, first_name])
        # возвратить список
        return {'login': login_pass, 'response': response}

    # логин курьера
    @allure.step('метод авторизовывает курьера')
    def login_courier(self, login, password):
        login_response = requests.post(URL.LOGIN_COURIER, data={'login': login, 'password': password})
        if login_response.status_code == 200:
            courier_id = login_response.json()['id']
            return courier_id, login_response
        else:
            return None, login_response


    # удаление созданного курьера
    @allure.step('метод удаляет курьера')
    def delete_courier(self, courier_id):
        url_delete = URL.DELETE_COURIER + str(courier_id)
        # удалить курьера
        requests.delete(url_delete, data=str(courier_id))

