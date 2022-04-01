from flask import request, Flask, Response
from homework_6.models.clients import Clients

app = Flask(__name__)

clients_json_schema = {
    "type": "object",
    "required": ["name", "is_vip"],
    "additionalProperties": False,
    "properties": {
        "name": {"type": "string", "minLength": 1},
        "is_vip": {"type": "boolean"},
    },
}


@app.route("/clients", methods=["POST"])
def create_clients():
    """Создание клиента."""
    clients_info = request.get_json()
    try:
        clients = Clients(id=clients_info["id"], name=clients_info["name"], car=clients_info["car"])
        clients.create_client()
        return Response("created!", status=201)
    except Exception:
        return Response("Неправильный запрос", status=400)


@app.route("/clients", methods=["GET"])
def find_clients(client_id):
    """Поиск клиентаов."""
    clients = Clients()
    try:
        response = clients.get_client(client_id)
        if response is None:
            return Response("Объект в базе не найден", status=404)
        return response
    except Exception:
        return Response("Неправильный запрос", status=400)


@app.route("/clients/<client_id>", methods=["DELETE"])
def delete_clients(client_id):
    """Удаление клиента."""
    clients = Clients()
    try:
        response = clients.get_client(client_id)
        clients.delete_client(client_id)
        if response is None:
            return Response("Объект в базе не найден", status=404)
        return Response("Удалено", status=204)
    except Exception:
        return Response("Неправильный запрос", status=400)


# client_info = request.get_json()
# # TODO: vlidate body
# new_cli = client(**body)
#
# db.session.add(new_cli)
# db.session.commit()