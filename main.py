import pygame
from collections import deque

pygame.init()
MAX_WIDTH = 1000
MAX_HEIGHT = 700
screen = pygame.display.set_mode((MAX_WIDTH, MAX_HEIGHT))
pygame.display.set_caption("Traffic Simulation")
# surface = pygame.Surface((MAX_HEIGHT, MAX_WIDTH))

# colors
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)
GRAY = (180, 180, 180)
BLACK = (0, 0, 0)

# font
font = pygame.font.Font(None, 28)

class PriorityQueue:
    def __init__(self):
        self.arr = []
    
    def push(self, item):
        self.arr.append(item)
        self.arr.sort(reverse=True, key=lambda x: x[0]) # desc

    def pop(self):
        if self.isEmpty():
            return None
        return self.arr.pop()
    
    def isEmpty(self):
        return len(self.arr) == 0

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
            print(curr)
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




# class Vehicle:
#     def __init__(self, color, pos):
#         # self.u = u
#         # self.v = v
#         # self.curr_vertex = u
#         self.color = color
#         self.speed = 0.01
#         self.x = pos[0]
#         self.y = pos[1]


graph = Graph()

# adding vertices
graph.add_vertex('A', (100, 100))
graph.add_vertex('B', (300, 100))
graph.add_vertex('C', (500, 100))
graph.add_vertex('D', (700, 100))
graph.add_vertex('E', (900, 100))
graph.add_vertex('F', (100, 300))
graph.add_vertex('G', (900, 300))
graph.add_vertex('H', (100, 400))
graph.add_vertex('I', (900, 400))
graph.add_vertex('J', (100, 600))
graph.add_vertex('K', (300, 600))
graph.add_vertex('L', (500, 600))
graph.add_vertex('M', (700, 600))
graph.add_vertex('N', (900, 600))

# adding bidirectional edges
graph.add_edge('A', 'B', 1, True)
graph.add_edge('B', 'C', 1, True)
graph.add_edge('C', 'D', 1, True)
graph.add_edge('D', 'E', 1, True)
graph.add_edge('J', 'K', 1, True)
graph.add_edge('K', 'L', 1, True)
graph.add_edge('L', 'M', 1, True)
graph.add_edge('M', 'N', 1, True)
graph.add_edge('A', 'F', 1, True)
graph.add_edge('F', 'A', 1, True)
graph.add_edge('G', 'E', 1, True)
graph.add_edge('E', 'G', 1, True)
graph.add_edge('H', 'J', 1, True)
graph.add_edge('J', 'H', 1, True)
graph.add_edge('I', 'N', 1, True)
graph.add_edge('N', 'I', 1, True)

# adding single direction edges
graph.add_edge('F', 'G', 1, False)
graph.add_edge('I', 'H', 1, False)

print(graph.dijkstra('A', 'Z'))

# screen = pygame.Surface((MAX_WIDTH, MAX_HEIGHT), pygame.SRCALPHA)
# screen.fill(BLACK)

# screen = pygame.Surface((MAX_WIDTH, MAX_HEIGHT),pygame.SRCALPHA)
# screen.fill(BLACK)

# 
u = 'A'
v = 'E'
start_pos = graph.vertices[u]
path = graph.dijkstra(u, v)
i = 1
speed = 0.01
t = 0
# 

# game loop
t=0
clock = pygame.time.Clock()
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # surface.fill((255, 0, 0))
    # screen.blit(surface, (0, 0))


    # drawing vehicles
    if (i < len(path)):
        end_pos = graph.vertices[path[i]]
        x = start_pos[0] + (end_pos[0] - start_pos[0]) * t
        y = start_pos[1] + (end_pos[1] - start_pos[1]) * t

        screen.fill(BLACK)
        pygame.draw.rect(screen, RED, (x-5, y-5, 10, 10))
        
        t += speed
        if (t>=1):
            t = 0
            i += 1
            start_pos = end_pos

        
    # drawing map
    for v, pos in graph.vertices.items():
        pygame.draw.circle(screen, BLUE, pos, 10)
        text_surface = font.render(v, True, WHITE)
        screen.blit(text_surface, (pos[0] + 10, pos[1] + 10))
        
    for (u, v, bi), w in graph.edges.items():
        color = GRAY if bi else GREEN
        pygame.draw.line(screen, color, graph.vertices[u], graph.vertices[v], 2)
        
    # screen.blit(screen, (0, 0))
    # screen.blit(screen, (0, 0))
    pygame.display.update()
    clock.tick(60)

pygame.quit()