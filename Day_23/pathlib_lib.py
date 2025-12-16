from pathlib import Path
p = Path('/Users/ginuram/Desktop/Dekstop/30DAYSOFPYTHON/MINI_PROJECTS/to_do_CLI')
files = p.rglob('*.py')

# for subdir in p.iterdir():
#     print(subdir)

# for f in files:
#     print(f)

with (p / 'storage.py').open('r') as f: #'w' will overwrite anything on the file
    content = f.read()
    print(content)
