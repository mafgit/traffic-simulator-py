import pygame
import pygame_menu
from pygame.locals import *
import pygame_menu.themes
import pygame_menu.widgets
from Graph import Graph
from create_graph import create_graph
from Vehicle import Vehicle
import random

pygame.init()
info = pygame.display.Info()
MAX_WIDTH = info.current_w
MAX_HEIGHT = info.current_h
# MAX_WIDTH = 1000
# MAX_HEIGHT = 700
screen = pygame.display.set_mode((MAX_WIDTH, MAX_HEIGHT), FULLSCREEN)
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
font2 = pygame.font.Font(None, 25)

# creating graph
graph = Graph()
create_graph(graph)

# vehicles
vehicles = []
vehicle_speeds = [0.8, 0.9, 1.0, 1.1, 1.2]
vehicle_colors = [PINK, ORANGE, YELLOW, PURPLE, CYAN, WHITE, GREEN, RED]
vehicle_id = 0
num_vehicles = 30
last_vehicle_id = num_vehicles - 1
for i in range(num_vehicles):
    random_from = graph.get_random_vertex()
    random_to = graph.get_random_vertex()
    random_color = vehicle_colors[random.randint(0, len(vehicle_colors) - 1)]
    random_speed = vehicle_speeds[random.randint(0, len(vehicle_speeds) - 1)]
    vehicles.append(Vehicle(vehicle_id, random_from, random_to, random_color, random_speed, graph))
    vehicle_id += 1

# vehicles = [
#     Vehicle(0, 'LO', 'RE', PINK, graph), 
#     Vehicle(1, 'TP', 'BA', ORANGE, graph), 
#     Vehicle(2, 'RN', 'LM', BLUE, graph), 
#     Vehicle(3, 'BK', 'TL', YELLOW, graph), 
# ]

# pygame-menu
from_input = 'LA'
to_input = 'BC'
color_input = (255, 0, 0)

def from_onchange(x):
    global from_input
    from_input = x
    
def to_onchange(x):
    global to_input
    to_input = x

def color_onchange(x):
    global color_input
    color_input = x

def on_add_vehicle():
    if graph.vertices.get(from_input) is not None and graph.vertices.get(to_input) is not None:
        global last_vehicle_id
        vehicles.append(Vehicle(last_vehicle_id + 1, from_input, to_input, color_input, 1, graph))
        last_vehicle_id += 1

menu = pygame_menu.Menu("", MAX_WIDTH-900, MAX_HEIGHT, theme=pygame_menu.themes.THEME_DARK)
menu.set_absolute_position(900, 0)
# menu.add.label("Press M to toggle map view mode", max_char=-1, font_size=18)
menu.add.label("You can add a vehicle", max_char=-1, font_size=24, margin=(10, 10))
menu.add.text_input("From: ", font_size=18, default="LA", background_color=(50, 50, 50), border_color=(255,255,255), padding=(5, 10), border_width=1,margin=(10,10),onchange=from_onchange)
menu.add.text_input("To: ", font_size=18, default="BC",  background_color=(50, 50, 50), border_color=(255,255,255), padding=(5, 10), border_width=1,margin=(10,10),onchange=to_onchange)
menu.add.color_input("Choose color: ", font_size=18, color_type=pygame_menu.widgets.COLORINPUT_TYPE_RGB, default=(255,0,0), background_color=(50, 50, 50), border_color=(255,255,255), margin=(10,10),padding=(5, 10), border_width=1, onchange=color_onchange)
menu.add.button("Click to Add Vehicle", on_add_vehicle, font_size=18, selection_color=(20,20,20), background_color=(255, 255, 255), padding=(10, 20), font_color=(20, 20, 20),margin=(10,10))



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

def coords_are_equal(a, b):
    return abs(a[0] - b[0]) <= 1e-5 and abs(a[1] - b[1]) <= 1e-5

# textures
main_road_img_width = 20
service_road_img_width = 12
main_road_img = pygame.image.load('textures/main-road-no-outline.jpg')
main_road_img = pygame.transform.scale(main_road_img, (main_road_img_width, main_road_img_width))
service_road_img = pygame.image.load('textures/service-road-no-outline.jpg')
service_road_img = pygame.transform.scale(service_road_img, (service_road_img_width, service_road_img_width))

# game loop
clock = pygame.time.Clock()
show_lines = False
run = True
while run:
    bg_color = BLACK if show_lines else DARK_GREEN # can be taken out of loop for performance, but will need to change bgcolor separately on clicking M
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_m:
                show_lines = not show_lines

    screen.fill(bg_color)
        
    # drawing edges
    for (u, v), edge in graph.edges.items():
        if show_lines:
            if len(edge['traffic']) >= edge['max_traffic']:
                color = RED
            else:
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
            is_main_road = not graph.edges[(u, v)]['bi']
            which_img = main_road_img if is_main_road else service_road_img
            which_img_width = main_road_img_width if is_main_road else service_road_img_width
            img_pos = (upos[0]-which_img_width/2,upos[1]-which_img_width/2)
            horizontal = upos[1] - vpos[1] == 0 and upos[0] - vpos[0] != 0
            if horizontal:
                img = pygame.transform.rotate(which_img, -90)
                img = pygame.transform.scale(img, (abs(vpos[0] - upos[0]) + which_img_width, which_img_width))
                to_left = vpos[0] - upos[0] < 0
                if to_left:
                    img_pos = (img_pos[0] - abs(vpos[0] - upos[0]), img_pos[1])
            else:
                img = pygame.transform.rotate(which_img, 0)
                img = pygame.transform.scale(img, (which_img_width,abs(vpos[1] - upos[1]) + which_img_width))
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

    text_surface = font2.render("Press M to toggle map view", True, WHITE)
    screen.blit(text_surface, (550, 680))

    # drawing vehicles
    for vehicle in vehicles:
        if (vehicle.i < len(vehicle.path)):
            # stop vehicle if at traffic signal stopping vertex
            if is_stopping_vertex(vehicle.path[vehicle.i - 1]):
                vehicle.speed = 0
            else:
                vehicle.speed = 1

            start_vertex = vehicle.path[vehicle.i-1]
            end_vertex = vehicle.path[vehicle.i]
            vehicle.end_pos = graph.vertices[end_vertex]['pos']
            edge = (start_vertex, end_vertex)
            coords = (vehicle.x, vehicle.y)

            # enter edge if at start of edge
            if coords_are_equal(coords, graph.vertices[start_vertex]['pos']):
                graph.edges[edge]['traffic'].add(vehicle.id)

            # exit edge
            # if coords_are_equal(coords, graph.vertices[end_vertex]['pos']):
            #     pass

            # if (vehicle.id == 0):
                # print(start_vertex, end_vertex)
                # print(coords, graph.vertices[end_vertex]['pos'], coords_are_equal(coords, graph.vertices[end_vertex]['pos']))
                # pass
            
            edge_dist = graph.edges[edge]['dist']
            # linear interpolation formula to calculate new x and y positions of vehicle:
            vehicle.x = vehicle.start_pos[0] + (vehicle.end_pos[0] - vehicle.start_pos[0]) * (vehicle.t / edge_dist)
            vehicle.y = vehicle.start_pos[1] + (vehicle.end_pos[1] - vehicle.start_pos[1]) * (vehicle.t / edge_dist)
            # ratio = vehicle.t / edge_dist
            # vehicle.t means distance travelled by vehicle  

            vehicle.t += vehicle.speed
            if (vehicle.t>=edge_dist):
                graph.edges[edge]['traffic'].remove(vehicle.id)

                # graph.exit_edge(vehicle.path[vehicle.i-1], vehicle.path[vehicle.i], vehicle.id)
                vehicle.t = 0
                vehicle.i += 1
                vehicle.start_pos = vehicle.end_pos
            
            # print(len(graph.edges[('LO', 'LG')]['traffic']))
        else:
            pass
            # remove vehicle from vehicles (also remove them from the edge they are in)
            # graph.edges[(vehicle.path[vehicle.i - 2], vehicle.path[vehicle.i-1])]['traffic'].remove(vehicle.id)
            # index = 0
            # for i, v in enumerate(vehicles):
            #     if v.id == vehicle.id:
            #         index = i
            # vehicles.pop(index)

        pygame.draw.rect(screen, vehicle.color, (vehicle.x-5, vehicle.y-5, 10, 10))
        
    # updating traffic light
    traffic_t += traffic_speed
    if traffic_t >= 1:
        traffic_t = 0
        traffic_i += 1
        if traffic_i > 3:
            traffic_i = 0

    # pygame-menu
    if menu.is_enabled():
        menu.update(events)
        menu.draw(screen)

    pygame.display.update() # or flip()
    clock.tick(60) # 60 fps

pygame.quit()