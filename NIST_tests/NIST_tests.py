import math


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
    return math.erfc(s / math.sqrt(2))


