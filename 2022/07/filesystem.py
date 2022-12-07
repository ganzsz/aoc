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

  def _toOneLine(self, index=0):
    return ('  '*index) + ' - ' + self.name + ' (' + self.type + ', size=' + str(self.size)+')\n'

  def print(self, index=0) -> str:
    if(self.type == 'dir'):
      ret = self._toOneLine(index)
      for f in self.cont.values():
        ret = ret + f.print(index+1)
      return ret
    else:
      return self._toOneLine(index)
  
  def __repr__(self) -> str:
    return self.print()


def getDir(dir:File, path:str) -> Dir:
  return dir.cont[path]

class FileSystem:
  root:File = File('/', 0, "dir", dict())

  '''
    This one is only for day1 puzzle 1
  '''
  dirsUnderSize:Dict[str, int] = dict()

  def _curDir(self, path:Path) -> File:
    if(len(path) == 0):
      return self.root
    else:
      return reduce(getDir, path, self.root)

  def _addInPath(self, path:Path, file:File):
    curDir = self._curDir(path)
    curDir.cont[file.name] = file
  
  def _updateDirSizes(self, path:Path):
    for i in range(len(path), -1, -1):
      p = path[0:i]
      curDir = self._curDir(p)
      curDir.size = 0
      for f in curDir.cont.values():
        curDir.size += f.size
      '''
        Follwoing is fo rday 1
      '''
      cdPath = '/'.join(p)
      self.dirsUnderSize[cdPath] = curDir.size
      if curDir.size > 100000:
        self.dirsUnderSize.pop(cdPath)

  def addFile(self, path:Path, name:str, size:int):
    self._addInPath(path, File(name, size, "file"))
    self._updateDirSizes(path)

  def addFolder(self, path:Path, name:str):
    self._addInPath(path, File(name, 0, "dir", dict()))