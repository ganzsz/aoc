import os
from api import get_input

with open('YEAR') as f:
    YEAR = f.read().strip()

try:
    os.listdir("../").index(YEAR)
except:
    os.mkdir(f"../{YEAR}")

l = list(filter(lambda x: "__" not in x in x, os.listdir(f"../{YEAR}")))
l = list(l)
n = int(sorted(l)[-1][:2]) + 1 if len(l) > 0 else 1

DEFAULT_FILE = f"with open('') as f:\n    "

try:
    os.mkdir(f"../{YEAR}")
except: pass

realInput = get_input(n,YEAR)

try:
    os.mkdir(f"../{YEAR}/{n:02d}")
except: pass

directory = f"../{YEAR}/{n:02d}/"
path = f"{directory}day{n}.py"
with open(path, "w") as f:
    f.write(DEFAULT_FILE)

with open(directory+"input.test", "w") as f:
    f.write("")

with open(directory+"input.real", 'w')as f:
    f.write(realInput)


print(f"Enter your solution in {path}")
