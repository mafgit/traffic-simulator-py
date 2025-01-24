class Vehicle:
    def __init__(self, id, u, v, color, speed, graph):
        self.id = id
        self.u = u
        self.v = v
        self.start_pos = graph.vertices[u]['pos']
        self.end_pos = graph.vertices[v]['pos']
        self.path = graph.dijkstra(u, v)
        self.i = 1
        self.t = 0
        self.speed = speed
        self.color = color
        self.x = 0
        self.y = 0