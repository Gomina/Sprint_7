import allure
import pytest
import requests

from data import TO
from urls import URL


class TestCreateOrder:
    @pytest.mark.parametrize(
        "order",
        [
            (TO.ORDER_1),
            (TO.ORDER_2),
            (TO.ORDER_3),
            (TO.ORDER_4),
        ]
    )


    @allure.title('Тест на успешное создание заказа')
    def test_create_order(self, order, create_order):
        # проверка статус-кода ответа
        assert create_order.status_code == 201
        # проверка тела ответа
        content = create_order.json()
        assert "track" in content, "В ответе отсутствует поле 'track'"


class TestListOrders:

    # проверка выведения списка заказов
    @allure.title('Тест на успешное выведения списка заказов')
    def test_list_order(self):
        response = requests.get(URL.ORDER_LIST)
        # проверка, что запрос прошел успешно
        assert response.status_code == 200
        content = response.json()
        assert "orders" in content
