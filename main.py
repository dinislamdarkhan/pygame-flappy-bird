import os
import random
import pygame
import sys


# If the code is frozen, use this path:
if getattr(sys, 'frozen', False):
    currentPath = sys._MEIPASS
# If it's not use the path we're on now
else:
    currentPath = os.path.dirname(__file__)


# Game Variables
game_active = False
game_start = True
gravity = 0.25
bird_movement = 0
score = 0
high_score = 0

SPAWNPIPE = pygame.USEREVENT
pygame.time.set_timer(SPAWNPIPE, 1200)
pipe_height = [300, 450, 600]

BIRDFLAP = pygame.USEREVENT + 1
pygame.time.set_timer(BIRDFLAP, 200)


def draw_flor():
    screen.blit(floor_surface, (floor_x_pos, 675))
    screen.blit(floor_surface, (floor_x_pos + 432, 675))


def create_pipe():
    random_pipe_pos = random.choice(pipe_height)
    bottom_pipe = pipe_surface.get_rect(midtop=(500, random_pipe_pos))
    top_pipe = pipe_surface.get_rect(midbottom=(500, random_pipe_pos - 250))
    return bottom_pipe, top_pipe


def move_pipes(pipes):
    for pipe in pipes:
        pipe.centerx -= 5
    return pipes


def draw_pipes(pipes):
    for pipe in pipes:
        if pipe.bottom >= 768:
            screen.blit(pipe_surface, pipe)
        else:
            flip_pipe = pygame.transform.flip(pipe_surface, False, True)
            screen.blit(flip_pipe, pipe)


def check_collision(pipes):
    for pipe in pipes:
        if bird_rect.colliderect(pipe):
            death_sound.play()
            return False
        if bird_rect.top <= -75 or bird_rect.bottom >= 675:
            death_sound.play()
            return False
    return True


def rotate_bird(bird):
    new_bird = pygame.transform.rotozoom(bird, -bird_movement * 3, 1)
    return new_bird


def bird_animation():
    new_bird = bird_frames[bird_index]
    new_bird_rect = new_bird.get_rect(center=(75, bird_rect.centery))
    return new_bird, new_bird_rect


def score_display(game_state):
    score_surface = game_font.render(f'Score: {int(score)}', True, (255, 255, 255))
    score_rect = score_surface.get_rect(center=(216, 75))
    screen.blit(score_surface, score_rect)

    if not game_state:
        high_score_surface = game_font.render(f'High Score: {int(high_score)}', True, (255, 255, 255))
        high_score_rect = high_score_surface.get_rect(center=(216, 735))
        screen.blit(high_score_surface, high_score_rect)


def update_score(score, high_score):
    if score > high_score:
        high_score = score
    return high_score


pygame.mixer.pre_init(frequency=44100, size=16, channels=1)
pygame.init()
screen = pygame.display.set_mode((432, 768))
clock = pygame.time.Clock()
game_font = pygame.font.Font(os.path.join(currentPath, 'fonts/04B_19.TTF'), 40)

bg_surface = pygame.transform.scale2x(
    pygame.image.load(os.path.join(currentPath, 'assets/background-night.png')).convert())

floor_surface = pygame.transform.scale2x(pygame.image.load(os.path.join(currentPath, 'assets/base.png')).convert())
floor_x_pos = 0

bird_downflap = pygame.transform.scale2x(
    pygame.image.load(os.path.join(currentPath, 'assets/yellowbird-downflap.png')).convert_alpha())
bird_midflap = pygame.transform.scale2x(
    pygame.image.load(os.path.join(currentPath, 'assets/yellowbird-midflap.png')).convert_alpha())
bird_upflap = pygame.transform.scale2x(pygame.image.load(os.path.join(currentPath, 'assets/yellowbird-upflap.png')).convert_alpha())
bird_frames = [bird_downflap, bird_midflap, bird_upflap]
bird_index = 0
bird_surface = bird_frames[bird_index]
bird_rect = bird_surface.get_rect(center=(75, 384))

pipe_surface = pygame.image.load(os.path.join(currentPath, "assets/pipe-green.png"))
pipe_surface = pygame.transform.scale2x(pipe_surface)
pipe_list = []

game_over_surface = pygame.transform.scale2x(pygame.image.load(os.path.join(currentPath, 'assets/gameover.png')).convert_alpha())
game_over_rect = game_over_surface.get_rect(center=(216, 384))

game_start_surface = pygame.transform.scale2x(pygame.image.load(os.path.join(currentPath, 'assets/message.png')).convert_alpha())
game_start_rect = game_over_surface.get_rect(center=(216, 192))

flap_sound = pygame.mixer.Sound(os.path.join(currentPath, 'sounds/sfx_wing.wav'))
death_sound = pygame.mixer.Sound(os.path.join(currentPath, 'sounds/sfx_die.wav'))
score_sound = pygame.mixer.Sound(os.path.join(currentPath, 'sounds/sfx_point.wav'))
score_sound_count = 0

while True:
    for event in pygame.event.get():
        # Quit
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            game_start = False
            # JUMP
            if game_active:
                flap_sound.play()
                bird_movement = 0
                bird_movement -= 7
            # Restart game
            else:
                game_active = True
                pipe_list.clear()
                bird_rect.center = (75, 384)
                bird_movement = 0
                score = 0
        # Create pipes
        if event.type == SPAWNPIPE and game_active:
            pipe_list.extend(create_pipe())
        # Bird animation states
        if event.type == BIRDFLAP:
            if bird_index >= 2:
                bird_index = 0
            bird_index += 1
            bird_surface, bird_rect = bird_animation()
    # BG
    screen.blit(bg_surface, (0, 0))
    # Floor
    floor_x_pos -= 1
    draw_flor()
    if floor_x_pos <= -384:
        floor_x_pos = 0

    if game_start:
        screen.blit(game_start_surface, game_start_rect)

    if game_active and not game_start:
        # Bird
        bird_movement += gravity
        rotated_bird = rotate_bird(bird_surface)

        bird_rect.centery += bird_movement
        screen.blit(rotated_bird, bird_rect)
        game_active = check_collision(pipe_list)
        # Pipe
        pipe_list = move_pipes(pipe_list)
        draw_pipes(pipe_list)

        score += 0.01
        score_sound_count += 1
        if score_sound_count >= 100:
            score_sound.play()
            score_sound_count = 0
        score_display(True)

    elif not game_start:
        screen.blit(game_over_surface, game_over_rect)
        high_score = update_score(score, high_score)
        score_display(False)

    pygame.display.update()
    clock.tick(120)
