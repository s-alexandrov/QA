from flask import request, Flask, Response
from homework_6.models.clients import Clients

app = Flask(__name__)


@app.route("/clients", methods=["POST"])
def create_clients():
    """Создание клиента."""
    clients_info = request.get_json()
    try:
        clients = Clients(id=clients_info["id"], name=clients_info["name"], car=clients_info["car"])
        clients.create_driver()
        return Response("created!", status=201)
    except Exception:
        return Response("Неправильный запрос", status=400)


@app.route("/clients", methods=["GET"])
def find_clients():
    """Поиск клиентаов."""
    clients = Clients()
    try:
        response = clients.get_driver(clients_id)
        if response is None:
            return Response("Объект в базе не найден", status=404)
        return response
    except Exception:
        return Response("Неправильный запрос", status=400)


@app.route("/clients/<client_id>", methods=["DELETE"])
def delete_clients():
    """Удаление клиента."""
    clients = Clients()
    try:
        response = clients.get_driver(clients_id)
        clients.delete_driver(clients_id)
        if response is None:
            return Response("Объект в базе не найден", status=404)
        return Response("Удалено", status=204)
    except Exception:
        return Response("Неправильный запрос", status=400)


client_info = request.get_json()
# TODO: vlidate body
new_cli = clients(**body)

db.session.add(new_cli)
db.session.commit()