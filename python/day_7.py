import os


def resolve_dirs(dirs, dir_to_resolve):
    for i in range(len(dirs[dir_to_resolve])):
        if isinstance(dirs[dir_to_resolve][i], str) and not dirs[dir_to_resolve][i].isnumeric():
            dirs[dir_to_resolve][i] = resolve_dirs(dirs, dirs[dir_to_resolve][i])
    return sum(dirs[dir_to_resolve])


if __name__ == '__main__':
    current_dir = []
    dirs = {}
    with open(os.path.join('..', 'day_7_input.txt'), 'r') as f:
        for line in f:
            if line.startswith('$'):
                if 'ls' in line:
                    print('ls')
                elif 'cd' in line:
                    _, _, param = line.split(' ')
                    param = param.strip()
                    print(f'CD\'ing to: {param}')
                    if param == '..':
                        current_dir.pop()
                    elif param == '/':
                        current_dir = ['']
                    else:
                        current_dir.append(param)
                    print(f'CD\'d to: {"/".join(current_dir)}')
            else:
                # Shall be `ls` output
                type_or_size, name = line.split(' ')
                name = name.strip()
                current = "/".join(current_dir)
                if current not in dirs:
                    dirs[current] = []
                if type_or_size != 'dir':
                    # Size
                    dirs[current].append(int(type_or_size))
                else:
                    dirs[current].append(current + f'/{name}')

    # Resolve nested dirs as we have collected all the data
    resolve_dirs(dirs, '')

    result = 0
    for dir, sizes in dirs.items():
        if sum(sizes) < 100000:
            result += sum(sizes)

    print(dirs)
    print(result)

    # First part answer: 1648397
    # Second part answer:
