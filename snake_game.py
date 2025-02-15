import pygame
import random
from flask import Flask, render_template, Response
import io
from PIL import Image

# Initialize Flask app
app = Flask(__name__)

# Initialize pygame
pygame.init()

# Game Settings
WIDTH = 640
HEIGHT = 480
snake_block = 10
snake_speed = 15
font_style = pygame.font.SysFont("bahnschrift", 25)

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (213, 50, 80)
GREEN = (0, 255, 0)
BLUE = (50, 153, 213)

# Game variables
x1 = WIDTH / 2
y1 = HEIGHT / 2
x1_change = 0
y1_change = 0
snake_List = []
Length_of_snake = 1

foodx = round(random.randrange(0, WIDTH - snake_block) / 10.0) * 10.0
foody = round(random.randrange(0, HEIGHT - snake_block) / 10.0) * 10.0

# Flask route for main game page
@app.route('/')
def index():
    return render_template('index.html')

# Function to draw the snake
def our_snake(snake_block, snake_List):
    for x in snake_List:
        pygame.draw.rect(game_screen, BLACK, [x[0], x[1], snake_block, snake_block])

# Generate image of the current game state
def generate_image():
    # Create a Pygame screen object
    global game_screen
    game_screen = pygame.Surface((WIDTH, HEIGHT))
    game_screen.fill(BLUE)
    pygame.draw.rect(game_screen, GREEN, [foodx, foody, snake_block, snake_block])

    # Draw snake
    snake_Head = []
    snake_Head.append(x1)
    snake_Head.append(y1)
    snake_List.append(snake_Head)
    if len(snake_List) > Length_of_snake:
        del snake_List[0]

    for x in snake_List[:-1]:
        if x == snake_Head:
            pass  # Game over condition, we could reset it here if desired.

    our_snake(snake_block, snake_List)

    # Convert to a format Flask can serve (PIL image)
    image = Image.frombytes('RGB', (WIDTH, HEIGHT), game_screen.get_buffer())
    return image

# Route to serve the game state as an image
@app.route('/game')
def game():
    img = generate_image()
    img_io = io.BytesIO()
    img.save(img_io, 'PNG')
    img_io.seek(0)
    return Response(img_io, mimetype='image/png')

if __name__ == '__main__':
    app.run(debug=True)
