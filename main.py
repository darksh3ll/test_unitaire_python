def adition(a: int, b: int) -> int:
    """

    :param a: numbers
    :type a: int
    :param b: numbers
    :type b: int
    :return: int
    :rtype:
    """
    return a + b


def invert_chaine(chaine: str) -> str:
    """

    :param chaine: str
    :type chaine:
    :return: str
    :rtype:
    """
    return "".join(reversed(chaine)).capitalize()


def is_multiple_two(array: list) -> list:
    """

    :param array: list number
    :type array: list
    :return: list
    :rtype:
    """
    return [x for x in array if x % 2 == 0]


def remove_consecutive_duplicates(s: str) -> str:
    if len(s) == 0:
        return s
    r = [s.split()[0]]
    for i in s.split():
        if i != r[-1]:
            r.append(i)
    return " ".join(r)
