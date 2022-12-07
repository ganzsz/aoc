from pprint import pprint
from filesystem import FileSystem


s = FileSystem()

# s.addFolder([], 'test')
# s.addFolder(['test'], '1')
# s.addFolder(['test'], '22')
# s.addFile(['test', '1'], '2', 8)
# s.addFile(['test'], 'f', 80)
# s.addFile([], 'GROOT', 888)
# print(s.root)

with open('/home/chiron/personal/advent-of-code/2022/07/realinput') as f:
  state = "idk"
  path = []
  for line in f.readlines():
    line = line.strip().split()
    if line[0] == '$':
      state = line[1]
      if state == 'cd':
        goto = line[2]
        if goto == '/':path = []
        elif goto == '..':path = path[0:-1]
        else: path.append(goto)
      continue

    if state == 'ls':
      if line[0] == 'dir':
        s.addFolder(path, line[1])
      else:
        s.addFile(path, line[1], int(line[0]))

  print(s.root)
  print(sum(s.dirsUnderSize.values()))
  pprint(s.dirsUnderSize)