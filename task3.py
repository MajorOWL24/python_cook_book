from operator import itemgetter
import os

def combine(files, filename):
    all_lines = []
    for file in files:
        file_lines = [os.path.basename(file)]
        lines = []
        for line in open(file, encoding='utf-8'):
            lines.append(line[:-1])
        file_lines.append(str(len(lines)))
        file_lines.extend(lines)
        all_lines.append(file_lines)

    f = open(filename, 'w', encoding='utf-8')
    for lines in sorted(all_lines, key=itemgetter(1)):
        for line in lines:
            f.write(line + '\r\n')

files = [
    'sorted/1.txt',
    'sorted/2.txt',
    'sorted/3.txt'
]
combine(files, 'sorted/output.txt')
