from files_work import *
from task_1.encoder import *


def main():
    try:
        text = read_txt_file("task_1/text.txt")
        print(text, '\n')
        alphabet = read_json_file("task_1/settings.json")["alphabet"]
        key = read_json_file("task_1/key.json")["key"]
        encrypted_text = encode(text, alphabet, key)
        write_txt_file("task_1/encrypted_text.txt", encrypted_text)
        print(encrypted_text, '\n')
        decrypted_text = decode(encrypted_text, alphabet, key)
        write_txt_file("task_1/decrypted_text", decrypted_text)
        print(decrypted_text, '\n')
    except FileNotFoundError as exc:
        print("Error: ", exc)
    except ValueError as exc:
        print("Error: ", exc)
    except Exception as exc:
        print("Error: ", exc)


if __name__ == "__main__":
    main()
