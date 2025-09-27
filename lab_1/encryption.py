import os
import struct

from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from files_work.files_work import *


def get_nonce() -> bytes:
    """
    Создаёт одноразовое случайное число для алгоритма шифрования ChaCha20
    :return: одноразовое случайное число
    """
    nonce = os.urandom(8)
    counter = 0
    return struct.pack("<Q", counter) + nonce


def encryption_text(text: str, key: bytes, nonce: bytes, filename: str) -> None:
    """
    шифрует текст и сохраняет его в файл
    :param text: исходный текст
    :param key: ключ для зашифровки
    :param nonce: одноразовое случайное число для алгоритма шифрования ChaCha20
    :param filename: файл в который будет сохранён текст
    """
    padder = padding.ANSIX923(32).padder()
    text_ = bytes(text, 'UTF-8')
    padded_text = padder.update(text_) + padder.finalize()
    algorithm = algorithms.ChaCha20(key, nonce)
    cipher = Cipher(algorithm, mode=None)
    encryptor = cipher.encryptor()
    write_binary_txt_file(filename, encryptor.update(padded_text) + encryptor.finalize())


def decryption_text(text_file: str, key: bytes, nonce: bytes, filename: str) -> None:
    """
    дешифрует текст и сохраняет его в файл
    :param text_file: файл с текстом, который нужно дешифровать текст
    :param key: файл с ключом для дешифровки
    :param nonce: одноразовое случайное число для алгоритма шифрования ChaCha20
    :param filename: файл в который будет дешифрованный сохранён текст
    """
    algorithm = algorithms.ChaCha20(key, nonce)
    cipher = Cipher(algorithm, mode=None)
    decryptor = cipher.decryptor()
    dc_text = decryptor.update(read_binary_txt_file(text_file)) + decryptor.finalize()
    write_txt_file(filename, dc_text.decode('UTF-8'))

