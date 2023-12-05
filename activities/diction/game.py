import subprocess
subprocess.check_call(["python", '-m', 'pip', 'install', 'pygame'])

import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# Game variables
word_values = {
    "easy": ["cat", "dog", "fish"],
    "medium": ["python", "giraffe", "elephant"],
    "hard": ["encyclopedia", "exaggerate", "university"]
}

current_word = ""
word_x = 0
word_y = screen_height // 2
font = pygame.font.Font(None, 36)
user_text = ''
speed = 1
score = 0

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Function to get a new word
def get_new_word():
    difficulty = random.choice(list(word_values.keys()))
    return random.choice(word_values[difficulty]), difficulty

# Main game loop
running = True
clock = pygame.time.Clock()

current_word, difficulty = get_new_word()

while running:
    screen.fill(WHITE)
    
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                user_text = user_text[:-1]
            else:
                user_text += event.unicode

            if user_text == current_word:
                score += len(current_word)
                current_word, difficulty = get_new_word()
                word_x = 0
                user_text = ''

    # Update word position
    word_x += speed
    if word_x > screen_width:
        current_word, difficulty = get_new_word()
        word_x = 0
        user_text = ''

    # Render text
    word_render = font.render(current_word, True, BLACK)
    input_render = font.render(user_text, True, BLACK)
    score_render = font.render(f"Score: {score}", True, BLACK)

    screen.blit(word_render, (word_x, word_y))
    screen.blit(input_render, (50, screen_height - 40))
    screen.blit(score_render, (screen_width - 150, 10))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
