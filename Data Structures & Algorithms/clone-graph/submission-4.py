"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return node
        adj = {}
        seen = set()
        queue = [node]
        while len(queue):
            curr = queue.pop(0)
            print("\nparse:", curr.val)
            # need to parse at least once
            if curr.val in seen:
                print("\t:skipping")
                continue
            seen.add(curr.val)
            # add copy
            if curr.val not in adj:
                adj[curr.val] = Node(val=curr.val)
            # add immediate neighbors
            print("\t:numOfNeighbours:",len(curr.neighbors))
            for neighbor in curr.neighbors:
                print("\t:neighbor:", neighbor.val, end="")
                print(f":Present?<{neighbor.val in adj}>", end="")
                neighbor_node = adj.setdefault(
                                    neighbor.val,
                                    Node(val=neighbor.val))
                print(":fetched:", neighbor_node.val)
                adj[curr.val].neighbors.append(neighbor_node)
                # add for next parse
                queue.append(neighbor)
        return adj[node.val]
