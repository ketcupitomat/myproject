import pygame
import sys
from ball import Ball

pygame.init()

WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Moving Ball")

clock = pygame.time.Clock()

# создаём шар
ball = Ball(
    x=WIDTH // 2,
    y=HEIGHT // 2,
    radius=25,
    screen_width=WIDTH,
    screen_height=HEIGHT
)

running = True
while running:
    screen.fill((255, 255, 255))  # белый фон

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                ball.move_left()

            elif event.key == pygame.K_RIGHT:
                ball.move_right()

            elif event.key == pygame.K_UP:
                ball.move_up()

            elif event.key == pygame.K_DOWN:
                ball.move_down()

    # рисуем шар
    pygame.draw.circle(screen, (255, 0, 0), (ball.x, ball.y), ball.radius)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()