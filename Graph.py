from PriorityQueue import PriorityQueue
import random

class Graph:
    def __init__(self):
        self.vertices = {}
        self.edges = {}
    
    def add_vertex(self, v, pos, type='point'):
        self.vertices[v] = {'pos':(100 + pos[0]/3, pos[1]/3 + 300), 'type':type}
        # self.vertices[v] = {'pos':((pos[0]*0.5-0), (pos[1]*0.5-0)), 'type':type}

    def get_random_vertex(self):
        vertex_names = list(self.vertices.keys())
        random_index = random.randint(0, len(vertex_names) - 1)
        return vertex_names[random_index]

    def add_edge(self, u, v, max_traffic=3, bi=False):
        upos = self.vertices[u]['pos']
        vpos = self.vertices[v]['pos']
        horizontal = int(upos[1]) - int(vpos[1]) == 0 and int(upos[0]) - int(vpos[0]) != 0
        dist = 0
        if horizontal:
            dist = abs(upos[0] - vpos[0])
        else:
            dist = abs(upos[1] - vpos[1])

        # if u == 'LG' and v == 'ITL':
        #     print(dist)
        edge = {'bi':bi, 'max_traffic':max_traffic, 'traffic':set(), 'dist': dist}
        self.edges[(u, v)] = edge
        if bi:
            self.edges[(v, u)] = edge

    def dijkstra(self, start, end):
        visited = set()
        # distances = {vertex: float('inf') for vertex in self.vertices}
        weights = {vertex: float('inf') for vertex in self.vertices}
        # weight = dist * alpha + traffic * beta
        parents = {}
        pq = PriorityQueue()
        pq.push((0, start))
        parents[start] = None
        weights[start] = 0

        alpha = 1 # weight unit for dist
        beta = 1 # weight unit for traffic

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
                    traffic = len(edge['traffic']) - edge['max_traffic'] # traffic = how many cars to remove to get a vacant space for a vehicle inside an edge
                    if traffic < 0:
                        traffic = 0
                    elif traffic == 0: # if equal
                        traffic = 1
                    weight = edge['dist'] * alpha + traffic * beta

                    if weight + weights[u] < weights[v]:
                        weights[v] = edge['dist'] + weights[u]
                        parents[v] = u
                        pq.push((weights[v], v))
        
        curr = end
        path = []
        while curr is not None:
            path.append(curr)
            curr = parents.get(curr)

        return path[::-1] if weights.get(end) != float('inf') and weights.get(end) != None else []
    