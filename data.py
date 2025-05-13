
# класс TEST COURIERS (TC)
class TC:

    # правильный курьер
    COURIER_1 ={
        "login": "Amigo",
        "password": "1234",
        "first_name": "Дружище"
    }

    # неверный пароль курьера 1
    WRONG_PASSWORD_COURIER_1 = {
        "password": "1111"
    }

    # отсутствующий пароль у курьера 1
    WITHOUT_PASSWORD_COURIER_1 = {
        "password": ""
    }

    # неверный логин курьера 1
    WRONG_LOGIN_COURIER_1 = {
        "login": "Amiga",
    }

    # отсутствующий логин у курьера 1
    WITHOUT_LOGIN_COURIER_1 = {
        "login": "",
    }

    # курьер без логина
    COURIER_2 = {
        "login": "",
        "password": "1234",
        "first_name": "Мужик"
    }

    # курьер без пароля
    COURIER_3 = {
        "login": "Нombre",
        "password": "",
        "first_name": "Мужик"
    }



# класс TEST ORDERS (TO)
class TO:
    #заказ 1
    ORDER_1 ={
        "firstName": "Naruto",
        "lastName": "Uchiha",
        "address": "Konoha, 142 apt.",
        "metroStation": 4,
        "phone": "+7 800 355 35 35",
        "rentTime": 5,
        "deliveryDate": "2020-06-06",
        "comment": "Saske, come back to Konoha",
        "color": [
            "BLACK"
        ]
    }
    # заказ 2
    ORDER_2 = {
        "firstName": "Naruto",
        "lastName": "Uchiha",
        "address": "Konoha, 142 apt.",
        "metroStation": 4,
        "phone": "+7 800 355 35 35",
        "rentTime": 5,
        "deliveryDate": "2020-06-06",
        "comment": "Saske, come back to Konoha",
        "color": [
            "GREY"
        ]
    }

    # заказ 3
    ORDER_3 = {
        "firstName": "Naruto",
        "lastName": "Uchiha",
        "address": "Konoha, 142 apt.",
        "metroStation": 4,
        "phone": "+7 800 355 35 35",
        "rentTime": 5,
        "deliveryDate": "2020-06-06",
        "comment": "Saske, come back to Konoha",
        "color": [
            "GREY",
            "BLACK"
        ]
    }

    # заказ 4
    ORDER_4 = {
        "firstName": "Naruto",
        "lastName": "Uchiha",
        "address": "Konoha, 142 apt.",
        "metroStation": 4,
        "phone": "+7 800 355 35 35",
        "rentTime": 5,
        "deliveryDate": "2020-06-06",
        "comment": "Saske, come back to Konoha",
        "color": [
        ]
    }