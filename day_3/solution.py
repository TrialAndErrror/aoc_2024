import re
from bisect import bisect_left


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

    multiply_matches = [
        (match.start(), match.group(0)) for match in re.finditer(pattern, data)
    ]

    dont_matches = [
        match.start() for match in re.finditer(r"don't\(\)", data)
    ]

    do_matches = [
        match.start() for match in re.finditer(r"do\(\)", data)
    ]

    print(multiply_matches)
    good_matches = []
    for start, match in multiply_matches:
        highest_dont = bisect_left(dont_matches, start) - 1
        highest_do = bisect_left(do_matches, start) - 1

        if do_matches[highest_do] > dont_matches[highest_dont]:
            good_matches.append(match)


    total = sum([evaluate_match(match) for match in good_matches])
    print(total)

part_2()