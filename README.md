# Тестовое задание от Банка СПб

## Задания по SQL

При решении задач использовалась **СУБД PostgreSQL** 16 версии.

### Решения задач

1. Задача № 1:
   * [Задача № 1 (а)](https://github.com/safonovpro/bspb/blob/master/tasks/sql/task_01_a.sql)
   * [Задача № 1 (б)](https://github.com/safonovpro/bspb/blob/master/tasks/sql/task_01_b.sql)
2. [Задача № 2](https://github.com/safonovpro/bspb/blob/master/tasks/sql/task_02.sql)
3. [Задача № 3](https://github.com/safonovpro/bspb/blob/master/tasks/sql/task_03.sql) — **обратите внимание**, что есть вариативность трактовки данного задания, из-за этого может отличаться результат. Для решения задачи, чтобы приблизить окружение максимально к заданию [создано](https://github.com/safonovpro/bspb/blob/master/docker/init/07_create_view_agg_month.sql) представление `agg_month.Transaction`.

### Дополнительная информация по релизации

Для выполнения задание была создана следующая структура таблиц:

![alt text](img/tables.png)

Полный код с комментариями можно посмотреть [в файле](https://github.com/safonovpro/bspb/blob/master/docker/init/01_create_dbs.sql) или вывести в консоли находясь в папке проекта:

```shell
cat docker/init/01_create_dbs.sql
```

К моему **глубокому сожалению** Вами не было предоставлено тестовых данных, поэтому большую часть времени я потратил именно на это. 
Код реализующий эту функцию можно изучить по [ссылке](https://github.com/safonovpro/bspb/blob/master/gen_fake_data.py). 
Всё реализовано с использованием стандартного функционала `python`, никаких доп. пакетов для воспроизведения не требуется. В папке проект необходимо выполнить:

```shell
python gen_fake_data.py
```

Скрипт генерирует следующий список файлов:

1. `docker/init/02_customer.sql`
2. `docker/init/03_card.sql`
3. `docker/init/04_customer_product.sql`
4. `docker/init/05_customer_kgd.sql`
5. `docker/init/06_transaction.sql`

Для запуска окружения сначала надо скопировать файл с переменными окружения и при необходимости его отредактировать:

```shell
cp .env_sample .env
```

Далее при наличии современной версии `docker` запустить в папке проекта:

```shell
docker compose up -d
```
