def unit_search(crators_array: list, x: int, y: int) -> None:
    """Проверяем вхождение в массив и ищем единицы."""
    if 0 <= x < len(crators_array) and 0 <= y < len(crators_array[0]):
        if crators_array[x][y] == 1:
            crators_array[x][y] = 0
            unit_search(crators_array, x - 1, y)
            unit_search(crators_array, x + 1, y)
            unit_search(crators_array, x, y - 1)
            unit_search(crators_array, x, y + 1)


def calculate(crators_array: list) -> int:
    """Определяем число краторов на луне."""
    count = 0
    # TODO Карта луны не обязательно должна быть квадраной, ширина может отличаться от длины
    for i in range(len(crators_array)):
        for j in range(len(crators_array[i])):
            if crators_array[i][j] == 1:
                unit_search(crators_array, i, j)
                count += 1
    return count


def read_file() -> list:
    """Создаем двумерный массив из полученных данных."""
    with open("myfile.txt", "r") as file:
        crators_array = file.readlines()
    crators_array = [[int(n) for n in x.split()] for x in crators_array]
    return crators_array


moon_map = read_file()
result = calculate(moon_map)
