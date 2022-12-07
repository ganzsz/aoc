from typing import Any, Union
from __future__ import annotations

Dict = type(dict(str,'File'))
class File:
  name:str
  size:int
  type:str
  content:Union[Dict, str]

class FileSystem:
  root:Dict = {}