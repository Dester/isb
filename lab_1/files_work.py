import json


def read_txt_file(filename: str) -> str:
    """
    Считывает данные из txt файла
    :param filename: название файла в формате txt
    :return: считанные данные из файла
    """
    if filename is not None:
        with open(filename, "r", encoding="utf-8") as file:
            return file.read()
    else:
        raise FileNotFoundError("File not found")


def write_txt_file(filename: str, text: str) -> None:
    """
    Записывает данные в txt файл
    :param filename: название файла в формате txt
    :param text: данные для записи в файл
    """
    with open(filename, "w", encoding="utf-8") as file:
        file.write(text)


def read_json_file(filename: str) -> dict:
    """
    Считывает данные из json файла
    :param filename: название файла в формате json
    :return: считанные данные из файла
    """
    if filename is not None:
        with open(filename, "r", encoding="utf-8") as file:
            return json.load(file)
    else:
        raise FileNotFoundError("File not found")
