from flask import request, Flask
from homework_6.models.clients import Clients

app = Flask(__name__)


@app.route("/clients", methods=["POST"])
def create_clients():
    clients_json = request


@app.route("/clients", methods=["GET"])
def find_clients():
    """Поиск клиентаов."""
    clients = Clients


@app.route("/clients/<client_id>", methods=["DELETE"])
def delete_clients():
    """Удаление клиента."""
    clients = Clients


    client_info = request.get_json()
    # TODO: vlidate body
    new_cli = clients(**body)

    db.session.add(new_cli)
    db.session.commit() 