import pygame,sys
from pygame.locals import *
#初始化pygame
pygame.init()
#创建屏幕，加载棋盘
windowSurface=pygame.display.set_mode((700,700),0,32)
pygame.display.set_caption("象棋")
qipan=pygame.image.load("象棋棋盘.jpg")
qipan1=pygame.transform.scale(qipan,(700,700))
qipan2 = qipan1.get_rect()
windowSurface.blit(qipan1,qipan2)
#单位长度
a=0
x0=69.8
y0=64.2
#颜色元组
WHITE=(255,255,255)
BLUE=(0,255,255)
#红兵
class rBing:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def fix(self):
        x=pygame.image.load("红兵.png")
        y=x.get_rect()
        y.centerx=70.4+x0*self.x
        y.centery=62.1+y0*self.y
        windowSurface.blit(x,y)
        return y
rBing0=[]
for i in range(5):
    m=rBing(2*i,3)
    rBing0.append(m.fix())
#黑兵
class bBing:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def fix(self):
        x=pygame.image.load("黑卒.png")
        y=x.get_rect()
        y.centerx=70.4+x0*self.x
        y.centery=62.1+y0*self.y
        windowSurface.blit(x,y)
        return y
bBing0=[]
for i in range(5):
    m=bBing(2*i,6)
    bBing0.append(m.fix())
#红炮
class rPao:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def fix(self):
        x=pygame.image.load("红炮.png")
        y=x.get_rect()
        y.centerx=70.4+x0*self.x
        y.centery=62.1+y0*self.y
        windowSurface.blit(x,y)
        return y
rPao0=[]
for i in range(2):
    m=rPao(6*i+1,2)
    rPao0.append(m.fix())
#黑炮
class bPao:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def fix(self):
        x=pygame.image.load("黑炮.png")
        y=x.get_rect()
        y.centerx=70.4+x0*self.x
        y.centery=62.1+y0*self.y
        windowSurface.blit(x,y)
        return y
bPao0=[]
for i in range(2):
    m=bPao(6*i+1,7)
    bPao0.append(m.fix())
#红车
class rChe:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def fix(self):
        x=pygame.image.load("红车.png")
        y=x.get_rect()
        y.centerx=70.4+x0*self.x
        y.centery=62.1+y0*self.y
        windowSurface.blit(x,y)
        return y
rChe0=[]
for i in range(2):
    m=rChe(8*i,0)
    rChe0.append(m.fix())
#黑车
class bChe:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def fix(self):
        x=pygame.image.load("黑车.png")
        y=x.get_rect()
        y.centerx=70.4+x0*self.x
        y.centery=62.1+y0*self.y
        windowSurface.blit(x,y)
        return y
bChe0=[]
for i in range(2):
    m=bChe(8*i,9)
    bChe0.append(m.fix())
#红马
class rMa:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def fix(self):
        x=pygame.image.load("红马.png")
        y=x.get_rect()
        y.centerx=70.4+x0*self.x
        y.centery=62.1+y0*self.y
        windowSurface.blit(x,y)
        return y
rMa0=[]
for i in range(2):
    m=rMa(6*i+1,0)
    rMa0.append(m.fix())
#黑马
class bMa:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def fix(self):
        x=pygame.image.load("黑马.png")
        y=x.get_rect()
        y.centerx=70.4+x0*self.x
        y.centery=62.1+y0*self.y
        windowSurface.blit(x,y)
        return y
bMa0=[]
for i in range(2):
    m=bMa(6*i+1,9)
    bMa0.append(m.fix())
#红象
class rXiang:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def fix(self):
        x=pygame.image.load("红象.png")
        y=x.get_rect()
        y.centerx=70.4+x0*self.x
        y.centery=62.1+y0*self.y
        windowSurface.blit(x,y)
        return y
rXiang0=[]
for i in range(2):
    m=rXiang(4*i+2,0)
    rXiang0.append(m.fix())
#黑象
class bXiang:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def fix(self):
        x=pygame.image.load("黑象.png")
        y=x.get_rect()
        y.centerx=70.4+x0*self.x
        y.centery=62.1+y0*self.y
        windowSurface.blit(x,y)
        return y
bXiang0=[]
for i in range(2):
    m=bXiang(4*i+2,9)
    bXiang0.append(m.fix())
#红士
class rShi:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def fix(self):
        x=pygame.image.load("红士.png")
        y=x.get_rect()
        y.centerx=70.4+x0*self.x
        y.centery=62.1+y0*self.y
        windowSurface.blit(x,y)
        return y
rShi0=[]
for i in range(2):
    m=rShi(2*i+3,0)
    rShi0.append(m.fix())
#黑士
class bShi:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def fix(self):
        x=pygame.image.load("黑士.png")
        y=x.get_rect()
        y.centerx=70.4+x0*self.x
        y.centery=62.1+y0*self.y
        windowSurface.blit(x,y)
        return y
bShi0=[]
for i in range(2):
    m=bShi(2*i+3,9)
    bShi0.append(m.fix())
#红帅
class rShuai:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def fix(self):
        x=pygame.image.load("红帅.png")
        y=x.get_rect()
        y.centerx=70.4+x0*self.x
        y.centery=62.1+y0*self.y
        windowSurface.blit(x,y)
        return y
rShuai0=[]
for i in range(1):
    m=rShuai(4,0)
    rShuai0.append(m.fix())
#黑将
class bJiang:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def fix(self):
        x=pygame.image.load("黑将.png")
        y=x.get_rect()
        y.centerx=70.4+x0*self.x
        y.centery=62.1+y0*self.y
        windowSurface.blit(x,y)
        return y
bJiang0=[]
for i in range(1):
    m=bJiang(4,9)
    bJiang0.append(m.fix())
#建立列表，将所有棋子放入
QIZI=[]
for i in rBing0[:]:
    QIZI.append(i)
for i in bBing0[:]:
    QIZI.append(i)
for i in rPao0[:]:
    QIZI.append(i)
for i in bPao0[:]:
    QIZI.append(i)
for i in rChe0[:]:
    QIZI.append(i)
for i in bChe0[:]:
    QIZI.append(i)
for i in rMa0[:]:
    QIZI.append(i)
for i in bMa0[:]:
    QIZI.append(i)
for i in rXiang0[:]:
    QIZI.append(i)
for i in bXiang0[:]:
    QIZI.append(i)
for i in rShi0[:]:
    QIZI.append(i)
for i in bShi0[:]:
    QIZI.append(i)
for i in rShuai0[:]:
    QIZI.append(i)
for i in bJiang0[:]:
    QIZI.append(i)
QIZI.append(None)
#各色棋子序号
R=[0,1,2,3,4,10,11,14,15,18,19,22,23,26,27,30]
B=[5,6,7,8,9,12,13,16,17,20,21,24,25,28,29,31]
#确定点所处位置是否有棋子
def inRect(x,y):
    for i in range(32):
        if QIZI[i]!=None:
            if x<=QIZI[i].right and x>=QIZI[i].left and y<=QIZI[i].bottom and y>=QIZI[i].top:
                return True
    else:
        return False
    
#确定是否为有效移动
def isRightMove(unit,x,y,b):
    #红兵走法
    if b>=0 and b<=4:
        if unit.centery<=(62.1+4.5*y0):
            if y-unit.centery<=1.3*y0 and y-unit.centery>=0.7*y0 and abs(x-unit.centerx)<=0.3*x0:
                for i in range(33):
                    if QIZI[i]!=None:
                        if x<=QIZI[i].right and x>=QIZI[i].left and y<=QIZI[i].bottom and y>=QIZI[i].top:
                            break
                if i in B or i==32:
                    return True
            else:
                return False
        else:
            if y-unit.centery<=1.3*y0 and y-unit.centery>=0.7*y0 and abs(x-unit.centerx)<=0.3*x0:
                for i in range(33):
                    if QIZI[i]!=None:
                        if x<=QIZI[i].right and x>=QIZI[i].left and y<=QIZI[i].bottom and y>=QIZI[i].top:
                            break
                if i in B or i==32:
                    return True
            elif abs(x-unit.centerx)<=1.3*x0 and abs(x-unit.centerx)>=0.7*x0 and abs(y-unit.centery)<=0.3*y0:
                for i in range(33):
                    if QIZI[i]!=None:
                        if x<=QIZI[i].right and x>=QIZI[i].left and y<=QIZI[i].bottom and y>=QIZI[i].top:
                            break
                if i in B or i==32:
                    return True
            else:
                return False
    #黑兵走法
    if b>=5 and b<=9:
        if unit.centery>=(62.1+4.5*y0):
            if unit.centery-y<=1.3*y0 and unit.centery-y>=0.7*y0 and abs(x-unit.centerx)<=0.3*x0:
                for i in range(33):
                    if QIZI[i]!=None:
                        if x<=QIZI[i].right and x>=QIZI[i].left and y<=QIZI[i].bottom and y>=QIZI[i].top:
                            break
                if i in R or i==32:
                    return True
            else:
                return False
        else:
            if unit.centery-y<=1.3*y0 and unit.centery-y>=0.7*y0 and abs(x-unit.centerx)<=0.3*x0:
                for i in range(33):
                    if QIZI[i]!=None:
                        if x<=QIZI[i].right and x>=QIZI[i].left and y<=QIZI[i].bottom and y>=QIZI[i].top:
                            break
                if i in R or i==32:
                    return True
            elif abs(x-unit.centerx)<=1.3*x0 and abs(x-unit.centerx)>=0.7*x0 and abs(y-unit.centery)<=0.3*y0:
                for i in range(33):
                    if QIZI[i]!=None:
                        if x<=QIZI[i].right and x>=QIZI[i].left and y<=QIZI[i].bottom and y>=QIZI[i].top:
                            break
                if i in R or i==32:
                    return True
            else:
                return False
    #红炮走法
    elif b>=10 and b<=11:
        if abs(y-unit.centery)<=0.3*y0:
            m0=(x-unit.centerx)/x0
            if x-unit.centerx>=0:
                for i in range(9):
                    if abs(i-m0)<=0.3:
                        m0=i
                        break
                n0=0
                for i in range(int(m0)):
                    if inRect(unit.centerx+i*x0,unit.centery):
                        n0=n0+1
                if n0==2 and inRect(x,y):
                    for i in range(33):
                        if QIZI[i]!=None:
                            if x<=QIZI[i].right and x>=QIZI[i].left and y<=QIZI[i].bottom and y>=QIZI[i].top:
                                break
                    if i in B or i==32:
                        return True
                elif n0==1 and not inRect(x,y):
                    for i in range(33):
                        if QIZI[i]!=None:
                            if x<=QIZI[i].right and x>=QIZI[i].left and y<=QIZI[i].bottom and y>=QIZI[i].top:
                                break
                    if i in B or i==32:
                        return True
                else:
                    return False
            elif x-unit.centerx<0:
                for i in range(9):
                    if abs(i+m0)<=0.3:
                        m0=i
                        break
                n0=0
                for i in range(int(m0)):
                    if inRect(unit.centerx-x0*i,unit.centery):
                        n0=n0+1
                if n0==2 and inRect(x,y):
                    for i in range(33):
                        if QIZI[i]!=None:
                            if x<=QIZI[i].right and x>=QIZI[i].left and y<=QIZI[i].bottom and y>=QIZI[i].top:
                                break
                    if i in B or i==32:
                        return True
                elif n0==1 and not inRect(x,y):
                    for i in range(33):
                        if QIZI[i]!=None:
                            if x<=QIZI[i].right and x>=QIZI[i].left and y<=QIZI[i].bottom and y>=QIZI[i].top:
                                break
                    if i in B or i==32:
                        return True
                else:
                    return False
        elif abs(x-unit.centerx)<=0.3*x0:
            m0=(y-unit.centery)/y0
            if y-unit.centery>=0:
                for i in range(9):
                    if abs(i-m0)<=0.3:
                        m0=i
                        break
                n0=0
                for i in range(int(m0)):
                    if inRect(unit.centerx,unit.centery+y0*i):
                        n0=n0+1
                if n0==2 and inRect(x,y):
                    for i in range(33):
                        if QIZI[i]!=None:
                            if x<=QIZI[i].right and x>=QIZI[i].left and y<=QIZI[i].bottom and y>=QIZI[i].top:
                                break
                    if i in B or i==32:
                        return True
                elif n0==1 and not inRect(x,y):
                    for i in range(33):
                        if QIZI[i]!=None:
                            if x<=QIZI[i].right and x>=QIZI[i].left and y<=QIZI[i].bottom and y>=QIZI[i].top:
                                break
                    if i in B or i==32:
                        return True
                else:
                    return False
            elif y-unit.centery<0:
                for i in range(9):
                    if abs(i+m0)<=0.3:
                        m0=i
                        break
                n0=0
                for i in range(int(m0)):
                    if inRect(unit.centerx,unit.centery-y0*i):
                        n0=n0+1
                if n0==2 and inRect(x,y):
                    for i in range(33):
                        if QIZI[i]!=None:
                            if x<=QIZI[i].right and x>=QIZI[i].left and y<=QIZI[i].bottom and y>=QIZI[i].top:
                                break
                    if i in B or i==32:
                        return True
                elif n0==1 and not inRect(x,y):
                    for i in range(33):
                        if QIZI[i]!=None:
                            if x<=QIZI[i].right and x>=QIZI[i].left and y<=QIZI[i].bottom and y>=QIZI[i].top:
                                break
                    if i in B or i==32:
                        return True
                else:
                    return False
    #黑炮走法
    elif b>=12 and b<=13:
        if abs(y-unit.centery)<=0.3*y0:
            m0=(x-unit.centerx)/x0
            if x-unit.centerx>=0:
                for i in range(9):
                    if abs(i-m0)<=0.3:
                        m0=i
                        break
                n0=0
                for i in range(int(m0)):
                    if inRect(unit.centerx+i*x0,unit.centery):
                        n0=n0+1
                if n0==2 and inRect(x,y):
                    for i in range(33):
                        if QIZI[i]!=None:
                            if x<=QIZI[i].right and x>=QIZI[i].left and y<=QIZI[i].bottom and y>=QIZI[i].top:
                                break
                    if i in R or i==32:
                        return True
                elif n0==1 and not inRect(x,y):
                    for i in range(33):
                        if QIZI[i]!=None:
                            if x<=QIZI[i].right and x>=QIZI[i].left and y<=QIZI[i].bottom and y>=QIZI[i].top:
                                break
                    if i in R or i==32:
                        return True
                else:
                    return False
            elif x-unit.centerx<0:
                for i in range(9):
                    if abs(i+m0)<=0.3:
                        m0=i
                        break
                n0=0
                for i in range(int(m0)):
                    if inRect(unit.centerx-x0*i,unit.centery):
                        n0=n0+1
                if n0==2 and inRect(x,y):
                    for i in range(33):
                        if QIZI[i]!=None:
                            if x<=QIZI[i].right and x>=QIZI[i].left and y<=QIZI[i].bottom and y>=QIZI[i].top:
                                break
                    if i in R or i==32:
                        return True
                elif n0==1 and not inRect(x,y):
                    for i in range(33):
                        if QIZI[i]!=None:
                            if x<=QIZI[i].right and x>=QIZI[i].left and y<=QIZI[i].bottom and y>=QIZI[i].top:
                                break
                    if i in R or i==32:
                        return True
                else:
                    return False
        elif abs(x-unit.centerx)<=0.3*x0:
            m0=(y-unit.centery)/y0
            if y-unit.centery>=0:
                for i in range(9):
                    if abs(i-m0)<=0.3:
                        m0=i
                        break
                n0=0
                for i in range(int(m0)):
                    if inRect(unit.centerx,unit.centery+y0*i):
                        n0=n0+1
                if n0==2 and inRect(x,y):
                    for i in range(33):
                        if QIZI[i]!=None:
                            if x<=QIZI[i].right and x>=QIZI[i].left and y<=QIZI[i].bottom and y>=QIZI[i].top:
                                break
                    if i in R or i==32:
                        return True
                elif n0==1 and not inRect(x,y):
                    for i in range(33):
                        if QIZI[i]!=None:
                            if x<=QIZI[i].right and x>=QIZI[i].left and y<=QIZI[i].bottom and y>=QIZI[i].top:
                                break
                    if i in R or i==32:
                        return True
                else:
                    return False
            elif y-unit.centery<0:
                for i in range(9):
                    if abs(i+m0)<=0.3:
                        m0=i
                        break
                n0=0
                for i in range(int(m0)):
                    if inRect(unit.centerx,unit.centery-y0*i):
                        n0=n0+1
                if n0==2 and inRect(x,y):
                    for i in range(33):
                        if QIZI[i]!=None:
                            if x<=QIZI[i].right and x>=QIZI[i].left and y<=QIZI[i].bottom and y>=QIZI[i].top:
                                break
                    if i in R or i==32:
                        return True
                elif n0==1 and not inRect(x,y):
                    for i in range(33):
                        if QIZI[i]!=None:
                            if x<=QIZI[i].right and x>=QIZI[i].left and y<=QIZI[i].bottom and y>=QIZI[i].top:
                                break
                    if i in R or i==32:
                        return True
                else:
                    return False

    #红车走法
    elif b>=14 and b<=15:
        if abs(x-unit.centerx)<=0.3*x0 and abs(y-unit.centery)>=0.7*y0:
            m0=(y-unit.centery)/y0
            if y-unit.centery>=0:
                for i in range(10):
                    if abs(i-m0)<=0.3:
                        m0=i
                        break
                for i in range(1,int(m0)):
                    if inRect(unit.centerx,unit.centery+i*y0):
                        return False
                for i in range(33):
                    if QIZI[i]!=None:
                        if x<=QIZI[i].right and x>=QIZI[i].left and y<=QIZI[i].bottom and y>=QIZI[i].top:
                            break
                if i in B or i==32:
                    return True
            if y<unit.centery:
                for i in range(10):
                    if abs(i+m0)<=0.3:
                        m0=i
                        break
                for i in range(1,int(m0)):
                    if inRect(unit.centerx,unit.centery-i*y0):
                        return False
                for i in range(33):
                    if QIZI[i]!=None:
                        if x<=QIZI[i].right and x>=QIZI[i].left and y<=QIZI[i].bottom and y>=QIZI[i].top:
                            break
                if i in B or i==32:
                    return True
        if abs(y-unit.centery)<=0.3*y0 and abs(x-unit.centerx)>=0.7*x0:
            m0=(x-unit.centerx)/x0
            if x>unit.centerx:
                for i in range(10):
                    if abs(i-m0)<=0.3:
                        m0=i
                        break
                for i in range(1,int(m0)):
                    if inRect(unit.centerx+i*x0,unit.centery):
                        return False
                for i in range(33):
                    if QIZI[i]!=None:
                        if x<=QIZI[i].right and x>=QIZI[i].left and y<=QIZI[i].bottom and y>=QIZI[i].top:
                            break
                if i in B or i==32:
                    return True
            if x<unit.centerx:
                for i in range(10):
                    if abs(i+m0)<=0.3:
                        m0=i
                        break
                for i in range(1,int(m0)):
                    if inRect(unit.centerx-i*x0,unit.centery):
                        return False
                for i in range(33):
                    if QIZI[i]!=None:
                        if x<=QIZI[i].right and x>=QIZI[i].left and y<=QIZI[i].bottom and y>=QIZI[i].top:
                            break
                if i in B or i==32:
                    return True
    #黑车走法
    elif b>=16 and b<=17:
        if abs(x-unit.centerx)<=0.3*x0 and abs(y-unit.centery)>=0.7*y0:
            m0=(y-unit.centery)/y0
            if y-unit.centery>=0:
                for i in range(10):
                    if abs(i-m0)<=0.3:
                        m0=i
                        break
                for i in range(1,int(m0)):
                    if inRect(unit.centerx,unit.centery+i*y0):
                        return False
                for i in range(33):
                    if QIZI[i]!=None:
                        if x<=QIZI[i].right and x>=QIZI[i].left and y<=QIZI[i].bottom and y>=QIZI[i].top:
                            break
                if i in R or i==32:
                    return True
            if y<unit.centery:
                for i in range(10):
                    if abs(i+m0)<=0.3:
                        m0=i
                        break
                for i in range(1,int(m0)):
                    if inRect(unit.centerx,unit.centery-i*y0):
                        return False
                for i in range(33):
                    if QIZI[i]!=None:
                        if x<=QIZI[i].right and x>=QIZI[i].left and y<=QIZI[i].bottom and y>=QIZI[i].top:
                            break
                if i in R or i==32:
                    return True
        if abs(y-unit.centery)<=0.3*y0 and abs(x-unit.centerx)>=0.7*x0:
            m0=(x-unit.centerx)/x0
            if x>unit.centerx:
                for i in range(10):
                    if abs(i-m0)<=0.3:
                        m0=i
                        break
                for i in range(1,int(m0)):
                    if inRect(unit.centerx+i*x0,unit.centery):
                        return False
                for i in range(33):
                    if QIZI[i]!=None:
                        if x<=QIZI[i].right and x>=QIZI[i].left and y<=QIZI[i].bottom and y>=QIZI[i].top:
                            break
                if i in R or i==32:
                    return True
            if x<unit.centerx:
                for i in range(10):
                    if abs(i+m0)<=0.3:
                        m0=i
                        break
                for i in range(1,int(m0)):
                    if inRect(unit.centerx-i*x0,unit.centery):
                        return False
                for i in range(33):
                    if QIZI[i]!=None:
                        if x<=QIZI[i].right and x>=QIZI[i].left and y<=QIZI[i].bottom and y>=QIZI[i].top:
                            break
                if i in R or i==32:
                    return True
    #红马走法
    if b>=18 and b<=19:
        if (inRect(unit.centerx+x0,unit.centery) and inRect(unit.centerx-x0,unit.centery) and inRect(unit.centerx,unit.centery+y0) and inRect(unit.centerx,unit.centery-y0)):
            return False
        elif 1.3*y0>=y-unit.centery>=0.7*y0 and not inRect(unit.centerx+x0,unit.centery) and 2.3*x0>=x-unit.centerx>=1.7*x0:#y+1,x+2
            for i in range(33):
                if QIZI[i]!=None:
                    if x<=QIZI[i].right and x>=QIZI[i].left and y<=QIZI[i].bottom and y>=QIZI[i].top:
                        break
            if i in B or i==32:
                return True
        elif 1.3*y0>=-y+unit.centery>=0.7*y0 and not inRect(unit.centerx+x0,unit.centery) and 2.3*x0>=x-unit.centerx>=1.7*x0:#y-1,x+2
            for i in range(33):
                if QIZI[i]!=None:
                    if x<=QIZI[i].right and x>=QIZI[i].left and y<=QIZI[i].bottom and y>=QIZI[i].top:
                        break
            if i in B or i==32:
                return True
        elif 2.3*y0>=y-unit.centery>=1.7*y0 and not inRect(unit.centerx,unit.centery+y0) and 1.3*x0>=x-unit.centerx>=0.7*x0:#y+2,x+1
            for i in range(33):
                if QIZI[i]!=None:
                    if x<=QIZI[i].right and x>=QIZI[i].left and y<=QIZI[i].bottom and y>=QIZI[i].top:
                        break
            if i in B or i==32:
                return True
        elif 2.3*y0>=y-unit.centery>=1.7*y0 and not inRect(unit.centerx,unit.centery+y0) and 1.3*x0>=-x+unit.centerx>=0.7*x0:#y+2,x-1
            for i in range(33):
                if QIZI[i]!=None:
                    if x<=QIZI[i].right and x>=QIZI[i].left and y<=QIZI[i].bottom and y>=QIZI[i].top:
                        break
            if i in B or i==32:
                return True
        elif 2.3*y0>=-y+unit.centery>=1.7*y0 and not inRect(unit.x,unit.centery-y0) and 1.3*x0>=x-unit.centerx>=0.7*x0:#y-2,x+1
            for i in range(33):
                if QIZI[i]!=None:
                    if x<=QIZI[i].right and x>=QIZI[i].left and y<=QIZI[i].bottom and y>=QIZI[i].top:
                        break
            if i in B or i==32:
                return True
        elif 2.3*y0>=-y+unit.centery>=1.7*y0 and not inRect(unit.centerx,unit.centery-y0) and 1.3*x0>=-x+unit.centerx>=0.7*x0:#y-2,x-1
            for i in range(33):
                if QIZI[i]!=None:
                    if x<=QIZI[i].right and x>=QIZI[i].left and y<=QIZI[i].bottom and y>=QIZI[i].top:
                        break
            if i in B or i==32:
                return True
        elif 1.3*y0>=y-unit.centery>=0.7*y0 and not inRect(unit.centerx-x0,unit.centery) and 2.3*x0>=-x+unit.centerx>=1.7*x0:#y+1,x-2
            for i in range(33):
                if QIZI[i]!=None:
                    if x<=QIZI[i].right and x>=QIZI[i].left and y<=QIZI[i].bottom and y>=QIZI[i].top:
                        break
            if i in B or i==32:
                return True
        elif 1.3*y0>=-y+unit.centery>=0.7*y0 and not inRect(unit.centerx-x0,unit.centery) and 2.3*x0>=-x+unit.centerx>=1.7*x0:#y-1,x-2
            for i in range(33):
                if QIZI[i]!=None:
                    if x<=QIZI[i].right and x>=QIZI[i].left and y<=QIZI[i].bottom and y>=QIZI[i].top:
                        break
            if i in B or i==32:
                return True
 #黑马走法
    if b>=20 and b<=21:
        if (inRect(unit.centerx+x0,unit.centery) and inRect(unit.centerx-x0,unit.centery) and inRect(unit.centerx,unit.centery+y0) and inRect(unit.centerx,unit.centery-y0)):
            return False
        elif 1.3*y0>=y-unit.centery>=0.7*y0 and not inRect(unit.centerx+x0,unit.centery) and 2.3*x0>=x-unit.centerx>=1.7*x0:#y+1,x+2
            for i in range(33):
                if QIZI[i]!=None:
                    if x<=QIZI[i].right and x>=QIZI[i].left and y<=QIZI[i].bottom and y>=QIZI[i].top:
                        break
            if i in R or i==32:
                return True
        elif 1.3*y0>=-y+unit.centery>=0.7*y0 and not inRect(unit.centerx+x0,unit.centery) and 2.3*x0>=x-unit.centerx>=1.7*x0:#y-1,x+2
            for i in range(33):
                if QIZI[i]!=None:
                    if x<=QIZI[i].right and x>=QIZI[i].left and y<=QIZI[i].bottom and y>=QIZI[i].top:
                        break
            if i in R or i==32:
                return True
        elif 2.3*y0>=y-unit.centery>=1.7*y0 and not inRect(unit.centerx,unit.centery+y0) and 1.3*x0>=x-unit.centerx>=0.7*x0:#y+2,x+1
            for i in range(33):
                if QIZI[i]!=None:
                    if x<=QIZI[i].right and x>=QIZI[i].left and y<=QIZI[i].bottom and y>=QIZI[i].top:
                        break
            if i in R or i==32:
                return True
        elif 2.3*y0>=y-unit.centery>=1.7*y0 and not inRect(unit.centerx,unit.centery+y0) and 1.3*x0>=-x+unit.centerx>=0.7*x0:#y+2,x-1
            for i in range(33):
                if QIZI[i]!=None:
                    if x<=QIZI[i].right and x>=QIZI[i].left and y<=QIZI[i].bottom and y>=QIZI[i].top:
                        break
            if i in R or i==32:
                return True
        elif 2.3*y0>=-y+unit.centery>=1.7*y0 and not inRect(unit.x,unit.centery-y0) and 1.3*x0>=x-unit.centerx>=0.7*x0:#y-2,x+1
            for i in range(33):
                if QIZI[i]!=None:
                    if x<=QIZI[i].right and x>=QIZI[i].left and y<=QIZI[i].bottom and y>=QIZI[i].top:
                        break
            if i in R or i==32:
                return True
        elif 2.3*y0>=-y+unit.centery>=1.7*y0 and not inRect(unit.centerx,unit.centery-y0) and 1.3*x0>=-x+unit.centerx>=0.7*x0:#y-2,x-1
            for i in range(33):
                if QIZI[i]!=None:
                    if x<=QIZI[i].right and x>=QIZI[i].left and y<=QIZI[i].bottom and y>=QIZI[i].top:
                        break
            if i in R or i==32:
                return True
        elif 1.3*y0>=y-unit.centery>=0.7*y0 and not inRect(unit.centerx-x0,unit.centery) and 2.3*x0>=-x+unit.centerx>=1.7*x0:#y+1,x-2
            for i in range(33):
                if QIZI[i]!=None:
                    if x<=QIZI[i].right and x>=QIZI[i].left and y<=QIZI[i].bottom and y>=QIZI[i].top:
                        break
            if i in R or i==32:
                return True
        elif 1.3*y0>=-y+unit.centery>=0.7*y0 and not inRect(unit.centerx-x0,unit.centery) and 2.3*x0>=-x+unit.centerx>=1.7*x0:#y-1,x-2
            for i in range(33):
                if QIZI[i]!=None:
                    if x<=QIZI[i].right and x>=QIZI[i].left and y<=QIZI[i].bottom and y>=QIZI[i].top:
                        break
            if i in R or i==32:
                return True
    #红象走法
    if b>=22 and b<=23:
        if 2.3*x0>=abs(x-unit.centerx)>=1.7*x0 and 2.3*y0>=abs(y-unit.centery)>=1.7*y0 and y<=(62.1+4.3*y0):
            if (x-unit.centerx)>0 and (y-unit.centery)>0:
                if not inRect(unit.centerx+x0,unit.centery+y0):
                    for i in range(33):
                        if QIZI[i]!=None:
                            if x<=QIZI[i].right and x>=QIZI[i].left and y<=QIZI[i].bottom and y>=QIZI[i].top:
                                break
                    if i in B or i==32:
                        return True
            if (x-unit.centerx)<0 and (y-unit.centery)>0:
                if not inRect(unit.centerx-x0,unit.centery+y0):
                    for i in range(33):
                        if QIZI[i]!=None:
                            if x<=QIZI[i].right and x>=QIZI[i].left and y<=QIZI[i].bottom and y>=QIZI[i].top:
                                break
                    if i in B or i==32:
                        return True
            if (x-unit.centerx)>0 and (y-unit.centery)<0:
                if not inRect(unit.centerx+x0,unit.centery-y0):
                    for i in range(33):
                        if QIZI[i]!=None:
                            if x<=QIZI[i].right and x>=QIZI[i].left and y<=QIZI[i].bottom and y>=QIZI[i].top:
                                break
                    if i in B or i==32:
                        return True
            if (x-unit.centerx)<0 and (y-unit.centery)<0:
                if not inRect(unit.centerx-x0,unit.centery-y0):
                    for i in range(33):
                        if QIZI[i]!=None:
                            if x<=QIZI[i].right and x>=QIZI[i].left and y<=QIZI[i].bottom and y>=QIZI[i].top:
                                break
                    if i in B or i==32:
                        return True
        else:
            return False
    #黑象走法
    if b>=24 and b<=25:
        if 2.3*x0>=abs(x-unit.centerx)>=1.7*x0 and 2.3*y0>=abs(y-unit.centery)>=1.7*y0 and y>=(62.1+4.3*y0):
            if (x-unit.centerx)>0 and (y-unit.centery)>0:
                if not inRect(unit.centerx+x0,unit.centery+y0):
                    for i in range(33):
                        if QIZI[i]!=None:
                            if x<=QIZI[i].right and x>=QIZI[i].left and y<=QIZI[i].bottom and y>=QIZI[i].top:
                                break
                    if i in R or i==32:
                        return True
            if (x-unit.centerx)<0 and (y-unit.centery)>0:
                if not inRect(unit.centerx-x0,unit.centery+y0):
                    for i in range(33):
                        if QIZI[i]!=None:
                            if x<=QIZI[i].right and x>=QIZI[i].left and y<=QIZI[i].bottom and y>=QIZI[i].top:
                                break
                    if i in R or i==32:
                        return True
            if (x-unit.centerx)<0 and (y-unit.centery)<0:
                if not inRect(unit.centerx-x0,unit.centery-y0):
                    for i in range(33):
                        if QIZI[i]!=None:
                            if x<=QIZI[i].right and x>=QIZI[i].left and y<=QIZI[i].bottom and y>=QIZI[i].top:
                                break
                    if i in R or i==32:
                        return True
            if (x-unit.centerx)>0 and (y-unit.centery)<0:
                if not inRect(unit.centerx+x0,unit.centery-y0):
                    for i in range(33):
                        if QIZI[i]!=None:
                            if x<=QIZI[i].right and x>=QIZI[i].left and y<=QIZI[i].bottom and y>=QIZI[i].top:
                                break
                    if i in R or i==32:
                        return True
        else:
            return False
    #红士走法
    if b>=26 and b<=27:
        if 0.7*x0<=abs(x-unit.centerx)<=1.3*x0 and 0.7*y0<=abs(y-unit.centery)<=1.3*y0 and 70.4+5.3*x0>=x>=70.4+2.7*x0 and 62.1+2.3*y0>=y>=62.1-0.3*y0:
            for i in range(33):
                if QIZI[i]!=None:
                    if x<=QIZI[i].right and x>=QIZI[i].left and y<=QIZI[i].bottom and y>=QIZI[i].top:
                        break
            if i in B or i==32:
                return True
        else:
            return False
    #黑士走法
    if b>=28 and b<=29:
        if 0.7*x0<=abs(x-unit.centerx)<=1.3*x0 and 0.7*y0<=abs(y-unit.centery)<=1.3*y0 and 70.4+5.3*x0>=x>=70.4+2.7*x0 and 62.1+9.3*y0>=y>=62.1+6.7*y0:
            for i in range(33):
                if QIZI[i]!=None:
                    if x<=QIZI[i].right and x>=QIZI[i].left and y<=QIZI[i].bottom and y>=QIZI[i].top:
                         break
            if i in R or i==32:
                return True
        else:
            return False
    #红帅走法
    if b==30:
        if ((0.7*x0<=abs(x-unit.centerx)<=1.3*x0 and abs(y-unit.centery)<=0.3*y0) or (0.7*y0<=abs(y-unit.centery)<=1.3*y0 and abs(x-unit.centerx)<=0.3*x0)) and 70.4+5.3*x0>=x>=70.4+2.7*x0 and 62.1+2.3*y0>=y>=62.1-0.3*y0:
            for i in range(33):
                if QIZI[i]!=None:
                    if x<=QIZI[i].right and x>=QIZI[i].left and y<=QIZI[i].bottom and y>=QIZI[i].top:
                        break
            if i in B or i==32:
                return True
        elif abs(QIZI[30].centerx-unit.centerx)<=0.3*x0 and abs(x-QIZI[31].centerx)<=0.3*x0 and abs(y-QIZI[31].centery)<=0.3*y0:
            m0=(y-unit.centery)/y0
            if y-unit.centery>=0:
                for i in range(10):
                    if abs(i-m0)<=0.3:
                        m0=i
                        break
                for i in range(1,int(m0)):
                    if inRect(unit.centerx,unit.centery+i*y0):
                        return False
            if y<unit.centery:
                for i in range(10):
                    if abs(i+m0)<=0.3:
                        m0=i
                        break
                for i in range(1,int(m0)):
                    if inRect(unit.centerx,unit.centery-i*y0):
                        return False
            for i in range(33):
                if QIZI[i]!=None:
                    if x<=QIZI[i].right and x>=QIZI[i].left and y<=QIZI[i].bottom and y>=QIZI[i].top:
                        break
            if i in B or i==32:
                return True
        else:
            return False
    #黑将走法
    if b==31:
        if ((0.7*x0<=abs(x-unit.centerx)<=1.3*x0 and abs(y-unit.centery)<=0.3*y0) or (0.7*y0<=abs(y-unit.centery)<=1.3*y0 and abs(x-unit.centerx)<=0.3*x0)) and 70.4+5.3*x0>=x>=70.4+2.7*x0 and 62.1+9.3*y0>=y>=62.1+6.7*y0:
            for i in range(33):
                if QIZI[i]!=None:
                    if x<=QIZI[i].right and x>=QIZI[i].left and y<=QIZI[i].bottom and y>=QIZI[i].top:
                        break
            if i in R or i==32:
                return True
        elif abs(QIZI[30].centerx-unit.centerx)<=0.3*x0 and abs(x-QIZI[30].centerx)<=0.3*x0 and abs(y-QIZI[30].centery)<=0.3*y0:
            m0=(y-unit.centery)/y0
            if y-unit.centery>=0:
                for i in range(10):
                    if abs(i-m0)<=0.3:
                        m0=i
                        break
                for i in range(1,int(m0)):
                    if inRect(unit.centerx,unit.centery+i*y0):
                        return False
            if y<unit.centery:
                for i in range(10):
                    if abs(i+m0)<=0.3:
                        m0=i
                        break
                for i in range(1,int(m0)):
                    if inRect(unit.centerx,unit.centery-i*y0):
                        return False
            for i in range(33):
                if QIZI[i]!=None:
                    if x<=QIZI[i].right and x>=QIZI[i].left and y<=QIZI[i].bottom and y>=QIZI[i].top:
                        break
            if i in R or i==32:
                return True
        else:
            return False
#判断是否吃子
def eat(x,y,QIZI):
    for i in range(32):
        if QIZI[i]!=None:
            if x<=QIZI[i].right and x>=QIZI[i].left and y<=QIZI[i].bottom and y>=QIZI[i].top:
                QIZI[i]=None
    return QIZI[:]
#判断是否胜利
def isWin(QIZI):
    if QIZI[30]!=None and QIZI[31]!=None:
        return False
    elif QIZI[30]==None:
        basicFont=pygame.font.SysFont(None,48)
        text=basicFont.render("BLACK WIN!!!",True,WHITE,BLUE)
        textRect=text.get_rect()
        textRect.centerx=windowSurface.get_rect().centerx
        textRect.centery=windowSurface.get_rect().centery
        windowSurface.blit(text,textRect)
        return True
    elif QIZI[31]==None:
        basicFont=pygame.font.SysFont(None,48)
        text=basicFont.render("RED WIN!!!",True,WHITE,BLUE)
        textRect=text.get_rect()
        textRect.centerx=windowSurface.get_rect().centerx
        textRect.centery=windowSurface.get_rect().centery
        windowSurface.blit(text,textRect)
        return True

#开始程序
pygame.display.update()
turn=0
while True:
    for event in pygame.event.get():
        if event.type== QUIT:
            pygame.quit()
            sys.exit()
        if event.type==MOUSEBUTTONDOWN:
            if a==0:
                for i in range(32):
                    if QIZI[i]!=None:
                        if event.pos[0]<=QIZI[i].right and event.pos[0]>=QIZI[i].left and event.pos[1]<=QIZI[i].bottom and event.pos[1]>=QIZI[i].top:
                            b=i
                            if turn==0:
                                if b in R:
                                    a=1
                            if turn==1:
                                if b in B:
                                    a=1
            elif a==1:
                if isRightMove(QIZI[b],event.pos[0],event.pos[1],b):
                    QIZI=eat(event.pos[0],event.pos[1],QIZI)
                    if isWin(QIZI):
                        pygame.display.update()
                        break
                    QIZI[b].centerx=event.pos[0]
                    QIZI[b].centery=event.pos[1]
                    windowSurface=pygame.display.set_mode((700,700),0,32)
                    qipan=pygame.image.load("象棋棋盘.jpg")
                    qipan1=pygame.transform.scale(qipan,(700,700))
                    qipan2 = qipan1.get_rect()
                    windowSurface.blit(qipan1,qipan2)
                    pygame.display.set_caption("象棋")
                    x=pygame.image.load("红兵.png")
                    for i in range(5):
                        if QIZI[i]!=None:
                            windowSurface.blit(x,QIZI[i])
                    x=pygame.image.load("黑卒.png")
                    for i in range(5,10):
                        if QIZI[i]!=None:
                            windowSurface.blit(x,QIZI[i])
                    x=pygame.image.load("红炮.png")
                    for i in range(10,12):
                        if QIZI[i]!=None:
                            windowSurface.blit(x,QIZI[i])
                    x=pygame.image.load("黑炮.png")
                    for i in range(12,14):
                        if QIZI[i]!=None:
                            windowSurface.blit(x,QIZI[i])
                    x=pygame.image.load("红车.png")
                    for i in range(14,16):
                        if QIZI[i]!=None:
                            windowSurface.blit(x,QIZI[i])
                    x=pygame.image.load("黑车.png")
                    for i in range(16,18):
                        if QIZI[i]!=None:
                            windowSurface.blit(x,QIZI[i])
                    x=pygame.image.load("红马.png")
                    for i in range(18,20):
                        if QIZI[i]!=None:
                            windowSurface.blit(x,QIZI[i])
                    x=pygame.image.load("黑马.png")
                    for i in range(20,22):
                        if QIZI[i]!=None:
                            windowSurface.blit(x,QIZI[i])
                    x=pygame.image.load("红象.png")
                    for i in range(22,24):
                        if QIZI[i]!=None:
                            windowSurface.blit(x,QIZI[i])
                    x=pygame.image.load("黑象.png")
                    for i in range(24,26):
                        if QIZI[i]!=None:
                            windowSurface.blit(x,QIZI[i])
                    x=pygame.image.load("红士.png")
                    for i in range(26,28):
                        if QIZI[i]!=None:
                            windowSurface.blit(x,QIZI[i])
                    x=pygame.image.load("黑士.png")
                    for i in range(28,30):
                        if QIZI[i]!=None:
                            windowSurface.blit(x,QIZI[i])
                    x=pygame.image.load("红帅.png")
                    for i in range(30,31):
                        if QIZI[i]!=None:
                            windowSurface.blit(x,QIZI[i])
                    x=pygame.image.load("黑将.png")
                    for i in range(31,32):
                        if QIZI[i]!=None:
                            windowSurface.blit(x,QIZI[i])
                    a=0
                    turn=1-turn
                else:
                    a=0
        pygame.display.update()















            
