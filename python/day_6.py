import os

if __name__ == '__main__':
    LENGTH = 14 # Set 4 for part 1
    with open(os.path.join('..', 'day_6_input.txt'), 'r') as f:
        for line in f:
            stack = []
            for i, c in enumerate(line, start=1):
                # Remove first char
                if len(stack) == LENGTH:
                    stack = stack[1:]
                stack.append(c)
                if len(stack) == len(set(stack)) and len(stack) == LENGTH:
                    print(i)
                    break

    # First part answer: 1578
    # Second part answer: 2178
