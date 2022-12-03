import os

if __name__ == '__main__':
    result = 0

    with open(os.path.join('..', 'day_3_input.txt'), 'r') as f:
        for line in f:
            line = line.strip()
            backpack_size = len(line) // 2
            backpack = {}
            for c in line[:backpack_size]:
                backpack[c] = True
            for c in line[backpack_size:]:
                if c in backpack:
                    # Found duplicate
                    score = 0
                    if c.islower():
                        score = ord(c) - 96
                    else:
                        score = ord(c) - 65 + 27
                    print(f'Dup is {c} ({score})')
                    result += score
                    break

    print(result)

    # First part answer:  7875
    # Second part answer:
