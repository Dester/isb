import math
from scipy.special import gammainc
from files_work.files_work import read_json_file


def bit_frequency_test(sequence: str) -> float:
    """
    Производит частотный побитовый анализ бинарной последовательности
    :param sequence: бинарная последовательность
    :return: P-значение последовательности
    """
    n = len(sequence)
    s = 0
    for i in sequence:
        match i:
            case "1":
                s += 1
            case "0":
                s -= 1
    s /= math.sqrt(n)
    return math.erfc(abs(s / math.sqrt(2)))


def identical_consecutive_bits_test(sequence: str) -> float:
    """
    Производит анализ бинарной последовательности на одинаковые подряд идущие биты
    :param sequence: бинарная последовательность
    :return: P-значение последовательности
    """
    n = len(sequence)
    s = 0
    for i in sequence:
        s += int(i)
    s /= n
    if not abs(s - 0.5) < 2 / math.sqrt(n):
        return 0
    v = 0
    for i in range(0, n-1):
        if sequence[i] != sequence[i+1]:
            v += 1
    return math.erfc(abs(v - 2 * n * s * (1 - s)) / (2 * math.sqrt(2 * n) * s * (1 - s)))


def longest_one_sequence_test(sequence: str) -> float:
    """
    Производит анализ бинарной последовательности на максимальную длину подряд идущих единиц
    :param sequence: бинарная последовательность
    :return: P-значение последовательности
    """
    p = read_json_file("NIST_tests/settings.json")["pi"]
    block_length = read_json_file("NIST_tests/settings.json")["block_length"]
    v = [0, 0, 0, 0]
    n = len(sequence)
    for i in range(0, n, block_length):
        max_length = 0
        current_length = 0
        for j in sequence[i: i + block_length]:
            if j:
                current_length += 1
                max_length = max(current_length, max_length)
            else:
                current_length = 0
        match max_length:
            case 0:
                v[0] += 1
            case 1:
                v[0] += 1
            case 2:
                v[1] += 1
            case 3:
                v[2] += 1
            case _:
                v[3] += 1
    x = 0
    for i in range(0, 4):
        x += (v[i] - 16 * p[i]) ** 2 / (16 * p[i])
    return gammainc(3 / 2, x / 2)
