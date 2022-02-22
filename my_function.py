def del_empty(num, last, first, datenais, level, note):
    if (
        num != ""
        or last != ""
        or first != ""
        or datenais != ""
        or level != ""
        or note != ""
    ):
        del (num, last, first, datenais, level, note)
        return True
    else:
        return False


def num_validation(num):
    if (
        len(num) == 7
        and num.isupper()
        and num.isalnum()
        and not num.isalpha()
        and not num.isdigit()
    ):
        return True
    else:
        return False


def name_validation(lastname, firstname):
    if (
        len(lastname) >= 2
        and lastname[0].isalpha()
        and len(firstname) >= 3
        and firstname[0].isalpha()
    ):
        return True
    else:
        return False


def level_validation(level):
    if level[1: len(level)] == "emA" or level[1 : len(level)] == "emB":
        return True
    else:
        return False


#
