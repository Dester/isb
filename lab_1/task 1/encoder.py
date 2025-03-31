def encode(text: str, alphabet: str,  key: int) -> str:
    """
    Шифрует текст с помощью шифра Цезаря
    :param text: текст, который необходимо зашифровать
    :param alphabet: алфавит символов, из которых будет состоять зашифрованный текст
    :param key: сдвиг символов в тексте
    :return: зашифрованный текст
    """
    if text is None:
        return ""
    if alphabet is None:
        raise ValueError("Alphabet not found")
    if key is None:
        raise ValueError("Key not found")
    encrypted_text = ""
    for i in text:
        if i in alphabet:
            encrypted_text += alphabet[(alphabet.index(i)-key) % len(alphabet)]
        else:
            encrypted_text += text[text.index(i)]
    return encrypted_text


def decode(text: str, alphabet: str, key: int) -> str:
    """
    Дешифрует текст с помощью шифра Цезаря
    :param text: текст, который необходимо дешифровать
    :param alphabet: алфавит символов, из которых будет состоять дешифрованный текст
    :param key: сдвиг символов в тексте
    :return: дешифрованный текст
    """
    if text is None:
        return ""
    if alphabet is None:
        raise ValueError("Alphabet not found")
    if key is None:
        raise ValueError("Key not found")
    decrypted_text = ""
    for i in text:
        if i in alphabet:
            decrypted_text += alphabet[(alphabet.index(i)+key) % len(alphabet)]
        else:
            decrypted_text += text[text.index(i)]
    return decrypted_text
