#Part D) Option 1 and Option 5
import turtle, random

class Game:
    '''
    Purpose: Represents the Snake Game
    Instance variables: 
        self.player: Represents that player's snake
        self.apple: Represents the food for the snake
    Methods: 
        init: Sets up the game board and creates two instance variables
        gameloop: Main loop that checks for collisions, and updates snake's movement
    '''

    def __init__(self):
        #Setup 700x700 pixel window
        turtle.setup(700, 700)

        #Bottom left of screen is (-40, -40), top right is (640, 640)
        turtle.setworldcoordinates(-40, -40, 640, 640)
        cv = turtle.getcanvas()
        cv.adjustScrolls()

        #Ensure turtle is running as fast as possible
        turtle.hideturtle()
        turtle.delay(0)
        turtle.tracer(0, 0)
        turtle.speed(0)

        #Draw the board as a square from (0,0) to (600,600)
        for i in range(4):
            turtle.forward(600)
            turtle.left(90)
        
        self.player = Snake(315, 315, 'green')
        self.apple = Food()

        self.gameloop()
        turtle.onkeypress(self.player.go_down, 'Down')
        turtle.onkeypress(self.player.go_up, 'Up')
        turtle.onkeypress(self.player.go_left, 'Left')
        turtle.onkeypress(self.player.go_right, 'Right')

        

        #These two lines must always be at the BOTTOM of __init__
        turtle.listen()
        turtle.mainloop()

        

    def gameloop(self):
        collide = Snake.collision(self.player)
        if collide == True:
            turtle.penup()
            turtle.goto(300, 300)
            turtle.write('Game Over', align='center', font=('Arial', 60, 'bold'))
        else:
            Snake.move(self.player, self.apple)
            turtle.ontimer(self.gameloop, 200)
        turtle.update()
    



class Snake:
    '''
    Purpose: Represents the Snake in the game
    Instance variables: 
        self.x: an integer represents the x-coord of the snake's head
        self.y: an integer represents the y-coord of the snake's head
        self.color: the color of the snake's head (str)
        self.segments: a list that stores the different segments of the snake (list)
        self.vx: an integer representing the velocity of the snake across the x-axis
        self.vy: an integer representing the veolicty of the snake across the y-axis
    Methods: 
        init: creates the instance variables of the snake
        grow: creates a segment and adds it to the snake
        move: updates the position of the snake and calls the grow method if the snake's head goes through a food
        go_down/up/right/left: changes the velocity of the snake to move in a direction
        collision: checks for collisions with the wall and the snake's own body. If a collision occurs, it stops the game
    '''

    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        self.segments = []
        self.vx = 30
        self.vy = 0
        self.grow()
        
    def grow(self):
        self.head = turtle.Turtle()
        self.head.speed(0)
        self.head.fillcolor(self.color)
        self.head.shape("square")
        self.head.shapesize(1.5)
        self.head.penup()
        self.head.setpos(self.x, self.y)
        self.segments.append(self.head)
        

    def move(self, food):
        self.x += self.vx 
        self.y += self.vy
        self.food = food
        self.head.setpos(self.x, self.y)
        head_pos = self.head.pos()
        if Food.food_pos(self.food) == head_pos:
            self.grow()
            self.food.change_pos()
        else:
            for i in range(len(self.segments)-1):
                self.x = self.segments[i+1].xcor()
                self.y = self.segments[i+1].ycor()
                self.segments[i].setpos(self.x, self.y)
        self.head.setpos(self.x, self.y)

    def go_down(self):
        self.vx = 0
        self.vy = -30
    def go_up(self):
        self.vx = 0
        self.vy = 30
    def go_right(self):
        self.vx = 30
        self.vy = 0
    def go_left(self):
        self.vx = -30
        self.vy = 0
    def collision(self):
        x = self.head.xcor()
        y = self.head.ycor()
        if x < 0 or x > 600 or y < 0 or y > 600:
            return True
        for segment in self.segments[:-2]:
            seg_x = segment.xcor()
            seg_y = segment.ycor()
            if seg_x == x and seg_y == y:
                return True
        return False



class Food:
    '''
    Purpose: Represents the food in the snake game
    Instance variables: 
        self.x: a random x-coord in the board for the food to spawn
        self.y: a random y-coord in the board for the food to spawn
    Methods: 
        init: creates the instance variables and calls the spawn_food method
        spawn_food: creates a food item and spawns it somewhere on the board
        food_pos: returns the position of the food
        change_pos: changes the position pf the food after it as been eaten
    '''

    def __init__(self):
        self.x = 15 + 30*random.randint(0,19)
        self.y = 15 + 30*random.randint(0,19)
        self.spawn_food()

    def spawn_food(self):
        self.food = turtle.Turtle()
        self.food.fillcolor('Red')
        self.food.shape('circle')
        self.food.shapesize(1.5)
        self.food.penup()
        self.food.setpos(self.x, self.y)
    def food_pos(self):
        return (self.x, self.y)
    
    def change_pos(self):
        self.x = 15 + 30*random.randint(0,19)
        self.y = 15 + 30*random.randint(0,19)
        self.food.setpos(self.x, self.y)





        
if __name__ == '__main__':
    Game()
