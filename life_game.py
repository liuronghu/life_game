import pygame
from pygame import QUIT
from random import *
from sys import exit
import numpy
import itertools
die = 0
life = 1
#1.初始化界面
#2.随机选择数值填充
def select_number(init_life_number,size):
    print("select_number(),init_life_number,size",init_life_number,size)
    select_list = []
    for x in range(init_life_number):
        x = randint(0,size[0]-1)
        y = randint(0,size[1]-1)
        select_list.append((x,y))
    print(select_list)
    return select_list
def screen_fill(screen,select_list):
    #print("screen_fill(),select_list",select_list)
    r, g, b = 255,255,255
    for num,value in enumerate(select_list):
        screen.set_at(value, (r, g, b))
def set_universe(screen,select_list,size):
    #0为死亡即为黑色 1为活着即为白色
    x,y = size
    universe_list = numpy.zeros(shape=(x+2,y+2))
    print("universe_list",universe_list[1:3])
    for num,value in enumerate(select_list):
        universe_list[value[0]+1][value[1]+1] = 1
    return universe_list

#3.选择算法
def get_human_number(universe_list,size):
    #print("get_human_number(),size",size)
    x,y = size
    list1 = universe_list[x-1][y-1] + universe_list[x-1][y] + universe_list[x-1][y+1]
    list2 = universe_list[x][y-1] + universe_list[x][y] + universe_list[x][y+1]
    list3 = universe_list[x+1][y-1] + universe_list[x+1][y] + universe_list[x+1][y+1]
    return list1 + list2 + list3
def rule_human(universe_list,size,side_human_value):
    #1． 每个细胞的状态由该细胞及周围八个细胞上一次的状态所决定；
    #2. 如果一个细胞周围有3个细胞为生，则该细胞为生，即该细胞若原先为死，则转为生，若原先为生，则保持不变；
    #3. 如果一个细胞周围有2个细胞为生，则该细胞的生死状态保持不变；
    #4. 在其它情况下，该细胞为死，即该细胞若原先为生，则转为死，若原先为死，则保持不变
    if side_human_value == 3:
        universe_list[size[0]][size[1]] = life
    elif side_human_value == 2:
        pass
    else:
        universe_list[size[0]][size[1]] = die
    return universe_list
def draw_wire(screen):
    width = 1
    pos = 10
    size = (50,50)
    for x in range(size[0]):
        for y in range(size[1]):
            pygame.draw.rect(screen,(255,0,255),(pos*x,pos*y,pos*x+pos,pos*y+pos),width)

def screen_fill_rect(screen,select_list,size,pos):
    #print("screen_fill(),select_list",select_list)
    width = 0
    
    #size = (50,50)
    rgb = (255,255,255)
    for x in range(len(select_list)):
        for y in range(len(select_list[0])):
            if select_list[x][y]:
                pygame.draw.rect(screen,(255,255,255),(pos*x,pos*y,pos*x+pos,pos*y+pos),width)
            else:
                pygame.draw.rect(screen,(0,0,0),(pos*x,pos*y,pos*x+pos,pos*y+pos),width)
if __name__=="__main__":
    init_life_number = 300
    pos = 10
    pygame.init()
    SCREEN_SIZE = (60, 60) #(1536, 864)
    screen = pygame.display.set_mode((SCREEN_SIZE[0]*pos,SCREEN_SIZE[1]*pos), 0, 32)
    #draw_wire(screen)
    select_list = select_number(init_life_number,SCREEN_SIZE)
    #screen_fill(screen,select_list)
    universe_list = set_universe(screen,select_list,SCREEN_SIZE)
    screen_fill_rect(screen,universe_list,SCREEN_SIZE,pos)
    pygame.display.update()
    #x = 1
    while True:
        for event in pygame.event.get():
            if event.type ==  QUIT:
                exit()
        #for x in range(1,SCREEN_SIZE[0]+1):
            #for y in range(1,SCREEN_SIZE[1]+1):
        for x,y in itertools.product(range(SCREEN_SIZE[0]),range(SCREEN_SIZE[1])):
            side_human_value = get_human_number(universe_list,(x,y))
            universe_list = rule_human(universe_list,(x,y),side_human_value)
        #screen_fill(screen,select_list)
        screen_fill_rect(screen,universe_list,SCREEN_SIZE,pos)
        pygame.display.update()
        #x += 1
        #if x >= SCREEN_SIZE[0]+1:
            #x = 1
    pygame.quit()