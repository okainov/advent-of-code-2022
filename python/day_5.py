import os
import re


def process_command(stacks, command):
    if not command:
        return
    print(f'Command: {command}')
    print(stacks)
    number, move_from, move_to = map(int, re.findall('\d+', command))
    move_to -= 1
    move_from -= 1
    elems_to_add = []
    for i in range(number):
        elems_to_add.append(stacks[move_from].pop())
    # Remove 'reversed' for part 1
    stacks[move_to].extend(reversed(elems_to_add))
    print('Stacks after move')
    print(stacks)


if __name__ == '__main__':
    stacks = [[]]

    with open(os.path.join('..', 'day_5_input.txt'), 'r') as f:
        for line in f:
            line = line.strip('\n')
            if not line:
                continue
            line_items = line.split(' ')
            if 'move' in line:
                process_command(stacks, line)
                continue
            elif '[' not in line:
                # Finish reading stacks: just number in line
                # Revert all stacks
                for i in range(len(stacks)):
                    stacks[i] = list(reversed(stacks[i]))
                continue
            i = 0
            current_stack = 0
            while i < len(line_items):
                if not line_items[i]:
                    # Empty element, do not add anything and skip 4 chars [A]<space>
                    i += 4
                else:
                    # Add element to current stack
                    stacks[current_stack].append(line_items[i].strip('[]'))
                    i += 1
                current_stack += 1
                if len(stacks) <= current_stack:
                    stacks.append([])

    result = ''
    for stack in stacks:
        if not stack:
            continue
        result += stack[-1]
    print(result)

    # First part answer:  ZSQVCCJLL
    # Second part answer: QZFJRWHGS
