import random
import pygame

# Set display surface
pygame.init()

# Set display surface
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 400
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Cookie Monster Isn't A Muppet")
pygame.display.set_icon(pygame.image.load('CookieMonster2.png'))

# Set FPS and clock
FPS = 60
clock = pygame.time.Clock()

# Set game values, Constants
Starting_Lives = 5
Starting_Velocity = 10
Starting_Coin_Velocity = 10
Starting_Coin_Acceleration = 0.5
score = 0
Buffer_Distance = 100
Speed = 0.75

'''constant player lives set it = to the constant above'''
Lives = Starting_Lives
'''constant coin velocity  set it = to the constant above'''
CoinVelocity = Starting_Coin_Velocity
PlayerSpeed = Starting_Velocity

# Set colors
OneEyedONneHornedFlyingPurplePeopleEater = (15, 0, 20)
ORANGE = (255, 159, 0)
RED = (86, 3, 25)
GREEN = (0, 255, 0)
DARK_GREEN = (10, 50, 10)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Set fonts
font = pygame.font.Font('AttackGraffiti.ttf', 32)
fontgo = pygame.font.Font('EBGaramond-VariableFont_wght.ttf', 40)


# Set text
# Score Text
score_text = font.render("Score:" + str(score), True, GREEN, DARK_GREEN)
score_rect = score_text.get_rect()
score_rect.topleft = (10, 10)

# Title Text
''' same deal as score'''
title_text = font.render("Feed The Dragon", True, RED, OneEyedONneHornedFlyingPurplePeopleEater)
title_rect = title_text.get_rect()
title_rect.centerx = WINDOW_WIDTH / 2
title_rect.y = 10

# Lives Text
lives_text = font.render("Lives:" + str(Lives), True, GREEN, DARK_GREEN)
Lives_rect = lives_text.get_rect()
Lives_rect.topright = (WINDOW_WIDTH - 10, 10)

# You Suck Text
game_over_text = fontgo.render("Cookie Monster Isn't A Muppet", True, RED, OneEyedONneHornedFlyingPurplePeopleEater)
game_over_rect = game_over_text.get_rect()
game_over_rect.center = (WINDOW_WIDTH // 2, (WINDOW_HEIGHT // 2) - 10)

# Continue Text
continue_text = fontgo.render("Would You Like To Try Again?", True, RED, OneEyedONneHornedFlyingPurplePeopleEater)
continue_text_rect = continue_text.get_rect()
continue_text_rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 + 32)

#Set sound & music
coin_sound = pygame.mixer.Sound("coin_sound.wav")

miss_sound = pygame.mixer.Sound("miss_sound.wav")
#miss_sound_volume = pygame.mixer_music.set_volume(0.1)
pygame.mixer.music.load("ftd_background_music.wav")


#Images
player_image = pygame.image.load("CookieMonster.png")
player_rect = player_image.get_rect()
player_rect.left = 32
player_rect.centery = WINDOW_HEIGHT // 2

coin_image = pygame.image.load("Cookie.png")
coin_rect = coin_image.get_rect()
coin_rect.centerx = WINDOW_WIDTH + Buffer_Distance
coin_rect.centery = random.randint(64, WINDOW_HEIGHT - 32)

pygame.mixer.music.play(-1, 0.0)


# Main Game Loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #Check for movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and player_rect.top > 64:
        player_rect.y -= Starting_Velocity
    if keys[pygame.K_DOWN] and player_rect.bottom < WINDOW_HEIGHT:
        player_rect.y += Starting_Velocity

    #Coin Movement
    if coin_rect.x < 0:
        #Miss Coin
        Lives -= 1
        miss_sound.play()
        coin_rect.centerx = WINDOW_WIDTH + Buffer_Distance
        coin_rect.centery = random.randint(64, WINDOW_HEIGHT - 32)
    else:
        #Move the Coin
        coin_rect.x -= CoinVelocity

    #Check for Collisions
    if player_rect.colliderect(coin_rect):
        score += 1
        coin_sound.play()
        CoinVelocity += Starting_Coin_Acceleration
        PlayerSpeed += Speed
        coin_rect.centerx = WINDOW_WIDTH + Buffer_Distance
        coin_rect.centery = random.randint(64, WINDOW_HEIGHT - 32)



    # UPDATE HUD
    score_text = font.render("Score:" + str(score), True, GREEN, DARK_GREEN)
    lives_text = font.render("Lives:" + str(Lives), True, GREEN, DARK_GREEN)

    #Game Over Check
    if Lives == 0:
        display_surface.blit(game_over_text, game_over_rect)
        display_surface.blit(continue_text, continue_text_rect)
        pygame.display.update()

        #pause game till reset
        pygame.mixer.music.stop()
        is_paused = True
        while is_paused:
            for event in pygame.event.get():
                #play again
                if event.type == pygame.KEYDOWN:
                    score = 0
                    Lives = Starting_Lives
                    player_rect.y = WINDOW_HEIGHT // 2
                    CoinVelocity = Starting_Coin_Velocity
                    PlayerSpeed = Starting_Velocity
                    pygame.mixer.music.play(-1, 0.0)
                    is_paused = False
                if event.type == pygame.QUIT:
                    is_paused = False
                    running = False


    # Fill the Display
    display_surface.fill(OneEyedONneHornedFlyingPurplePeopleEater)

    display_surface.blit(score_text, score_rect)
    display_surface.blit(title_text, title_rect)
    display_surface.blit(lives_text, Lives_rect)
    display_surface.blit(player_image, player_rect)
    display_surface.blit(coin_image, coin_rect)
    pygame.draw.line(display_surface, ORANGE, (0, 64), (WINDOW_WIDTH, 64), 2)



    pygame.display.update()
    clock.tick(FPS)
pygame.quit()
