import re


def load_data():
    with open('inputs.txt') as file:
        return file.read()

def evaluate_match(match: str):
    data = match.replace('mul(', "").replace(")", "").split(",")
    return int(data[0]) * int(data[1])


def part_1():
    pattern = re.compile(r'mul\(\d+,\d+\)')
    data = load_data()
    matches = re.findall(pattern, data)
    total = 0
    for match in matches:
        total += evaluate_match(match)

    print(total)



def part_2():
    pattern = re.compile(r'mul\(\d+,\d+\)')
    data = load_data()
    ends = []
    idx = 0

    good_ops = []

    position = 0
    while True:
        match = re.search(pattern, data[position:])
        if match is None:
            break

        new_match = position + match.start()
        print(f"{match.start()=}")
        print(f"{new_match=}")

        try:
            last_end = ends[idx - 1]
        except IndexError:
            pass
        else:
            print(f"{last_end=}")
            fail_regex = re.compile(r"don't\(\)(?!do\(\))")
            if (result := fail_regex.search(data[last_end:new_match])) is None:
                good_ops.append(match.group(0))
            else:
                print(f"{result.group(0)=}")

        position += match.end()
        ends.append(position)
        idx += 1

    total = sum([evaluate_match(match) for match in good_ops])
    print(total)

part_2()