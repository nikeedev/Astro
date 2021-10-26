import pygame

pygame.init()
 
pygame.mixer

screen = pygame.display.set_mode((800, 500))
pygame.display.set_caption("Nik The Game")

player = pygame.image.load("person.png")
player2 = pygame.image.load("person.png")
playerX = 380
playerY = 250
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

def person():
    screen.blit(player, (playerX, playerY))
def person2():
    screen.blit(player2, (player2X, player2Y))

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
        playerX += 0.5
    if move_left:
        playerX -= 0.5
    if move_up:
        playerY -= 0.5
    if move_down:
        playerY += 0.5

    if move_right2:
        player2X += 0.5
    if move_left2:
        player2X -= 0.5
    if move_up2:
        player2Y -= 0.5
    if move_down2:
        player2Y += 0.5

    if playerY >= 480:
        playerY = 470
    if playerY <= 0:
        playerY = 10 
    if playerX >= 785:
        playerX = 775
    if playerX <= 0:
        playerX = 10 

    if player2Y >= 480:
        player2Y = 470
    if player2Y <= 0:
        player2Y = 10 
    if player2X >= 785:
        player2X = 775
    if player2X <= 0:
        player2X = 10

    screen.fill((93, 115, 240))

    person()
    person2()

    pygame.display.update()
