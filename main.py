# Constantes
WIDTH = 640
HEIGHT = 480
GRID_SIZE = 20

# Couleurs
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Création de la fenêtre
import turtle
screen = turtle.Screen()
screen.setup(width=WIDTH, height=HEIGHT)
screen.bgcolor(WHITE)
screen.title('Snake')

# Création du serpent et de la nourriture
import turtle
snake = turtle.Turtle()
snake.speed(0)
snake.shape('square')
snake.color(GREEN)
snake.penup()
snake.goto(200, 200)

food = turtle.Turtle()
food.speed(0)
food.shape('circle')
food.color(RED)
food.penup()
food.goto(random.randint(0, WIDTH//GRID_SIZE) * GRID_SIZE, random.randint(0, HEIGHT//GRID_SIZE) * GRID_SIZE)

# Variables de déplacement
dx = 0
dy = 0

# Fonction pour déplacer le serpent
def move_snake():
    global dx, dy, snake
    new_head = (snake.xcor() + dx, snake.ycor() + dy)
    snake.goto(new_head)

# Fonction pour détecter la collision avec la nourriture
def detect_food_collision():
    global food, snake
    if snake.distance(food) < 20:
        food.goto(random.randint(0, WIDTH//GRID_SIZE) * GRID_SIZE, random.randint(0, HEIGHT//GRID_SIZE) * GRID_SIZE)
        snake.goto(snake.xcor() + 20, snake.ycor())

# Fonction pour détecter la collision avec les murs
def detect_wall_collision():
    global dx, dy, snake
    if snake.xcor() < -WIDTH/2 or snake.xcor() > WIDTH/2 or snake.ycor() < -HEIGHT/2 or snake.ycor() > HEIGHT/2:
        snake.goto(0, 0)

# Fonction pour détecter la collision avec le corps du serpent
def detect_self_collision():
    global dx, dy, snake
    segments = snake.get_segments()
    if segments[0] in segments[1:]:
        snake.goto(0, 0)

# Boucle principale du jeu
import time
import random
while True:
    screen.update()

    # Gestion des événements
    for event in turtle.event.get():
        if event.type == turtle.ONKEYPRESS:
            if event.key == 'Up':
                dx = 0
                dy = -GRID_SIZE
            if event.key == 'Down':
                dx = 0
                dy = GRID_SIZE
            if event.key == 'Left':
                dx = -GRID_SIZE
                dy = 0
            if event.key == 'Right':
                dx = GRID_SIZE
                dy = 0

    # Mise à jour de la position du serpent
    move_snake()

    # Vérification de la collision avec la nourriture
    detect_food_collision()

    # Vérification de la collision avec les murs
    detect_wall_collision()

    # Vérification de la collision avec le corps du serpent
    detect_self_collision()

    time.sleep(0.1)

turtle.done()