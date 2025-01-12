from PriorityQueue import PriorityQueue

class Graph:
    def __init__(self):
        self.vertices = {}
        self.edges = {}
    
    def add_vertex(self, v, pos, type='point'):
        self.vertices[v] = {'pos':(100 + pos[0]/3, pos[1]/3 + 250), 'type':type}

    def add_edge(self, u, v, dist=1, max_traffic = 5, bi=False):
        edge = {'bi':bi, 'max_traffic':max_traffic, 'traffic':set(), 'dist':dist}
        self.edges[(u, v)] = edge
        if bi:
            self.edges[(v, u)] = edge
    
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
            for (u,v), edge  in self.edges.items():
                if u == curr[1] and v not in visited:
                    if edge['dist'] + distances[u] < distances[v]:
                        distances[v] = edge['dist'] + distances[u]
                        parents[v] = u
                        pq.push((distances[v], v))
        
        curr = end
        path = []
        while curr is not None:
            path.append(curr)
            curr = parents.get(curr)

        return path[::-1] if distances.get(end) != float('inf') and distances.get(end) != None else []

    def enter_edge(self, u, v, id):
        if self.edges.get((u, v)) is None:
            print((u, v))
            return
        if id not in self.edges[(u, v)]['traffic']:
            self.edges[(u, v)]['traffic'].add(id)

    def exit_edge(self, u, v, id):
        if self.edges.get((u, v)) is None:
            return
        if id in self.edges[(u, v)]['traffic']:
            self.edges[(u, v)]['traffic'].remove(id)

