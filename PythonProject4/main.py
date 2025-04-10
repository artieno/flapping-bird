import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 400, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Bird")

# Colors
WHITE = (255, 255, 255)
BLUE = (135, 206, 250)
GREEN = (0, 200, 0)

# Game variables
gravity = 0.35
bird_movement = -6
score = 0
font = pygame.font.SysFont(None, 40)

# Load bird
bird = pygame.Rect(50, 300, 30, 30)

# Pipe variables
pipe_width = 70
pipe_gap = 150
pipe_velocity = 3
pipes = []

def create_pipe():
    height = random.randint(150, 400)
    top_pipe = pygame.Rect(WIDTH, 0, pipe_width, height - pipe_gap // 2)
    bottom_pipe = pygame.Rect(WIDTH, height + pipe_gap // 2, pipe_width, HEIGHT)
    return top_pipe, bottom_pipe

# Initial pipe
pipes.extend(create_pipe())

clock = pygame.time.Clock()

# Game loop
running = True
while running:
    clock.tick(60)
    screen.fill(BLUE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Flap
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird_movement = -8

    # Bird movement
    bird_movement += gravity
    bird.y += int(bird_movement)

    # Pipe movement
    for pipe in pipes:
        pipe.x -= pipe_velocity

    # Remove off-screen pipes
    if pipes[0].x + pipe_width < 0:
        pipes.pop(0)
        pipes.pop(0)
        score += 1
        pipes.extend(create_pipe())

    # Collision detection
    for pipe in pipes:
        if bird.colliderect(pipe):
            running = False

    if bird.top <= 0 or bird.bottom >= HEIGHT:
        running = False

    # Draw bird
    pygame.draw.ellipse(screen, WHITE, bird)

    # Draw pipes
    for pipe in pipes:
        pygame.draw.rect(screen, GREEN, pipe)

    # Draw score
    score_surface = font.render(f'Score: {score}', True, WHITE)
    screen.blit(score_surface, (10, 10))

    pygame.display.update()

pygame.quit()
sys.exit()

         