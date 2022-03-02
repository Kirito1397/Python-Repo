from multiprocessing import cpu_count
import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((500,500))

# Provides the time in millisecond
clock = pygame.time.Clock()

current_time = 0
button_press_time = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            button_press_time = pygame.time.get_ticks()
            screen.fill((255,255,200))
           
    current_time = pygame.time.get_ticks()

    if (current_time- button_press_time) > 2000:
        screen.fill((0,0,0))

    # print(f"current_time : {current_time} button time : {button_press_time}")
    
    # Update the display using flip
    pygame.display.flip()

    # Sets the number of frames to be displayed per second
    clock.tick(60)