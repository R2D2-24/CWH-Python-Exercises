import pygame
import random
pygame.init()

# Colours Definition
White = (255, 255, 255)
Red = (255, 0, 0)
Black = (0, 0, 0)
Yellow = (255, 255, 0)
Pink = (255, 192, 203)
# These are RGB Values

# Display Of Game
Screen_Width = 700
Screen_Height = 400
Game_Window = pygame.display.set_mode((Screen_Width, Screen_Height))
pygame.display.set_caption("SnakesWithRishav")
pygame.display.update()
"""display.update function is very important after we make any
change in the display of the window"""

# Game Variables
Exit_Game = False
Game_Over = False
Snake_x = 45
Snake_y = 55
Velocity_x = 0
Velocity_y = 0

Food_x = random.randint(20, Screen_Width - 20)
Food_y = random.randint(20, Screen_Height - 20)
Snake_Size_x = 30
Snake_Size_y = 25
Food_Size = 20
Score = 0

# To print the Score on the Screen
Font = pygame.font.SysFont("None", 55)

def text_screen(text, colour, x, y):
    screen_text = Font.render(text, True, colour)
    Game_Window.blit(screen_text, [x, y])

fps = 30
Clock = pygame.time.Clock()

# Game Loop
while not Exit_Game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Exit_Game = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                Velocity_x = 10
                Velocity_y = 0

            if event.key == pygame.K_LEFT:
                Velocity_x = -10
                Velocity_y = 0

            if event.key == pygame.K_UP:
                Velocity_y = -10
                Velocity_x = 0
                Snake_Size_x = Snake_Size_y

            if event.key == pygame.K_DOWN:
                Velocity_y = 10
                Velocity_x = 0
                Snake_Size_x = Snake_Size_y

    Snake_x = Snake_x + Velocity_x
    Snake_y = Snake_y + Velocity_y

    if abs(Snake_x - Food_x) < 6 and abs(Snake_y - Food_y) < 6:
        Score = Score + 1

        print("Score", Score * 10)
        Food_x = random.randint(20, Screen_Width - 20)
        Food_y = random.randint(20, Screen_Height - 20)

    Game_Window.fill(White)  # To fill the background colour
    text_screen("Score: " + str(Score * 10), Red, 5, 5)
    Snake_Food = pygame.draw.rect(Game_Window, Red, [Food_x, Food_y, Food_Size, Food_Size])
    Snake_Head = pygame.draw.rect(Game_Window, Black, [Snake_x, Snake_y, Snake_Size_x, Snake_Size_y])
    pygame.display.update()
    Clock.tick(fps)

pygame.exit()
exit()
