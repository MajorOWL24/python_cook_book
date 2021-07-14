def combine(files, filename):
    all_lines = []
    for file in files:
        all_lines.append(file)

        count = 0
        lines = []
        for line in open(file, encoding='utf-8'):
            lines.append(line[:-1])

        all_lines.append(str(len(lines)))
        for line in lines:
            all_lines.append(line)

    f = open(filename, 'w', encoding='utf-8')
    for line in all_lines:
        f.write(line + '\r\n')

files = [
    'sorted/1.txt',
    'sorted/2.txt',
    'sorted/3.txt'
]
combine(files, 'sorted/output.txt')
