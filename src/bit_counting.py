# see https://www.codewars.com/kata/526571aae218b8ee490006f4/train/python


def count_bits(n):
    n = str(int(bin(n)[2:]))
    bits = 0

    for char in n:
        if char == "1":
            bits += 1

    return bits


if __name__ == "__main__":
    count_bits(4)
