import os
import re
import random


def gen_customer_data(customers_count: int) -> list:
    loyalty_programs = ['Ярко', 'Travel', 'CashBack']
    customers = []

    for i in range(0, customers_count + 1):
        customer_id = i + 1
        customers.append({
            '"ID"': str(customer_id),
            '"Возраст"': str(random.randrange(18, 100, step=1)),
            '"Программа_лояльности"': "'" + loyalty_programs[random.randrange(0, 3, step=1)] + "'"
        })

    return customers


def gen_card_data(customers_count: int) -> list:
    cards_count = round(customers_count * 1.5)
    cards = []

    for i in range(0, cards_count + 1):
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


if __name__ == '__main__':
    main()
