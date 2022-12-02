import os

if __name__ == '__main__':
    result = 0
    scores = {
        # A/X - rock, B/Y - paper, C/Z - scissors
        ('A', 'X'): 1 + 3,
        ('A', 'Y'): 2 + 6,
        ('A', 'Z'): 3 + 0,

        ('B', 'X'): 1 + 0,
        ('B', 'Y'): 2 + 3,
        ('B', 'Z'): 3 + 6,

        ('C', 'X'): 1 + 6,
        ('C', 'Y'): 2 + 0,
        ('C', 'Z'): 3 + 3,
    }
    with open(os.path.join('..', 'day_2_input.txt'), 'r') as f:
        for line in f:
            theirs, ours = line.strip().split(' ')
            result += scores[(theirs, ours)]

    print(result)

    # First part answer:  9651
    # Second part answer:
