import copy
import multiprocessing
import sys
from typing import Dict, List, Set



with open('/home/ubuntu/projects/advent-of-code/2022/16/input.test') as f:
    valves:Dict[str,int] = dict()
    graph:Dict[str,List[str]] = dict()
    for line in f.readlines():
        line = line.split('; ') #Valve AA has flow rate=0
        name, rate = line[0].split(' ')[1], line[0].split('=')[-1]
        valves[name] = int(rate)
        tunnels = ''.join(line[1].strip().split(' ')[4:]).split(',')  #tunnels lead to valves DD, II, BB
        graph[name] = tunnels
'''
    Shameleslly stolen from https://www.geeksforgeeks.org/find-paths-given-source-destination/
'''
paths:List[List[str]] = []
def addAllPathsUtil(u:str, d:str, visited:Dict[str,bool], path:List[str], explored:Dict[str, Set[str]]):
    # Mark the current node as visited and store in path
    visited[u]= True
    path.append(u)

    # If current vertex is same as destination, then print
    # current path[]
    if u == d:
        path.reverse()
        paths.append(copy.deepcopy(path))
        path.reverse()
    else:
    # If current vertex is not destination
    # Recur for all the vertices adjacent to this vertex
        for i in graph[u]:
            if i not in explored[u]:
                explored[u].add(i)
                addAllPathsUtil(i, d, visited, path, explored)

    # Remove current vertex from path[] and mark it as unvisited
    path.pop()
    visited[u]= False


# Prints all paths from 's' to 'd'
def addAllPaths(graph:Dict[str, List[str]]):
    # Mark all the vertices as not visited
    visited = {}
    explored = {}
    for k in graph.keys():
        visited[k] = False
        explored[k] = set()

    # Create an array to store paths
    path = []

    # Call the recursive helper function to print all paths
    addAllPathsUtil(path)

for k in graph.keys():
    if k == 'AA': continue
    addAllPaths('AA', k, graph)

def tryPathUtil(path:List[str], flow:int, minutes:int, openValves:Set[str], flowRate:int) -> int:
    if len(path) == 0:
        if minutes >= 30: return flow;
        else:
            timeLeft = 30 - minutes
            return flow + flowRate * timeLeft
    node = path.pop()
    minutes += 1 #travel time
    flow += flowRate
    if minutes >= 30: return flow;
    if node not in openValves and valves[node] > 0:
        closedFlow = tryPathUtil(path, flow, minutes, openValves, flowRate)
        minutes += 1
        flow += flowRate
        if minutes >= 30: return flow
        flowRate += valves[node]
        openValves.add(node)
        openFlow = tryPathUtil(path, flow, minutes, openValves, flowRate)
        return max(openFlow, closedFlow)
    else:
        return tryPathUtil(path, flow, minutes, openValves, flowRate)

def tryPath(path:List[str]):
    minutes = 0
    flow = 0
    flowRate = 0
    openValves = set()
    return tryPathUtil(path[0:-1], flow, minutes, openValves, flowRate)

pool = multiprocessing.Pool(processes=4)
flow = 0
plen = len(paths)
# for i, r in enumerate(pool.imap_unordered(tryPath, paths)):
#     flow = max(r,flow)
#     sys.stderr.write('\rdone {0:%}'.format(i/plen))
print()
print(flow)