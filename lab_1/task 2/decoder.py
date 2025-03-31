from lab_1.files_work import read_json_file


def char_frequency(text: str) -> dict:
    """
    Составляет частотный анализ текста
    :param text: текст, частотный анализ которого нужно составить
    :return: множество, где ключ - это символ, а значение его частота в данном тексте
    """
    quantity = {}
    for i in text:
        if i in quantity:
            quantity[i] += 1
        else:
            quantity[i] = 1
    for i in quantity:
        quantity[i] /= len(text)
    return quantity


def decoder(text: str) -> str:
    """
    Расшифровывет текст, закодированный шифром моноалфавитной подстановки
    :param text: текст, который необходимо расшифровать
    :return: расшифрованный текст
    """
    if text is None:
        return ""
    new_text = text
    frequency = char_frequency(text)
    alphabet_frequency = read_json_file("settings.json")["frequency"]
    for i in frequency:
        for j in alphabet_frequency:
            if frequency[i] == alphabet_frequency[j]:
                new_text[i] = alphabet_frequency[j]
    return new_text
