import itertools
import json
from typing import Iterable, Dict, Optional, List, Any


class OutOfResourceError(Exception):
    def __init__(self: Any, message: str) -> None:
        super().__init__(message)


def read_json(json_file: str) -> Any:
    """Читаем json из файла."""
    with open(json_file, "r", encoding="utf-8") as file:
        json_dict = json.load(file)
    return json_dict


def get_coffee_machine(item: Dict) -> Optional[int]:
    # return item.get("чашка")
    return item.get("тип")


def calculate(mydict: Iterable) -> List:
    c_machine_resource = itertools.groupby(mydict, get_coffee_machine)
    overall_instruction = list()
    c_machine_manager = dict()
    for key, group in c_machine_resource:
        if not c_machine_manager.get(key):
            c_machine_manager[key] = dict()
            c_machine_manager[key]["арабика"] = dict()
            c_machine_manager[key]["вода"] = dict()
            c_machine_manager[key]["молоко"] = dict()
            c_machine_manager[key]["карамель"] = dict()
            c_machine_manager[key]["добавки"] = list()
        for resource in group:
            if resource.get("ресурс") == "арабика":
                c_machine_manager[key]["арабика"] = resource
            elif resource.get("ресурс") == "вода":
                c_machine_manager[key]["вода"] = resource
            elif resource.get("ресурс") == "молоко":
                c_machine_manager[key]["молоко"] = resource
            elif resource.get("ресурс") == "карамель":
                c_machine_manager[key]["карамель"] = resource
            else:
                c_machine_manager[key]["добавки"].append(resource)

    for key, item in c_machine_manager.items():
        coffee = item.get("арабика")
        water = item.get("вода")
        milk = item.get("молоко")
        caramel = item.get("карамель")
        other_resources = item.get("добавки")
        for resource in item:
            if resource.get("тип") == "кофе" and (resource.get("количество") // resource.get("порция")) > 0:
                coffee[resource.get("ресурс")] = "кофе"
            elif resource.get("тип") == "вода" and (resource.get("количество") // resource.get("порция")) > 0:
                water[resource.get("ресурс")] = "вода"
            elif resource.get("тип") == "молоко" and (resource.get("количество") // resource.get("порция")) > 0:
                milk[resource.get("ресурс")] = "молоко"
            elif resource.get("тип") == "сироп" and (resource.get("количество") // resource.get("порция")) > 0:
                caramel[resource.get("ресурс")] = "сироп"

            for _ in range(resource):
                overall_instruction.append({
                    coffee.get("кофе"): coffee.get("арабика"),
                    water.get("вода"): water.get("вода"),
                    }
                )

        if overall_instruction == []:
            raise OutOfResourceError("no production")

        return overall_instruction


j_file = read_json("input_example.json")
calculate(j_file)
