import os

if __name__ == '__main__':
    result_p1 = 0
    result_p2 = 0
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
    scores_p2 = {
        # A/X - rock, B/Y - paper, C/Z - scissors
        # Y - draw
        # Z - win
        # X - lose
        ('A', 'X'): 3 + 0,
        ('A', 'Y'): 1 + 3,
        ('A', 'Z'): 2 + 6,

        ('B', 'X'): 1 + 0,
        ('B', 'Y'): 2 + 3,
        ('B', 'Z'): 3 + 6,

        ('C', 'X'): 2 + 0,
        ('C', 'Y'): 3 + 3,
        ('C', 'Z'): 1 + 6,
    }

    with open(os.path.join('..', 'day_2_input.txt'), 'r') as f:
        for line in f:
            theirs, ours = line.strip().split(' ')

            result_p1 += scores[(theirs, ours)]
            result_p2 += scores_p2[(theirs, ours)]

    print(result_p1)
    print(result_p2)

    # First part answer:  9651
    # Second part answer: 10560
