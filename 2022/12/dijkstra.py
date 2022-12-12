from pprint import pprint


finity = 9999
multiplicationFactor = 1000

def printGrid(dists):
    grid = [[]]
    i = -1
    for k, v in dists.items():
        if k%multiplicationFactor == 0:
            grid.append([])
            i+=1
        grid[i].append(v)
    for k,i in enumerate(grid):
        print('\n ROW',k)
        print(i)

# Dijkstra algorithm, returns the next step to reach a goal
def dijkstra(nodes, start, goal): # Electric boogaloo
    dists = {}
    prevs = {}
    Q = {}

    if goal is start:
        return start

    # fill a list with the nodes so we can clear nodes out of this list w/o damaging the original nodes
    for node in nodes.values():
        dists[node.id] = finity*finity
        Q[node.id] = node
    dists[start.id] = 0

    # Algorithm loop, as long as there are nodes keep testing them
    startlen = len(Q)
    while Q:
        # print(round(100-(len(Q)/startlen)*100,2),'%')
        current = False
        # Find node with shortest distance
        for i in Q:
            if not current or dists[i] < dists[current.id]:
                current = Q[i]
        
        Q.pop(current.id, False)

        # If we reached the goal return the first step to reach the goal
        if current is goal:
            # printGrid(dists)
            return dists[goal.id]
        #     last = prevs[current.id]
        #     while last is not start:
        #         current = last
        #         last = prevs[last.id]
            
        #     return current

        # Update distance list for all nodes adjacent to current nodes
        for link in current.links:
            if link.node.id in Q:
                alt = dists[current.id] + link.dist
                if alt < dists[link.node.id]:
                    dists[link.node.id] = alt
                    prevs[link.node.id] = current
    raise LookupError(Text="Could not find dest in nodes")


# Node for Dijkstra, links to other nodes so we can recursively find a path
class Node:
    def __init__(self, id):
        self.id = id
        self.dist = float("inf")
        self.links = []

    # Bidirectional link to another node
    def linkTo(self, node, dist):
        self.links.append(Link(node, dist))
        node.links.append(Link(self, dist))

    # Easier printing
    def __repr__(self) -> str:
        return "Node (" + str(self.id) + ")"

# Link class for nodes
class Link:
    def __init__(self, node, dist):
        self.node = node
        self.dist = dist
    
    def __repr__(self) -> str:
        return "LinkTo (" + str(self.node) + ")"