from turtle import *

total_score = 0
class Sprite(Turtle):
    
    def __init__(self,x,y,step = 10,color = 'red',shape = 'square'):
        super().__init__()
        self.color(color)
        self.shape(shape)
        self.step = step
        self.penup()
        self.goto(x,y)
        self.speed(10)

    def set_move(self,x_start,y_start,x_end,y_end):
        self.x_start = x_start
        self.y_start = y_start
        self.x_end = x_end
        self.y_end = y_end
        self.goto(x_start,y_start)
        self.setheading(self.towards(self.x_end,self.y_end))


    def make_step(self):
        #ход
        self.forward(self.step)
        #проверяю
        if self.step > self.distance(self.x_end,self.y_end):
        #поворачиваю меняя
            self.set_move(self.x_end,self.y_end,self.x_start,self.y_start)

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

speed_enemy = 0
speed_player = 0
choice = input('Выберите сложность:\n1 - лёгкая\n2 - сложная')
if choice == '1':
    speed_enemy = 8
    speed_player = 15
else:
    speed_enemy = 20
    speed_player = 5

sprite = Sprite(0,-200,speed_player,'orange','circle')
sprite_sqr = Sprite(-200,100,speed_enemy)
sprite_sqr.set_move(-200,100,200,100)
sprite_sqr1 = Sprite(200,-100,speed_enemy)
sprite_sqr1.set_move(200,-100,-200,-100)
sprite_finish = Sprite(0,250,0,'green','triangle')

scr = sprite.getscreen()

scr.onkey(sprite.move_left,'Left')
scr.onkey(sprite.move_right,'Right')
scr.onkey(sprite.move_down,'Down')
scr.onkey(sprite.move_up,'Up')

scr.listen()


while total_score < 3:
    sprite_sqr.make_step()
    sprite_sqr1.make_step()

    if sprite.is_collide(sprite_finish) == True:
        total_score += 1
        sprite.goto(0,-200)
    if sprite.is_collide(sprite_sqr) == True or sprite.is_collide(sprite_sqr1) == True:
        sprite_finish.hideturtle()
        break

if total_score == 3:
    sprite_sqr.hideturtle()
    sprite_sqr1.hideturtle()
