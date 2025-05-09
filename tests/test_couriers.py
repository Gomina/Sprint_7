import allure
import pytest
from allure_commons.types import Severity

from data import TC
from helper import CouriersMethods


class TestCreationCourier:

    # тест на успешную регистрацию
    @allure.title('Тест успешное создание курьера')
    def test_creating_courier(self):
        # результат регистрации:
        with CouriersMethods.register_new_courier_and_return_login_password() as result:
            # проверка статус-код ответа
            assert result['response'].status_code == 201
            # проверка тела ответа:
            content = result['response'].json()
            assert content.get("ok") is True



    # тест на невозможность создания двух одинаковых курьеров
    @allure.title('Тест на то, что нельзя создать двух одинаковых курьеров')
    def test_creating_two_identical_courier(self):
        # создание экземпляр класса CouriersMethods
        couriers_methods = CouriersMethods()
        # результат регистрации:
        couriers_methods.given_register_new_courier(**TC.COURIER_1)
        result = couriers_methods.given_register_new_courier(**TC.COURIER_1)
        # проверка статус-код ответа
        assert result['response'].status_code == 409
        # проверка тела ответа:
        content = result['response'].json()
        assert content.get("message") == "Этот логин уже используется. Попробуйте другой."
        # удаление курьера
        courier_id = couriers_methods.login_courier(TC.COURIER_1['login'], TC.COURIER_1['password'])
        if courier_id:
            couriers_methods.delete_courier(courier_id[0])




    @pytest.mark.parametrize(
        "courier",
        [
            (TC.COURIER_2),
            (TC.COURIER_3),
        ]
    )

    # нет логина или пароля, тест возвращает ошибку
    @allure.title('Тест на то, что нельзя создать курьера без логина или пароля')
    def test_register_new_courier_without_login(self, courier):
        # создание экземпляр класса CouriersMethods
        couriers_methods = CouriersMethods()
        # результат регистрации:
        result = couriers_methods.given_register_new_courier(**courier)
        # проверка статус-код ответа
        assert result['response'].status_code == 400
        # проверка тела ответа:
        content = result['response'].json()
        assert content.get("message") == "Недостаточно данных для создания учетной записи"



class TestLoginCourier:

    # успешная авторизация курьера
    @allure.title('Тест на то, что курьер может авторизоваться')
    def test_login_courier(self):
        # создание экземпляр класса CouriersMethods
        couriers_methods = CouriersMethods()
        # создание курьера
        couriers_methods.given_register_new_courier(**TC.COURIER_1)
        # регистрация курьера
        courier_id, login_response = couriers_methods.login_courier(TC.COURIER_1['login'], TC.COURIER_1['password'])
        # проверка статус-код ответа
        assert login_response.status_code == 200
        # проверка тела ответа:
        assert courier_id is not None
        print(f"Успешный логин! ID курьера: {courier_id}")
        # удаление курьера
        couriers_methods.delete_courier(courier_id)



    # ошибка на авторизацию курьера с неправильно указанным логином или паролем
    @pytest.mark.parametrize(
        'login, password',
        [
            (TC.COURIER_1['login'], TC.WRONG_PASSWORD_COURIER_1['password']),
            (TC.WRONG_LOGIN_COURIER_1['login'], TC.COURIER_1['password'])
        ]
    )
    @allure.title('Тест на выпадение ошибки при авторизации курьера с неверным логином или паролем')
    def test_login_courier_wrong_data(self, login, password):
        # создание экземпляр класса CouriersMethods
        couriers_methods = CouriersMethods()
        # создание курьера
        couriers_methods.given_register_new_courier(**TC.COURIER_1)
        try:
            # попытка авторизации с неверными данными
            courier_id, login_response = couriers_methods.login_courier(login, password)
            # проверка статус-код ответа
            assert login_response.status_code == 404
            # проверка тела ответа:
            content = login_response.json()
            assert content.get("message") == "Учетная запись не найдена"

        finally:
            # удаление курьера (используются правильные данные для авторизации)
            courier_id = couriers_methods.login_courier(
                TC.COURIER_1['login'],
                TC.COURIER_1['password']
            )
            couriers_methods.delete_courier(courier_id[0])



    # ошибка на авторизацию курьера с отсутствующим логином или паролем
    @pytest.mark.parametrize(
        'login, password',
        [
            (TC.COURIER_1['login'], TC.WITHOUT_PASSWORD_COURIER_1['password']),
            (TC.WITHOUT_LOGIN_COURIER_1['login'], TC.COURIER_1['password'])
        ]
    )
    @allure.title('Тест на выпадение ошибки при авторизации курьера без логина или пароля')
    def test_login_courier_without_data(self, login, password):
        # создание экземпляр класса CouriersMethods
        couriers_methods = CouriersMethods()
        # создание курьера
        couriers_methods.given_register_new_courier(**TC.COURIER_1)
        try:
            # попытка авторизации с неверными данными
            courier_id, login_response = couriers_methods.login_courier(login, password)
            # проверка статус-код ответа
            assert login_response.status_code == 400
            # проверка тела ответа:
            content = login_response.json()
            assert content.get("message") == "Недостаточно данных для входа"

        finally:
            # удаление курьера (используются правильные данные для авторизации)
            courier_id = couriers_methods.login_courier(
                TC.COURIER_1['login'],
                TC.COURIER_1['password']
            )
            couriers_methods.delete_courier(courier_id[0])


    # ошибка при авторизации, если курьер не создан
    @allure.title('Тест на выпадение ошибки при авторизации несуществующего курьера')
    def test_login_not_creating_courier(self):
        # создание экземпляр класса CouriersMethods
        couriers_methods = CouriersMethods()
        courier_id, login_response = couriers_methods.login_courier(TC.COURIER_1['login'], TC.COURIER_1['password'])
        # проверка статус-код ответа
        assert login_response.status_code == 404
        # проверка тела ответа:
        content = login_response.json()
        assert content.get("message") == "Учетная запись не найдена"