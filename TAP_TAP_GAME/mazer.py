import pygame
import random
from sys import exit

pygame.init()
WIDTH, HEIGHT, = 470, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))

coin_count = 0

# ASSETS


BACK_IMAGE = pygame.transform.scale(pygame.image.load("my_game/Background.png"), (WIDTH, HEIGHT))
BACK_IMAGE_RECT = BACK_IMAGE.get_rect(topleft=(0, 0))

PLAYER_IMAGE = pygame.transform.scale(pygame.image.load("my_game/items.png"), (40, 40))
PLAYER_IMAGE_RECT = PLAYER_IMAGE.get_rect(center=(50, 50))

COIN_IMAGE = pygame.image.load("my_game/coin.png")
COIN_IMAGE_RECT = COIN_IMAGE.get_rect(center=(100, 100))

FPS = 60
clock = pygame.time.Clock()
gravity = 0


def control_movement():
    global gravity
    keys = pygame.key.get_pressed()
    gravity += 0.7

    PLAYER_IMAGE_RECT.y += gravity
    if keys[pygame.K_SPACE] and PLAYER_IMAGE_RECT.y >= 100:
        PLAYER_IMAGE_RECT.y -= 1
        gravity = -10

    if keys[pygame.K_LEFT] and PLAYER_IMAGE_RECT.x >= -30:
        PLAYER_IMAGE_RECT.x -= 5
    if keys[pygame.K_RIGHT] and PLAYER_IMAGE_RECT.x <= WIDTH - 70:
        PLAYER_IMAGE_RECT.x += 5


def coin_move():
    global coin_count
    COIN_IMAGE_RECT.y += 2
    if COIN_IMAGE_RECT.colliderect(PLAYER_IMAGE_RECT):
        coin_count += 1
        print(coin_count)
        COIN_IMAGE_RECT.x = random.randrange(50, 400)
        COIN_IMAGE_RECT.y = -50
    if COIN_IMAGE_RECT.y >= HEIGHT:
        COIN_IMAGE_RECT.x = random.randrange(50, 400)
        COIN_IMAGE_RECT.y = -50
        coin_count -= 5


ffont = pygame.font.Font("Nasa21-l23X.ttf", 50)
ffont_2 = pygame.font.Font("Nasa21-l23X.ttf", 25)
margin_left = 50


def coin_counter():
    global current_time
    current_time = pygame.time.get_ticks() / 1000
    score_surf = ffont.render(f"{coin_count}", False, (255, 255, 255))
    time_surf = ffont_2.render(f"{int(current_time)}", False, (255, 255, 255))
    global margin_left
    # screen.blit(time_surf,(10,60))
    screen.blit(score_surf, (10, 10))
    screen.blit(COIN_IMAGE, (margin_left, 25))
    if current_time >= 10:
        COIN_IMAGE_RECT.y += 3
        margin_left = 60
    if current_time >= 20:
        COIN_IMAGE_RECT.y += 5


game = True
while True:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()


        if event.type == pygame.KEYDOWN and event.key == pygame.K_r and game is False:
            current_time = 0

    if game:
        CHEST_RANDOM_NUMBER = random.randrange(1, 100)
        screen.blit(BACK_IMAGE, BACK_IMAGE_RECT)

        screen.blit(COIN_IMAGE, COIN_IMAGE_RECT)
        screen.blit(PLAYER_IMAGE, PLAYER_IMAGE_RECT)
        border_bottom = pygame.draw.rect(screen, (255, 0, 0), (0, HEIGHT - 10, WIDTH, 10))

        coin_counter()
        # movement-PLAYER

        control_movement()
        coin_move()

    if border_bottom.colliderect(PLAYER_IMAGE_RECT) or coin_count < 0:
        game = False

    if game == False:
        screen.fill((255, 0, 0))
        x = ffont.render("press R", False, (255, 255, 255))
        screen.blit(x, (WIDTH / 2 - 100, HEIGHT / 2 - 100))

        keys = pygame.key.get_pressed()

        if keys[pygame.K_r]:
            game = True

            PLAYER_IMAGE_RECT.x = 100
            PLAYER_IMAGE_RECT.y = 50
            coin_count = 0

            COIN_IMAGE_RECT.y += 2

    pygame.display.update()
