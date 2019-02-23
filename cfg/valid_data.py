import re


def valid_mail(mail: str) -> bool:
    expr = re.compile("^[A-Z0-9._%+-]+@[A-Z]{3,8}.+.[A-Z]{2,4}$", re.IGNORECASE)
    result = expr.match(mail)

    if result is None: return False
    if result.string != mail: return False
    return True


def valid_username(un: str) -> bool:
    expr = re.compile("^[A-Z]+[0-9]*$", re.IGNORECASE)
    result = expr.match(un)

    print(result)

    if result is None: return False
    if result.string != un: return False
    return True


def valid_pair(en: str, ru: str) -> bool:
    expr_en = re.compile("^[A-Z]+$", re.IGNORECASE)
    expr_ru = re.compile("^[А-ЯЁ]+$", re.IGNORECASE)

    result1 = expr_en.match(en)
    result2 = expr_ru.match(ru)

    if result1 is None or result2 is None: return False
    if result1.string != en or result2.string != ru: return False
    return True


if __name__ == '__main__':
    print(valid_pair('вфы', 'dasd'))
    print(valid_pair('afsf', 'вфывф'))
    print(valid_pair('1213', '4214'))
    print(valid_pair('в.ф.ю.ы', 'd!asd'))
    print(valid_pair('dsada', 'dasd'))
