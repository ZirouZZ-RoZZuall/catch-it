from turtle import *

total_score = 0
class Sprite(Turtle):
    
    def __init__(self,x,y,color = 'red',shape = 'square',step = 10):
        super().__init__()
        self.color(color)
        self.shape(shape)
        self.step = step
        self.penup()
        self.goto(x,y)
        #self.speed(10)

    def move_left(self):
        self.goto(self.xcor() - self.step,self.ycor())

    def move_right(self):
        self.goto(self.xcor() + self.step,self.ycor())

    def move_down(self):
        self.goto(self.xcor(),self.ycor() - self.step)

    def move_up(self):
        self.goto(self.xcor(),self.ycor() + self.step)
    
    def is_collide(self,sprite_finish):

        dis = self.distance(sprite_finish.xcor(),sprite_finish.ycor())
        if dis < 30:
            return True
        else:
            return False


sprite = Sprite(0,-200,'orange','circle',10)
sprite_sqr = Sprite(-200,100)
sprite_sqr1 = Sprite(200,-100)
sprite_finish = Sprite(0,250,'green','triangle')

#sprite_sqr.goto(x,y)

scr = sprite.getscreen()


#scr.onkey(keyUp,'Up')

scr.onkey(sprite.move_left,'Left')
scr.onkey(sprite.move_right,'Right')
scr.onkey(sprite.move_down,'Down')
scr.onkey(sprite.move_up,'Up')

scr.listen()



while total_score < 3:
    if sprite.is_collide(sprite_finish) == True:
        total_score += 1
        sprite.goto(0,-200)
    if sprite.is_collide(sprite_sqr) == True or sprite.is_collide(sprite_sqr1) == True:
        sprite_finish.hideturtle()
        break

if total_score == 3:
    sprite_sqr.hideturtle()
    sprite_sqr1.hideturtle()
