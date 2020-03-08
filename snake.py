import turtle
import time
import random
import ctypes

# Pisteet
score = 0
high_score = 0

# Luodaan pelikenttä
win = turtle.Screen()
win.title("Matopeli")
win.bgcolor("Black")
win.setup(width=600, height=600)
win.tracer(0)
delay = 0.1

# Luodaan käärmeen pää ruudulle
head = turtle.Turtle()
head.speed(0)
head.shape("circle")
head.color("Green")
head.penup()
head.goto(0,0)
head.direction = "stop"

# Näytetään ruoka ruudulla
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0,100)

# käärmeen keho
body = []

# Näytetään pisteet ruudulla
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: 0  High Score: 0", align="center", font=("Comic Sans", 24, "normal"))

# määritetään miten käärme liikkuu
def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":
        head.direction = "right"

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

# Luodaan kuuntelija joka katsoo mitä nappeja painetaan
# ja sen perusteella määrätään mitä tapahtuu
# jos esim painetaan "w" näppäintä, niin käärme lähtee ylös
win.listen()
win.onkeypress(go_up, "w")
win.onkeypress(go_down, "s")
win.onkeypress(go_left, "a")
win.onkeypress(go_right, "d")

# itse pelin looppi
while True:
    win.update()

    # Jos käärme menee rajojen ulkopuolelle: peli päättyy
    if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
        head.goto(0,0)
        head.direction = "stop"
        ctypes.windll.user32.MessageBoxW(0, "HÄHÄÄ, HÄVISIT", "", 1)

        # Poistetaan kuollut käärme näytöltä
        for bod in body:
            bod.goto(1000, 1000)
        
        # Nollataan käärmeen pituus
        body.clear()

        # Nollataan pisteet
        score = 0

        pen.clear()
        pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Comic Sans", 24, "normal")) 


    # Jos käärme syö ruoan niin se kasvaa yhdellä ja uusi ruoka arvotaan.
    if head.distance(food) < 20:
        # arvotaan omenan uusi paikka
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x,y)

        # lisätään käärmeen pituutta
        new_bod = turtle.Turtle()
        new_bod.speed(0)
        new_bod.shape("square")
        new_bod.color("green")
        new_bod.penup()
        body.append(new_bod)


        # Lisätään pisteitä
        score += 10

        if score > high_score:
            high_score = score
        
        pen.clear()
        pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Comic Sans", 24, "normal")) 

    # Näiden kahden avulla käärmeen keho kulkee pään perässä
    for index in range(len(body)-1, 0, -1):
        x = body[index-1].xcor()
        y = body[index-1].ycor()
        body[index].goto(x, y)

    if len(body) > 0:
        x = head.xcor()
        y = head.ycor()
        body[0].goto(x,y)

    move()    

    # Jos käärme osuu itseensä, peli loppuu.
    for bod in body:
        if bod.distance(head) < 20:
            time.sleep(1)
            head.goto(0,0)
            head.direction = "stop"
            ctypes.windll.user32.MessageBoxW(0, "HÄHÄÄ, HÄVISIT", "Luuseri", 1)
        
            # Tyhjennetään lista
            for bod in body:
                bod.goto(1000, 1000)

            body.clear()

            # Nollataan pisteet
            score = 0

            # Päivitetään pisteet
            pen.clear()
            pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Comic Sans", 24, "normal"))

    time.sleep(delay)

win.mainloop()