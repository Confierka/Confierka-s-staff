import pygame
import random

BACKGROUND_COLOR = (255, 255, 255)
OBJECT_COLOR = (0, 0, 255)
WIDTH, HEIGHT = 1000, 1000

FPS = 60
FRAMETIME = 1 / FPS

def lerp(p, q, x):
    return (q-p)*x+p

class PhysicalObject:
    def __init__(self, x, y, vx, vy, radius, color=OBJECT_COLOR):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.radius = radius
        self.color = color

        self.prev = [(x, y)]

    def move_tail(self):
        self.prev.append((self.x, self.y))
        if len(self.prev) > 50:
            self.prev.pop(0)

    def move_bounce(self, width, height):
        if self.x - self.radius < 0:
            self.x += 2*(self.radius-self.x)
            self.vx = abs(self.vx)

        if self.x + self.radius > width:
            self.x -= 2*(self.x+self.radius- width)
            self.vx = -abs(self.vx)

        if self.y-self.radius < 0:
            self.y += 2*(self.radius - self.y)
            self.vy = abs(self.vy)

        if self.y+self.radius > height:
            self.y -= 2*(self.y + self.radius - height)
            self.vy = -abs(self.vy)

    def move_gravity(self):
        cx = WIDTH // 2
        cy = WIDTH // 2

        dx, dy = cx-self.x, cy-self.y

        d = (dx**2+dy**2)**0.5
        dx /= d
        dy /= d

        acc = 25 * 100000 / d ** 2
        dx *= acc
        dy *= acc

        self.vx += dx * FRAMETIME
        self.vy += dy * FRAMETIME

    def move_phisics(self):
        self.x += self.vx * FRAMETIME
        self.y += self.vy * FRAMETIME


    def move(self, width, height):
        self.move_gravity()
        self.move_phisics()
        self.move_bounce(width, height)
        self.move_tail() 

    def draw(self, screen):
        for i in range(len(self.prev) - 1):
            t = i / (len(self.prev) - 1)

            r = lerp(255,   255,    t)
            g = lerp(255,   0,      t)
            b = lerp(255,   0,      t)

            pygame.draw.line(screen, (r, g, b), self.prev[i], self.prev[i+1])
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)


pygame.init()
radius = 3
cx, cy = WIDTH//2, HEIGHT//2

screen = pygame.display.set_mode(size=(WIDTH, HEIGHT), vsync=1)
pygame.display.set_caption('cde')
A = []

# A.append(PhysicalObject(100, 100, 500, 0, radius))

def draw_rect(start, end, color):
    x_min, x_max = min(start[0], end[0]), max(start[0], end[0])
    y_min, y_max = min(start[1], end[1]), max(start[1], end[1])
    
    for x in range(x_min, x_max + 1):
        for y in range(y_min, y_max + 1):
            screen.set_at((x, y), color)
            
            
x, y = 0, 0

screen.fill(BACKGROUND_COLOR)
clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    for i in range(len(A)):
        A[i].move(WIDTH, HEIGHT)

    screen.fill(BACKGROUND_COLOR)

    draw_rect((x, y), (x + 800, y + 800), (0, 255, 0))
    
    x += 3
    y += 3

    for i in range(len(A)):
        A[i].draw(screen)
    pygame.display.flip()

    clock.tick(FPS)

