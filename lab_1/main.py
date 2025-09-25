from files_work.files_work import *
from key import *
from encryption import *


def main():
    try:
        paths = read_json_file("settings.json")["paths"]
        key = gen_symmetric_key(32)
        write_binary_txt_file(paths["key"], key)
        print("Symmetric_key:", read_binary_txt_file(paths["key"]))
        serialization_private_key(paths["closed_key"])
        print("Private_key:", read_binary_txt_file(paths["closed_key"]))
        serialization_public_key(paths["open_key"])
        print("Public_key:", read_binary_txt_file(paths["open_key"]))
        public_key = deserialization_public_key(paths["open_key"])
        encrypted_key = encrypt_key(key, public_key)
        write_binary_txt_file(paths["encrypted_key"], encrypted_key)
        print("Encrypted_key:", encrypted_key)
        private_key = deserialization_private_key(paths["closed_key"])
        # decrypted_key = decrypt_key(encrypted_key, private_key)
        text = read_txt_file(paths["text"])
        encryption_text(text, key, paths["encrypted_text"])
        decryption_text(paths["encrypted_text"], key, paths["decrypted_text"])
    except FileNotFoundError as exc:
        print("Error: ", exc)
    except PermissionError as exc:
        print("Error: ", exc)
    except Exception as exc:
        print("Error: ", exc)


if __name__ == "__main__":
    main()
