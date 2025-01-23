def basic_op(o, v1, v2):
    if o == "+":
        return v1 + v2
    elif o == "-":
        return v1 - v2
    elif o == "*":
        return v1 * v2
    else:
        return v1 / v2


def string_to_number(s):
    return int(s)


def bool_to_word(boolean):
    # TODO
    if boolean:
        return "Yes"
    else:
        return "No"