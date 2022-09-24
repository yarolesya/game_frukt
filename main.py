import pygame
import random

a = list(range(100, 1001, 100))

random_numbers = random.sample(a, 4)

q = random_numbers[0]
q1 = random_numbers[1]
q2 = random_numbers[2]
q3 = random_numbers[3]

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

# q = random.randint(100, 1000)
# q1 = random.randint(100, 1000)
# q2 = random.randint(100, 1000)
# q3 = random.randint(100, 1000)
a = list(range(40, 120, 21))

random_numbers = random.sample(a, 4)

speedorange = random_numbers[0]/100
speedlemon = random_numbers[1]/100
speedarbuz = random_numbers[2]/100
speedbomba = random_numbers[3]/100

p = 50
n = 50

f = 50
c = 50

t = 50
d = 60

run = True

score = 0

while run:
    for i in pygame.event.get():
        keys = pygame.key.get_pressed()
        if i.type == pygame.QUIT:
            run = False
    if keys[pygame.K_LEFT]:
        z -= 4
    if keys[pygame.K_RIGHT]:
        z += 4

    if z < -200:
        z = 1550
    if z > 1550:
        z = -200

    sharik += speedorange
    if sharik > ty - 18 and q <= z + 165 and q >= z - 25 and sharik < 800:
        x = 0
        y = 0
    frukt = pygame.transform.scale(frukt, (x, y))

    sharik1 += speedlemon
    if sharik1 > ty - 18 and q1 <= z + 168 and q1 >= z - 35 and sharik1 < 800:
        n = 0
        p = 0
    frukt1 = pygame.transform.scale(frukt1, (p, n))

    sharik2 += speedarbuz
    if sharik2 > ty - 18 and q2 <= z + 168 and q2 >= z - 35 and sharik2 < 800:
        c = 0
        f = 0
    frukt2 = pygame.transform.scale(frukt2, (f, c))

    sharik3 += speedbomba
    if sharik3 > ty - 18 and q3 <= z + 168 and q3 >= z - 35 and sharik3 < 800:
        t = 0
        d = 0
        win1 = 0
        win2 = 0
        win3 = 0
        v = 0
        z = 0
        f = 0
        c = 0
        p = 0
        n = 0
        x = 0
        y = 0
        score = 0
    frukt3 = pygame.transform.scale(frukt3, (d, t))
    frukt2 = pygame.transform.scale(frukt2, (f, c))
    frukt1 = pygame.transform.scale(frukt1, (p, n))
    frukt = pygame.transform.scale(frukt, (x, y))
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

    win.fill([win1, win2, win3])
    win.blit(b, [z, ty])
    win.blit(frukt, [q, sharik])
    win.blit(frukt1, [q1, sharik1])
    win.blit(frukt2, [q2, sharik2])
    win.blit(frukt3, [q3, sharik3])

    if sharik >= ty - 18 and sharik < ty - 18 + speedorange and q <= z + 168 and q >= z - 35:
        score += 1

    if sharik1 >= ty - 18 and sharik1 < ty - 18 + speedlemon and q1 <= z + 168 and q1 >= z - 35:
        score += 1

    if sharik2 >= ty - 18 and sharik2 < ty - 18 + speedarbuz and q2 <= z + 168 and q2 >= z - 35:
        score += 1

    # ввод текста на экран
    font = pygame.font.Font(pygame.font.get_default_font(), 36)
    text_surface = font.render('Score: {}'.format(score), True, (255, 0, 0))
    win.blit(text_surface, dest=(0, 0))

    pygame.display.update()
pygame.quit()
