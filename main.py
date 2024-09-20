import turtle
import guy
import gun
import enemies
import bullet
import score

turtle.speed(0)
screen = turtle.Screen()
turtle.bgcolor("black")

guy = guy.Guy(-650, 0)
gun = gun.Gun(-650, 0)
scores = score.Score()

PACE = 20

#draw line
def draw_line():
    """to draw a line"""
    turtle.setheading(90)
    turtle.setposition(-600, -325)
    turtle.color('white')
    
    for i in range(360//30):
        turtle.fd(30)
        turtle.penup()
        turtle.fd(30)
        turtle.pendown()
#draws the cross line        
draw_line()

all_enemies = [] #buffer to hold enemies

#listens to key presses on keyboard
turtle.listen()

#move guy and gun
def armed_guy_up():
    guy.move_up() # type: ignore
    gun.move_up() # type: ignore
def armed_guy_down():
    guy.move_down() # type: ignore # type
    gun.move_down() # type: ignore
    
#show score
scores.show_score()

game_on = True
while game_on:
    #contrls the pace of enemies object
    if scores.score > 55:
       PACE = 90
    elif scores.score > 45:
       PACE = 70
    elif scores.score > 25:
       PACE = 50
    elif scores.score > 15:
       PACE = 40
    #controls
    screen.onkey(fun=armed_guy_up, key="Up")
    screen.onkey(fun=armed_guy_down, key="Down")

    #enemies moving
    #spawn enemy
    enemy = enemies.Ops(PACE)
    all_enemies.append(enemy)
    for op in all_enemies:
        #moves all the enemies
        op.walk()
        if op.xcor() <= -640:
            #checks if guy has been hit
            game_on = False
            del guy
            scores.game_over()
            break
            
    #get the position of gun turtle object
    pos = gun.current_position 
    #passes as an arguement to bullet object
    bullets = bullet.Bullet(pos)

    #check if enemy hit
    #move bullet at certain velocity
    def shoot(op):
       for i in range(66):
           bullets.speed(6)
           bullets.setx(bullets.xcor()+20) #constant velocity
           for ops in all_enemies:
               if bullets.distance(ops) < 20:                  
                   ops.die()
                   del ops
                   scores.update_score()
    #shoot enemy
    shoot(op)
    
turtle.mainloop()