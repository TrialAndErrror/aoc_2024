#!/usr/bin/env python3
import collections

def read_data():
    left_data = list()
    right_data = list()

    with open("day1_p1.txt", "r") as file:
        data = file.readlines()

    all_entries = [item.strip().split("   ") for item in data]
    for entry in all_entries:
        left_data.append(int(entry[0]))
        right_data.append(int(entry[1]))


    return left_data, right_data


def part_one():
        left_data, right_data = read_data()
        all_data = list(zip(sorted(left_data), sorted(right_data)))
        all_distances = [abs(entry[1] - entry[0]) for entry in all_data]
        print(sum(all_distances))


def part_two():
        left_data, right_data = read_data()
        right_counter = collections.Counter(right_data)
        score = sum(
            [
                (item * right_counter[item])
                for item in left_data
            ]
        )
        print(score)

part_two()
