from ast import Raise


def count_bits(n):
    # see https://www.codewars.com/kata/526571aae218b8ee490006f4/train/python

    n = str(int(bin(n)[2:]))
    bits = 0

    for char in n:
        if char == "1":
            bits += 1

    return bits


def likes(names):
    """Solution see https://www.codewars.com/kata/5266876b8f4bf2da9b000362/solutions/python/all/best_practices"""
    n = len(names)
    return {
        0: "no one likes this",
        1: "{} likes this",
        2: "{} and {} like this",
        3: "{}, {} and {} like this",
        4: "{}, {} and {others} others like this",
    }[min(4, n)].format(*names[:3], others=n - 2)


def who_likes(ppl_who_liked_array):
    msg = ""
    size_arr = len(ppl_who_liked_array)

    if size_arr == 0:
        msg = "No one likes this"
        return msg

    if size_arr >= 1:
        if size_arr == 1:
            msg = f"{ppl_who_liked_array[0]} likes this"
            return msg

        if size_arr == 2:
            msg = f"{ppl_who_liked_array[0]} and {ppl_who_liked_array[1]} like this"
            return msg

        if size_arr == 3:
            # using enumerate to get the index too
            for index, people in enumerate(ppl_who_liked_array):
                if index == 2:
                    msg += " and "

                msg += f"{people}"

                if index == 0 and index <= 1:
                    msg += ", "

            msg += " like this"
            return msg

        if size_arr >= 4:
            first_two_ppl = ppl_who_liked_array[:2]
            rest_ppl = len(ppl_who_liked_array[2:])

            for index, people in enumerate(first_two_ppl):
                msg += f"{people}"

                if index == 0 and index <= 1:
                    msg += ", "

            return msg + f" and {rest_ppl} others like this"


def tower_builder():
    # see https://www.codewars.com/kata/576757b1df89ecf5bd00073b/train/python

    n_floors = 10
    blocks = []

    for i in range(n_floors):
        blocks.append("*")

    print(blocks)


def str_to_hash(st):
    # see https://www.codewars.com/kata/52180ce6f626d55cf8000071
    if len(st) != 0:
        st = st.split(", ")
        splitted = []
        dic = {}

        for s in st:
            splitted.append(s.split("="))

        for spli in splitted:
            dic[spli[0]] = int(spli[1])

        return dic

    return {}


def deadfish_parser(command: str):
    """
    https://www.codewars.com/kata/51e0007c1f9378fa810002a9

    Write a simple parser that will parse and run Deadfish.
    Deadfish has 4 commands, each 1 character long:

    i increments the value (initially 0)
    d decrements the value
    s squares the value
    o outputs the value into the return array

    ex: parse("iiisdoso")  ==>  [8, 64]
    """
    valid_commands = ["i", "d", "s", "o"]
    values = []
    init_value = 0

    for char in command:
        if char in valid_commands:
            if char == "i":
                init_value += 1

            if char == "d":
                init_value -= 1

            if char == "s":
                init_value = init_value**2

            if char == "o":
                values.append(init_value)

        else:
            raise Exception("Invalid command.")

    return values
