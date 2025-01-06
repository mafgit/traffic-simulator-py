import pygame

pygame.init()
MAX_HEIGHT = 1000
MAX_WIDTH = 800
screen = pygame.display.set_mode((MAX_HEIGHT, MAX_WIDTH), pygame.FULLSCREEN)
pygame.display.set_caption("Traffic Simulation")
# surface = pygame.Surface((MAX_HEIGHT, MAX_WIDTH))


vertices = {
    'A': (100,100),
    'B': (300,100),
    'C': (500,100),
    'D': (700,100),
    'E': (900,100),

    'F': (100,300),
    'G': (900,300),

    'H': (100,400),
    'I': (900,400),

    'J': (100, 600),
    'K': (300,600),
    'L': (500,600),
    'M': (700,600),
    'N': (900,600),
}

edges = {
    ('A', 'B', True): 1,
    ('B', 'A', True): 1,

    ('B', 'C', True): 1,
    ('C', 'B', True): 1,

    ('C', 'D', True): 1,
    ('D', 'C', True): 1,

    ('D', 'E', True): 1,
    ('E', 'D', True): 1,

    # ...

    ('J', 'K', True): 1,
    ('K', 'J', True): 1,

    ('K', 'L', True): 1,
    ('L', 'K', True): 1,

    ('L', 'M', True): 1,
    ('M', 'L', True): 1,

    ('M', 'N', True): 1,
    ('N', 'M', True): 1,

    # ...

    ('F','G', False):1,
    ('I','H', False):1,

    # ...

    ('A','F', True):1,
    ('F','A', True):1,

    ('G','E', True):1,
    ('E','G', True):1,

    ('H','J', True):1,
    ('J','H', True):1,

    ('I','N', True):1,
    ('N','I', True):1,
}

def add_edge(u, v, w, bi=False):
    edges[(u, v, type)] = w
    if bi:
        edges[(v, u, type)] = w

RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)
GRAY = (180, 180, 180)

font = pygame.font.Font(None, 28)

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # surface.fill((255, 0, 0))
    # screen.blit(surface, (0, 0))

    # drawing map
    for v, pos in vertices.items():
        pygame.draw.circle(screen, BLUE, pos, 10)
        text_surface = font.render(v, True, WHITE)
        screen.blit(text_surface, (pos[0] + 10, pos[1] + 10))
        

    for (u, v, bi), w in edges.items():
        color = GRAY if bi else GREEN
        pygame.draw.line(screen, color, vertices[u], vertices[v], 2)
        
    pygame.display.update()

pygame.quit()