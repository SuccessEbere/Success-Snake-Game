import random
import pygame

pygame.init()

# Screen
WIDTH = 600
HEIGHT = 400

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Success' Snake Game")

clock = pygame.time.Clock()

# Snake settings
BLOCK_SIZE = 5

x = WIDTH // 2
y = HEIGHT // 2

x_change = 0
y_change = 0

snake_list = []
snake_length = 1

# Font
font = pygame.font.SysFont(None, 35)

# Food
while True:
    food_x = random.randrange(0, WIDTH, BLOCK_SIZE)
    food_y = random.randrange(0, HEIGHT, BLOCK_SIZE)
    if [food_x, food_y] not in snake_list:
        break

running = True
game_over = False

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x_change != BLOCK_SIZE:
        x_change = -BLOCK_SIZE
        y_change = 0

    if keys[pygame.K_RIGHT] and x_change != -BLOCK_SIZE:
        x_change = BLOCK_SIZE
        y_change = 0

    if keys[pygame.K_UP] and y_change != BLOCK_SIZE:
        y_change = -BLOCK_SIZE
        x_change = 0

    if keys[pygame.K_DOWN] and y_change != -BLOCK_SIZE:
        y_change = BLOCK_SIZE
        x_change = 0

    # Snake movement
    x += x_change
    y += y_change

    # Screen wrapping
    if x >= WIDTH:
        x = 0
    elif x < 0:
        x = WIDTH - BLOCK_SIZE

    if y >= HEIGHT:
        y = 0
    elif y < 0:
        y = HEIGHT - BLOCK_SIZE

    # Snake head
    snake_head = [x, y]
    snake_list.append(snake_head)

    if len(snake_list) > snake_length:
        del snake_list[0]

    # Self collision
    for segment in snake_list[:-1]:
        if segment == snake_head:
            game_over = True
            running = False

    # Eat food
    if x == food_x and y == food_y:
        snake_length += 1

        while True:
            food_x = random.randrange(0, WIDTH, BLOCK_SIZE)
            food_y = random.randrange(0, HEIGHT, BLOCK_SIZE)

            if [food_x, food_y] not in snake_list:
                break

    screen.fill((0, 0, 0))

    pygame.draw.rect(screen, (255, 0, 0),
                     (food_x, food_y, BLOCK_SIZE, BLOCK_SIZE))

    for block in snake_list:
        pygame.draw.rect(screen, (0, 255, 0),
                         (block[0], block[1], BLOCK_SIZE, BLOCK_SIZE))

    # Score
    score_text = font.render(
        f"Score: {snake_length - 5}", True, (255, 255, 255)
    )
    screen.blit(score_text, (10, 10))

    pygame.display.flip()
    clock.tick(15)

# Game Over Screen
if game_over:
    screen.fill((0, 0, 0))

    game_over_font = pygame.font.SysFont(None, 60)
    score_font = pygame.font.SysFont(None, 40)

    text = game_over_font.render("GAME OVER", True, (255, 0, 0))
    final_score = score_font.render(
        f"Final Score: {snake_length - 5}", True, (255, 255, 255)
    )

    screen.blit(text, (160, 150))
    screen.blit(final_score, (210, 220))

    pygame.display.update()
    pygame.time.delay(3000)

pygame.quit()
