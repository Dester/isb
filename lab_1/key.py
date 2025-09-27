import os
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.serialization import load_pem_public_key, load_pem_private_key
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes


def gen_symmetric_key(byte: int) -> bytes:
    """
    генерирует симметричный ключ
    :param byte: длина ключа
    :return: сгенерированный ключ
    """
    return os.urandom(byte)


def gen_asymmetric_keys() -> tuple:
    """
    генерирует приватный и публичный ключ
    :return: кортеж: приватный ключ, публичный ключ
    """
    keys = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048
    )
    public_key = keys.public_key()
    return keys, public_key


def serialization_private_key(private_key, filename: str) -> None:
    """
    сериализует приватный ключ
    :param private_key: приватный ключ
    :param filename: файл в который сериализуется приватный ключ
    """
    try:
        with open(filename, 'wb') as private_out:
            private_out.write(private_key.private_bytes(encoding=serialization.Encoding.PEM,
                                                        format=serialization.PrivateFormat.TraditionalOpenSSL,
                                                        encryption_algorithm=serialization.NoEncryption()))
    except PermissionError as exc:
        print("File access denied, ", exc)
    except Exception as exc:
        print("Error reading from file, ", exc)


def serialization_public_key(public_key, filename: str):
    """
    сериализует публичный ключ
    :param public_key: публичный ключ
    :param filename: файл в который сериализуется публичный ключ
    """
    try:
        with open(filename, 'wb') as public_out:
            public_out.write(public_key.public_bytes(encoding=serialization.Encoding.PEM,
                                                     format=serialization.PublicFormat.SubjectPublicKeyInfo))
    except PermissionError as exc:
        print("File access denied, ", exc)
    except Exception as exc:
        print("Error reading from file, ", exc)


def deserialization_private_key(filename: str):
    """
        Считывает данные из бинарного txt файла
        :param filename: название бинарного файла в формате txt
        :return: считанные данные из файла
        """
    try:
        with open(filename, 'rb') as pem_in:
            private_bytes = pem_in.read()
        return load_pem_private_key(private_bytes, password=None, )
    except FileNotFoundError as exc:
        print("File not found, ", exc)
    except PermissionError as exc:
        print("File access denied, ", exc)
    except Exception as exc:
        print("Error reading from file, ", exc)


def deserialization_public_key(filename: str):
    """
        Считывает данные из бинарного txt файла
        :param filename: название бинарного файла в формате txt
        :return: считанные данные из файла
        """
    try:
        with open(filename, 'rb') as pem_in:
            public_bytes = pem_in.read()
        return load_pem_public_key(public_bytes)
    except FileNotFoundError as exc:
        print("File not found, ", exc)
    except PermissionError as exc:
        print("File access denied, ", exc)
    except Exception as exc:
        print("Error reading from file, ", exc)


def encrypt_key(encryption_key: bytes, public_key):
    """
    Шифрует симметричный ключ с помощью алгоритма RSA-OAEP и публичного ключа
    :param encryption_key: ключ, который необходимо зашифровать
    :param public_key: публичный ключ
    :return: зашифрованный ключ
    """
    return public_key.encrypt(encryption_key,
                              padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()), algorithm=hashes.SHA256(),
                                           label=None))


def decrypt_key(decryption_key: bytes, private_key):
    """
    Дешифрует симметричный ключ с помощью алгоритма RSA-OAEP и приватного ключа
    :param decryption_key: ключ, который необходимо дешифровать
    :param private_key: приватный ключ
    :return: дешифрованный ключ
    """
    dc_key = private_key.decrypt(decryption_key,
                                 padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()), algorithm=hashes.SHA256(),
                                              label=None))
    return dc_key
