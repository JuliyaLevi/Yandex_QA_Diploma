# Юлия Левицкая, 22А когорта — Финальный проект. Инженер по тестированию плюс

import requests
import configuration
import data

def create_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER,
                         json=body,
                         headers=data.headers)

def get_order(track_id):
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER,
                         params={"t": track_id},
                         headers=data.headers)

def positive_assert(body):
    create_order_response = create_order(body)
    track_id = create_order_response.json()["track"]
    order_response = get_order(track_id)
    assert order_response.status_code == 200
    assert order_response.json()["order"]["track"] == track_id

def negative_assert_not_full_params(body):
    create_order_response = create_order(body)
    assert create_order_response.status_code == 400

def negative_assert_not_created_order(track):
    kit_response = get_order(track)
    # Проверяется, что код ответа равен 404
    assert kit_response.status_code == 404

# Тест 1. Успешное создание заказа.
def test_create_order():
    positive_assert(data.order_body)

# Тест 2. Поиск несуществующего заказа.
def test_get_not_created_order():
    negative_assert_not_created_order(9999)

# Тест 3. Успешное создание заказа.
def test_create_order_without_last_name():
    body = data.order_body.copy()
    body.pop("lastName")
    positive_assert(body)