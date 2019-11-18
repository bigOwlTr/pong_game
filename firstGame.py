# This will be a game
import random
import pygame
pygame.init()  # initialises pygame


ball_vel_randint_x = random.randint(1, 5)  # this creates the random int to create the
ball_vel_randint_y = random.randint(1, 5)  # random speed and direction for the ball

left_count = 0    # counts how many times the bar has been moved in a direction
right_count = 0

screen_width = 1000
screen_hight = 550
Red = (255, 0, 0)
Black = (0, 0, 0)
White = (255, 255, 255)

window = pygame.display.set_mode((screen_width, screen_hight))  # sets the size of the window
pygame.display.set_caption("Game")  # sets the caption on the window

width = 100                      # sizes and coords for the paddle
x = screen_width/2 - width/2
y = screen_hight - 70
hight = 20
vel = 9    # the interval by which the ball moves

numTargets = 11
numTargetsPerRow = 7
target_x = {x: (63 + x * 80) for x in range(numTargets)}
target_x2 = {x: (63 + x * 80) for x in range(numTargets)}

#for x in range(numTargets):
#    target['xpos'][x]= 100
#    target['ypos'][x]= 55
#    target['color'] = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))


target_y = {x: 0 for x in range(numTargets)}
target_y2 = {x: 42 for x in range(numTargets)}
colour = {x: (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)) for x in range(numTargets*2)}
colour2 = {x: (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)) for x in range(numTargets*2)}
ball_width = 20              # ball variables to make other statements easyer
ball_radius = 20
ball_x = int(screen_width/2)
ball_y = int(screen_hight - (70 + ball_radius))
ball_y_vel = 1
ball_x_vel = 1

ball_moving_left = False
ball_moving_right = False

target_not_hit = {x: True for x in range(14)}
target_not_hit2 = {x: True for x in range(14)}
run = True       # the main loop that updates everything
while run:
    pygame.time.delay(15)   # millisecond delay so that the loop isn't too fast
# the next bit will end the check loop and close the window if you hit the red exit button
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    window.fill(Black)        # basically resets the screen every time

    total_count = right_count + left_count

    if keys[pygame.K_LEFT] and total_count < 1:   # if its the first move sends the ball off randomly
        ball_x_vel += ball_vel_randint_x
        ball_y_vel += ball_vel_randint_y
        ball_moving_left = True

    if keys[pygame.K_RIGHT] and total_count < 1:  # ditto
        ball_x_vel += ball_vel_randint_x
        ball_y_vel += ball_vel_randint_y
        ball_moving_right = True

    if keys[pygame.K_LEFT] and x > 0:   # moves the paddle
        x -= vel
        left_count += 1
    if keys[pygame.K_RIGHT]and x < screen_width - width:  # ditto
        x += vel
        right_count += 1

    if ball_moving_left:    # means the coords change by the set velocity
        ball_x -= ball_x_vel
        ball_y -= ball_y_vel

    if ball_moving_right:    # ditto but for moving right
        ball_x += ball_x_vel
        ball_y -= ball_y_vel

    if ball_x < ball_radius or ball_x > screen_width - ball_radius:  # bounces the ball off the side walls
        ball_x_vel = ball_x_vel * -1

    if ball_y < ball_radius:   # bounces the ball off the ceiling
        ball_y_vel = ball_y_vel * -1

    if x < ball_x < (x + width) and y < ball_y + ball_radius < (y + hight):  # bounces off the paddle
        ball_y_vel = ball_y_vel * -1

    if ball_y > screen_hight - ball_radius:  # ends the program if the ball hits the bottom
        run = False

    for target in range(numTargets ):
        if target_x[target] <= ball_x <= target_x[target] + 100 and target_y[target] + 50 >= ball_y >= target_y[target] and target_not_hit[target]:
            ball_y_vel = ball_y_vel * -1
            # ball hits the target (blue) it bounces and says the target is hit 1
            target_not_hit[target] = False

        if 200 - ball_radius < ball_y < 50 + ball_radius and target_x[target] < ball_x < target_x[target] + 100 and target_not_hit[target]:
            ball_x_vel = ball_x_vel * -1    # ball bounces off the sides of the target 2
            target_not_hit[target] = False

        if target_not_hit[target]:   # the target 1 will only show if it hasn't been hit, it will disappear
            pygame.draw.rect(window, colour[target], (target_x[target], target_y[target], 75, 37))

    for target in range(numTargets):
        if target_x2[target] <= ball_x <= target_x2[target] + 75 and target_y2[target] + 37 >= ball_y >= target_y2[target] and target_not_hit2[target]:
            ball_y_vel = ball_y_vel * -1
            # ball hits the target (blue) it bounces and says the target is hit 1
            target_not_hit2[target] = False

        if 200 - ball_radius < ball_y < 37 + ball_radius and target_x2[target] < ball_x < target_x2[target] + 75 and target_not_hit2[target]:
            ball_x_vel = ball_x_vel * -1  # ball bounces off the sides of the target 2
            target_not_hit2[target] = False

        if target_not_hit2[target]:  # the target 1 will only show if it hasn't been hit, it will disappear
            pygame.draw.rect(window, colour2[target], (target_x2[target], target_y2[target], 75, 37))

    pygame.draw.rect(window, Red, (x, y, width, hight))  # draws the paddle
    pygame.draw.circle(window, (255, 255, 255), (ball_x, ball_y), ball_radius, ball_width)  # draws the ball

    pygame.display.update()   # updates the display


pygame.quit()
# ends the code and closes the window when the loop ends
