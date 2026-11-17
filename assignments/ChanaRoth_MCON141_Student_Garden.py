import turtle
import random

def ret_random_pos():
    screen_width = screen.window_width()
    screen_height = screen.window_height()

    rand_x = random.randint(int(screen_width / 2) * -1, int(screen_width / 2) )
    rand_y = random.randint(int(screen_height / 2) * -1, int(screen_height / 2) )


    print(f"random {rand_x} {rand_y}")
    return rand_x, rand_y


def one_square():
#code below converts mouse pointers current position to turtle coordinates.
    canvas = screen.getcanvas()
    mouse_x = canvas.winfo_pointerx() - canvas.winfo_rootx() - (screen.window_width()/2)
    mouse_y = (screen.window_height()/2) - (canvas.winfo_pointery() - canvas.winfo_rooty())
    pen.penup()
    pen.goto(mouse_x, mouse_y)
    pen.pendown()


    color1 = random.choice(colors)
    color2 = random.choice(colors)
    length = 100
    pen.color(color1)
    pen.pensize(30)
    pen.shape("turtle")
    pen.fillcolor(color2)
    pen.begin_fill()
    for side in range(4):
        pen.forward(length)
        pen.right(90)
    pen.end_fill()
    pen.penup()


def draw_many_squares(pen):
    for i in range(10):
        outer_color = random.choice(colors)
        inner_color = random.choice(colors)

        pen.penup()
        rand_x, rand_y = ret_random_pos()
        pen.goto(rand_x, rand_y)
        pen.pendown()
        one_square()
        pen.penup()

def draw_flower(x,y):
    pen.penup()
    # rand_x, rand_y = ret_random_pos()
    pen.pensize(1)
    pen.goto(x,y)
    pen.pendown()

    pen.fillcolor(random.choice(colors))
    pen.begin_fill()
    for petal in range(8):
        pen.circle(30)
        pen.right(45)
    pen.end_fill()

    pen.penup()


def draw_many_flowers(pen):
    pen.pensize(4)
    for i in range(40):
        draw_flower(*ret_random_pos())

#new function to clear page of all drawings - later see can be done by clicking c key.
def clear_garden():
    pen.clear()

#added/replaced 3 colors to the color list.
colors  = [
   "hot pink",
   "coral",
   "tomato",
   "orange",
   "gold",
   "yellow",
   "orchid",
   "violet",
   "purple",
   "magenta",
   "deep pink",
   "turquoise",
   "medium aquamarine",
   "sky blue",
   "plum",
   "salmon",
   "light pink",
   "medium violet red",
   "forest green",
   "red",
   "white"
]

screen = turtle.Screen()
screen.title("My Screen")
screen.bgcolor("green") #changed from hot pink to this green background.

pen = turtle.Turtle()
pen.speed(0)
pen.penup()

# TODO: Register draw_flower as the mouse-click handler.
# TODO: Register one_square with the "a" key.
# TODO: Enable keyboard listening.

screen.onclick(draw_flower)
screen.onkey(one_square, "a")
screen.onkey(clear_garden, "c")#new feature for clearing whole page.
screen.listen()



turtle.done()


#Project Explanation:
# I chose option A - The student garden. For the new keyboard command, I added the clearing page function (clear_garden()). This allows the user to press the key "c" to erase the whole page of any drawings. In order to clear I used the pen.clear() with screen.onkey(). Also I personalized my garden by changing the background from hot pink to green, and added/replaced 3 colors (red, forest green, and white) to the color list.