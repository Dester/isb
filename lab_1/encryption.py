import os
import struct

from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from files_work.files_work import *


def encryption_text(text: str, key: bytes, filename: str) -> None:
    """
    шифрует текст и сохраняет его в файл
    :param text: исходный текст
    :param key: ключ для зашифровки
    :param filename: файл в который будет сохранён текст
    """
    padder = padding.ANSIX923(32).padder()
    text_ = bytes(text, 'UTF-8')
    padded_text = padder.update(text_) + padder.finalize()
    nonce = os.urandom(8)
    counter = 0
    full_nonce = struct.pack("<Q", counter) + nonce
    algorithm = algorithms.ChaCha20(key, full_nonce)
    cipher = Cipher(algorithm, mode=None)
    encryptor = cipher.encryptor()
    write_binary_txt_file(filename, encryptor.update(padded_text) + encryptor.finalize())


def decryption_text(text_file: str, key: bytes, file: str) -> None:
    """
    дешифрует текст и сохраняет его в файл
    :param text_file: файл с текстом, который нужно дешифровать
    :param key: файл с ключом для дешифровки
    :param file: файл в который будет дешифрованный сохранён текст
    """
    nonce = os.urandom(8)
    counter = 0
    full_nonce = struct.pack("<Q", counter) + nonce
    algorithm = algorithms.ChaCha20(key, full_nonce)
    cipher = Cipher(algorithm, mode=None)
    decryptor = cipher.decryptor()
    dc_text = decryptor.update(read_binary_txt_file(text_file)) + decryptor.finalize()
    print(dc_text.decode('UTF-8'))
    unpadder = padding.ANSIX923(32).unpadder()
    unpadded_dc_text = unpadder.update(dc_text)
    print(unpadded_dc_text.decode('UTF-8'))
    # write_txt_file(file, dc_text.decode('UTF-8'))
    # iv = os.urandom(16)
    # cipher = Cipher(algorithms.AES(read_binary_txt_file(key_file)), modes.CBC(iv))
    # decryptor = cipher.decryptor()
    # dc_text = decryptor.update(read_binary_txt_file(text_file)) + decryptor.finalize()
    # unpadder = padding.ANSIX923(32).unpadder()
    # write_binary_txt_file(file, unpadder.update(dc_text) + unpadder.finalize())
