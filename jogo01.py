import pygame
from random import randint
pygame.init()

x = 30
y = 300
velocidade = 12
x2 = 550
y2 = 275
velocidade2 = 10

tela_inicial = pygame.image.load("tela.png")
fundo = pygame.image.load("fundo.png")
machista = pygame.image.load("machista.png")
barbie_jogo = pygame.image.load("barbie_jogo.png")
barbie_socando_direita = pygame.image.load("barbiesocando.png")
barbie_socando_esquerda = pygame.image.load("barbiesocando2.png")

barbie = barbie_jogo

retangulo1 = barbie.get_rect()
tamanho1 = retangulo1[2]
retangulo2 = machista.get_rect()
tamanho2 = retangulo2[2]

vida_machista = 100
vida_barbie = 100

fonte = pygame.font.SysFont('arial black',20)
fonte2 = pygame.font.SysFont('arial black',70)

janela = pygame.display.set_mode((800, 650))
janela.blit(tela_inicial, (0, 0))
pygame.display.flip()

pygame.display.set_caption('Barbie Power')

clock = pygame.time.Clock()

janela_aberta = True

while janela_aberta == True:
    #numero de frames por segundo:
    clock.tick(10)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            janela_aberta = False

    comandos = pygame.key.get_pressed()

    if comandos[pygame.K_RETURN]:
        tela_inicial = fundo

    texto = fonte.render("Vida da Barbie: {} ".format(vida_barbie), True, (255, 255, 255))
    texto2 = fonte.render('Vida do machista: {}'.format(vida_machista), True, (255, 255, 255))

    machistax = x2 + tamanho2
    barbiex = x + tamanho1

    if barbiex >= x2 and machistax >= x and comandos[pygame.K_RETURN]:
        if x <= x2:
       # x=x2-50
            barbie = barbie_socando_direita
            vida_machista = vida_machista - 10
            x2 = randint(0,600)
        if x >= x2:
            barbie = barbie_socando_esquerda
            vida_machista = vida_machista - 10
            x2 = randint(0, 600)
    else:
        barbie = barbie_jogo

    # movimentos e colisao

    if x > -20:
        if comandos[pygame.K_LEFT]:
            x = x - velocidade

    if x < 678 :
        if comandos[pygame.K_RIGHT]:
            x = x + velocidade

    final = fonte2.render("MAN DOWN!!!", True, (255,255,255))


    janela.blit(tela_inicial, (0, 0))
    janela.blit(barbie, (x, y))
    janela.blit(machista, (x2, y2))
    janela.blit(texto, (25, 7))
    janela.blit(texto2, (540, 7))
    if vida_machista <= 0:
        janela.blit(final, (150, 525))

    pygame.display.update()
pygame.quit()