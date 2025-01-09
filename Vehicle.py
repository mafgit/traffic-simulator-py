class Vehicle:
    def __init__(self, u, v, speed, color, graph):
        self.u = u
        self.v = v
        self.start_pos = graph.vertices[u]['pos']
        self.end_pos = graph.vertices[v]['pos']
        self.path = graph.dijkstra(u, v)
        self.i = 1
        self.t = 0
        self.speed = speed
        self.color = color