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
DARK_GREEN = (3, 163, 41)
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

# creating graph
graph = Graph()
create_graph(graph)

# vehicles
vehicles = [
    Vehicle(0, 'LO', 'RE', PINK, graph), 
    Vehicle(1, 'TP', 'BA', ORANGE, graph), 
    Vehicle(2, 'RN', 'LM', BLUE, graph), 
    Vehicle(3, 'BK', 'TL', YELLOW, graph), 
]

# traffic
traffic_signals = ['ITL', 'ITR', 'IBR', 'IBL']
stopping_vertices = ['LG', 'TH', 'RH', 'BG']
traffic_i = 0
traffic_t = 0
traffic_speed = 0.0035

def is_stopping_vertex(u):
    for i in range(len(traffic_signals)):
        if i != traffic_i:
            if u == stopping_vertices[i]:
                return True

    return False

img_width = 20
road_img = pygame.image.load('textures/road.jpg')
road_img = pygame.transform.scale(road_img, (img_width, img_width))

# game loop
clock = pygame.time.Clock()
show_lines = False
run = True
while run:
    bg_color = BLACK if show_lines else DARK_GREEN # can be taken out of loop for performance, but will need to change bgcolor separately on clicking M

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_m:
                show_lines = not show_lines

    screen.fill(bg_color)
        
    # drawing edges
    for (u, v), edge in graph.edges.items():
        if show_lines:
            color = GRAY if edge['bi'] else GREEN
            pygame.draw.line(screen, color, graph.vertices[u]['pos'], graph.vertices[v]['pos'], 2)
        else:
            # problems with drawing roads:
            # edge b/w 2 points: [ .-]-----[-. ]
            # some area is left on right and left side, so I must add `img_width` to the length of road
            # and I should translate the road a little to the left
            # another problem: if my road is going from right to left (v <-- u):
            # the image will still be drawn from `u` but to the right side of u,
            # so I need to translate it back by the length of the whole road

            upos = graph.vertices.get(u)['pos'] 
            vpos = graph.vertices.get(v)['pos'] 

            # repeating img
            # horizontal = upos[1] - vpos[1] == 0 and upos[0] - vpos[0] != 0
            # road_length = abs(upos[0] - vpos[0]) if horizontal else abs(upos[1] - vpos[1])
            # img_count = int(road_length) // int(img_width)
            # # remainder = road_length - img_count * int(img_width)
            # if horizontal:
            #     img = pygame.transform.rotate(road_img, -90)
            # else:
            #     img = road_img

            # startpos = upos
            # for i in range(img_count):
            #     screen.blit(img, (startpos[0] - img_width/2, startpos[1] - img_width/2))
            #     if horizontal:
            #         startpos = (startpos[0] + img_width, startpos[1])
            #     else:
            #         startpos = (startpos[0], startpos[1] + img_width)

            # scaling img
            img_pos = (upos[0]-img_width/2,upos[1]-img_width/2)
            horizontal = upos[1] - vpos[1] == 0 and upos[0] - vpos[0] != 0
            if horizontal:
                img = pygame.transform.rotate(road_img, -90)
                img = pygame.transform.scale(img, (abs(vpos[0] - upos[0]) + img_width, img_width))
                to_left = vpos[0] - upos[0] < 0
                if to_left:
                    img_pos = (img_pos[0] - abs(vpos[0] - upos[0]), img_pos[1])
            else:
                img = pygame.transform.rotate(road_img, 0)
                img = pygame.transform.scale(img, (img_width,abs(vpos[1] - upos[1]) + img_width))
                to_top = vpos[1] - upos[1] < 0
                if to_top:
                    img_pos = (img_pos[0], img_pos[1] - abs(vpos[1] - upos[1]))
            
            screen.blit(img, img_pos)


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
            # stop vehicle if at traffic signal stopping vertex
            if is_stopping_vertex(vehicle.path[vehicle.i - 1]):
                vehicle.speed = 0
            else:
                vehicle.speed = 0.01

            vehicle.end_pos = graph.vertices[vehicle.path[vehicle.i]]['pos']
            # graph.enter_edge(vehicle.path[vehicle.i-1], vehicle.path[vehicle.i], vehicle.id)
            

            # linear interpolation
            vehicle.x = vehicle.start_pos[0] + (vehicle.end_pos[0] - vehicle.start_pos[0]) * vehicle.t
            vehicle.y = vehicle.start_pos[1] + (vehicle.end_pos[1] - vehicle.start_pos[1]) * vehicle.t

            vehicle.t += vehicle.speed
            if (vehicle.t>=1):
                # graph.exit_edge(vehicle.path[vehicle.i-1], vehicle.path[vehicle.i], vehicle.id)
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