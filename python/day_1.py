import os

if __name__ == '__main__':
    result = 0
    with open(os.path.join('..', 'day_1_input.txt'), 'r') as f:
        elves_cal = []
        current_elf_cal = 0
        for line in f:
            if not line.strip():
                elves_cal.append(current_elf_cal)
                current_elf_cal = 0
                continue
            current_elf_cal += int(line)

    print(max(elves_cal))
    print(sum(sorted(elves_cal)[-3:]))

    # First part answer:  70613
    # Second part answer: 205805
