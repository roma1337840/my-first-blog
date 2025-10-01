# class Animal:
#     def __init__ (self, name,kind):
#         self.name = name
#         self.kind = kind
#         self.sound = sound
#     def save_to_file(self, filename="animals.txt"):
#         with open(filename, "a") as file:
#             file.write(f"{self.kind} {self.name} говорит: {self.sound}\n")
#
# cat = Animal("Мурка","Кошка", "мяу")
# cat.save_to_file()


# import pygame
# pygame.init()
# dis=pygame.display.set_mode((500,400))
#
# blue = (0,0,255)
# brown = (150,75,0)
# red = (255,0,0)
# yellow = (255,255,0)
#
# dis_over=False
# while not dis_over:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             print(event)
#             pygame.quit()
#     walls = pygame.Rect(150,200,200,150)
#     pygame.draw.rect(dis,brown,walls)
#     door = pygame.Rect(230,270,40,80)
#     pygame.draw.rect(dis,blue,door)
#     pygame.draw.polygon(dis,red, [(140,200),(260,100), (360,200)])
#     window = pygame.Rect(180,230,40,40)
#     pygame.draw.rect(dis,yellow,window)
#
#     pygame.display.update()
# quit()

import pygame
pygame.init()
dis=pygame.display.set_mode((500,400))
yellow = (255,255,0)
white = (255,255,255)
dis_over=False
while not dis_over:
     for event in pygame.event.get():
         if event.type == pygame.QUIT:
             dis_over = True
     pygame.draw.circle(dis,yellow,(250,200),80)
     pygame.draw.circle(dis,white,(220,180),15)
     pygame.draw.circle(dis,white, (280,180), 15)
     rect = pygame.Rect(210,220,80,40)
     pygame.draw.ellipse(dis, (255,0,0), rect, 4)
     pygame.display.update()
pygame.quit()



