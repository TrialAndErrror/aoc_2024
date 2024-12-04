
def report_is_safe(entry: list):
    # Unsafe if not sorted
    if sorted(entry) != entry and sorted(entry, reverse=True) != entry:
        return False

    # Unsafe if difference between two values is more than 2
    idx = 1
    while idx < len(entry):
        change = abs(entry[idx] - entry[idx - 1])
        if change > 3 or change < 1:
            return False
        idx += 1

    return True

def part_1():
    all_data = []
    with open('inputs.txt') as file:
        for line in file.readlines():
            data = line.strip().split(' ')
            all_data.append([int(item) for item in data])


    safe_entries = 0
    for idx, item in enumerate(all_data):
        result = report_is_safe(item)
        print(f"{idx}: {result} [{item}]")
        if result:
            safe_entries += 1

    return safe_entries


def part_2():
    all_data = []
    with open('inputs.txt') as file:
        for line in file.readlines():
            data = line.strip().split(' ')
            all_data.append([int(item) for item in data])


    safe_entries = 0
    for idx, item in enumerate(all_data):
        result = report_is_safe(item)
        print(f"{idx}: {result} [{item}]")
        if result:
            safe_entries += 1
        else:
            for option in range(len(item)):
                new_item = item.copy()
                new_item.pop(option)
                result = report_is_safe(new_item)
                print(f"{idx} (option {option}: {result} [{new_item}]")
                if result:
                    safe_entries += 1
                    break

    return safe_entries


print(part_2())