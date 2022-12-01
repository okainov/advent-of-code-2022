import os

if __name__ == '__main__':
    result = 0
    with open(os.path.join('..', 'day_1_input.txt'), 'r') as f:
        current_elf_cal = 0
        max_cal = 0
        for line in f:
            if not line.strip():
                if max_cal < current_elf_cal:
                    max_cal = current_elf_cal
                current_elf_cal = 0
                continue
            current_elf_cal += int(line)

    print(max_cal)

    # First part answer:  70613
    # Second part answer:
