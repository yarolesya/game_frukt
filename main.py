import pygame
import random

# рандомное число

for i in range(20):
  num = random.randint(0, 10)
  print(num)


pygame.init()
win = pygame.display.set_mode((1550, 800))
pygame.display.set_caption('')

frukt = pygame.image.load('jranges.png')
frukt = pygame.transform.scale(frukt, (50, 50))

b = pygame.image.load('телегаа.png')
b = pygame.transform.scale(b, (200, 150))

frukt1 = pygame.image.load('lemon.png')
frukt1 = pygame.transform.scale(frukt1, (50, 50))

frukt2 = pygame.image.load('arbuz.png')
frukt2 = pygame.transform.scale(frukt2, (50, 50))

frukt3 = pygame.image.load('bomba.png')
frukt3 = pygame.transform.scale(frukt3, (50, 50))


win1 = 25
win2 = 71
win3 = 87


z = 0
ty = 650


sharik = 0
sharik1 = 0
sharik2 = 0
sharik3 = 0


x = 50
y = 50

u = 200
v = 150


speedorange = random.randint(3, 10)/10
speedlemon = random.randint(3, 10)/10
speedarbuz = random.randint(3, 10)/10
speedbomba = random.randint(3, 10)/10


p = 50
n = 50

f = 50
c = 50

t = 50
d = 60

run = True

g = 0

while run:
  for i in pygame.event.get():
    keys = pygame.key.get_pressed()
    if i. type == pygame.QUIT:
      run = False
  if keys[pygame.K_LEFT]:
    z -= 4
  if keys[pygame.K_RIGHT]:
    z += 4




  if z < -200:
    z = 1550
  if z > 1550:
    z = -200




  sharik+=speedorange
  if sharik > ty-18 and 500 <= z+165 and 500 >= z-25 and sharik < 800:
    x = 0
    y = 0
  frukt = pygame.transform.scale(frukt, (x, y))





  sharik1 += speedlemon
  if sharik1 > ty - 18 and 800 <= z + 168 and 800 >= z - 35 and sharik1 < 800:
    n = 0
    p = 0
  frukt1 = pygame.transform.scale(frukt1, (p, n))





  sharik2 += speedarbuz
  if sharik2 > ty - 18 and 200 <= z + 168 and 200 >= z - 35 and sharik2 < 800:
    c = 0
    f = 0
  frukt2 = pygame.transform.scale(frukt2, (f, c))





  sharik3 += speedbomba
  if sharik3 > ty - 18 and 600 <= z + 168 and 600 >= z - 35 and sharik3 < 800:
    t = 0
    d = 0
    win1 = 0
    win2 = 0
    win3 = 0
    v = 0
    z = 0
  frukt3 = pygame.transform.scale(frukt3, (d, t))
  b = pygame.transform.scale(b, (u, v))



  if sharik > 800:
   x = 0
   y = 0
  frukt = pygame.transform.scale(frukt, (x, y))





  if sharik1 > 800:
   n = 0
   p = 0
  frukt1 = pygame.transform.scale(frukt1, (p, n))



  if sharik2 > 800:
   f = 0
   c = 0
  frukt2 = pygame.transform.scale(frukt2, (c, f))


  if sharik3 > 800:
   d = 0
   t = 0
  frukt3 = pygame.transform.scale(frukt3, (d, t))








  win.fill([win1,win2,win3])
  win.blit(b, [z, ty])
  win.blit(frukt, [500, sharik])
  win.blit(frukt1, [800, sharik1])
  win.blit(frukt2, [200, sharik2])
  win.blit(frukt3, [600, sharik3])


  g += 1
  # вывод текста на экран
  font = pygame.font.Font(pygame.font.get_default_font(), 36)
  text_surface = font.render('Score: {}'.format(g), True, (255, 0, 0))
  win.blit(text_surface, dest=(0, 0))


  pygame.display.update()
pygame.quit()
