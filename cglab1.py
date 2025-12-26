# x1=int(input("Enter first x coordinate:"))
# y1=int(input("Enter first y coordinate:"))
# x2=int(input("Enter second x coordinate:"))
# y2=int(input("Enter second y coordinate:"))
# dx=abs(x2-x1)
# dy=abs(y2-y1)
# if(dx>dy):
#     step=dx
# else:
#     step=dy
# xinc=dx/step
# yinc=dy/step
# x=x1
# y=y1
# for i in range(step):
#     x=x+xinc
#     y=y+yinc
#     print(x,y)

# import pygame 
# import sys
# pygame.init()
# w,h=400,300
# screen=pygame.display.set_mode((w,h))
# WHITE=(255,255,255)
# black=(0,0,0)
# def drawline_dda(x1,x2,y1,y2):
#     print("hello")
#     dx=abs(x2-x1)
#     dy=abs(y2-y1)
#     if abs(dx)>abs(dy):
#         step=abs(dx)
#     else:
#         step=abs(dy)
#     xinc=dx/step
#     yinc=dy/step
#     x=x1
#     y=y1
#     for i in range(step):
#         x=x+xinc
#         y=y+yinc
#         screen.set_at((round(x),round(y)),WHITE)
# def main():
#     screen.fill(black)
#     drawline_dda(100,150,200,250)
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
w,h=400,300
screen=pygame.display.set_mode((w,h))
WHITE=(255,255,255)
black=(0,0,0)
def drawline_dda(x1,x2,y1,y2):
    print("hello")
    dx=abs(x2-x1)
    dy=abs(y2-y1)
    if abs(dx)>abs(dy):
        step=abs(dx)
    else:
        step=abs(dy)
    xinc=dx/step
    yinc=dy/step
    x=x1
    y=y1
    for i in range(step):
        x=x+xinc
        y=y+yinc
        screen.set_at((round(x),round(y)),WHITE)
def main():
    screen.fill(black)
    drawline_dda(100,150,200,250)
    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

if __name__ == "__main__":
    main()            

