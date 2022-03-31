from flask import request, Flask
from homework_6.models.orders import Orders

app = Flask(__name__)

orders_json_schema = {
    "type": "object",
    "required": ["client_id", "driver_id", "date_created", "status", "address_from", "address_to"],
    "additionalProperties": False,
    "properties": {
        "client_id": {"type": "integer"},
        "driver_id": {"type": "integer"},
        "date_created": {"type": "string", "format": "date-time"},
        "status": {
            "type": "string",
            "enum": ["not_accepted", "in_progress", "done", "cancelled"],
        },
        "address_from": {"type": "string", "minLength": 1},
        "address_to": {"type": "string", "minLength": 1},
    },
}

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


@app.route("/orders/<order_id>", methods=["PUT"])
def update_order(order_id: str):
    """Изменение заказа."""
    orders = Orders
