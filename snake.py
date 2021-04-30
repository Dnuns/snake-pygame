import pygame
import random

blue = (50, 100, 213)
red = (216, 31, 42)
black = (0, 0, 0)
dimensions = (600,600)

#=================================
#Initial values

x = 300
y = 300
d = 20

snake_list = [[x, y]]

delta_x = 0
delta_y = 0

x_food = round(random.randrange(0, 600 - d) / 20) * 20
y_food = round(random.randrange(0, 600 - d) / 20) * 20 

#=================================

screen = pygame.display.set_mode((dimensions))
pygame.display.set_caption('Snake Game')

screen.fill(blue)

clock = pygame.time.Clock()

def draw_snake(snake_list):
    
    screen.fill(blue)
    
    for unity in snake_list:
        
        pygame.draw.rect(screen, red, [unity[0],unity[1],d,d])

def move_snake(delta_x, delta_y, snake_list):

    for event in pygame.event.get():

        if event.type == pygame.KEYDOWN:
            
            if event.key == pygame.K_LEFT:
                delta_x = -d
                delta_y = 0
        
            elif event.key == pygame.K_RIGHT:
                delta_x = d
                delta_y = 0

            elif event.key == pygame.K_UP:
                delta_x = 0
                delta_y = -d

            elif event.key == pygame.K_DOWN:
                delta_x = 0
                delta_y = d

    new_x = snake_list[-1][0] + delta_x
    new_y = snake_list[-1][1] + delta_y

    snake_list.append([new_x, new_y])

    del snake_list[0]

    return delta_x, delta_y, snake_list                

def verify_food(delta_x, delta_y, x_food, y_food, snake_list):

    head = snake_list[-1]

    new_x = head[0] + delta_x
    new_y = head[1] + delta_y

    if head[0] == x_food and head[1] == y_food:

        snake_list.append([new_x, new_y])

    pygame.draw.rect(screen, black, [x_food, y_food, d, d])

    return x_food, y_food, snake_list

while True:

    pygame.display.update()

    draw_snake(snake_list)

    delta_x, delta_y, snake_list = move_snake(delta_x, delta_y, snake_list) 

    x_food, y_food, snake_list = verify_food(delta_x, delta_y, x_food, y_food, snake_list)

    clock.tick(10)