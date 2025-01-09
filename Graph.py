from PriorityQueue import PriorityQueue

class Graph:
    def __init__(self):
        self.vertices = {}
        self.edges = {}
    
    def add_vertex(self, v, pos):
        self.vertices[v] = pos

    def add_edge(self, u, v, w, bi=False):
        self.edges[(u, v, bi)] = w
        if bi:
            self.edges[(v, u, bi)] = w
    
    def dijkstra(self, start, end):
        visited = set()
        distances = {vertex: float('inf') for vertex in self.vertices}
        parents = {}
        pq = PriorityQueue()
        pq.push((0, start))
        parents[start] = None
        distances[start] = 0

        while not pq.isEmpty():
            curr = pq.pop()
            # print(curr)
            if (curr[1] == end):
                break
            if(curr[1] in visited):
                continue

            visited.add(curr[1])
            for (u,v,type), w  in self.edges.items():
                if u == curr[1] and v not in visited:
                    if w + distances[u] < distances[v]:
                        distances[v] = w + distances[u]
                        parents[v] = u
                        pq.push((distances[v], v))
        
        curr = end
        path = []
        while curr is not None:
            path.append(curr)
            curr = parents.get(curr)

        return path[::-1] if distances.get(end) != float('inf') and distances.get(end) != None else []


