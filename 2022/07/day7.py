from pprint import pprint
from filesystem import FileSystem


s = FileSystem()

s.addFolder([], 'test')
s.addFolder(['test'], '1')
s.addFolder(['test'], '22')
s.addFile(['test', '1'], '2', 8)
s.addFile(['test'], 'f', 80)
s.addFile([], 'GROOT', 888)
print(s.root)
