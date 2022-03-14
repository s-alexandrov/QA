import sqlite3
import json
import jsonschema
from typing import Any
from jsonschema import validate


def read_json() -> Any:
    """Читаем json из файла."""
    with open("input_example.json", "r", encoding="utf-8") as file:
        loads_json = json.load(file)
        return loads_json


def validate_json() -> Any:
    """Валидацию входных данных"""
    input_json = read_json()
    try:
        with open("goods.schema_.json", "r", encoding="utf-8") as file:
            schema = json.load(file)
            validate(instance=input_json, schema=schema)
    except jsonschema.exceptions.ValidationError as err:
        return "Ошибка валидации данных!"
    return "Валидация данных успешна!"


def for_bd() -> Any:
    """Переменные для данных."""
    x = read_json()
    for key, value in x.items():
        if isinstance(value, list):
            for i in value:
                if isinstance(i, dict):
                    new_json = {
                        "id": x["id"],
                        "name": x["name"],
                        "type": x["package_params"]["type"],
                        "width": x["package_params"]["width"],
                        "height": x["package_params"]["height"],
                        "depth": x["package_params"]["depth"],
                        "location_and_quantity": x["location_and_quantity"],
                        "location": i["location"],
                        "amount": i["amount"]
                    }
                    return new_json


def create_table(conn: Any) -> None:
    """Создаем таблицы базы данных."""
    c = conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS "goods" (
      "id" INTEGER PRIMARY KEY NOT NULL,
      "name" varchar(50) NOT NULL,
      "package_id" int,
      FOREIGN KEY ("id") REFERENCES "shops_goods" ("id_good")
    );""")
    c.execute("""CREATE TABLE IF NOT EXISTS "packages" (
      "id" INTEGER PRIMARY KEY AUTOINCREMENT,
      "type" package_type,
      "height" float NOT NULL,
      "width" float NOT NULL,
      "depth" float NOT NULL,
      FOREIGN KEY ("id") REFERENCES "goods" ("package_id")
    );""")
    c.execute("""CREATE TABLE IF NOT EXISTS "shops" (
      "id" INTEGER PRIMARY KEY AUTOINCREMENT,
      "address" varchar(100) NOT NULL
    );""")
    c.execute("""CREATE TABLE IF NOT EXISTS "shops_goods" (
      "id" INTEGER PRIMARY KEY AUTOINCREMENT,
      "id_good" int NOT NULL,
      "id_shop" int NOT NULL,
      "amount" int NOT NULL,
      FOREIGN KEY ("id_shop") REFERENCES "shops" ("id"),
      FOREIGN KEY ("id_good") REFERENCES "goods" ("id")
    );""")
    conn.commit()


def insert_table(conn: Any) -> None:
    """Добавляем данные в таблицы."""
    y = for_bd()
    loc_and_qa = y["location_and_quantity"]
    try:
        c = conn.cursor()
        c.execute(f"""INSERT INTO packages (type, height, width, depth) VALUES \
            ("{y["type"]}", "{y["height"]}", "{y["width"]}", "{y["depth"]}");""")
        package_id = c.execute("""SELECT MAX(id) FROM packages""")
        c.execute(f"""INSERT INTO goods (id, name, package_id) VALUES ("{y["id"]}", "{y["name"]}", "{package_id}");""")
        for items in loc_and_qa:
            c.execute(f"""INSERT INTO shops (address) VALUES ("{items["location"]}");""")
            id_good = c.execute("""SELECT id FROM goods""")
            id_shop = c.execute("""SELECT id FROM shops""")
            c.execute(f"""INSERT INTO shops_goods (id_good, id_shop, amount) VALUES ("{id_good}", "{id_shop}", \
            "{items["amount"]}");""")
        print("Данные успешно добавлены!")
        conn.commit()

    except sqlite3.IntegrityError:
        print("Ошибка! Вы пытаетесь добавить данные по предмету уже имеющемуся в базе!")


def main() -> None:
    """Основная функция."""
    conn = sqlite3.connect('TASK.db')
    validate_json()
    create_table(conn)
    insert_table(conn)
    conn.close()


if __name__ == "__main__":
    main()
