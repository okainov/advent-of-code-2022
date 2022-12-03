import os


def get_priority(c):
    if c.islower():
        return ord(c) - 96
    else:
        return ord(c) - 65 + 27


if __name__ == '__main__':
    result = 0
    result_2 = 0

    with open(os.path.join('..', 'day_3_input.txt'), 'r') as f:
        group_items = {}
        for i, line in enumerate(f):
            line = line.strip()

            for c in set(line):
                if c not in group_items:
                    group_items[c] = 0
                group_items[c] += 1
            if i % 3 == 2:
                # Find common item: the one with counter 3
                for key, value in group_items.items():
                    if value == 3:
                        result_2 += get_priority(key)
                # End of line, cleanup
                group_items = {}

            backpack_size = len(line) // 2
            backpack = {}
            for c in line[:backpack_size]:
                backpack[c] = True
            for c in line[backpack_size:]:
                if c in backpack:
                    # Found duplicate
                    score = get_priority(c)
                    # print(f'Dup is {c} ({score})')
                    result += score
                    break

    print(result)
    print(result_2)

    # First part answer:  7875
    # Second part answer: 2479
