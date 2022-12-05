import os

if __name__ == '__main__':
    result = 0
    result_2 = 0

    with open(os.path.join('..', 'day_4_input.txt'), 'r') as f:
        for line in f:
            line = line.strip()
            pair_1, pair_2 = line.split(',')
            from_1, to_1 = map(int, pair_1.split('-'))
            from_2, to_2 = map(int, pair_2.split('-'))

            if (from_1 >= from_2 and to_1 <= to_2) or (from_2 >= from_1 and to_2 <= to_1):
                result += 1
            if (from_1 >= from_2 and from_1 <= to_2) or (from_2 >= from_1 and from_2 <= to_1):
                result_2 += 1
    print(result)
    print(result_2)

    # First part answer:  453
    # Second part answer: 919
