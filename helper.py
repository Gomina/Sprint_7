from contextlib import contextmanager

import allure
import requests
import random
import string

from urls import URL


class CouriersMethods:

    # метод регистрации нового курьера возвращает список из логина и пароля
    # если регистрация не удалась, возвращает пустой список
    @allure.step('метод создает курьера с случайными логином, паролем, именем. После теста удаляет курьера')
    @contextmanager
    def register_new_courier_and_return_login_password():
        # метод генерирует строку, состоящую только из букв нижнего регистра, в качестве параметра передаём длину строки
        def generate_random_string(length):
            letters = string.ascii_lowercase
            random_string = ''.join(random.choice(letters) for i in range(length))
            return random_string
        # создаём список, чтобы метод мог его вернуть
        login_pass = []
        # генерируем логин, пароль и имя курьера
        login = generate_random_string(10)
        password = generate_random_string(10)
        first_name = generate_random_string(10)
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
            print(f"Успешная регистрация! Логин: {login}, Пароль: {password}, Имя: {first_name}")
        # возвращаем список
        yield {'login': login_pass, 'response': response}

        # после теста удаляем курьера
        # залогинить курьера, чтобы узнать ID
        login_date = {
            "login": login,
            "password": password
        }
        login_response = requests.post(URL.LOGIN_COURIER, data=login_date)
        if login_response.status_code == 200:
            courier_id = login_response.json()['id']
            print(f"Успешный логин! ID курьера: {courier_id}")
        url_delete = URL.DELETE_COURIER + str(courier_id)
        # удаляем курьера
        delete_courier = requests.delete(url_delete, data=str(courier_id))
        if delete_courier.status_code == 200:
            print(f"Курьер удален")




    # создание курьера с заданными данными
    @allure.step('метод создает курьера с задаными данными')
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
            print(f"Успешный логин! ID курьера: {courier_id}")
            return courier_id, login_response
        else:
            print(f"Ошибка логина! Статус-код: {login_response.status_code}")
            return None, login_response


    # удаление созданного курьера
    @allure.step('метод удаляет курьера')
    def delete_courier(self, courier_id):
        url_delete = URL.DELETE_COURIER + str(courier_id)
        # удалить курьера
        delete_courier = requests.delete(url_delete, data=str(courier_id))
        if delete_courier.status_code == 200:
            print(f"Курьер удален")
        else:
            print(f"Ошибка удаления! Статус-код: {delete_courier.status_code}")
