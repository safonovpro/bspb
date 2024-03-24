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
    customer_data = gen_customer_data(records_count)
    customer_sql_path = 'docker/init/02_customer.sql'
    save_as_sql(customer_data, '"Customer"', customer_sql_path)


if __name__ == '__main__':
    main()

