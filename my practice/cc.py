# import pygame
# pygame.init()
# dis=pygame.display.set_mode((500,400))
# red = (255,0,0)
# yellow = (255,255,0)
# blue = (0,0,255)
# dis_over=False
# while not dis_over:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             print(event)
#             pygame.quit()
#     walls = pygame.Rect(0,0,100,100)
#     pygame.draw.rect(dis, red, walls)
#     walls2 = pygame.Rect(100,0,100,100)
#     pygame.draw.rect(dis, yellow, walls2)
#     walls3 = pygame.Rect(200, 0, 100, 100)
#     pygame.draw.rect(dis, blue, walls3)
#     walls4 = pygame.Rect(300,0,100,100)
#     pygame.draw.rect(dis, red, walls4)
#     walls5 = pygame.Rect(400, 0, 100, 100)
#     pygame.draw.rect(dis, yellow, walls5)
#
#     pygame.display.update()
# quit()

import pygame

pygame.init()
dis = pygame.display.set_mode((400, 400))
clock = pygame.time.Clock()
colors = [(255, 0, 0), (255, 255, 0), (0, 0, 255)]

dis_over = False
offset_y = 0
speed = 20

while not dis_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    dis.fill((0, 0, 0))
    for i in range(5):
        for j in range(4):
            x = i * 100
            y = j * 100 + offset_y
            color = colors[(i+j) % len(colors)]
            wall = pygame.Rect(x,y, 100,100)
            pygame.draw.rect(dis,color, (x,y,100,100))

    pygame.display.update()
    offset_y += (offset_y + speed) % 400
    clock.tick(2)

pygame.quit()



