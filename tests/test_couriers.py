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
    def test_creating_two_identical_courier(self, registered_courier):
        # создание экземпляр класса CouriersMethods
        couriers_methods = CouriersMethods()
        # попытка зарегистрировать курьера с уже существующими данными:
        result = couriers_methods.given_register_new_courier(**TC.COURIER_1)
        # проверка статус-код ответа
        assert result['response'].status_code == 409
        # проверка тела ответа:
        content = result['response'].json()
        assert content.get("message") == "Этот логин уже используется. Попробуйте другой."


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
    def test_login_courier(self, registered_courier):
        # создание экземпляр класса CouriersMethods
        couriers_methods = CouriersMethods()
        # регистрация курьера
        courier_id, login_response = couriers_methods.login_courier(
            TC.COURIER_1['login'],
            TC.COURIER_1['password']
        )
        # проверка статус-код ответа
        assert login_response.status_code == 200
        # проверка тела ответа:
        assert courier_id is not None
        print(f"Успешный логин! ID курьера: {courier_id}")




    # ошибка на авторизацию курьера с неправильно указанным логином или паролем
    @pytest.mark.parametrize(
        'login, password',
        [
            (TC.COURIER_1['login'], TC.WRONG_PASSWORD_COURIER_1['password']),
            (TC.WRONG_LOGIN_COURIER_1['login'], TC.COURIER_1['password'])
        ]
    )
    @allure.title('Тест на выпадение ошибки при авторизации курьера с неверным логином или паролем')
    def test_login_courier_wrong_data(self, login, password, registered_courier):
        # создание экземпляр класса CouriersMethods
        couriers_methods = CouriersMethods()
        # попытка авторизации с неверными данными
        courier_id, login_response = couriers_methods.login_courier(login, password)
        # проверка статус-код
        assert login_response.status_code == 404
        # проверка тела ответа
        content = login_response.json()
        assert content.get("message") == "Учетная запись не найдена"


    # ошибка на авторизацию курьера с отсутствующим логином или паролем
    @pytest.mark.parametrize(
        'login, password',
        [
            (TC.COURIER_1['login'], TC.WITHOUT_PASSWORD_COURIER_1['password']),
            (TC.WITHOUT_LOGIN_COURIER_1['login'], TC.COURIER_1['password'])
        ]
    )
    @allure.title('Тест на выпадение ошибки при авторизации курьера без логина или пароля')
    def test_login_courier_without_data(self, login, password, registered_courier):
        # создание экземпляр класса CouriersMethods
        couriers_methods = CouriersMethods()

        # проверка, что авторизация с отсутствующим паролем или логином вызывает ошибку
        courier_id, login_response = couriers_methods.login_courier(login, password)
        # Проверяем статус код и сообщение об ошибке
        assert login_response.status_code == 400
        content = login_response.json()
        assert content.get("message") == "Недостаточно данных для входа"



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