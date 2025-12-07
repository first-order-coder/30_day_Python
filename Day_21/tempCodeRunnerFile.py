import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Set up display
width, height = 640, 480
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

# Colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

# Snake
snake_size = 20
snake_speed = 15
snake = [(width // 2, height // 2)]
snake_direction = (1, 0)

# Food
food_size = 20
food = (random.randrange(1, (width // food_size)) * food_size,
        random.randrange(1, (height // food_size)) * food_size)

# Score
score = 0

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake_direction != (0, 1):
                snake_direction = (0, -1)
            elif event.key == pygame.K_DOWN and snake_direction != (0, -1):
                snake_direction = (0, 1)
            elif event.key == pygame.K_LEFT and snake_direction != (1, 0):
                snake_direction = (-1, 0)
            elif event.key == pygame.K_RIGHT and snake_direction != (-1, 0):
                snake_direction = (1, 0)

    # Move the snake
    x, y = snake[0]
    x += snake_direction[0] * snake_size
    y += snake_direction[1] * snake_size

    # Check for collisions with walls or itself
    if x < 0 or x >= width or y < 0 or y >= height or (x, y) in snake[1:]:
        pygame.quit()
        sys.exit()

    # Check for collision with food
    if x == food[0] and y == food[1]:
        score += 1
        food = (random.randrange(1, (width // food_size)) * food_size,
                random.randrange(1, (height // food_size)) * food_size)
    else:
        snake.pop()

    # Update snake position
    snake.insert(0, (x, y))

    # Draw everything
    screen.fill(black)

    # Draw snake
    for segment in snake:
        pygame.draw.rect(screen, white, (segment[0], segment[1], snake_size, snake_size))

    # Draw food
    pygame.draw.rect(screen, red, (food[0], food[1], food_size, food_size))

    # Draw score
    font = pygame.font.SysFont(None, 25)
    score_text = font.render(f"Score: {score}", True, white)
    screen.blit(score_text, (10, 10))

    pygame.display.update()

    # Control the snake's speed
    pygame.time.Clock().tick(snake_speed)

import random
min = 1
max = 10

for _ in range(5):
    print(random.randint(min, max))