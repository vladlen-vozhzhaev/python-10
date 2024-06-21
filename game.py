import sys
import pygame

pygame.init()
screen = pygame.display.set_mode((1600, 900))
plane = pygame.image.load("img/plane.png")
plane = pygame.transform.scale(plane, (200, 75))
clock = pygame.time.Clock()
plane_x = 0
plane_y = 20
plane_velocity = 1
up = False
pitch = 0
def draw_img(image, x, y, angle):
    rotated_image = pygame.transform.rotate(image, angle)
    screen.blit(rotated_image, rotated_image.get_rect(center=image.get_rect(topleft=(x, y)).center).topleft)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill((0, 0, 0))
    pygame.draw.line(screen, (0, 255, 0), [0, 400], [1600, 400])
    pygame.draw.line(screen, (0, 255, 0), [900, 380], [900, 420])
    if plane_y != 400-75 and not up:
        plane_y += 1
    elif plane_velocity > 0 and not up:
        plane_velocity -= 0.002
    elif plane_velocity <= 0 and not up:
        up = True
    if up:
        plane_velocity += 0.002
    if plane_x != 900 - 200:
        plane_x += plane_velocity
    if plane_velocity >= 1 and up:
        plane_y -= 1
        if pitch < 20:
            pitch += 0.2
            draw_img(plane, plane_x, plane_y, pitch)
        else:
            draw_img(plane, plane_x, plane_y, pitch)
    else:
        screen.blit(plane, (plane_x, plane_y))

    pygame.display.flip()
    clock.tick(60)