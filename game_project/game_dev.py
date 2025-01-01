######################################################################################################
# MODULES TO BE IMPORTED #
######################################################################################################

import pygame  # Making use of the Pygame Library to create a simple 2D game.
import os  # We are going to need to make use of profile paths to select our Images and Sounds.
import sys # used for calling system methods.
import time # Used for the countdown timer.
from moviepy import *

pygame.init() #initializes our pygame library

# ##############################################################################
#                   # ENTRANCE SEQUENCE  #
# ##############################################################################
# Video path
video_path = "entrance_video1.mp4"  # Path to your video file

# Function to display the video
def play_video():
    try:
        clip = VideoFileClip(video_path)
        screen = pygame.display.set_mode((WIDTH, HEIGHT))
        clock = pygame.time.Clock()

        # Temporary audio handling
        audio_path = "temp_audio.mp3"
        if clip.audio:
            clip.audio.write_audiofile(audio_path, logger=None)
            pygame.mixer.music.load(audio_path)
            pygame.mixer.music.play()

        video_fps = clip.fps if clip.fps else 60

        for frame in clip.iter_frames(fps=video_fps, dtype='uint8'):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.mixer.music.stop()
                    clip.close()
                    if os.path.exists(audio_path):
                        os.remove(audio_path)
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    pygame.mixer.music.stop()
                    clip.close()
                    if os.path.exists(audio_path):
                        os.remove(audio_path)
                    start_background_music()  # Start background music for the game
                    game_dev()
                    return

            frame_surface = pygame.surfarray.make_surface(frame.swapaxes(0, 1))
            screen.blit(pygame.transform.scale(frame_surface, (WIDTH, HEIGHT)), (0, 0))
            pygame.display.update()
            clock.tick(video_fps)

        # Cleanup after video ends
        pygame.mixer.music.stop()
        clip.close()
        if os.path.exists(audio_path):
            os.remove(audio_path)
        start_background_music()  # Start background music for the game
        game_dev()

    except Exception as e:
        print(f"Error during video playback: {e}")
        if 'clip' in locals():
            clip.close()
        if os.path.exists(audio_path):
            try:
                os.remove(audio_path)
            except PermissionError:
                print(f"Could not delete {audio_path}, ensure it is not in use.")
        start_background_music()  # Start background music for the game
        game_dev()

def start_background_music():
    try:
        pygame.mixer.music.load('backround_sound.mp3')  # Load your background music file
        pygame.mixer.music.set_volume(0.01)  # Set volume to 10% 
        pygame.mixer.music.play(-1)  # Loop indefinitely
    except Exception as e:
        print(f"Error starting background music: {e}")       

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

WIDTH, HEIGHT = 1280, 720  # Resolution - You may change this as required
WIN = pygame.display.set_mode((WIDTH, HEIGHT), pygame.DOUBLEBUF)  # Setting the Window Size
pygame.display.set_caption("Dragonball Z - Mini-Hero's")

WHITE = (255, 255, 255)  # Making use of standard RGB Format.
STAGE = pygame.transform.scale(pygame.image.load('namek.png'), (WIDTH, HEIGHT))

FPS = 60  # Frames Per Second for window refresh rate
MOVEMENT = 10
BEAM_MOVE = 12
GOKU_WIDTH, GOKU_HEIGHT = 250, 180  # Setting global variables for our character
VEGETA_WIDTH, VEGETA_HEIGHT = 300, 200  # Setting global variables for our character
GOKU_BEAM_IMAGE = pygame.image.load('kaneha.png')  # Load beam image
GOKU_BEAM = pygame.transform.scale(GOKU_BEAM_IMAGE, (100, 60))  # Scale to appropriate size
VEGETA_BEAM_IMAGE = pygame.image.load('gallick.png')  # Load beam image
VEGETA_BEAM = pygame.transform.scale(VEGETA_BEAM_IMAGE, (100, 60))  # Scale to appropriate size
WIDTH, HEIGHT = 1280, 720
FPS = 60
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

GOKU_DAMAGE = pygame.USEREVENT + 1  # DAMAGE TAKEN EVENT
VEGETA_DAMAGE = pygame.USEREVENT + 2  # DAMAGE TAKEN EVENT

WINNER_FONT = pygame.font.SysFont('comicsans', 100)

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


def draw_winner(text):
    draw_text = WINNER_FONT.render(text, 1, WHITE)
    WIN.blit(draw_text, (WIDTH//2 - draw_text.get_width()/2, HEIGHT/2 - draw_text.get_height()/2))
    pygame.display.update()
    pygame.time.delay(5000)

##########################################################################################################
                           # COUNTDOWN TIMER AT THE END OF THE GAME #
##########################################################################################################

def countdown_timer():
    font = pygame.font.SysFont('comicsans', 30)
    countdown = 10
    clock = pygame.time.Clock()  # Use Pygame's clock for accurate timing

    while countdown > 0:
        WIN.fill(BLACK)
        text = font.render(f"Do you want to continue? Press 'R' or wait {countdown} seconds.", True, WHITE)
        WIN.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2))
        pygame.display.update()

        # Limit the frame rate to 60 FPS
        clock.tick(60)

        # Check for events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                return True  # Restart the game

        # Wait for one second
        pygame.time.delay(1000)
        countdown -= 1

    return False  # Quit the game

def game_over():
    if countdown_timer():  # Timer ends or player presses 'R'
        restart_game()  # Restart the game if player chooses to continue
    else:
        pygame.mixer.music.stop()  # Stop music before quitting
        pygame.quit()  # Quit the game when the countdown ends
        sys.exit()

def restart_game():
    global goku_health, vegeta_health, goku_pos, vegeta_pos, goku_beams, vegeta_beams
    goku_health = 100
    vegeta_health = 100
    goku_pos = pygame.Rect(700, 300, 50, 50)
    vegeta_pos = pygame.Rect(100, 300, 50, 50)
    goku_beams.clear()
    vegeta_beams.clear()
    # Avoid calling game_dev directly; allow the main loop to reinitialize.    


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
            pygame.event.post(pygame.event.Event(GOKU_DAMAGE))
            goku_beams.remove(beam)
            

    for beam in vegeta_beams[:]:
        if goku_pos.colliderect(beam):
            pygame.event.post(pygame.event.Event(VEGETA_DAMAGE))
            vegeta_beams.remove(beam)
          

######################################################################################################
# MAIN GAME LOGIC #
######################################################################################################

def game_dev():
    global goku_health, vegeta_health, goku_pos, vegeta_pos, goku_beams, vegeta_beams
    goku_pos = pygame.Rect(100, 300, GOKU_WIDTH, GOKU_HEIGHT)
    vegeta_pos = pygame.Rect(700, 300, VEGETA_WIDTH, VEGETA_HEIGHT)
    goku_beams = []
    vegeta_beams = []
    goku_health = 100
    vegeta_health = 100

    goku_transformed = False  # Track transformation state
    vegeta_transformed = False  # Track transformation state for Vegeta
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
                if event.key == pygame.K_p and not vegeta_transformed:
                    global VEGETA
                    VEGETA_IMAGE = pygame.image.load('vegeta-super.png')
                    VEGETA = pygame.transform.scale(VEGETA_IMAGE, (VEGETA_WIDTH, VEGETA_HEIGHT))
                    vegeta_transformed = True                    

            if event.type == VEGETA_DAMAGE:
                vegeta_health -= 25

            if event.type == GOKU_DAMAGE:
                goku_health -= 25

        keys_pressed = pygame.key.get_pressed()
        goku_movement(keys_pressed, goku_pos)
        vegeta_movement(keys_pressed, vegeta_pos)
        move_beams(goku_beams, 1, WIDTH)
        move_beams(vegeta_beams, -1, WIDTH)
        handle_beams(goku_beams, vegeta_beams, goku_pos, vegeta_pos)
        draw_window(goku_pos, vegeta_pos, goku_beams, vegeta_beams, goku_health, vegeta_health)

        # Check for win condition
        if goku_health <= 0:
            draw_winner("Goku Wins!")
            game_over()  # Calls countdown or quits
            run = False  # Exit the loop

        elif vegeta_health <= 0:
            draw_winner("Vegeta Wins!")
            game_over()  # Calls countdown or quits
            run = False  # Exit the loop

def reinitialize_sounds():
    pygame.mixer.quit()  # Quit the mixer
    pygame.mixer.init()  # Reinitialize the mixer
    pygame.mixer.music.load('backround_sound.mp3')  # Load the background music again
    pygame.mixer.music.play(-1)  # Restart the background music

if __name__ == "__main__":
    play_video()
    game_dev()

    pygame.quit()
    sys.exit()


