import pygame
from pygame.locals import *
from Graph import Graph
from create_graph import create_graph
from Vehicle import Vehicle

pygame.init()
MAX_WIDTH = 1000
MAX_HEIGHT = 700
screen = pygame.display.set_mode((MAX_WIDTH, MAX_HEIGHT), RESIZABLE)
pygame.display.set_caption("Traffic Simulation")
# pygame.display.toggle_fullscreen()

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
CYAN = (0, 125, 255)

# font
font = pygame.font.Font(None, 15)


graph = Graph()
create_graph(graph)



vehicles = [
    Vehicle('LA', 'RN', 0.01, PINK, graph), 
    Vehicle('TE', 'BJ', 0.01, ORANGE, graph), 
    # Vehicle('LH', 'LI', 0.01, PINK, graph), 
    # Vehicle('LF', 'LG', 0.01, YELLOW, graph), 
    # Vehicle('LA', 'LF', 0.01, PINK, graph), 
    # Vehicle('LG', 'LE', 0.01, ORANGE, graph), 
    # Vehicle('LH', 'LJ', 0.01, YELLOW, graph), 
    # Vehicle('LI', 'LN', 0.01, PINK, graph),
]

traffic_signals = ['ITL', 'ITR', 'IBR', 'IBL']
traffic_i = 0
traffic_t = 0
traffic_speed = 0.005

# game loop
clock = pygame.time.Clock()
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    screen.fill(BLACK)
        
    # drawing edges
    for (u, v), edge in graph.edges.items():
        color = GRAY if edge['bi'] else GREEN
        pygame.draw.line(screen, color, graph.vertices[u]['pos'], graph.vertices[v]['pos'], 2)
    
    # drawing vertices
    for v, vertex in graph.vertices.items():
        color = CYAN
        if vertex['type'] == 'intersection':
            if traffic_signals[traffic_i] == v:
                color = GREEN
            else:
                color = RED

        pygame.draw.circle(screen, color, (vertex['pos'][0], vertex['pos'][1]), 3)
        text_surface = font.render(v, True, WHITE)
        screen.blit(text_surface, (vertex['pos'][0]+2, vertex['pos'][1] + 2))


    # drawing vehicles
    for vehicle in vehicles:
        if (vehicle.i < len(vehicle.path)):
            vehicle.end_pos = graph.vertices[vehicle.path[vehicle.i]]['pos']
            vehicle.x = vehicle.start_pos[0] + (vehicle.end_pos[0] - vehicle.start_pos[0]) * vehicle.t
            vehicle.y = vehicle.start_pos[1] + (vehicle.end_pos[1] - vehicle.start_pos[1]) * vehicle.t

            vehicle.t += vehicle.speed
            if (vehicle.t>=1):
                vehicle.t = 0
                vehicle.i += 1
                vehicle.start_pos = vehicle.end_pos
            
        pygame.draw.rect(screen, vehicle.color, (vehicle.x-5, vehicle.y-5, 10, 10))
        
    # updating traffic light
    traffic_t += traffic_speed
    if traffic_t >= 1:
        traffic_t = 0
        traffic_i += 1
        if traffic_i > 3:
            traffic_i = 0

    pygame.display.update()
    clock.tick(60)

pygame.quit()