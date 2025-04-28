import pygame
from pygame import Vector2
pygame.init()

SIZE = WIDTH, HEIGHT = 1400,900
WIN = pygame.display.set_mode(SIZE)
CLOCK = pygame.time.Clock()

class Game():
    def __init__(self,screen,width,height):
        self.screen = screen
        self.width = width
        self.height = height
        self.x = 0
        self.y = 800
        # self.speed = 850
        self.level = 1
        # Scoring
        self.font = pygame.font.Font('Pixeltype.ttf',size = 30)
        self.death_count = 0

        self.onground = True

        self.beforetime = 0
        self.aftertime = 0
        
        self.collide = False

        self.velocity = 0
        self.velocity_rate = 100

        # Gravity
        self.gravity = Vector2(0,0)
        
        # Objects
        self.object_list = []

        # Hitbox
        self.hitboxes = []
        self.triangle_hitbox = pygame.Surface((60,60))
        self.triangle_hitbox.fill('red')
        self.triangle_hitbox_rect = None


        #Trianlge
        self.triangle = pygame.transform.scale(pygame.image.load('triangle.png'),(130,120))

        # Cube
        self.cube = pygame.Surface((80,80))
        self.cube_rect = self.cube.get_rect(bottomleft = (self.x,self.y))
        self.cube.fill('#68ad07')

        # Ground
        self.ground = pygame.Surface((self.width,100))
        self.ground_rect = self.ground.get_rect(topleft = (0,800))

    def draw_score(self):
        score_font = self.font.render(f'Room: {self.level}',False,'Green')
        death_count_font = self.font.render(f'Death Count: {self.death_count}',False,'green')
        self.screen.blit(score_font,(10,10))
        self.screen.blit(death_count_font,(700,10))

    def update(self,keys,dt):

        # Gravity
        self.gravity.y += 2
        self.y += self.gravity.y
        if self.y >= self.ground_rect.top:
            self.y = self.ground_rect.top
            self.onground = True
        
        # left right movement

        if not self.collide:
            if keys[pygame.K_d]:
                self.velocity += self.velocity_rate
                self.x += self.velocity *dt
                if self.velocity >= 830:
                    self.velocity = 830
                if self.cube_rect.right >= self.width:
                    # self.hitboxes.clear()
                    self.level += 1
                    self.x = 0
                    self.y = 800


            elif keys[pygame.K_a]:
                self.velocity += self.velocity_rate
                self.x -= self.velocity *dt
                if self.velocity >= 830:
                    self.velocity = 830
                if self.x <= 0:
                    self.x =0
            else:
                self.velocity = 0

            
        if self.collide:
            self.aftertime = pygame.time.get_ticks()
            if self.aftertime - self.beforetime >=200:
                self.collide = False
                self.velocity = 0

        

        self.cube_rect = self.cube.get_rect(bottomleft = (self.x,self.y))
        # self.cube_rect.x = self.x
        # self.cube_rect.bottom = self.y

    def draw_triangles(self,x,y):
        # y position should be 804 for  
        self.triangle_rect = self.triangle.get_rect(bottomleft = (x,y))
        self.triangle_hitbox_rect = self.triangle_hitbox.get_rect(bottomleft= (x+35,y-4))
        self.hitboxes.append(self.triangle_hitbox_rect)
        self.screen.blit(self.triangle,self.triangle_rect)

    def main_screen(self):
        ...
    
    def collision(self):
        if self.triangle_hitbox_rect:
            for hitbox in self.hitboxes:
                if self.cube_rect.colliderect(hitbox):
                    self.hitboxes.clear()
                    self.x = 0
                    self.screen.fill('black')
                    self.beforetime = pygame.time.get_ticks()
                    self.collide = True
                    self.death_count += 1

        for object in self.object_list:
            if self.cube_rect.colliderect(object):
                if self.cube_rect.top < object.bottom:
                    self.gravity.y = - self.gravity.y
                    self.object_list.clear()
                
               
    def objects(self,width,height,x,y):
        self.object = pygame.Surface((width,height))
        self.object.fill('black')
        self.object_rect = self.object.get_rect(bottomleft = (x,y))
        self.object_list.append(self.object_rect)
        self.screen.blit(self.object,self.object_rect)

    def level1(self):
        # screen
        self.screen.fill('#b88dc4')
        self.screen.blit(self.cube,self.cube_rect)

        # Ground
        self.ground.fill('Black')
        self.screen.blit(self.ground,self.ground_rect)

    def level2(self):
        # Screen
        self.screen.fill('#b881c7')

        # Ground
        self.ground.fill('black')
        self.screen.blit(self.ground,self.ground_rect)
        
        # Triangle
        self.draw_triangles(700,804)
       
        # Cube
        self.screen.blit(self.cube,self.cube_rect)

    def level3(self):
        # Screen
        self.screen.fill('#b972cc')

        # Ground
        self.ground.fill('black')
        self.screen.blit(self.ground,self.ground_rect)
        
        # Triangle
        self.draw_triangles(700,804)
        self.draw_triangles(600,804)
        
        # Cube
        self.screen.blit(self.cube,self.cube_rect)   

    def level4(self):
        # Screen
        self.screen.fill('#9e52b3')

        # Ground
        self.ground.fill('black')
        self.screen.blit(self.ground,self.ground_rect)
        
        # Cube
        self.screen.blit(self.cube,self.cube_rect)
        # Triangle
        self.draw_triangles(700,804)
        self.draw_triangles(600,804)
        self.draw_triangles(800,804)

    def level5(self): # 2x2 spikes
        # Screen
        self.screen.fill('#873b9c')

        # Ground
        self.ground.fill('black')
        self.screen.blit(self.ground,self.ground_rect)
        
        # Cube
        self.screen.blit(self.cube,self.cube_rect)

        # Triangle
        self.draw_triangles(700,804)
        self.draw_triangles(600,804)
        self.draw_triangles(800,804)
        self.draw_triangles(900,804)

    def level6(self):# medium 4 spikes
        # Screen
        self.screen.fill('#68277a')

        # Ground
        self.ground.fill('black')
        self.screen.blit(self.ground,self.ground_rect)
        
        # Cube
        self.screen.blit(self.cube,self.cube_rect)

        # Triangle
        self.draw_triangles(200,804)
        self.draw_triangles(500,804)
        self.draw_triangles(800,804)
        self.draw_triangles(1100,804)

    def level7(self): # 2x2x2x2 spikes normal
        # Screen
        self.screen.fill('#531a63')

        # Ground
        self.ground.fill('black')
        self.screen.blit(self.ground,self.ground_rect)
        
        # Cube
        self.screen.blit(self.cube,self.cube_rect)

        # Triangle
        self.draw_triangles(200,804)
        self.draw_triangles(310,804)

        self.draw_triangles(500,804)
        self.draw_triangles(610,804)

        self.draw_triangles(800,804)
        self.draw_triangles(910,804)

        self.draw_triangles(1100,804)
        self.draw_triangles(1210,804)

    def level8(self): #Hard 4 spikes x2
        # Screen
        self.screen.fill('#531a63')

        # Ground
        self.ground.fill('black')
        self.screen.blit(self.ground,self.ground_rect)
        
        # Cube
        self.screen.blit(self.cube,self.cube_rect)

        # Triangle
        self.draw_triangles(200,804)
        self.draw_triangles(300,804)
        self.draw_triangles(400,804)
        self.draw_triangles(505,804)

        self.draw_triangles(800,804)
        self.draw_triangles(900,804)
        self.draw_triangles(1000,804)
        self.draw_triangles(1105,804)

    def level9(self): # Hard
        # Screen
        self.screen.fill('#3a0947')

        # Ground
        self.ground.fill('black')
        self.screen.blit(self.ground,self.ground_rect)
        
        # Cube
        self.screen.blit(self.cube,self.cube_rect)

        # Triangle
        self.draw_triangles(100,804)
        self.draw_triangles(200,804)
        self.draw_triangles(300,804)

        self.draw_triangles(500,804)

        self.draw_triangles(600,804)

        self.draw_triangles(800,804)
        self.draw_triangles(890,804)

        self.draw_triangles(980,804)
        self.draw_triangles(1080,804)

        self.draw_triangles(1300,804)

    def level10(self):
        # Screen
        self.screen.fill('#2b0236')

        # Ground
        self.ground.fill('black')
        self.screen.blit(self.ground,self.ground_rect)
        
        # Cube
        self.screen.blit(self.cube,self.cube_rect)

        # Triangle
        self.draw_triangles(100,804)
        self.draw_triangles(200,804)
        self.draw_triangles(300,804)

        self.draw_triangles(500,804)
        self.draw_triangles(600,804)
        self.draw_triangles(700,804)


        # self.draw_triangles(1100,804)
        # self.draw_triangles(1200,804)

        self.draw_triangles(900,804)
        self.draw_triangles(998,804)
        self.draw_triangles(1096,804)
        self.draw_triangles(1195,804)

    def level11(self):
        # Screen
        self.screen.fill('#b881c7')

        # Ground
        self.ground.fill('black')
        self.screen.blit(self.ground,self.ground_rect)
        
        # Triangle
        self.draw_triangles(700,804)

       
        # Cube
        self.screen.blit(self.cube,self.cube_rect)

        #Object
        self.objects(1400,100,0,550)

    def level12(self):
        # Screen
        self.screen.fill('#b881c7')

        # Ground
        self.ground.fill('black')
        self.screen.blit(self.ground,self.ground_rect)
        
        # Triangle
        self.draw_triangles(700,804)

       
        # Cube
        self.screen.blit(self.cube,self.cube_rect)

        #Object
        self.objects(1400,100,0,570)

    def level13(self):
        # Screen
        self.screen.fill('#b881c7')

        # Ground
        self.ground.fill('black')
        self.screen.blit(self.ground,self.ground_rect)
        
        # Triangle
        self.draw_triangles(700,804)
        

       
        # Cube
        self.screen.blit(self.cube,self.cube_rect)

        #Object
        self.objects(1400,100,0,585)

    def level14(self):
        # Screen
        self.screen.fill('#b881c7')

        # Ground
        self.ground.fill('black')
        self.screen.blit(self.ground,self.ground_rect)
        
        # Triangle
        self.draw_triangles(700,804)
        self.draw_triangles(800,804)

        # Cube
        self.screen.blit(self.cube,self.cube_rect)

        #Object
        self.objects(1400,100,0,500)

    def level15(self):
        # Screen
        self.screen.fill('#b881c7')

        # Ground
        self.ground.fill('black')
        self.screen.blit(self.ground,self.ground_rect)
        
        # Triangle
        self.draw_triangles(700,804)
        self.draw_triangles(800,804)
       
        # Cube
        self.screen.blit(self.cube,self.cube_rect)

        #Object
        self.objects(1400,100,0,525)

    def level16(self):
        # Screen
        self.screen.fill('#b881c7')

        # Ground
        self.ground.fill('black')
        self.screen.blit(self.ground,self.ground_rect)
        
        # Triangle
        self.draw_triangles(700,804)
        self.draw_triangles(800,804)
        self.draw_triangles(600,804)

        # Cube
        self.screen.blit(self.cube,self.cube_rect)

        #Object
        self.objects(1400,100,0,485)

game = Game(WIN,WIDTH,HEIGHT)

def levels():
    if game.level == 0:
        game.level0()
    if game.level == 1:
        game.level1()
    elif game.level == 2:
        game.level2()
    elif game.level == 3:
        game.level3()
    elif game.level == 4:
        game.level4()
    elif game.level == 5:
        game.level5()
    if game.level ==6:
        game.level6()
    elif game.level == 7:
        game.level7()
    elif game.level == 8:
        game.level8()
    elif game.level == 9:
        game.level9()
    elif game.level == 10:
        game.level10()
    if game.level ==11:
        game.level11()
    elif game.level == 12:
        game.level12()
    elif game.level == 13:
        game.level13()
    elif game.level == 14:
        game.level14()
    elif game.level == 15:
        game.level15()
    if game.level ==16:
        game.level16()
while True:
    dt = CLOCK.tick(60) / 1000
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if game.onground:
            if event.type == pygame.MOUSEBUTTONDOWN:
                game.gravity.y = -33
                game.onground = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE or event.key == pygame.K_w:
                    game.gravity.y = -33
                    game.onground = False

    keys = pygame.key.get_pressed()
    game.update(keys,dt)
    levels()
    game.draw_score()
    game.collision()

    # game.screen.blit(game.score_font,(10,10))
    
    pygame.display.update()
