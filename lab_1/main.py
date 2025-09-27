from files_work.files_work import *
from key import *
from encryption import *
import argparse


def parsing():
    """
    выбор режима работы программы из консоли:
    '-gen', '--generation' - режим генерации ключей
    '-enc', '--encryption' - режим шифрования
    '-dec', '--decryption' - режим дешифрования
    :return: аргументы для выбора режима работы
    """
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group(required=False)
    group.add_argument('-gen', '--generation', action='store_true', help='Запускает режим генерации ключей')
    group.add_argument('-enc', '--encryption', action='store_true', help='Запускает режим шифрования')
    group.add_argument('-dec', '--decryption', action='store_true', help='Запускает режим дешифрования')
    return parser.parse_args()


def main():
    try:
        paths = read_json_file("settings.json")["paths"]
        args = parsing()
        if args.generation:
            print("Key generation")
            key = gen_symmetric_key(32)
            write_binary_txt_file(paths["key"], key)
            print("Symmetric_key:", read_binary_txt_file(paths["key"]))
            keys = gen_asymmetric_keys()
            serialization_private_key(keys[0], paths["closed_key"])
            print("Private_key:", read_binary_txt_file(paths["closed_key"]))
            serialization_public_key(keys[1], paths["open_key"])
            print("Public_key:", read_binary_txt_file(paths["open_key"]))
            public_key = deserialization_public_key(paths["open_key"])
            encrypted_key = encrypt_key(key, public_key)
            write_binary_txt_file(paths["encrypted_key"], encrypted_key)
            print("Encrypted_key:", encrypted_key)
            print("Key generation - successful")
        elif args.encryption:
            print("Text encryption")
            nonce = get_nonce()
            write_binary_txt_file(paths["nonce"], nonce)
            encrypted_key = read_binary_txt_file(paths["encrypted_key"])
            private_key = deserialization_private_key(paths["closed_key"])
            decrypted_key = decrypt_key(encrypted_key, private_key)
            print("Decrypted_key:", decrypted_key)
            text = read_txt_file(paths["text"])
            encryption_text(text, decrypted_key, nonce, paths["encrypted_text"])
            print("Text encryption - successful")
        elif args.decryption:
            print("Text decryption")
            nonce = read_binary_txt_file(paths["nonce"])
            encrypted_key = read_binary_txt_file(paths["encrypted_key"])
            private_key = deserialization_private_key(paths["closed_key"])
            decrypted_key = decrypt_key(encrypted_key, private_key)
            decryption_text(paths["encrypted_text"], decrypted_key, nonce, paths["decrypted_text"])
            print("Text decryption - successful")
        else:
            key = gen_symmetric_key(32)
            write_binary_txt_file(paths["key"], key)
            print("Symmetric_key:", read_binary_txt_file(paths["key"]))
            keys = gen_asymmetric_keys()
            serialization_private_key(keys[0], paths["closed_key"])
            print("Private_key:", read_binary_txt_file(paths["closed_key"]))
            serialization_public_key(keys[1], paths["open_key"])
            print("Public_key:", read_binary_txt_file(paths["open_key"]))
            public_key = deserialization_public_key(paths["open_key"])
            encrypted_key = encrypt_key(key, public_key)
            write_binary_txt_file(paths["encrypted_key"], encrypted_key)
            print("Encrypted_key:", encrypted_key)
            private_key = deserialization_private_key(paths["closed_key"])
            decrypted_key = decrypt_key(encrypted_key, private_key)
            print("Decrypted_key:", decrypted_key)
            text = read_txt_file(paths["text"])
            nonce = get_nonce()
            encryption_text(text, decrypted_key, nonce, paths["encrypted_text"])
            decryption_text(paths["encrypted_text"], decrypted_key, nonce, paths["decrypted_text"])

    except FileNotFoundError as exc:
        print("Error: ", exc)
    except PermissionError as exc:
        print("Error: ", exc)
    except Exception as exc:
        print("Error: ", exc)


if __name__ == "__main__":
    main()
