# Sprint_7
Тестирование сайта "Самокат на пару дней"
URL сайта - 'https://qa-scooter.praktikum-services.ru/'
Документация 'https://qa-scooter.praktikum-services.ru/docs/'

Тесты "Создание курьера"
1. test_creating_courier - тестирует успешную регистрацию курьера на сайте
2. test_creating_two_identical_courier - тестирует невозможность создания двух курьеров с одинаковым логином
3. test_register_new_courier_without_login - тестирует невозможность создания курьера без логина или пароля

Тесты "Логин курьера в системе"
4. test_login_courier - тестирует успешный логин курьера в системе
5. test_login_courier_wrong_data - тестирует невозможность залогиниться с неверным логином или паролем
6. test_login_courier_without_data - тестирует невозможность залогиниться без логина или пароля
7. test_login_not_creating_courier - тестирует невозможность залогиниться, если курьер не был создан

Тесты "Создание заказа"
8. test_create_order - тест на успешное создание заказа

Тесты "Получение списка заказов"
9. test_list_order - тест на успешное выведение списка заказов

