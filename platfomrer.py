import pygame
import sys
 
# Initialize Pygame
pygame.init()
 
# Set up the window
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simple Platformer")
 
# Colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
 
# Constants
PLAYER_WIDTH = 20
PLAYER_HEIGHT = 100
PLATFORM_WIDTH = 100
PLATFORM_HEIGHT = 20
 
# Player attributes
player_x = 20
player_y = HEIGHT/2-PLAYER_HEIGHT/2
player_vel_x = 0
player_vel_y = 0
jumping = False
gravity = 0.1
 
# Platform attributes
platform_x = 200
platform_y = HEIGHT - 100
 
# Main loop
running = True
while running:
    screen.fill(WHITE)
 
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                player_vel_y = -5
                platform_vel_x=-5
            elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                player_vel_y = 5
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player_vel_x = 0

 
    # Move the player
    platform_vel_y=-2
    platform_vel_x=-2
    
    player_x += player_vel_x
    player_y += player_vel_y
    platform_x += platform_vel_x
    platform_y += platform_vel_y 
    
    if platform_x>WIDTH or platform_x<0:
        platform_vel_x=-platform_vel_x
        
    if platform_y>HEIGHT or platform_y<0:
        platform_vel_y=-platform_vel_y
 
    # Collision detection with platform
    player_rect = pygame.Rect(player_x, player_y, PLAYER_WIDTH, PLAYER_HEIGHT)
    platform_rect = pygame.Rect(platform_x, platform_y, PLATFORM_WIDTH, PLATFORM_HEIGHT)
    if player_rect.colliderect(platform_rect) and player_vel_y > 0:
        player_y = platform_y - PLAYER_HEIGHT
        player_vel_y = 0
        jumping = False
 
    # Keep the player inside the screen
    player_x = max(0, min(player_x, WIDTH - PLAYER_WIDTH))
 
    # Draw the player
    pygame.draw.rect(screen, BLUE, (player_x, player_y, PLAYER_WIDTH, PLAYER_HEIGHT))
 
    # Draw the platform
    pygame.draw.rect(screen, BLACK, (platform_x, platform_y, PLATFORM_WIDTH, PLATFORM_HEIGHT))
 
    # Update the display
    pygame.display.flip()
 
    # Cap the frame rate
    pygame.time.Clock().tick(60)