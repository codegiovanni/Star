import pygame
import math

pygame.init()

WIDTH = 800
HEIGHT = 800

screen = pygame.display.set_mode((WIDTH, HEIGHT))

black = (0, 0, 0)
yellow = (255, 255, 0)

font = pygame.font.Font('freesansbold.ttf', 50)
character = "*"

x_start = WIDTH // 2
y_start = HEIGHT // 2


def draw_object(a, b, c, d, n, char, scale):
    x_max = math.sqrt(-1 / (b ** 2.0) * math.log(2 * math.e ** (-a ** 2.0) - 1))
    r0 = d * x_max
    r = r0 + 1 / c * math.sqrt(-math.log(
        2 * math.e ** (-a ** 2.0) - math.e ** (-b ** 2 * x_max ** 2 * math.sin(
            (fi - 3 * math.pi / 2) * n / 2) ** 2)))

    x = x_start + r * math.cos(fi) * scale
    y = y_start + r * math.sin(fi) * scale

    text = font.render(str(char), True, yellow)
    screen.blit(text, (x, y))


fi = 0
scale = 300

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_ESCAPE]:
            running = False

    screen.fill(black)

    while fi < math.pi * 2:
        draw_object(a=0.81, b=0.14, c=1, d=0.1, n=5, char=character, scale=100)
        # draw_object(a=0.7, b=0.2, c=0.3, d=1.2, n=5, char=character, scale=20)
        # draw_object(a=0.81, b=0.022, c=1, d=-0.05, n=5, char=character, scale=50)
        # draw_object(a=0.81, b=0.022, c=1, d=0.05, n=5, char=character, scale=50)
        # draw_object(a=0.1, b=1, c=1, d=1, n=5, char=character, scale=1000)

        pygame.time.wait(100)
        pygame.display.update()
        fi += 0.1

pygame.quit()
