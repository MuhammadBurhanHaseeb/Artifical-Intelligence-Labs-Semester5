class AdjNode:
    def __init__(self, value):
        self.vertex = value
        self.next = None

class Graph:
    def __init__(self, num):
        self.V = num
        self.graph = [None] * self.V

    def add_edge(self, s, d):
        node = AdjNode(d)
        node.next = self.graph[s]
        self.graph[s] = node

        node = AdjNode(s)
        node.next = self.graph[d]
        self.graph[d] = node

    def getConnectedNodes(self, node):
        connected_nodes = []
        temp = self.graph[node]
        while temp:
            connected_nodes.append(temp.vertex)
            temp = temp.next
        return connected_nodes

    def getEdge(self, node1, node2):
        temp = self.graph[node1]
        while temp:
            if temp.vertex == node2:
                return node2
            temp = temp.next
        temp = self.graph[node2]
        while temp:
            if temp.vertex == node1:
                return node1
            temp = temp.next

        return None

    def areConnected(self, node1, node2):
        temp = self.graph[node1]
        while temp:
            if temp.vertex == node2:
                return True
            temp = temp.next
        return False

    def isValidPath(self, path):
        for i in range(len(path) - 1):
            if not self.areConnected(path[i], path[i + 1]):
                return False
        return True


if __name__ == "__main__":
    V = 5

    graph = Graph(V)
    graph.add_edge(0, 1)
    graph.add_edge(0, 2)
    graph.add_edge(0, 3)
    graph.add_edge(1, 2)

    print("Connected nodes of node 0:", graph.getConnectedNodes(0))
    print("Edge between nodes 0 and 1:", graph.getEdge(0, 1))
    print("Are nodes 1 and 3 connected?", graph.areConnected(1, 3))
    print("Is [0, 1, 2] a valid path?", graph.isValidPath([0, 1, 2]))


