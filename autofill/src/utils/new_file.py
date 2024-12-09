import os
from api import get_input

CWD = os.getcwd();

with open('YEAR') as f:
    YEAR = f.read().strip()

try:
    os.listdir("../").index(YEAR)
except:
    os.mkdir(f"../{YEAR}")

l = os.walk(os.path.join(CWD, '../', YEAR)).__next__()[1]
l = list(filter(lambda x: "__" not in x in x, l))
l = list(l)
n = int(sorted(l)[-1][:2]) + 1 if len(l) > 0 else 1

try:
    os.mkdir(f"../{YEAR}")
except: pass

realInput = get_input(n,YEAR)

try:
    os.mkdir(f"../{YEAR}/{n:02d}")
except: pass

templatePath = os.listdir(os.path.join(CWD, "template"))[0]
with open(os.path.join(CWD, "template", templatePath)) as f:
    template = f.read();
templateExt = templatePath.split('.')[-1];

directory = f"../{YEAR}/{n:02d}/"
path = f"{directory}index.php"
with open(path, "w") as f:
    f.write(template)

with open(directory+"input.test", "w") as f:
    f.write("")

with open(directory+"input.real", 'w')as f:
    f.write(realInput)


print(f"Enter your solution in {path}")
