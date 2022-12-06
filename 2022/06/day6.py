def findDupes(b):
    seen = set()
    seen_dupe = set()
    for x in b:
        if x in seen and x not in seen_dupe:
            seen_dupe.add(x)
        else:
            seen.add(x)
    return list(seen_dupe)



with open('/home/chiron/personal/advent-of-code/2022/06/realinput') as f:
  stream = f.read().strip()
  buf = []
  for i in range(0, len(stream)):
    c = stream[i]
    buf.append(stream[i])
    if len(buf) > 14:
      del buf[0:-14]
    if len(buf) < 14: continue
    
    dupes = findDupes(buf)
    if len(dupes)==0:
      print(i+1)
      break