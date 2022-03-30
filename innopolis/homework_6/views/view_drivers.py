from flask import request, Flask, Response
from sqlalchemy.orm import sessionmaker
from homework_6.models.drivers import Drivers

app = Flask(__name__)


@app.route("/drivers", methods=['POST'])
def create_driver():
    """Создание водителя."""
    drivers_info = request.get_json()
    try:
        driver = Drivers(id=drivers_info["id"], name=drivers_info["name"], car=drivers_info["car"])
        driver.create_driver()
        return Response("created!", status=201)
    except Exception:
        return Response("Неправильный запрос", status=400)


@app.route("/drivers", methods=["GET"])
def find_drivers(driver_id):
    """Поиск водителя."""
    drivers = Drivers()
    try:
        response = drivers.get_driver(driver_id)
        if response is None:
            return Response("Объект в базе не найден", status=404)
        return response
    except Exception:
        return Response("Неправильный запрос", status=400)


@app.route("/drivers/<drivers_id>", methods=['DELETE'])
def delete_drivers(driver_id):
    """Удаление водителя."""
    drivers = Drivers()
    try:
        response = drivers.get_driver(driver_id)
        drivers.delete_driver(driver_id)
        if response is None:
            return Response("Объект в базе не найден", status=404)
        return Response("Удалено", status=204)
    except Exception:
        return Response("Неправильный запрос", status=400)


# создание новой сессии, для выполнения действий
# Session = sessionmaker(bind=engine)
# session = Session()