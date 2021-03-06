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


def is_multiple_two(array: list[int]) -> list[int]:
    return [x for x in array if x % 2 == 0]


def remove_consecutive_duplicates(s: str) -> str:
    if len(s) == 0:
        return s
    r = [s.split()[0]]
    for i in s.split():
        if i != r[-1]:
            r.append(i)
    return " ".join(r)


def generate_list_numbers(number: int) -> list[int]:
    outpout = []
    for i in range(1, number + 1):
        outpout.append(i)
    return outpout


def is_palindrome(chaine: str):
    try:
        return chaine == "".join(reversed(chaine))
    except TypeError:
        return None


def get_sum_of_digits(num: str):
    try:
        return sum([int(x) for x in list(str(num))])
    except ValueError:
        return None


def duplicate_elements(m: list[int], n: list[int]) -> bool:
    return any(list(map(lambda s: s in n, m)))


def valid_spacing(s: str) -> bool:
    return '' not in s.split(' ')


print(valid_spacing('Hello world'))
