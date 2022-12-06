import os

if __name__ == '__main__':
    with open(os.path.join('..', 'day_6_input.txt'), 'r') as f:
        for line in f:
            stack = []
            for i, c in enumerate(line, start=1):
                # Remove first char
                if len(stack) == 4:
                    stack = stack[1:]
                stack.append(c)
                if len(stack) == len(set(stack)) and len(stack) == 4:
                    print(i)
                    break


    # First part answer: 1578
    # Second part answer:
