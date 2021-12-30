import pygame

pygame.init()

width = 800
height = 500

img = pygame.image.load('data/person.png')
pygame.display.set_icon(img)

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Astro")
font = pygame.font.SysFont("arial", 20, bold=pygame.font.Font.bold)

black = (0, 0, 0)
white = (255, 255, 255)
background_color = (93, 115, 240)
brick = pygame.image.load("data/brick.png")
brickX = brick.get_rect().x + 20
brickY = brick.get_rect().y + 20


player1 = pygame.image.load("data/person.png")
player2 = pygame.image.load("data/person.png")
player1X = 380
player1Y = 250
player2X = 420
player2Y = 250
move_right = False
move_left = False
move_down = False
move_up = False
move_right2 = False
move_left2 = False
move_down2 = False
move_up2 = False
running = True
colliding = False

whole_text = ("Player 1: X: ", player1X, "Y: ", player1Y, "Player 2: X: ", player2X, "Y: ", player2Y)
text = font.render(str(whole_text), True, white, background_color)


def create_person():
    screen.blit(player1, (player1X, player1Y))


def create_person2():
    screen.blit(player2, (player2X, player2Y))


def create_brick():
    screen.blit(brick, (brickX, brickY))


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                move_left = True
            if event.key == pygame.K_RIGHT:
                move_right = True
            if event.key == pygame.K_DOWN:
                move_down = True
            if event.key == pygame.K_UP:
                move_up = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                move_left = False
            if event.key == pygame.K_RIGHT:
                move_right = False
            if event.key == pygame.K_DOWN:
                move_down = False
            if event.key == pygame.K_UP:
                move_up = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                move_left2 = True
            if event.key == pygame.K_d:
                move_right2 = True
            if event.key == pygame.K_s:
                move_down2 = True
            if event.key == pygame.K_w:
                move_up2 = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                move_left2 = False
            if event.key == pygame.K_d:
                move_right2 = False
            if event.key == pygame.K_s:
                move_down2 = False
            if event.key == pygame.K_w:
                move_up2 = False

    if move_right:
        player1X += 0.5
    if move_left:
        player1X -= 0.5
    if move_up:
        player1Y -= 0.5
    if move_down:
        player1Y += 0.5

    if move_right2:
        player2X += 0.5
    if move_left2:
        player2X -= 0.5
    if move_up2:
        player2Y -= 0.5
    if move_down2:
        player2Y += 0.5

    if player1Y >= 480:
        player1Y = 470
    if player1Y <= 0:
        player1Y = 10
    if player1X >= 785:
        player1X = 775
    if player1X <= 0:
        player1X = 10

    if player2Y >= 480:
        player2Y = 470
    if player2Y <= 0:
        player2Y = 10
    if player2X >= 785:
        player2X = 775
    if player2X <= 0:
        player2X = 10

    screen.fill(background_color)

    create_brick()
    create_person()
    create_person2()
    whole_text = ("Player 1: X: ", player1X, "Y: ", player1Y, "Player 2: X: ", player2X, "Y: ", player2Y)
    text = font.render(str(whole_text), True, white, background_color)
    screen.blit(text, (50, height - 50))

    pygame.display.update()
