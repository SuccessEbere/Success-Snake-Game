import random
import pygame

pygame.init()

screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Success' Snake Game")

clock = pygame.time.Clock()

x = 300
y = 200

x_change = 0
y_change = 0

snake_list = []
snake_length = 5

food_x = random.randrange(0, 600, 20)
food_y = random.randrange(0, 400, 20)

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        x_change = -5
        y_change = 0

    if keys[pygame.K_RIGHT]:
        x_change = 5
        y_change = 0

    if keys[pygame.K_UP]:
        y_change = -5
        x_change = 0

    if keys[pygame.K_DOWN]:
        y_change = 5
        x_change = 0

    x += x_change
    y += y_change

    if x >= 600:
        x = 0
    elif x < 0:
        x = 580

    if y >= 400:
        y = 0
    elif y < 0:
        y = 380

    snake_head = [] 
    snake_head.append(x)
    snake_head.append(y)

    snake_list.append(snake_head)

    if len(snake_list) > snake_length:
        del snake_list[0] 

    if x == food_x and y == food_y:
        food_x = random.randrange(0, 600, 20)
        food_y = random.randrange(0, 400, 20)

        snake_length += 1

    screen.fill((0, 0, 0))

    for block in snake_list:
        pygame.draw.rect(screen, (0, 255, 0), (block[0], block[1], 20, 20))         
   
    pygame.display.flip()
    clock.tick(15)

pygame.quit()