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
    new_text = str(text)
    a = ""
    frequency1 = char_frequency(text)
    del frequency1['\n']
    frequency = sorted(frequency1.items(), key=lambda item: item[1])
    print(frequency)
    alphabet_frequency = sorted(read_json_file("task_2/settings.json")["frequency"].items(), key=lambda item: item[1])
    print(alphabet_frequency)
    for i in range(len(frequency)):
        new_text = new_text.replace(frequency[i][0], alphabet_frequency[i][0])
        #print('\n', new_text)
    print(len(frequency), len(alphabet_frequency))
    print()
    return new_text
