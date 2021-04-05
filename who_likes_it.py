def likes(names):
    """"Solution see https://www.codewars.com/kata/5266876b8f4bf2da9b000362/solutions/python/all/best_practices"""
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


if __name__ == "__main__":
    ppls = ["Marc", "Benoit", "Camille", "Jean", "Louise"]
    who_likes(ppls)
