import json
import itertools
from typing import Iterable, Dict, Optional, List, Any


class NetworkInitialConfigurationError(Exception):
    """Исключение, если из имеющихся ресурсов не запланировать ни одного напитка"""
    def __init__(self, message: str):
        super().__init__(self)
        self.message = message

    def __str__(self) -> str:
        return "Ошибка узла"


def read_json(json_file: str) -> Any:
    """Читаем json из файла."""
    with open(json_file, "r", encoding="utf-8") as file:
        json_dict = json.load(file)
    return json_dict


def get_node(item: Dict) -> Optional[int]:
    """Собираем все node_id."""
    return item.get("node_id")


def get_node_connections_list(item: Dict) -> Optional[int]:
    """Собираем все node_connections_list."""
    return item.get("node_connections_list")


def calculate(mydict: Iterable) -> List:
    output_result = [[]]
    nodes_resource = itertools.groupby(mydict, get_node)
    nodes_list = []
    for key, group in nodes_resource:
        for resource in group:
            nodes_list.append(resource.get("node_id"))  # складываем node_id в отдельный список

    nodes_resource = itertools.groupby(mydict, get_node_connections_list)
    connection_list = []
    for key, group in nodes_resource:
        for resource in group:
            connection_list.append(resource.get("node_connections_list"))

    for connection in mydict:
        for node in connection["node_connections_list"]:
            if (node not in nodes_list) or (node == connection["node_id"]):
                raise NetworkInitialConfigurationError("Ошибка узла")
        required_connection_list = list(nodes_list)
        required_connection_list.remove(connection["node_id"])
        required_connection_dict = []
        for conn in required_connection_list:
            for x in mydict:
                if x["node_id"] == conn:
                    required_connection_dict.append(x)
        for conn in required_connection_dict:
            if connection["node_id"] in conn["node_connections_list"]:
                required_connection_list.remove(conn["node_id"])
        if set(required_connection_list).issubset(connection["node_connections_list"]) == False:
            output_result[0].append(connection["node_id"])
    if output_result[0] == []:
        return []
    else:
        return output_result


j_file = read_json("input_example.json")
print(calculate(j_file))
