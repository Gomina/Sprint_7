import allure
import pytest
import requests

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