from contextlib import contextmanager

import allure
import pytest
import requests

from data import TC
from helper import CouriersMethods
from urls import URL


# фикстура создания заказа
@allure.step('метод создает заказ')
@pytest.fixture()
def create_order(order):
    # добавить заголовок Content-Type для корректной обработки JSON
    headers = {'Content-Type': 'application/json'}
    # использовать json
    response = requests.post(URL.CREATE_ORDER, json=order, headers=headers)
    return response

# фикстура создания курьера с определенными данными и удаление его после теста
@allure.step('метод создает курьера с дананными данными и удаляет его после теста')
@pytest.fixture
def registered_courier():
    couriers_methods = CouriersMethods()
    couriers_methods.given_register_new_courier(**TC.COURIER_1)
    yield
    # После выполнения теста удаляем курьера
    courier_id = couriers_methods.login_courier(
        TC.COURIER_1['login'],
        TC.COURIER_1['password']
    )
    if courier_id and courier_id[0]:
        couriers_methods.delete_courier(courier_id[0])


# фикстура создания курьера с рандомными данными и удаление его после теста
@pytest.fixture
def temporary_courier():
    courier_methods = CouriersMethods()

    # генерация рандомных тестовых данных
    login = f"test_user_{courier_methods.generate_random_string(5)}"
    password = courier_methods.generate_random_string(8)
    first_name = "TestUser"

    # создаем рандомного курьера
    courier = courier_methods.create_courier(
        login=login,
        password=password,
        first_name=first_name
    )

    yield courier

    # удаление курьера после выполнения теста
    courier_id, _ = courier_methods.login_courier(login, password)
    courier_methods.delete_courier(courier_id)
