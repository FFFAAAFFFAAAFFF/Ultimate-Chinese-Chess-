#Chinese Chess
#main game

import pygame, sys, os, math
from pygame.locals import *
pygame.init()

def judgepos(x1, y1):
    for each in coordinate.keys():
        if (x1 - coordinate[each][0]) ** 2 + (y1 - coordinate[each][1]) ** 2 < 20 ** 2:
            return each
    else:
        return False

def judgewin():
    count = 0
    pos = []
    for each in state.keys():
        if state[each] == rshuai or state[each] == bshuai:
            count += 1
            pos.append(each)
    if count == 1:
        return 1
    else:
        if pos[0][0] != pos[1][0] and pos[0][1] != pos[1][1]:
            return 0
        elif pos[0][0] == pos[1][0]:
            for i in range(min(pos[0][1], pos[1][1]) + 1, max(pos[1][1], pos[0][1])):
                if state[(pos[0][0], i)] != None:
                    return 0
            else:
                return 2
        elif pos[0][1] == pos[1][1]:
            for i in range(min(pos[0][0], pos[1][0]) + 1, max(pos[1][0], pos[0][0])):
                if state[(i, pos[0][1])] != None:
                    return 0
            else:
                return 2
            
windowSurface = pygame.display.set_mode((700,700),0,32)
pygame.display.set_caption("中国象棋")
chessboard = pygame.transform.scale(pygame.image.load(os.path.join(".", "images\\象棋棋盘.jpg")), (700, 700))
rbing_img = pygame.transform.scale(pygame.image.load(os.path.join(".", "images\\红兵.png")), (64, 64))
bbing_img = pygame.transform.scale(pygame.image.load(os.path.join(".", "images\\黑卒.png")), (64, 64))
rpao_img = pygame.transform.scale(pygame.image.load(os.path.join(".", "images\\红炮.png")), (64, 64))
bpao_img = pygame.transform.scale(pygame.image.load(os.path.join(".", "images\\黑炮.png")), (64, 64))
rju_img = pygame.transform.scale(pygame.image.load(os.path.join(".", "images\\红车.jpg")), (64, 64))
bju_img = pygame.transform.scale(pygame.image.load(os.path.join(".", "images\\黑车.png")), (64, 64))
rma_img = pygame.transform.scale(pygame.image.load(os.path.join(".", "images\\红马.png")), (64, 64))
bma_img = pygame.transform.scale(pygame.image.load(os.path.join(".", "images\\黑马.png")), (64, 64))
rxiang_img = pygame.transform.scale(pygame.image.load(os.path.join(".", "images\\红象.png")), (64, 64))
bxiang_img = pygame.transform.scale(pygame.image.load(os.path.join(".", "images\\黑象.png")), (64, 64))
rshi_img = pygame.transform.scale(pygame.image.load(os.path.join(".", "images\\红士.png")), (64, 64))
bshi_img = pygame.transform.scale(pygame.image.load(os.path.join(".", "images\\黑士.png")), (64, 64))
rshuai_img = pygame.transform.scale(pygame.image.load(os.path.join(".", "images\\红帅.png")), (64, 64))
bshuai_img = pygame.transform.scale(pygame.image.load(os.path.join(".", "images\\黑将.png")), (64, 64))


class rBing:
    def __init__(self, x, y):
        self.x, self.y = x, y
        self.color = 'r'
        self.image = rbing_img
        self.rect = pygame.Rect(coordinate[(x, y)][0] - 32, coordinate[(x, y)][1] - 32, 64, 64)
    def move(self, x ,y):
        if self.y < 5:
            target = [(self.x, self.y + 1)]
        else:
            target = [(self.x, self.y + 1), (self.x - 1, self.y), (self.x + 1, self.y)]
        tar = list.copy(target)    
        for each in tar:
            if each[0] < 0 or each[0] > 8 or each[1] > 9:
                target.remove(each)
        tar = list.copy(target)
        for each in tar:
            if state[each] != None and state[each].color == 'r':
                target.remove(each)
        if (x, y) in target:
            state[(self.x, self.y)] = None
            state[(x, y)] = self
            self.x, self.y = x, y
            self.rect.centerx, self.rect.centery = coordinate[(x, y)]
            return True
        else:
            return False


        
class bBing:
    def __init__(self, x, y):
        self.x, self.y = x, y
        self.color = 'b'
        self.image = bbing_img
        self.rect = pygame.Rect(coordinate[(x, y)][0] - 32, coordinate[(x, y)][1] - 32, 64, 64)

    def move(self, x ,y):
        if self.y > 4:
            target = [(self.x, self.y - 1)]
        else:
            target = [(self.x, self.y - 1), (self.x - 1, self.y), (self.x + 1, self.y)]
        tar = list.copy(target)    
        for each in tar:
            if each[0] < 0 or each[0] > 8 or each[1] < 0:
                target.remove(each)
        tar = list.copy(target)
        for each in tar:
            if state[each] != None and state[each].color == 'b':
                target.remove(each)
            
        if (x, y) in target:
            state[(self.x, self.y)] = None
            state[(x, y)] = self
            self.x, self.y = x, y
            self.rect.centerx, self.rect.centery = coordinate[(x, y)]
            return True
        else:
            return False

                

                
class rPao:
    def __init__(self, x, y):
        self.x, self.y = x, y
        self.color = 'r'
        self.image = rpao_img
        self.rect = pygame.Rect(coordinate[(x, y)][0] - 32, coordinate[(x, y)][1] - 32, 64, 64)

    def move(self, x, y):
        target = []
        over = False
        for each in list(range(self.x-1,-1,-1)):
                if state[(each, self.y)] == None and over == False:
                    target.append((each, self.y))
                    continue
                if state[(each, self.y)] != None and over == False:
                    over = True
                    continue
                if over == True:
                    if state[(each,self.y)] != None and state[(each, self.y)].color == 'r':
                        break
                    if state[(each,self.y)] != None and state[(each, self.y)].color == 'b':
                        target.append((each, self.y))
                        break
        over = False
        for each in range(self.x + 1, 9):
                if state[(each, self.y)] == None and over == False:
                    target.append((each, self.y))
                if state[(each, self.y)] != None and over == False:
                    over = True
                    continue
                if over == True:
                    if state[(each,self.y)] != None and state[(each, self.y)].color == 'r':
                        break
                    if state[(each,self.y)] != None and state[(each, self.y)].color == 'b':
                        target.append((each, self.y))
                        break
        over = False
        for each in list(range(self.y-1,-1,-1)):
                if state[(self.x, each)] == None and over == False:
                    target.append((self.x, each))
                if state[(self.x, each)] != None and over == False:
                    over = True
                    continue
                if over == True:
                    if state[(self.x,each)] != None and state[(self.x, each)].color == 'r':
                        break
                    if state[(self.x,each)] != None and state[(self.x, each)].color == 'b':
                        target.append((self.x, each))
                        break
        over = False
        for each in range(self.y + 1, 10):
                if state[(self.x, each)] == None and over == False:
                    target.append((self.x, each))
                if state[(self.x, each)] != None and over == False:
                    over = True
                    continue
                if over == True:
                    if state[(self.x,each)] != None and state[(self.x, each)].color == 'r':
                        break
                    if state[(self.x,each)] != None and state[(self.x, each)].color == 'b':
                        target.append((self.x, each))
                        break
        if (x, y) in target:
            state[(self.x, self.y)] = None
            state[(x, y)] = self
            self.x, self.y = x, y
            self.rect.centerx, self.rect.centery = coordinate[(x, y)]
            return True
        else:
            return False

                
class bPao:
    def __init__(self, x, y):
        self.x, self.y = x, y
        self.color = 'b'
        self.image = bpao_img
        self.rect = pygame.Rect(coordinate[(x, y)][0] - 32, coordinate[(x, y)][1] - 32, 64, 64)

    def move(self, x, y):
        target = []
        over = False
        for each in list(range(self.x-1,-1,-1)):
                if state[(each, self.y)] == None and over == False:
                    target.append((each, self.y))
                    continue
                if state[(each, self.y)] != None and over == False:
                    over = True
                    continue
                if over == True:
                    if state[(each,self.y)] != None and state[(each, self.y)].color == 'b':
                        break
                    if state[(each,self.y)] != None and state[(each, self.y)].color == 'r':
                        target.append((each, self.y))
                        break
        over = False
        for each in range(self.x + 1, 9):
                if state[(each, self.y)] == None and over == False:
                    target.append((each, self.y))
                if state[(each, self.y)] != None and over == False:
                    over = True
                    continue
                if over == True:
                    if state[(each,self.y)] != None and state[(each, self.y)].color == 'b':
                        break
                    if state[(each,self.y)] != None and state[(each, self.y)].color == 'r':
                        target.append((each, self.y))
                        break
        over = False
        for each in list(range(self.y-1,-1,-1)):
                if state[(self.x, each)] == None and over == False:
                    target.append((self.x, each))
                if state[(self.x, each)] != None and over == False:
                    over = True
                    continue
                if over == True:
                    if state[(self.x,each)] != None and state[(self.x, each)].color == 'b':
                        break
                    if state[(self.x,each)] != None and state[(self.x, each)].color == 'r':
                        target.append((self.x, each))
                        break
        over = False
        for each in range(self.y + 1, 10):
                if state[(self.x, each)] == None and over == False:
                    target.append((self.x, each))
                if state[(self.x, each)] != None and over == False:
                    over = True
                    continue
                if over == True:
                    if state[(self.x,each)] != None and state[(self.x, each)].color == 'b':
                        break
                    if state[(self.x,each)] != None and state[(self.x, each)].color == 'r':
                        target.append((self.x, each))
                        break
        if (x, y) in target:
            state[(self.x, self.y)] = None
            state[(x, y)] = self
            self.x, self.y = x, y
            self.rect.centerx, self.rect.centery = coordinate[(x, y)]
            return True
        else:
            return False

class rJu:
    def __init__(self, x, y):
        self.x, self.y = x, y
        self.color = 'r'
        self.image = rju_img
        self.rect = pygame.Rect(coordinate[(x, y)][0] - 32, coordinate[(x, y)][1] - 32, 64, 64)

    def move(self, x, y):
        target = []
        over = False
        if self.x < 8:
            for each in range(self.x + 1, 9):
                if (over): break
                if state[(each, self.y)] != None :
                    over = True
                    if state[(each, self.y)].color =='r':
                        break
                target.append((each, self.y))
            over = False
        if self.x > 0:
            for each in range(self.x - 1, -1, -1):
                if (over): break
                if state[(each, self.y)] != None :
                    over = True
                    if state[(each, self.y)].color == 'r':
                        break
                target.append((each, self.y))
            over = False
        if self.y < 9:
            for each in range(self.y + 1, 10):
                if (over): break
                if state[(self.x, each)] != None :
                    over = True
                    if state[(self.x, each)].color =='r':
                        break
                target.append((self.x, each))
            over = False
        if self.y > 0:
            for each in range(self.y - 1, -1, -1):
                if (over): break
                if state[(self.x, each)] != None :
                    over = True
                    if state[(self.x, each)].color =='r':
                        break
                target.append((self.x, each))
        if (x, y) in target:
            state[(self.x, self.y)] = None
            state[(x, y)] = self
            self.x, self.y = x, y
            self.rect.centerx, self.rect.centery = coordinate[(x, y)]
            return True
        else:
            return False



class bJu:
    def __init__(self, x, y):
        self.x, self.y = x, y
        self.color = 'b'
        self.image = bju_img
        self.rect = pygame.Rect(coordinate[(x, y)][0] - 32, coordinate[(x, y)][1] - 32, 64, 64)

    def move(self, x, y):
        target = []
        over = False
        if self.x < 8:
            for each in range(self.x + 1, 9):
                if (over): break
                if state[(each, self.y)] != None :
                    over = True
                    if state[(each, self.y)].color =='b':
                        break
                target.append((each, self.y))
            over = False
        if self.x > 0:
            for each in range(self.x - 1, -1, -1):
                if (over): break
                if state[(each, self.y)] != None :
                    over = True
                    if state[(each, self.y)].color == 'b':
                        break
                target.append((each, self.y))
            over = False
        if self.y < 9:
            for each in range(self.y + 1, 10):
                if (over): break
                if state[(self.x, each)] != None :
                    over = True
                    if state[(self.x, each)].color =='b':
                        break
                target.append((self.x, each))
            over = False
        if self.y > 0:
            for each in range(self.y - 1, -1, -1):
                if (over): break
                if state[(self.x, each)] != None :
                    over = True
                    if state[(self.x, each)].color =='b':
                        break
                target.append((self.x, each))
        if (x, y) in target:
            state[(self.x, self.y)] = None
            state[(x, y)] = self
            self.x, self.y = x, y
            self.rect.centerx, self.rect.centery = coordinate[(x, y)]
            return True
        else:
            return False


class rMa:
    def __init__(self, x, y):
        self.x, self.y = x, y
        self.color = 'r'
        self.image = rma_img
        self.rect = pygame.Rect(coordinate[(x, y)][0] - 32,coordinate[(x, y)][1] - 32, 64, 64)

    def move(self, x, y):
        target = [(self.x+2,self.y+1),(self.x+2,self.y-1),(self.x+1,self.y+2),(self.x+1,self.y-2),(self.x-1,self.y+2),(self.x-1,self.y-2),(self.x-2,self.y+1),(self.x-2,self.y-1)]
        tar=list.copy(target)
        for each in tar:
            if each[0] < 0 or each[0] > 8 or each[1] < 0 or each[1] > 9:
                target.remove(each)
                continue
            if (state[each] != None and state[each].color == 'r') :
                target.remove(each)
                continue
            if each[0] > self.x and each[1] > self.y and state[(math.floor((self.x+each[0])/2),math.floor((self.y+each[1])/2))] != None:
                target.remove(each)
                continue
            elif each[0] > self.x and each[1] < self.y and state[(math.floor((self.x+each[0])/2),math.ceil((self.y+each[1])/2))] != None:
                target.remove(each)
                continue
            elif each[1] > self.y and each[0] < self.x and state[(math.ceil((self.x+each[0])/2), math.floor((self.y+each[1])/2))] != None:
                target.remove(each)
                continue
            elif each[1] < self.y and each[0] < self.x and state[(math.ceil((self.x+each[0])/2), math.ceil((self.y+each[1])/2))] != None :
                target.remove(each)
                continue
        if (x,y) in target:
            state[(self.x,self.y)] = None
            state[(x,y)] = self
            self.x, self.y = x, y
            self.rect.centerx, self.rect.centery = coordinate[(x,y)]
            return True
        else:
            return False

class bMa:
    def __init__(self, x, y):
        self.x, self.y = x, y
        self.color = 'b'
        self.image = bma_img
        self.rect = pygame.Rect(coordinate[(x, y)][0] - 32, coordinate[(x, y)][1] - 32, 64, 64)
    def move(self, x, y):
        target = [(self.x+2,self.y+1),(self.x+2,self.y-1),(self.x+1,self.y+2),(self.x+1,self.y-2),(self.x-1,self.y+2),(self.x-1,self.y-2),(self.x-2,self.y+1),(self.x-2,self.y-1)]
        tar=list.copy(target)
        for each in tar:
            if each[0] < 0 or each[0] > 8 or each[1] < 0 or each[1] > 9:
                target.remove(each)
                continue
            if (state[each] != None and state[each].color == 'b') :
                target.remove(each)
                continue
            if each[0] > self.x and each[1] > self.y and state[(math.floor((self.x+each[0])/2),math.floor((self.y+each[1])/2))] != None:
                target.remove(each)
                continue
            elif each[0] > self.x and each[1] < self.y and state[(math.floor((self.x+each[0])/2),math.ceil((self.y+each[1])/2))] != None:
                target.remove(each)
                continue
            elif each[1] > self.y and each[0] < self.x and state[(math.ceil((self.x+each[0])/2), math.floor((self.y+each[1])/2))] != None:
                target.remove(each)
                continue
            elif each[1] < self.y and each[0] < self.x and state[(math.ceil((self.x+each[0])/2), math.ceil((self.y+each[1])/2))] != None :
                target.remove(each)
                continue
            
        if (x,y) in target:
            state[(self.x,self.y)] = None
            state[(x,y)] = self
            self.x, self.y = x, y
            self.rect.centerx, self.rect.centery = coordinate[(x,y)]
            return True
        else:
            return False



class rXiang:
    def __init__(self, x, y):
        self.x, self.y = x, y
        self.color = 'r'
        self.image = rxiang_img
        self.rect = pygame.Rect(coordinate[(x, y)][0] - 32, coordinate[(x, y)][1] - 32, 64, 64)

    def move(self, x, y):
        target = [(self.x - 2, self.y - 2), (self.x - 2, self.y + 2), (self.x + 2, self.y + 2), (self.x + 2, self.y - 2)]
        tar = list.copy(target)
        for each in tar:
            if each[0] < 0 or each[0] > 8 or each[1] < 0 or each[1] > 4:
                target.remove(each)
        tar = list.copy(target)
        for each in tar:
            if (state[each] != None and state[each].color == 'r') or state[((self.x + each[0])/2, (self.y + each[1])/2)] != None:
                target.remove(each)

        if (x, y) in target:
            state[(self.x, self.y)] = None
            state[(x, y)] = self
            self.x, self.y = x, y
            self.rect.centerx, self.rect.centery = coordinate[(x, y)]
            return True
        else:
            return False


class bXiang:
    def __init__(self, x, y):
        self.x, self.y = x, y
        self.color = 'b'
        self.image = bxiang_img
        self.rect = pygame.Rect(coordinate[(x, y)][0] - 32, coordinate[(x, y)][1] - 32, 64, 64)

    def move(self, x, y):
        target = [(self.x - 2, self.y - 2), (self.x - 2, self.y + 2), (self.x + 2, self.y + 2), (self.x + 2, self.y - 2)]
        tar = list.copy(target)
        for each in tar:
            if each[0] < 0 or each[0] > 8 or each[1] < 5 or each[1] > 9:
                target.remove(each)
        tar = list.copy(target)
        for each in tar:
            if (state[each] != None and state[each].color == 'b') or state[((self.x + each[0])/2, (self.y + each[1])/2)] != None:
                target.remove(each)

        if (x, y) in target:
            state[(self.x, self.y)] = None
            state[(x, y)] = self
            self.x, self.y = x, y
            self.rect.centerx, self.rect.centery = coordinate[(x, y)]
            return True
        else:
            return False



class rShi:
    def __init__(self, x, y):
        self.x, self.y = x, y
        self.color = 'r'
        self.image = rshi_img
        self.rect = pygame.Rect(coordinate[(x, y)][0] - 32, coordinate[(x, y)][1] - 32, 64, 64)

    def move(self,x,y):
        target = [(self.x + 1, self.y + 1),(self.x + 1, self.y - 1),(self.x - 1, self.y + 1),(self.x - 1, self.y - 1)]
        tar = list.copy(target)
        for each in tar:
            if each[0] < 3 or each[0] > 5 or each[1] < 0 or each[1] > 2 or (state[each] != None and state[each].color == 'r'):
                target.remove(each)
        if (x, y) in target:
            state[(self.x, self.y)] = None
            state[(x, y)] = self
            self.x, self.y = x, y
            self.rect.centerx, self.rect.centery = coordinate[(x, y)]
            return True
        else:
            return False

class bShi:
    def __init__(self, x, y):
        self.x, self.y = x, y
        self.color = 'b'
        self.image = bshi_img
        self.rect = pygame.Rect(coordinate[(x, y)][0] - 32, coordinate[(x, y)][1] - 32, 64, 64)

    def move(self, x, y):
        target = [(self.x + 1, self.y + 1),(self.x + 1, self.y - 1), (self.x - 1, self.y + 1), (self.x - 1, self.y - 1)]
        tar = list.copy(target)
        for each in tar:
            if each[0] < 3 or each[0] > 5 or each[1] < 7 or each[1] > 9 or (state[each] != None and state[each].color == 'b'):
                target.remove(each)
        if (x, y) in target:
            state[(self.x, self.y)] = None
            state[(x, y)] = self
            self.x, self.y = x, y
            self.rect.centerx, self.rect.centery = coordinate[(x, y)]
            return True
        else:
            return False
        

class rShuai:
    def __init__(self, x, y):
        self.x, self.y = x, y
        self.color = 'r'
        self.image = rshuai_img
        self.rect = pygame.Rect(coordinate[(x, y)][0] - 32, coordinate[(x, y)][1] - 32, 64, 64)

    def move(self, x, y):
        target = [(self.x + 1, self.y), (self.x - 1, self.y), (self.x, self.y - 1), (self.x, self.y + 1)]
        tar = list.copy(target)
        for each in tar:
            if each[0] < 3 or each[0] > 5 or each[1] < 0 or each[1] > 2:
                target.remove(each)
        tar = list.copy(target)
        for each in tar:
            if state[each] != None and state[each].color == 'r':
                target.remove(each)
        if (x, y) in target:
            state[(self.x, self.y)] = None
            state[(x, y)] = self
            self.x, self.y = x, y
            self.rect.centerx, self.rect.centery = coordinate[(x, y)]
            return True
        else:
            return False

class bShuai:
    def __init__(self, x, y):
        self.x, self.y = x, y
        self.color = 'b'
        self.image = bshuai_img
        self.rect = pygame.Rect(coordinate[(x, y)][0] - 32, coordinate[(x, y)][1] - 32, 64, 64)

    def move(self, x, y):
        target = [(self.x + 1, self.y), (self.x - 1, self.y), (self.x, self.y - 1), (self.x, self.y + 1)]
        tar = list.copy(target)
        for each in tar:
            if each[0] < 3 or each[0] > 5 or each[1] < 7 or each[1] > 9:
                target.remove(each)
        tar = list.copy(target)
        for each in tar:
            if state[each] != None and state[each].color == 'b':
                target.remove(each)
        if (x, y) in target:
            state[(self.x, self.y)] = None
            state[(x, y)] = self
            self.x, self.y = x, y
            self.rect.centerx, self.rect.centery = coordinate[(x, y)]
            return True
        else:
            return False


coordinate = {}
for i in range(9):
    for j in range(10):
        coordinate[(i, j)] = (71 + 69.8 * i, 63 + 64.5 * j)

rbing1 = rBing(0, 3)
rbing2 = rBing(2, 3)
rbing3 = rBing(4, 3)
rbing4 = rBing(6, 3)
rbing5 = rBing(8, 3)
rpao1 = rPao(1, 2)
rpao2 = rPao(7, 2)
rju1 = rJu(0, 0)
rju2 = rJu(8, 0)
rma1 = rMa(1, 0)
rma2 = rMa(7, 0)
rxiang1 = rXiang(2, 0)
rxiang2 = rXiang(6, 0)
rshi1 = rShi(3, 0)
rshi2 = rShi(5, 0)
rshuai = rShuai(4, 0)
bbing1 = bBing(0, 6)
bbing2 = bBing(2, 6)
bbing3 = bBing(4, 6)
bbing4 = bBing(6, 6)
bbing5 = bBing(8, 6)
bpao1 = bPao(1, 7)
bpao2 = bPao(7, 7)
bju1 = bJu(0, 9)
bju2 = bJu(8, 9)
bma1 = bMa(1, 9)
bma2 = bMa(7, 9)
bxiang1 = bXiang(2, 9)
bxiang2 = bXiang(6, 9)
bshi1 = bShi(3, 9)
bshi2 = bShi(5, 9)
bshuai = bShuai(4, 9)


state = {}
for i in range(9):
    for j in range(10):
        state[(i, j)] = None
state[(0, 3)] = rbing1
state[(2, 3)] = rbing2
state[(4, 3)] = rbing3
state[(6, 3)] = rbing4
state[(8, 3)] = rbing5
state[(1, 2)] = rpao1
state[(7, 2)] = rpao2
state[(0, 0)] = rju1
state[(8, 0)] = rju2
state[(1, 0)] = rma1
state[(7, 0)] = rma2
state[(2, 0)] = rxiang1
state[(6, 0)] = rxiang2
state[(3, 0)] = rshi1
state[(5, 0)] = rshi2
state[(4, 0)] = rshuai
state[(0, 6)] = bbing1
state[(2, 6)] = bbing2
state[(4, 6)] = bbing3
state[(6, 6)] = bbing4
state[(8, 6)] = bbing5
state[(1, 7)] = bpao1
state[(7, 7)] = bpao2
state[(0, 9)] = bju1
state[(8, 9)] = bju2
state[(1, 9)] = bma1
state[(7, 9)] = bma2
state[(2, 9)] = bxiang1
state[(6, 9)] = bxiang2
state[(3, 9)] = bshi1
state[(5, 9)] = bshi2
state[(4, 9)] = bshuai

turn = True
lock = None
outcome = 0
font = pygame.font.Font(None, 100)
rect1 = pygame.Rect(150, 150, 400, 200)
rect2 = pygame.Rect(150, 500, 400, 200)
win = 'b'

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if outcome == 0:
            if event.type == MOUSEBUTTONDOWN:
                position = judgepos(event.pos[0], event.pos[1])
                if position != False:
                    if turn:
                        if state[position] != None and state[position].color == 'b':
                                lock = state[position]
                        if (state[position] == None or (state[position] != None and state[position].color != 'b')) and lock != None:
                            result = lock.move(position[0], position[1])
                            if result:
                                turn = not turn
                                lock = None
                                outcome = judgewin()
                                if outcome == 1:
                                    win = 'b'
                                elif outcome == 2:
                                    win = 'r'
                            
                    else:
                        if state[position] != None and state[position].color == 'r':
                                lock = state[position]
                        if (state[position] == None or (state[position] != None and state[position].color != 'r')) and lock != None:
                            result = lock.move(position[0], position[1])
                            if result:
                                turn = not turn
                                lock = None
                                outcome = judgewin()
                                if outcome == 1:
                                    win = 'r'
                                elif outcome == 2:
                                    win = 'b'
        
    windowSurface.fill((255, 255, 255))
    windowSurface.blit(chessboard, chessboard.get_rect())
    for each in state.values():
        if each != None:
            windowSurface.blit(each.image, each.rect)
    if outcome != 0:
        if win ==  'r':
            text1 = font.render("RED    WIN", True, (0, 0, 255))
            text2 = font.render("BLACK FAIL", True, (0, 0, 255))
        else:
            text1 = font.render("RED  FAIL", True, (0, 0, 255))
            text2 = font.render("BLACK WIN", True, (0, 0, 255))
        windowSurface.blit(text1, rect1)
        windowSurface.blit(text2, rect2)
    pygame.display.flip()

















    
