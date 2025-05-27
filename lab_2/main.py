from files_work.files_work import *
from NIST_tests.NIST_tests import *


def main():
    try:
        path = read_json_file("settings.json")["path"]
        cpp = read_json_file(path)["cpp"]
        java = read_json_file(path)["java"]
        print("cpp: ", cpp)
        print("java: ", java)
        print(bit_frequency_test(cpp))
        print(identical_consecutive_bits_test(cpp))
        print(longest_one_sequence_test(cpp))
        print(bit_frequency_test(java))
        print(identical_consecutive_bits_test(java))
        print(longest_one_sequence_test(java))
    except FileNotFoundError as exc:
        print("Error: ", exc)
    except PermissionError as exc:
        print("Error: ", exc)
    except Exception as exc:
        print("Error: ", exc)


if __name__ == "__main__":
    main()
