from files_work import *
from task_1.encoder import *
from task_2.decoder import decoder, char_frequency


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

        text2 = read_txt_file("task_2/cod13.txt")
        print(text2, '\n')
        decrypted_text2 = decoder(text2)

        #print(char_frequency(text2))
        #print(read_json_file("task_2/settings.json")["frequency"])
        write_txt_file("task_2/decrypted_text2.txt", decrypted_text2)
        print(decrypted_text2)
    except FileNotFoundError as exc:
        print("Error: ", exc)
    except ValueError as exc:
        print("Error: ", exc)
    except Exception as exc:
        print("Error: ", exc)


if __name__ == "__main__":
    main()
