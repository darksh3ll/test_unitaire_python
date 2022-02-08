def adition(a: int, b: int) -> int:
    return a + b


def invert_chaine(chaine: str) -> str:
    return "".join(reversed(chaine)).capitalize()


print(invert_chaine("abc"))
