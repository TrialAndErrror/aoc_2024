import re


def load_data():
    with open('inputs.txt') as file:
        return file.read()


def part_1():
    pattern = re.compile(r'mul\(\d+,\d+\)')
    data = load_data()
    matches = re.findall(pattern, data)
    total = 0
    for match in matches:
        data = match.replace('mul(', "").replace(")", "").split(",")
        total += int(data[0]) * int(data[1])

    print(total)



def part_2():
    pattern = re.compile(r'mul\(\d+,\d+\)')
    data = load_data()
    position = 0
    while True:
        match = re.search(pattern, data[position:])
        if match is None:
            break

        print(match.start() + position)
        print(match.end() + position)

        position += match.end()

part_2()