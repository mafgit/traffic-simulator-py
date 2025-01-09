import pygame
from Graph import Graph
from create_graph import create_graph
from Vehicle import Vehicle

pygame.init()
MAX_WIDTH = 1000
MAX_HEIGHT = 700
screen = pygame.display.set_mode((MAX_WIDTH, MAX_HEIGHT))
pygame.display.set_caption("Traffic Simulation")

# colors
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)
GRAY = (184, 184, 184)
BLACK = (0, 0, 0)
ORANGE = (255, 165, 0)
PINK = (255, 20, 147)
PURPLE = (128, 0, 128)
YELLOW = (255, 255, 0)

# font
font = pygame.font.Font(None, 28)


graph = Graph()
create_graph(graph)



vehicles = [
    Vehicle('A', 'B', 0.01, PURPLE, graph), 
    Vehicle('J', 'N', 0.01, ORANGE, graph), 
    Vehicle('H', 'I', 0.01, PINK, graph), 
    Vehicle('F', 'G', 0.01, YELLOW, graph), 
    Vehicle('A', 'F', 0.01, RED, graph), 
    Vehicle('G', 'E', 0.01, GREEN, graph), 
    Vehicle('H', 'J', 0.01, BLUE, graph), 
    Vehicle('I', 'N', 0.01, WHITE, graph),
]

# game loop
clock = pygame.time.Clock()
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    screen.fill(BLACK)
        
    # drawing map
    for (u, v, bi), w in graph.edges.items():
        color = GRAY if bi else GREEN
        pygame.draw.line(screen, color, graph.vertices[u], graph.vertices[v], 30)
    
    for v, pos in graph.vertices.items():
        pygame.draw.rect(screen, BLUE, (pos[0]-15, pos[1]-15, 30, 30))
        text_surface = font.render(v, True, WHITE)
        screen.blit(text_surface, (pos[0]-7.5, pos[1]-7.5))


    # drawing vehicles
    for vehicle in vehicles:
        if (vehicle.i < len(vehicle.path)):
            vehicle.end_pos = graph.vertices[vehicle.path[vehicle.i]]
            vehicle.x = vehicle.start_pos[0] + (vehicle.end_pos[0] - vehicle.start_pos[0]) * vehicle.t
            vehicle.y = vehicle.start_pos[1] + (vehicle.end_pos[1] - vehicle.start_pos[1]) * vehicle.t

            vehicle.t += vehicle.speed
            if (vehicle.t>=1):
                vehicle.t = 0
                vehicle.i += 1
                vehicle.start_pos = vehicle.end_pos
            
        pygame.draw.rect(screen, vehicle.color, (vehicle.x-5, vehicle.y-5, 10, 10))
        
        
    pygame.display.update()
    clock.tick(60)

pygame.quit()