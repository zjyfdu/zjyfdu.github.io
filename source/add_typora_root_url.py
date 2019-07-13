
import os

path_root = './_posts/'
files = os.listdir(path_root)
files = [path_root + x for x in files if x.endswith('.md')]
insert_line = 'typora-root-url: ../../source'

for file in files:
    with open(file) as f:
        lines = f.readlines()

    if any([insert_line in x for x in lines]):
        continue

    lines.insert(2, insert_line + '\n')
    with open(file, 'w') as f:
        f.writelines(lines)
