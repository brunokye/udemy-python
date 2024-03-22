"""
PyMySQL - um cliente MySQL feito em Python Puro
Doc: https://pymysql.readthedocs.io/en/latest/
Pypy: https://pypi.org/project/pymysql/
GitHub: https://github.com/PyMySQL/PyMySQL
"""

import os
import pymysql
import pymysql.cursors
import dotenv

# from typing import cast

TABLE_NAME = "customers"
# CURRENT_CURSOR = pymysql.cursors.SSDictCursor

dotenv.load_dotenv()

connection = pymysql.connect(
    host=os.environ["MYSQl_HOST"],
    user=os.environ["MYSQl_USER"],
    password=os.environ["MYSQl_PASSWORD"],
    database=os.environ["MYSQl_DATABASE"],
    charset="utf8mb4",
    # cursorclass=pymysql.cursors.Cursor,
    cursorclass=pymysql.cursors.DictCursor,
    # cursorclass=pymysql.cursors.SSDictCursor,
)

with connection:
    with connection.cursor() as cursor:
        # cursor = cast(CURRENT_CURSOR, cursor)

        cursor.execute(
            f"CREATE TABLE IF NOT EXISTS {TABLE_NAME} ("
            "id INT NOT NULL AUTO_INCREMENT, "
            "nome VARCHAR(50) NOT NULL, "
            "idade INT NOT NULL, "
            "PRIMARY KEY (id)"
            ")"
        )

        # Cuidado, isso limpa a tabela.
        cursor.execute(f"TRUNCATE TABLE {TABLE_NAME}")

        # connection.commit()
        # CREATE TABLE não precisa de commit

    with connection.cursor() as cursor:
        sql = f"INSERT INTO {TABLE_NAME} (nome, idade) VALUES (%s, %s)"
        data = ("Luiz", 18)
        cursor.execute(sql, data)

    connection.commit()

    with connection.cursor() as cursor:
        sql = (
            f"INSERT INTO {TABLE_NAME} "
            "(nome, idade) VALUES (%(nome)s, %(idade)s)"
        )
        data = (
            {"nome": "Rafael", "idade": 25},
            {"nome": "Pedro", "idade": 32},
            {"nome": "Julia", "idade": 53},
        )
        # data = (
        #     ("Rafael", 25),
        #     ("Pedro", 32),
        #     ("Julia", 53),
        # )

        cursor.executemany(sql, data)

    connection.commit()

    with connection.cursor() as cursor:
        # menor_id = int(input("Digite o menor id: "))
        # maior_id = int(input("Digite o maior id: "))
        menor_id, maior_id = 1, 2

        sql = f"SELECT * FROM {TABLE_NAME} WHERE id BETWEEN %s AND %s"
        cursor.execute(sql, (menor_id, maior_id))

        # Caso queira utilizar os valores mais de uma vez
        # data = cursor.fetchall()

        # Verificar qual o comando que está sendo executado no SQL
        # print(cursor.mogrify(sql, (menor_id, maior_id)))

        # print(f"\n{20 * '-'}\n")

        # for row in cursor.fetchall():
        #     print(row)

    with connection.cursor() as cursor:
        delete = f"DELETE FROM {TABLE_NAME} WHERE id = 2"
        cursor.execute(delete)
        connection.commit()

        select = f"SELECT * FROM {TABLE_NAME}"
        cursor.execute(select)

        # for row in cursor.fetchall():
        #     print(row)

    with connection.cursor() as cursor:
        update = f"UPDATE {TABLE_NAME} SET nome = %s, idade = %s WHERE id = %s"
        data = ("Gabriela", "200", 4)
        cursor.execute(update, data)
        connection.commit()

        select = f"SELECT * FROM {TABLE_NAME}"
        cursor.execute(select)

        # for row in cursor.fetchall():
        #     print(row)

    with connection.cursor() as cursor:
        select = f"SELECT * FROM {TABLE_NAME}"
        cursor.execute(select)

        # for row in cursor.fetchall():
        #     _id, name, age = row
        #     print(_id, name, age)

        # for row in cursor.fetchall_unbuffered():
        #     print(row)

        #     if row["id"] >= 1:
        #         break

        # print(f"\n{20 * '-'}\n")

        # # cursor.scroll(-1)
        # for row in cursor.fetchall_unbuffered():
        #     print(row)

    with connection.cursor() as cursor:
        select = f"SELECT * FROM {TABLE_NAME}"
        sql = cursor.execute(select)
        data = cursor.fetchall()

        for row in data:
            print(row)

        print(f"\n{20 * '-'}\n")

        print(f"SELECT: {sql}")
        print(f"len(data): {len(data)}")
        print(f"rowcount: {cursor.rowcount}")
        print(f"rownumber: {cursor.rownumber}")

        print(f"\n{20 * '-'}\n")

        # sql = f"INSERT INTO {TABLE_NAME} (nome, idade) VALUES (%s, %s)"
        # data = ("Diogo", 20)
        # cursor.execute(sql, data)

        sql = (
            f"INSERT INTO {TABLE_NAME} "
            "(nome, idade) VALUES (%(nome)s, %(idade)s)"
        )
        data = (
            {"nome": "Jéssica", "idade": 25},
            {"nome": "Henrique", "idade": 32},
            {"nome": "Lucas", "idade": 53},
        )
        # data = (
        #     ("Rafael", 25),
        #     ("Pedro", 32),
        #     ("Julia", 53),
        # )

        cursor.executemany(sql, data)

        print(f"lastrowid: {cursor.lastrowid}")

        cursor.execute(f"SELECT id FROM {TABLE_NAME} ORDER BY id DESC LIMIT 1")
        lastIdFromSelect = cursor.fetchone()
        print(f"lastrowid (manual): {lastIdFromSelect}")

    connection.commit()
