﻿# API Order Status Automation

## Описание проекта

Этот проект автоматизирует процесс проверки создания заказа через API, а также проверку статусов заказов в базе данных. В проекте выполнены два задания: работа с базой данных и автотест для проверки работы API.

### Задание 1: Работа с базой данных

Необходимо вывести список логинов курьеров с количеством их заказов в статусе «В доставке» (поле `inDelivery = true`).

### Задание 2: Работа с базой данных

Необходимо убедиться, что статусы заказов записываются корректно в базе данных. Статусы определяются по следующим правилам:
- Если поле `finished` = true, то статус 2.
- Если поле `cancelled` = true, то статус -1.
- Если поле `inDelivery` = true, то статус 1.
- Для остальных случаев статус 0.

### Автоматизация теста к API

Цель автотеста: проверить, что после создания заказа его можно получить по номеру трека через API.

#### Шаги автотеста:

1. Выполнить запрос на создание заказа.
2. Сохранить номер трека заказа.
3. Выполнить запрос на получение заказа по треку.
4. Проверить, что код ответа API равен 200.

## Структура репозитория

- **Работа с базой данных - Задание 1.sql** – SQL-запрос для первого задания.
- **Работа с базой данных - Задание 2.sql** – SQL-запрос для второго задания.
- **configuration.py** – файл конфигураций (подключение к базе данных и API).
- **create_order_test.py** – автотест для проверки создания и получения заказа через API.
- **data.py** – вспомогательный файл с данными.
- **Запуск теста в PyCharm.png** – скриншот успешного запуска автотеста в PyCharm.

## Скриншот

![Запуск теста в PyCharm](Запуск%20теста%20в%20PyCharm.png)

