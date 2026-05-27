import pygame
import random

pygame.init()

# =========================
# WINDOW
# =========================
WIDTH, HEIGHT = 700, 500
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Labyrinth - Treasure Hunt")

clock = pygame.time.Clock()
fps = 60
font = pygame.font.SysFont(None, 36)

background = pygame.image.load("background.jpg")
background = pygame.transform.scale(background, (WIDTH, HEIGHT))

imghero = pygame.image.load("hero.png")
imghero = pygame.transform.scale(imghero, (30, 30))

imgtreasure = pygame.image.load("treasure.png")
imgtreasure = pygame.transform.scale(imgtreasure, (40, 40))

# =========================
# VARS
# =========================
wins = 0
streak = 0
deaths = 0

psize = 30
player = pygame.Rect(30, 30, psize, psize)
pspeed = 5
startpos = (30, 30)

treasure = pygame.Rect(620, 420, 40, 40)

# =========================
# LEVELS
# =========================

lvl1 = [
    pygame.Rect(150, 0, 20, 300),
    pygame.Rect(300, 200, 20, 300),
    pygame.Rect(450, 0, 20, 300),
]

lvl2 = [
    pygame.Rect(100, 100, 500, 20),
    pygame.Rect(100, 250, 500, 20),
    pygame.Rect(200, 100, 20, 170),
    pygame.Rect(480, 250, 20, 170),
]

lvl3 = [
    pygame.Rect(120, 80, 20, 340),
    pygame.Rect(260, 0, 20, 300),
    pygame.Rect(400, 200, 20, 300),
    pygame.Rect(540, 0, 20, 300),
]

lvl4 = [
    pygame.Rect(80, 60, 540, 20),
    pygame.Rect(80, 60, 20, 320),
    pygame.Rect(80, 360, 540, 20),
    pygame.Rect(600, 60, 20, 320),

    pygame.Rect(180, 140, 20, 220),
    pygame.Rect(300, 60, 20, 220),
    pygame.Rect(420, 140, 20, 220),
]

lvl5 = [
    pygame.Rect(100, 0, 20, 400),
    pygame.Rect(220, 100, 20, 400),
    pygame.Rect(340, 0, 20, 400),
    pygame.Rect(460, 100, 20, 400),
    pygame.Rect(580, 0, 20, 350),

    pygame.Rect(100, 380, 500, 20),
]

lvl6 = [
    pygame.Rect(150, 50, 400, 20),
    pygame.Rect(150, 150, 20, 250),
    pygame.Rect(300, 0, 20, 300),
    pygame.Rect(450, 150, 20, 250),
]

lvl7 = [
    pygame.Rect(100, 100, 20, 300),
    pygame.Rect(200, 0, 20, 250),
    pygame.Rect(300, 250, 20, 250),
    pygame.Rect(400, 0, 20, 250),
    pygame.Rect(500, 250, 20, 250),
]

lvl8 = [
    pygame.Rect(50, 80, 600, 20),
    pygame.Rect(50, 200, 600, 20),
    pygame.Rect(50, 320, 600, 20),

    pygame.Rect(150, 80, 20, 140),
    pygame.Rect(300, 200, 20, 140),
    pygame.Rect(450, 80, 20, 140),
]

lvl9 = [
    pygame.Rect(120, 0, 20, 350),
    pygame.Rect(240, 150, 20, 350),
    pygame.Rect(360, 0, 20, 350),
    pygame.Rect(480, 150, 20, 350),

    pygame.Rect(120, 330, 260, 20),
]

lvl10 = [
    pygame.Rect(80, 80, 540, 20),
    pygame.Rect(80, 80, 20, 300),
    pygame.Rect(80, 360, 540, 20),
    pygame.Rect(600, 80, 20, 300),

    pygame.Rect(200, 160, 300, 20),
    pygame.Rect(200, 260, 300, 20),

    pygame.Rect(200, 160, 20, 120),
    pygame.Rect(480, 160, 20, 120),
]

levels = [
    lvl1,
    lvl2,
    lvl3,
    lvl4,
    lvl5,
    lvl6,
    lvl7,
    lvl8,
    lvl9,
    lvl10
]

curWalls = random.choice(levels)

# =========================
# MAIN LOOP
# =========================
game = True

while game:

    clock.tick(fps)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False

    keys = pygame.key.get_pressed()

    oldpos = player.topleft


    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        player.x -= pspeed

    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        player.x += pspeed

    if keys[pygame.K_UP] or keys[pygame.K_w]:
        player.y -= pspeed

    if keys[pygame.K_DOWN] or keys[pygame.K_s]:
        player.y += pspeed


    player.left = max(player.left, 0)
    player.right = min(player.right, WIDTH)

    player.top = max(player.top, 0)
    player.bottom = min(player.bottom, HEIGHT)

    hit_wall = False

    for wall in curWalls:
        if player.colliderect(wall):
            hit_wall = True
            break

    if hit_wall:
        deaths += 1
        streak = 0

        player.topleft = startpos
        curWalls = random.choice(levels)

    if player.colliderect(treasure):

        wins += 1
        streak += 1

        player.topleft = startpos

        curWalls = random.choice(levels)


    window.blit(background, (0, 0))

    for wall in curWalls:
        pygame.draw.rect(window, (180, 20, 20), wall)

    window.blit(imgtreasure, treasure)
    window.blit(imghero, player)

    #ui
    scoretxt = font.render(
        f"Wins: {wins} | Streak: {streak} | Deaths: {deaths}",
        True,
        (255, 255, 255)
    )

    window.blit(scoretxt, (20, 10))

    pygame.display.update()

pygame.quit()