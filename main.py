import pygame 
from pygame.math import Vector2
import random
pygame.init()
cell_size= 40
cell_number=20
screen= pygame.display.set_mode((cell_size*cell_number,cell_size*cell_number))
pygame.display.set_caption("shake game ")
WHITE= (20,250,255)

class Snake:
    def __init__(self):
        self.body = [Vector2(7,10),Vector2(6,10),Vector2(5,10)]
        self.direction= Vector2(1,0)
        self.new_block= False
    def draw_snake(self):
        for block in self.body:
            block_rect= pygame.Rect(block.x*cell_size,block.y*cell_size,cell_size,cell_size)
            pygame.draw.rect(screen,(0,0,0), block_rect)

    def snake_move(self):
        if self.new_block:
            snake_copy= self.body[:]
            snake_copy.insert(0,snake_copy[0]+self.direction)
            self.body= snake_copy[:]
            self.new_block= False
        else:
            snake_copy= self.body[:-1]
            snake_copy.insert(0,snake_copy[0]+self.direction)
            self.body= snake_copy[:]

    def add_block(self):
        self.new_block=True
        
class Fruit:
    def __init__(self):
        self.randomize()
        
    def draw_fruit(self):
        fruit_rect= pygame.Rect(cell_size*self.pos.x, cell_size*self.pos.y,cell_size,cell_size)
        pygame.draw.rect(screen,(222,30,111),fruit_rect)

    def randomize(self):
        self.x= random.randint(0,cell_number-1)
        self.y= random.randint(0,cell_number-1)
        self.pos= Vector2(self.x, self.y)

class MAIN:
    def __init__(self) -> None:
        self.snake= Snake()
        self.fruit=Fruit()

    def update(self):
        self.snake.snake_move()
        self.check_collision()
        self.check_collision()
        self.check_fail()
        
    def drew(self):
        self.fruit.draw_fruit()
        self.snake.draw_snake()
    def check_collision(self):
        if self.snake.body[0]==self.fruit.pos:
            self.fruit.randomize()
            self.snake.add_block()

    def check_fail(self):
        for block in self.snake.body[1:]:
            if block == self.snake.body[0]:
                self.game_over()
        if not 0<= self.snake.body[0].x<cell_number or not 0<= self.snake.body[0].y<cell_number:
            self.game_over()        



    def game_over(self):
        pygame.quit()
        



        
main_game=MAIN()  
           
fruit= Fruit()
snake=Snake()
SCREEN_UPDADE= pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDADE,150)

running= True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running= False
        if event.type== SCREEN_UPDADE:
            main_game.update()
        if event.type== pygame.KEYDOWN:
            if event.key== pygame.K_UP:
                if main_game.snake.direction.y != 1:
                    main_game.snake.direction= Vector2(0,-1)
            if event.key== pygame.K_DOWN:
                if main_game.snake.direction.y != -1:
                    main_game.snake.direction= Vector2(0,1)
            if event.key== pygame.K_LEFT:
                if main_game.snake.direction.x != 1:
                    main_game.snake.direction= Vector2(-1,0)
            if event.key== pygame.K_RIGHT:
                if main_game.snake.direction.x != -1:
                    main_game.snake.direction= Vector2(1,0)

                
    screen.fill(WHITE)
    main_game.drew()
    
    pygame.display.update()

