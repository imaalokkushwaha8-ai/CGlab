# def drawline_bla(x1,y1,x2,y2):
#     x=x1
#     y=y1
#     dx=abs(x2-x1)
#     dy=abs(y2-y1)
#     if(x2>x1):
#         lx=1
#     else:
#         lx=-1
#     if(y2>y1):
#         ly=1
#     else:
#         ly=-1
#     print(x1,y1)
#     if (dx>dy):
#         p=2*dy-dx
#         for k in range(dx):
#             if (p<0):
#                 x=x+lx
#                 y=y
#                 p=p+2*dy
#             else:
#                 x=x+lx
#                 y=y+ly
#                 p=p+(2*dy)-(2*dx)
#             print(x,y)
#     else:
#         p=(2*dx)-dy
#         for k in range(dy):
#             if (p<0):
#                 x=x
#                 y=y+ly
#                 p=p+2*dx
#             else:
#                 x=x+lx
#                 y=y+ly
#                 p=p+(2*dx)-(2*dy)
#             print(x,y) 
# drawline_bla(0,1,7,6)

# import pygame 
# import sys
# pygame.init()
# w,h=800,800
# screen=pygame.display.set_mode((w,h))
# WHITE=(255,255,255)
# black=(0,0,0)
# def drawline_bla(x1,y1,x2,y2):
#     x=x1
#     y=y1
#     dx=abs(x2-x1)
#     dy=abs(y2-y1)
#     if(x2>x1):
#         lx=1
#     else:
#         lx=-1
#     if(y2>y1):
#         ly=1
#     else:
#         ly=-1
#     if (dx>dy):
#         p=2*dy-dx
#         for k in range(dx):
#             if (p<0):
#                 x=x+lx
#                 y=y
#                 p=p+2*dy
#             else:
#                 x=x+lx
#                 y=y+ly
#                 p=p+(2*dy)-(2*dx)
#             screen.set_at((x,y),WHITE)
#     else:
#         p=(2*dx)-dy
#         for k in range(dy):
#             if (p<0):
#                 x=x
#                 y=y+ly
#                 p=p+2*dx
#             else:
#                 x=x+lx
#                 y=y+ly
#                 p=p+(2*dx)-(2*dy)
#                 screen.set_at((x,y),WHITE) 

# def main():
#     screen.fill(black)
#     drawline_bla(100,150,500,600)
#     pygame.display.flip()

#     while True:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 sys.exit()

# if __name__ == "__main__":
#     main()            

import pygame 
import sys
pygame.init()
w,h=700,700
screen=pygame.display.set_mode((w,h))
WHITE=(255,255,255)
black=(0,0,0)
def drawline_bla(x1,y1,x2,y2):
    x=x1
    y=y1
    dx=abs(x2-x1)
    dy=abs(y2-y1)
    if(x2>x1):
        lx=1
    else:
        lx=-1
    if(y2>y1):
        ly=1
    else:
        ly=-1
    if (dx>dy):
        p=2*dy-dx
        for k in range(dx):
            if (p<0):
                x=x+lx
                y=y
                p=p+2*dy
            else:
                x=x+lx
                y=y+ly
                p=p+(2*dy)-(2*dx)
            screen.set_at((x,y),WHITE)
    else:
        p=(2*dx)-dy
        for k in range(dy):
            if (p<0):
                x=x
                y=y+ly
                p=p+2*dx
            else:
                x=x+lx
                y=y+ly
                p=p+(2*dx)-(2*dy)
            screen.set_at((x,y),WHITE) 

def main():
    screen.fill(black)
    drawline_bla(100,200,600,200)
    drawline_bla(100,500,600,500)
    drawline_bla(200,100,200,600)
    drawline_bla(500,100,500,600)
    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

if __name__ == "__main__":
    main()            

# import pygame 
# import sys
# pygame.init()
# w,h=700,700
# screen=pygame.display.set_mode((w,h))
# WHITE=(255,255,255)
# black=(0,0,0)
# def drawline_bla(x1,y1,x2,y2):
#     x=x1
#     y=y1
#     dx=abs(x2-x1)
#     dy=abs(y2-y1)
#     if(x2>x1):
#         lx=1
#     else:
#         lx=-1
#     if(y2>y1):
#         ly=1
#     else:
#         ly=-1
#     if (dx>dy):
#         p=2*dy-dx
#         for k in range(dx):
#             if (p<0):
#                 x=x+lx
#                 y=y
#                 p=p+2*dy
#             else:
#                 x=x+lx
#                 y=y+ly
#                 p=p+(2*dy)-(2*dx)
#             screen.set_at((x,y),WHITE)
#     else:
#         p=(2*dx)-dy
#         for k in range(dy):
#             if (p<0):
#                 x=x
#                 y=y+ly
#                 p=p+2*dx
#             else:
#                 x=x+lx
#                 y=y+ly
#                 p=p+(2*dx)-(2*dy)
#             screen.set_at((x,y),WHITE) 

# def main():
#     screen.fill(black)
#     drawline_bla(350,100,600,600)
#     drawline_bla(100,300,600,600)
#     drawline_bla(100,300,600,300)
#     drawline_bla(600,300,100,600)
#     drawline_bla(100,600,350,100)
#     pygame.display.flip()

#     while True:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 sys.exit()

# if __name__ == "__main__":
#     main()            
