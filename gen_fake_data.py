import os
import re
import time
import random
from datetime import datetime


def gen_customer_data(customers_count: int) -> list:
    loyalty_programs = ['Ярко', 'Travel', 'CashBack']
    customers = []

    for i in range(0, customers_count):
        customer_id = i + 1
        customers.append({
            '"ID"': str(customer_id),
            '"Возраст"': str(random.randrange(18, 100, step=1)),
            '"Программа_лояльности"': "'" + loyalty_programs[random.randrange(0, len(loyalty_programs), step=1)] + "'"
        })

    return customers


def gen_card_data(customers_count: int) -> list:
    cards_count = round(customers_count * 1.5)
    cards = []

    for i in range(0, cards_count):
        card_id = i + 1
        cards.append({
            '"ID"': str(card_id),
            '"Customer_id"': str(random.randrange(1, customers_count, step=1)),
            # вариативность поля «тип_карты» не была описана, предположил ниже следующее
            '"тип_карты"': f"'{['кредитная', 'дебетовая'][random.randrange(0, 2, step=1)]}'",
            # ниже следующие поля никак не участвуют в задачах,
            # по этим причина поля заполняются значениями по умолчанию
            'dfrom': "'2020-01-01'",
            'dto': "'2030-12-31'"
        })

    return cards


def gen_customer_product_data(customers_count: int) -> list:
    products_count = round(customers_count * 2)
    product_types = ['Потреб', 'Дебетовая карта', 'Кредитная карта', 'Ипотека', 'Вклад']
    products = []

    for i in range(0, products_count):
        end_year = random.randrange(2020, 2030 + 1, step=1)

        products.append({
            '"Customer_id"': str(random.randrange(1, customers_count, step=1)),
            '"Тип_Продукта" ': "'" + product_types[random.randrange(0, len(product_types))] + "'",
            '"Дата начала действия"': "'2020-01-01'",
            '"Дата окончания действия"': f"'{end_year}-12-31'",
            # Осознано формируется случайным образом
            'current_is_active': f"{['true', 'false'][random.randrange(0, 2, step=1)]}",
        })

    return products


def gen_customer_kgd(customer_count: int) -> list:
    cities = ['Москва', 'Санкт-Петербург', 'Калининград']
    kgds = []

    for i in range(0, customer_count):
        customer_id = i + 1
        kgds.append({
            '"Customer_id"': str(customer_id),
            '"Отделение"': f"'{random.randrange(1, 10, step=1)} - {cities[random.randrange(0, len(cities), step=1)]}'"
        })

    return kgds


def gen_transaction(customers_count: int, cards_count: int) -> list:
    transaction_count = round(customers_count * 100)
    timestamp_start = 1577826000  # 2020-01-01 00:00:00
    transactions = []

    for i in range(0, transaction_count):
        item_timestamp = random.randrange(timestamp_start, round(time.time()), step=3600)

        transactions.append({
            '"дата"': "'" + datetime.utcfromtimestamp(item_timestamp).strftime('%Y-%m-%d %H:%M:%S') + "'",  # str(random.randrange(timestamp_start, round(time.time()), step=3600)),
            '"сумма"': str(float(random.randrange(100, 10000, step=5))),
            '"ID_карта" ': str(random.randrange(0, cards_count, step=1) + 1),
            # ниже следующие поля никак не участвуют в задачах,
            # по этим причина поля заполняются значениями по умолчанию
            'mcc': "'0000'",
            '"номер терминала"': str(random.randrange(0, 10, step=1) + 1)
        })

    return transactions


def save_as_sql(data: list, table: str, file_path: str):
    columns = data[0].keys()
    sql_tpl = re.sub(r'^\s+', '', '''
        insert into {table} ({columns}) values
        {rows};
    ''', flags=re.MULTILINE)
    rows = []

    for item in data:
        rows.append(f"\t({', '.join(item.values())})")

    sql = sql_tpl.format(
        table=table,
        columns=', '.join(columns),
        rows=',\n'.join(rows)
    )

    with open(file_path, 'w') as f:
        f.write(sql)


def main():
    records_count = 1000

    customer_data, customer_sql_path = gen_customer_data(records_count), 'docker/init/02_customer.sql'
    if not os.path.exists(customer_sql_path):
        save_as_sql(customer_data, '"Customer"', customer_sql_path)

    card_data, card_sql_path = gen_card_data(records_count), 'docker/init/03_card.sql'
    if not os.path.exists(card_sql_path):
        save_as_sql(card_data, '"Card"', card_sql_path)

    customer_product_data, customer_product_sql_path = gen_customer_product_data(records_count), 'docker/init/04_customer_product.sql'
    if not os.path.exists(customer_product_sql_path):
        save_as_sql(customer_product_data, '"CustomerProduct"', customer_product_sql_path)

    customer_kgd_data, customer_kgd_sql_path = gen_customer_kgd(records_count), 'docker/init/05_customer_kgd.sql'
    if not os.path.exists(customer_kgd_sql_path):
        save_as_sql(customer_kgd_data, '"Customer_KGD"', customer_kgd_sql_path)

    transaction_data, transaction_sql_path = gen_transaction(records_count, len(card_data)), 'docker/init/06_transaction.sql'
    if not os.path.exists(transaction_sql_path):
        save_as_sql(transaction_data, '"Transaction"', transaction_sql_path)


if __name__ == '__main__':
    main()
