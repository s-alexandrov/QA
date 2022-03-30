from flask import request, Flask
from homework_6.models.orders import Orders

app = Flask(__name__)


@app.route("/orders", methods=["POST"])
def create_order():
    """Создание заказа."""
    orders_info = request.get_json()
    try:
        orders = Orders(
            id = orders_info["id"],
            address_from = orders_info["address_from"],
            address_to = orders_info["address_to"],
            client_id = orders_info["client_id"],
            driver_id = orders_info["driver_id"],
            date_created = orders_info["date_created"],
            status = orders_info["status"],
        )
        orders.create_order()
        return "Запись создана"
    except Exception:
        return "Неправильный запрос"


@app.route("/orders", methods=["GET"])
def find_orders():
    """Поиск заказа."""
    orders = Orders
    try:
        response = orders


@app.route("/orders/<order_id>", methods=["PUT"])
def update_order(order_id: str):
    """Изменение заказа."""
    orders = Orders