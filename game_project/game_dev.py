######################################################################################################
# MODULES TO BE IMPORTED #
######################################################################################################

import pygame  # Making use of the Pygame Library to create a simple 2D game.
import os  # We are going to need to make use of profile paths to select our Images and Sounds.
pygame.init()

######################################################################################################
# LOADING SOUNDS #
######################################################################################################
# Initialize Pygame mixer
pygame.mixer.init()

# Load the MP3 file
pygame.mixer.music.load('backround_sound.mp3')  # Path to your background music.

# Play the music (-1 for looping)
pygame.mixer.music.play(-1)

# Load sound effects for beams
GOKU_BEAM_SOUND = pygame.mixer.Sound('kiblast.mp3')  # Sound for Goku's beam
VEGETA_BEAM_SOUND = pygame.mixer.Sound('blaster.mp3')  # Sound for Vegeta's beam

######################################################################################################
# NAMED CONSTANTS #
######################################################################################################

WIDTH, HEIGHT = 1024, 768  # Named Constants with Resolution set
WIN = pygame.display.set_mode((WIDTH, HEIGHT), pygame.DOUBLEBUF)  # Setting the Window Size
pygame.display.set_caption("Dragonball Z - Mini-Hero's")

WHITE = (255, 255, 255)  # Making use of standard RGB Format.
STAGE = pygame.transform.scale(pygame.image.load('namek.png'), (WIDTH, HEIGHT))

FPS = 60  # Frames Per Second for window refresh rate
MOVEMENT = 10
BEAM_MOVE = 12
GOKU_WIDTH, GOKU_HEIGHT = 250, 180  # Setting global variables for our character
VEGETA_WIDTH, VEGETA_HEIGHT = 250, 180  # Setting global variables for our character
GOKU_BEAM_IMAGE = pygame.image.load('kaneha.png')  # Load beam image
GOKU_BEAM = pygame.transform.scale(GOKU_BEAM_IMAGE, (100, 60))  # Scale to appropriate size
VEGETA_BEAM_IMAGE = pygame.image.load('gallick.png')  # Load beam image
VEGETA_BEAM = pygame.transform.scale(VEGETA_BEAM_IMAGE, (100, 60))  # Scale to appropriate size

GOKU_DAMAGE = pygame.USEREVENT + 1  # DAMAGE TAKEN EVENT
VEGETA_DAMAGE = pygame.USEREVENT + 2  # DAMAGE TAKEN EVENT

######################################################################################################
# IMPORTING IMAGES FROM SYSTEM LOCALE #
######################################################################################################

GOKU_IMAGE = pygame.image.load('goku2.png')  # Using pygame library to load our Goku sprite
GOKU = pygame.transform.scale(GOKU_IMAGE, (GOKU_WIDTH, GOKU_HEIGHT))  # Resizing Goku sprite

VEGETA_IMAGE = pygame.image.load('vegeta.png')  # Using pygame library to load our Vegeta sprite
VEGETA = pygame.transform.scale(VEGETA_IMAGE, (VEGETA_WIDTH, VEGETA_HEIGHT))  # Resizing Vegeta sprite

######################################################################################################
# IMAGE / SPRITE GENERATION #
######################################################################################################

def draw_window(goku, vegeta, goku_beams, vegeta_beams, goku_health, vegeta_health):
    WIN.blit(STAGE, (0, 0))
    WIN.blit(GOKU, (goku.x, goku.y))  # Injecting images onto screen
    WIN.blit(VEGETA, (vegeta.x, vegeta.y))  # Injecting images onto screen

    # Fonts for player names
    font = pygame.font.SysFont('comicsans', 30)  # Using a Comic Sans font
    goku_text = font.render("Goku", True, WHITE)
    vegeta_text = font.render("Vegeta", True, WHITE)

    # Draw names above the health bars
    WIN.blit(goku_text, (10, 40))  # Goku's name
    WIN.blit(vegeta_text, (WIDTH - 110, 40))  # Vegeta's name

    # Draw health bars
    pygame.draw.rect(WIN, (0, 0, 0), (10, 10, 200, 20), 2)  # Vegeta's health bar border
    pygame.draw.rect(WIN, (255, 0, 0), (10, 10, 200, 20))  # Vegeta's health background
    pygame.draw.rect(WIN, (0, 255, 0), (10, 10, vegeta_health * 2, 20))  # Vegeta's health

    pygame.draw.rect(WIN, (0, 0, 0), (WIDTH - 210, 10, 200, 20), 2)  # Goku's health bar border
    pygame.draw.rect(WIN, (255, 0, 0), (WIDTH - 210, 10, 200, 20))  # Goku's health background
    pygame.draw.rect(WIN, (0, 255, 0), (WIDTH - 210, 10, goku_health * 2, 20))  # Goku's health

    for beam in goku_beams:  # Draw each Goku beam
        WIN.blit(GOKU_BEAM, (beam.x, beam.y))
    for beam in vegeta_beams:  # Draw each Vegeta beam
        WIN.blit(VEGETA_BEAM, (beam.x, beam.y))

    pygame.display.update()

def move_beams(beams, direction, max_width):
    for beam in beams[:]:  # Iterate over a copy of the list to allow removal
        beam.x += direction * BEAM_MOVE  # Move beam
        if beam.x < 0 or beam.x > max_width:  # Remove beams that go out of screen bounds
            beams.remove(beam)

######################################################################################################
# MOVEMENT FUNCTIONS #
######################################################################################################

def goku_movement(keys_pressed, goku_pos):
    if keys_pressed[pygame.K_a]:  # Left Direction
        goku_pos.x -= MOVEMENT
    if keys_pressed[pygame.K_d]:  # Right Direction
        goku_pos.x += MOVEMENT
    if keys_pressed[pygame.K_w]:  # Up Direction
        goku_pos.y -= MOVEMENT
    if keys_pressed[pygame.K_s]:  # Down Direction
        goku_pos.y += MOVEMENT

def vegeta_movement(keys_pressed, vegeta_pos):
    if keys_pressed[pygame.K_LEFT]:  # Left Direction
        vegeta_pos.x -= MOVEMENT
    if keys_pressed[pygame.K_RIGHT]:  # Right Direction
        vegeta_pos.x += MOVEMENT
    if keys_pressed[pygame.K_UP]:  # Up Direction
        vegeta_pos.y -= MOVEMENT
    if keys_pressed[pygame.K_DOWN]:  # Down Direction
        vegeta_pos.y += MOVEMENT

######################################################################################################
# PROJECTILE LOGIC #
######################################################################################################

def handle_beams(goku_beams, vegeta_beams, goku_pos, vegeta_pos):
    for beam in goku_beams[:]:
        if vegeta_pos.colliderect(beam):
            pygame.event.post(pygame.event.Event(VEGETA_DAMAGE))
            goku_beams.remove(beam)
            

    for beam in vegeta_beams[:]:
        if goku_pos.colliderect(beam):
            pygame.event.post(pygame.event.Event(GOKU_DAMAGE))
            vegeta_beams.remove(beam)
          

######################################################################################################
# MAIN GAME LOGIC #
######################################################################################################

def game_dev():
    goku_pos = pygame.Rect(100, 300, GOKU_WIDTH, GOKU_HEIGHT)
    vegeta_pos = pygame.Rect(700, 300, VEGETA_WIDTH, VEGETA_HEIGHT)
    goku_beams = []
    vegeta_beams = []
    goku_health = 100
    vegeta_health = 100

    goku_transformed = False  # Track transformation state
    clock = pygame.time.Clock()
    run = True

    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LCTRL:
                    goku_beams.append(pygame.Rect(goku_pos.x + GOKU_WIDTH, goku_pos.y + GOKU_HEIGHT // 2, 50, 20))
                    GOKU_BEAM_SOUND.play()
                if event.key == pygame.K_RCTRL:
                    vegeta_beams.append(pygame.Rect(vegeta_pos.x, vegeta_pos.y + VEGETA_HEIGHT // 2, 50, 20))
                    VEGETA_BEAM_SOUND.play()
                if event.key == pygame.K_q and not goku_transformed:
                    global GOKU
                    GOKU_IMAGE = pygame.image.load('goku-super3.png')
                    GOKU = pygame.transform.scale(GOKU_IMAGE, (GOKU_WIDTH, GOKU_HEIGHT))
                    goku_transformed = True

            if event.type == VEGETA_DAMAGE:
                goku_health -= 25

            if event.type == GOKU_DAMAGE:
                vegeta_health -= 25

        keys_pressed = pygame.key.get_pressed()
        goku_movement(keys_pressed, goku_pos)
        vegeta_movement(keys_pressed, vegeta_pos)
        move_beams(goku_beams, 1, WIDTH)
        move_beams(vegeta_beams, -1, WIDTH)
        handle_beams(goku_beams, vegeta_beams, goku_pos, vegeta_pos)
        draw_window(goku_pos, vegeta_pos, goku_beams, vegeta_beams, goku_health, vegeta_health)

        if vegeta_health <= 0:
            print("Goku Wins!")
            run = False
        if goku_health <= 0:
            print("Vegeta Wins!")
            run = False

    pygame.quit()

if __name__ == "__main__":
    game_dev()
