import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)
CYAN = (0, 255, 255)  # New color for vulnerable ghosts
PACMAN_RADIUS = 30
GHOST_RADIUS = 25
PELLET_RADIUS = 5
POWERUP_RADIUS = 10
POWERUP_TIME = 5000  # milliseconds

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pac-Man")

# Clock to control the frame rate
clock = pygame.time.Clock()

# Pac-Man properties
pacman_x = WIDTH // 2
pacman_y = HEIGHT // 2
pacman_direction = 0  # 0: right, 1: up, 2: left, 3: down

# Ghost properties
ghosts = [{'x': random.randint(50, WIDTH-50),
           'y': random.randint(50, HEIGHT-50),
           'direction': random.choice([0, 1, 2, 3]),
           'vulnerable': False,
           'vulnerable_timer': 0} for _ in range(3)]

# Pellet properties
pellets = [{'x': random.randint(50, WIDTH-50),
            'y': random.randint(50, HEIGHT-50)} for _ in range(20)]

# Power-up properties
powerups = []

# Score
score = 0

# Game state
game_active = False
game_over = False

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN and not game_active:
            game_active = True
            game_over = False
            pacman_x = WIDTH // 2
            pacman_y = HEIGHT // 2
            pacman_direction = 0
            ghosts = [{'x': random.randint(50, WIDTH - 50),
                       'y': random.randint(50, HEIGHT - 50),
                       'direction': random.choice([0, 1, 2, 3]),
                       'vulnerable': False,
                       'vulnerable_timer': 0} for _ in range(3)]
            pellets = [{'x': random.randint(50, WIDTH - 50),
                        'y': random.randint(50, HEIGHT - 50)} for _ in range(20)]
            powerups = []
            score = 0

    if game_active:
        # Handle key events to change Pac-Man's direction
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            pacman_direction = 0
        elif keys[pygame.K_UP]:
            pacman_direction = 1
        elif keys[pygame.K_LEFT]:
            pacman_direction = 2
        elif keys[pygame.K_DOWN]:
            pacman_direction = 3

        # Update Pac-Man's position based on direction
        if pacman_direction == 0:
            pacman_x = (pacman_x + 5) % WIDTH
        elif pacman_direction == 1:
            pacman_y = (pacman_y - 5) % HEIGHT
        elif pacman_direction == 2:
            pacman_x = (pacman_x - 5) % WIDTH
        elif pacman_direction == 3:
            pacman_y = (pacman_y + 5) % HEIGHT

        # Check for collisions with pellets
        for pellet in pellets:
            distance = pygame.math.Vector2(pacman_x - pellet['x'], pacman_y - pellet['y']).length()
            if distance < PACMAN_RADIUS + PELLET_RADIUS:
                pellets.remove(pellet)
                score += 10

        # Check for collisions with power-ups
        for powerup in powerups:
            distance = pygame.math.Vector2(pacman_x - powerup['x'], pacman_y - powerup['y']).length()
            if distance < PACMAN_RADIUS + POWERUP_RADIUS:
                powerups.remove(powerup)
                for ghost in ghosts:
                    ghost['vulnerable'] = True
                    ghost['vulnerable_timer'] = pygame.time.get_ticks() + POWERUP_TIME

        # Update ghost positions and check for collisions with Pac-Man
        for ghost in ghosts:
            # Update ghost position based on direction
            if ghost['direction'] == 0:
                ghost['x'] = (ghost['x'] + 3) % WIDTH
            elif ghost['direction'] == 1:
                ghost['y'] = (ghost['y'] - 3) % HEIGHT
            elif ghost['direction'] == 2:
                ghost['x'] = (ghost['x'] - 3) % WIDTH
            elif ghost['direction'] == 3:
                ghost['y'] = (ghost['y'] + 3) % HEIGHT

            # Check for collisions with Pac-Man
            distance = pygame.math.Vector2(pacman_x - ghost['x'], pacman_y - ghost['y']).length()
            if distance < PACMAN_RADIUS + GHOST_RADIUS:
                if ghost['vulnerable']:
                    ghosts.remove(ghost)
                    score += 50
                else:
                    game_active = False
                    game_over = True

            # Reverse direction if hitting the screen edge
            if ghost['x'] <= GHOST_RADIUS or ghost['x'] >= WIDTH - GHOST_RADIUS:
                ghost['direction'] = (ghost['direction'] + 2) % 4
            if ghost['y'] <= GHOST_RADIUS or ghost['y'] >= HEIGHT - GHOST_RADIUS:
                ghost['direction'] = (ghost['direction'] + 2) % 4

            # Check and update vulnerable state
            if ghost['vulnerable'] and pygame.time.get_ticks() > ghost['vulnerable_timer']:
                ghost['vulnerable'] = False

        # Add new power-ups randomly, only if there are still pellets
        if len(powerups) < 3 and pellets:
            powerups.append({'x': random.randint(50, WIDTH-50), 'y': random.randint(50, HEIGHT-50)})

        # Check if all pellets are eaten
        if not pellets:
            game_active = False
            game_over = True

        # Check if all ghosts are dead
        if not ghosts:
            game_active = False
            game_over = True

    # Draw the background
    screen.fill(BLACK)

    if game_active:
        # Draw pellets
        for pellet in pellets:
            pygame.draw.circle(screen, YELLOW, (pellet['x'], pellet['y']), PELLET_RADIUS)

        # Draw power-ups
        for powerup in powerups:
            pygame.draw.circle(screen, CYAN, (powerup['x'], powerup['y']), POWERUP_RADIUS)

        # Draw ghosts
        for ghost in ghosts:
            color = CYAN if ghost['vulnerable'] else RED
            pygame.draw.circle(screen, color, (ghost['x'], ghost['y']), GHOST_RADIUS)

        # Draw Pac-Man
        pygame.draw.circle(screen, YELLOW, (pacman_x, pacman_y), PACMAN_RADIUS)

        # Display score
        font = pygame.font.Font(None, 36)
        score_text = font.render("Score: {}".format(score), True, YELLOW)
        screen.blit(score_text, (10, 10))
    elif game_over:
        # Display game over message
        font = pygame.font.Font(None, 50)
        game_over_text = font.render("Game Over", True, YELLOW)
        game_over_rect = game_over_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 30))
        screen.blit(game_over_text, game_over_rect)

        # Display final score
        final_score_text = font.render("Final Score: {}".format(score), True, YELLOW)
        final_score_rect = final_score_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 30))
        screen.blit(final_score_text, final_score_rect)

        # Display restart instructions
        restart_text = font.render("Click to Restart", True, YELLOW)
        restart_rect = restart_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 90))
        screen.blit(restart_text, restart_rect)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(FPS)
