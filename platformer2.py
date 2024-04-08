import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up display
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hero Jumping on Platform")

# Load images
hero_image = pygame.image.load("BggZ2G.gif").convert_alpha()  # Adjust the path to your hero image
platform_image = pygame.image.load("platform-removebg-preview.png").convert_alpha()  # Adjust the path to your platform image
original_size = platform_image.get_size()
new_size = (original_size[0] // 3, original_size[1] // 3)
platform_image = pygame.transform.scale(platform_image, new_size)
# Initial positions
hero_x, hero_y = 200, HEIGHT - 300
hero_y_vel=1
platform_x, platform_y = 200, HEIGHT - 100
onground=False

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill((255, 255, 255))
    
    if hero_y>HEIGHT-150:
        onground=True
        hero_y_vel=0
        hero_y=HEIGHT-150
    
    if onground==False:
        hero_y_vel=hero_y_vel+1   
     
    hero_y_vel+=0.001
    hero_y=hero_y+hero_y_vel

    # Blit the platform
    screen.blit(platform_image, (platform_x, platform_y))
    
    

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_UP or event.key == pygame.K_w:
            hero_y_vel -= 2  # Adjust this value for different jump speeds
        if event.key == pygame.K_LEFT or event.key == pygame.K_w:
            hero_x -= 1  # Adjust this value for different jump speeds
        if event.key == pygame.K_RIGHT or event.key == pygame.K_w:
            hero_x -= -1  # Adjust this value for different jump speeds

    # Limit hero's jump height
    if hero_y <= HEIGHT - 300:
        hero_y = HEIGHT - 300

    # Blit the hero
    screen.blit(hero_image, (hero_x, hero_y))

    # Update the display
    pygame.display.flip()

    # Add a delay to control the frame rate
    pygame.time.delay(10)

pygame.quit()
sys.exit()
