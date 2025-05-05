import pygame
from pyautogui import size
from pygame import Vector2
pygame.init()
pygame.mixer.init()
WIDTH, HEIGHT = size()
# WIDTH = 1900
HEIGHT = HEIGHT-100

WIN = pygame.display.set_mode((WIDTH,HEIGHT))
CLOCK = pygame.time.Clock()
pygame.mouse.set_visible(False)
class Game():
    def __init__(self,screen,width,height):
        self.screen = screen
        self.width = width
        self.height = height
        self.x = 0
        self.y = self.height -100
        # self.speed = 850
        self.level = 1
        # Scoring
        self.font = pygame.font.Font('assets/font/Pixeltype.ttf',size = 60)
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
        self.triangle = pygame.transform.scale(pygame.image.load('assets/triangle.png'),(130,120))

        # Cube
        self.cube = pygame.Surface((80,80))
        self.cube_rect = self.cube.get_rect(bottomleft = (self.x,self.y))
        self.cube.fill('#68ad07')

        # Ground
        self.ground = pygame.Surface((self.width,100))
        self.ground_rect = self.ground.get_rect(topleft = (0,self.height-100))

        #collision sound
        self.sound = pygame.mixer.Sound('assets/music/collision.wav')

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
                    self.y = self.height - 100


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
        self.triangle_rect = self.triangle.get_rect(bottomleft = (x,self.height-96))
        self.triangle_hitbox_rect = self.triangle_hitbox.get_rect(bottomleft= (x+35,self.height-100))
        self.hitboxes.append(self.triangle_hitbox_rect)
        self.screen.blit(self.triangle,self.triangle_rect)
        # self.screen.blit(self.triangle_hitbox,self.triangle_hitbox_rect)

    def collision(self):
        if self.triangle_hitbox_rect:
            for hitbox in self.hitboxes:
                if self.cube_rect.colliderect(hitbox):
                    self.sound.play()
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
        self.object = pygame.Surface((self.width,self.height))
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
        self.draw_triangles(((self.width/2)+300)-self.width/4,804)
       
        # Cube
        self.screen.blit(self.cube,self.cube_rect)

    def level3(self):
        # Screen
        self.screen.fill('#b972cc')

        # Ground
        self.ground.fill('black')
        self.screen.blit(self.ground,self.ground_rect)
        
        # Triangle
        self.draw_triangles(((self.width/2)+200)-self.width/4,804)
        self.draw_triangles(((self.width/2)+300)-self.width/4,804)
        
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
        # # Triangle

        self.draw_triangles((self.width/2)+200-self.width/4,804)
        self.draw_triangles(((self.width/2)+400)-self.width/4,804)

        self.draw_triangles(((self.width/2)+300)-self.width/4,804)

    def level5(self): # 2x2 spikes
        # Screen
        self.screen.fill('#873b9c')

        # Ground
        self.ground.fill('black')
        self.screen.blit(self.ground,self.ground_rect)
        
        # Cube
        self.screen.blit(self.cube,self.cube_rect)

        # Triangle

        self.draw_triangles((self.width/2)+400-self.width/4,804)
        self.draw_triangles(((self.width/2)+100)-self.width/4,804)

        self.draw_triangles(((self.width/2)+200)-self.width/4,804)
        self.draw_triangles(((self.width/2)+300)-self.width/4,804)

    def level6(self):# medium 4 spikes
        # Screen
        self.screen.fill('#68277a')

        # Ground
        self.ground.fill('black')
        self.screen.blit(self.ground,self.ground_rect)
        
        # Cube
        self.screen.blit(self.cube,self.cube_rect)

        # # Triangle
        # self.draw_triangles(200,804)
        # self.draw_triangles(500,804)

        # self.draw_triangles(800,804)
        # self.draw_triangles(1100,804)

        self.draw_triangles((self.width/2)-200-self.width/4,804)
        self.draw_triangles(((self.width/2)+100)-self.width/4,804)

        self.draw_triangles(((self.width/2)+700)-self.width/4,804)
        self.draw_triangles(((self.width/2)+400)-self.width/4,804)

        self.draw_triangles(((self.width/2)+1000)-self.width/4,804)

    def level7(self): # 2x2x2x2 spikes normal
        # Screen
        self.screen.fill('#531a63')

        # Ground
        self.ground.fill('black')
        self.screen.blit(self.ground,self.ground_rect)
        
        # Cube
        self.screen.blit(self.cube,self.cube_rect)

        # Triangle

        self.draw_triangles((self.width/2)-200-self.width/4,804)
        self.draw_triangles(((self.width/2)-90)-self.width/4,804)

        self.draw_triangles(((self.width/2)+185)-self.width/4,804)
        self.draw_triangles(((self.width/2)+295)-self.width/4,804)

        self.draw_triangles((self.width/2)+485-self.width/4,804)
        self.draw_triangles(((self.width/2)+595)-self.width/4,804)

        self.draw_triangles(((self.width/2)+785)-self.width/4,804)
        self.draw_triangles(((self.width/2)+895)-self.width/4,804)

    def level8(self): #Hard 4 spikes x2
        # Screen
        self.screen.fill('#531a63')

        # Ground
        self.ground.fill('black')
        self.screen.blit(self.ground,self.ground_rect)
        
        # Cube
        self.screen.blit(self.cube,self.cube_rect)

        # Triangle
        # self.draw_triangles(200,804)
        # self.draw_triangles(300,804)
        # self.draw_triangles(400,804)
        # self.draw_triangles(505,804)

        self.draw_triangles((self.width/2)-200-self.width/4,804)
        self.draw_triangles(((self.width/2)-100)-self.width/4,804)
        self.draw_triangles(((self.width/2))-self.width/4,804)
        self.draw_triangles(((self.width/2)+100)-self.width/4,804)

        self.draw_triangles((self.width/2)+395-self.width/4,804)
        self.draw_triangles(((self.width/2)+495)-self.width/4,804)
        self.draw_triangles(((self.width/2)+595)-self.width/4,804)
        self.draw_triangles(((self.width/2)+700)-self.width/4,804)

    def level9(self): # Hard
        # Screen
        self.screen.fill('#3a0947')

        # Ground
        self.ground.fill('black')
        self.screen.blit(self.ground,self.ground_rect)
        
        # Cube
        self.screen.blit(self.cube,self.cube_rect)

        # Triangle

        self.draw_triangles((self.width/2)-200-self.width/4,804)
        self.draw_triangles(((self.width/2)-100)-self.width/4,804)
        self.draw_triangles(((self.width/2))-self.width/4,804)


        self.draw_triangles((self.width/2)+200-self.width/4,804)
        self.draw_triangles(((self.width/2)+300)-self.width/4,804)

        self.draw_triangles((self.width/2)+500-self.width/4,804)
        self.draw_triangles(((self.width/2)+590)-self.width/4,804)
        self.draw_triangles(((self.width/2)+680)-self.width/4,804)
        self.draw_triangles(((self.width/2)+790)-self.width/4,804)

        self.draw_triangles((self.width/2)+1010-self.width/4,804)

    def level10(self):
        # Screen
        self.screen.fill('#2b0236')

        # Ground
        self.ground.fill('black')
        self.screen.blit(self.ground,self.ground_rect)
        
        # Cube
        self.screen.blit(self.cube,self.cube_rect)

        # Triangle
        # self.draw_triangles((self.width/2)-self.width/4,804)
        # self.draw_triangles(200,804)
        # self.draw_triangles(300,804)

        self.draw_triangles((self.width/2)-200-self.width/4,804)
        self.draw_triangles(((self.width/2)-100)-self.width/4,804)
        self.draw_triangles(((self.width/2))-self.width/4,804)

        self.draw_triangles((self.width/2)+200-self.width/4,804)
        self.draw_triangles(((self.width/2)+300)-self.width/4,804)
        self.draw_triangles(((self.width/2)+400)-self.width/4,804)


        self.draw_triangles((self.width/2)+600-self.width/4,804)
        self.draw_triangles(((self.width/2)+700)-self.width/4,804)


        self.draw_triangles((self.width/2)+900-self.width/4,804)
        self.draw_triangles(((self.width/2)+998)-self.width/4,804)
        self.draw_triangles(((self.width/2)+1096)-self.width/4,804)
        self.draw_triangles((self.width/2)+1195-self.width/4,804)

    def level11(self):
        # Screen
        self.screen.fill('#b881c7')

        # Ground
        self.ground.fill('black')
        self.screen.blit(self.ground,self.ground_rect)
        
        # Triangle
        self.draw_triangles((self.width)/2,804)

       
        # Cube
        self.screen.blit(self.cube,self.cube_rect)

        #Object
        self.objects(1400,100,0,self.height - 380)

    def level12(self):
        # Screen
        self.screen.fill('#b881c7')

        # Ground
        self.ground.fill('black')
        self.screen.blit(self.ground,self.ground_rect)
        
        # Triangle
        self.draw_triangles((self.width)/2,804)

       
        # Cube
        self.screen.blit(self.cube,self.cube_rect)

        #Object
        self.objects(1400,100,0,self.height - 350)

    def level13(self):
        # Screen
        self.screen.fill('#b881c7')

        # Ground
        self.ground.fill('black')
        self.screen.blit(self.ground,self.ground_rect)
        
        # Triangle
        self.draw_triangles((self.width)/2,804)
        

       
        # Cube
        self.screen.blit(self.cube,self.cube_rect)

        #Object
        self.objects(1400,100,0,self.height - 338)

    def level14(self):
        # Screen
        self.screen.fill('#b881c7')

        # Ground
        self.ground.fill('black')
        self.screen.blit(self.ground,self.ground_rect)
        
        # Triangle
        self.draw_triangles(self.width/2,804)
        self.draw_triangles((self.width/2)+100,804)

        # Cube
        self.screen.blit(self.cube,self.cube_rect)

        #Object
        self.objects(1400,100,0,self.height-400)

    def level15(self):
        # Screen
        self.screen.fill('#b881c7')

        # Ground
        self.ground.fill('black')
        self.screen.blit(self.ground,self.ground_rect)
        
        # Triangle
        self.draw_triangles((self.width/2),804)
        self.draw_triangles((self.width/2)+100,804)
       
        # Cube
        self.screen.blit(self.cube,self.cube_rect)

        #Object
        self.objects(1400,100,0,self.height - 390)

    def level16(self):
        # Screen
        self.screen.fill('#b881c7')

        # Ground
        self.ground.fill('black')
        self.screen.blit(self.ground,self.ground_rect)
        
        # Triangle
        self.draw_triangles((self.width/2)+100,804)
        self.draw_triangles((self.width/2)+200,804)
        self.draw_triangles((self.width/2),804)

        # Cube
        self.screen.blit(self.cube,self.cube_rect)

        #Object
        self.objects(1400,100,0,self.height-426)

    def win_screen(self):
        image = pygame.image.load('')
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

    if game.level >16:
        game.win_screen()

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

    pygame.display.update()