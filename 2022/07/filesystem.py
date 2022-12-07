from __future__ import annotations
from functools import reduce
import operator
import pprint
from typing import Dict, List, Union

Dir = Dict[str, "File"]
Path = List[str]
Content = Union[Dir, str]
class File:
  name:str
  size:int
  type:str
  cont:Content

  def __init__(self, name:str, size:int, type:str, cont:Content = None) -> None:
    self.name = name
    self.size = size
    self.type = type
    self.cont = cont
    pass

  def print(self, index=0) -> str:
    if(self.type == 'dir'):
      ret = ('  '*index) + ' - ' + self.name + ' (dir)'+'\n'
      for f in self.cont.values():
        ret = ret + f.print(index+1)
      return ret
    else:
      return ('  '*index) + ' - ' + self.name + ' (' + self.type + ', size=' + str(self.size)+')\n'
  
  def __repr__(self) -> str:
    return self.print()


def getDir(dir:File, path:str) -> Dir:
  return dir.cont[path]

class FileSystem:
  root:File = File('/', 0, "dir", dict())

  def _addInPath(self, path:Path, file:File) -> bool:
    if(len(path) == 0):
      curDir = self.root
    else:
      curDir = reduce(getDir, path, self.root)
    curDir.cont[file.name] = file
    pass

  def addFile(self, path:Path, name:str, size:int) -> bool:
    self._addInPath(path, File(name, size, "file"))
    pass

  def addFolder(self, path:Path, name:str) -> bool:
    self._addInPath(path, File(name, 0, "dir", dict()))
    pass