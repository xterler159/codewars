# see https://www.codewars.com/kata/576757b1df89ecf5bd00073b/train/python


def tower_builder():
    n_floors = 10
    blocks = []

    for i in range(n_floors):
        blocks.append("*")

    print(blocks)


if __name__ == "__main__":
    tower_builder()
