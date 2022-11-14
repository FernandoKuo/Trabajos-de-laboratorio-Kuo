#importar librerias
import sys, os, random, time
import pygame as pg
from pygame.locals import *
from nombres_paises import *

pg.init() #inicializacion de pygame

def main(): #funcion principal
    global score, status

    #setup
    clock = pg.time.Clock() #fps
    size = width, height = 1000, 500
    screen = pg.display.set_mode(size)
    path_buttons = 'images/buttons' #path para entrar a los archivos
    path_flags = 'images/flags'
    pg.display.set_caption('Flags Guess')
    icon = None #icono del juego aun no decidido
    #pg.display.set_icon(icon)

    font = pg.font.Font(None, 60) #default font: freesansbold
    sfont = pg.font.Font(None, 45)

    #functions
    def paused():
        while pausing[0]:
            for event in pg.event.get():
                if event.type == QUIT:
                    pg.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_p or event.key == K_ESCAPE:
                        pausing[0] = False
            
            pausa_titulo.draw()
            pausa_resumir.draw()
            pausa_reiniciar.draw()
            pausa_irmenu.draw()

            pg.display.update()
            clock.tick(50)

    #classes
    #convertir las tres clases de botones en una: mision, talvez no
    class button(pg.sprite.Sprite):
        def __init__(self, pos):
            super().__init__()
            self.defaultimage = pg.image.load(os.path.join(path_buttons, 'default_button.png'))
            self.image = self.defaultimage
            self.rect = self.image.get_rect()
            self.rect.topleft = pos
            self.clicked = False
        def draw(self, name, image='default'):
            self.text = font.render(name, True, (0, 0, 0))
            self.trect = self.text.get_rect()
            self.trect.topleft = (self.rect.x + (self.rect.width-self.trect.width)/2, 
                                  self.rect.y + (self.rect.height-self.trect.height)/2)
            if image == 'default': screen.blit(self.defaultimage, self.rect) #mostrar boton (diferentes formas)
            else: screen.blit(self.image, self.rect)
            screen.blit(self.text, self.trect) #mostrar texto sobre el boton
        def choose(self, name, answer):
            #"si la posicion del mouse esta dentro del area del boton"
            if self.rect.collidepoint(pg.mouse.get_pos()):
                if not answered[0]: 
                    self.image = pg.image.load(os.path.join(path_buttons, 'hover_button.png'))
                else: self.image = self.defaultimage
                if not pg.mouse.get_pressed()[0]: self.clicked = True
                if pg.mouse.get_pressed()[0]:
                    if self.clicked:
                        if name == answer: 
                            self.defaultimage = pg.image.load(os.path.join(path_buttons, 'right_button.png'))
                            right[0] = True
                        else:
                            self.defaultimage = pg.image.load(os.path.join(path_buttons, 'wrong_button.png'))
                        answered[0] = True
            else: 
                self.image = self.defaultimage
                self.clicked = False
            self.draw(name, 'IFoundAmogus')
    
    class next_button(pg.sprite.Sprite):
        def __init__(self, pos):
            super().__init__()
            self.image = pg.image.load(os.path.join(path_buttons, 'default_next_button.png'))
            self.rect = self.image.get_rect()
            self.rect.topleft = pos
            self.clicked = False
        def draw(self):
            if self.rect.collidepoint(pg.mouse.get_pos()):
                self.image = pg.image.load(os.path.join(path_buttons, 'hover_next_button.png'))
                if not pg.mouse.get_pressed()[0]: self.clicked = True
                if pg.mouse.get_pressed()[0]:
                    if self.clicked:
                        answered[0] = False
            else: 
                self.image = pg.image.load(os.path.join(path_buttons, 'default_next_button.png'))
                self.clicked = False
            self.text = font.render('NEXT', True, (0, 0, 0))
            self.trect = self.text.get_rect()
            self.trect.topleft = (789, 410)
            screen.blit(self.image, self.rect)
            screen.blit(self.text, self.trect)

    class draw_button(pg.sprite.Sprite):
        def __init__(self, text, rect, color1, color2):
            super().__init__()
            self.surface = pg.Surface((rect[2], rect[3]))
            self.rect = self.surface.get_rect()
            self.rect.topleft = (rect[0], rect[1])
            self.default_color = color1
            self.hover_color = color2
            self.word = text
            self.clicked = False
        def draw(self):
            if self.rect.collidepoint(pg.mouse.get_pos()):
                self.surface.fill(self.hover_color)
                if not pg.mouse.get_pressed()[0]: self.clicked = True
                if pg.mouse.get_pressed()[0]:
                    if self.clicked:
                        pausing[0] = False
                        if not self.word == 'Resumir':
                            running[0] = False
                            if self.word == 'Ir al menu':
                                status[0] = 'menu'
            else: 
                self.surface.fill(self.default_color)
                self.clicked = False
            self.text = sfont.render(self.word, True, (0, 0, 0))
            self.trect = self.text.get_rect()
            self.trect.topleft = (self.rect[0] + (self.rect[2] - self.trect.width)/2, 
                                  self.rect[1] + (self.rect[3] - self.trect.height)/2)
            screen.blit(self.surface, self.rect)
            screen.blit(self.text, self.trect)
            pg.draw.rect(screen, (0, 0, 0), self.rect, 4)

    class flag(pg.sprite.Sprite):
        def __init__(self, name):
            super().__init__()
            self.name = name
            self.image = pg.image.load(os.path.join(path_flags, f'{self.name}.png'))
            self.image = pg.transform.scale(self.image, (500, 333))
            self.rect = self.image.get_rect()
            self.rect.topleft = (30, 30)

    #reiniciar empieza por aca
    flags = []
    for country in countries:
        flags.append(flag(country))

    answered = [False]
    score = 10
    BN = next_button((730, 390))
    pausa_titulo = draw_button('Juego en pausa', (360, 120, 280, 70), (200, 200, 100), (200, 200, 100))
    pausa_resumir = draw_button('Resumir', (390, 210, 220, 50), (0, 128, 255), (51, 153, 255))
    pausa_reiniciar = draw_button('Reiniciar', (390, 280, 220, 50), (0, 128, 255), (51, 153, 255))
    pausa_irmenu = draw_button('Ir al menu', (390, 350, 220, 50), (0, 128, 255), (51, 153, 255))
    
    surf = pg.Surface(size, SRCALPHA)
    pg.draw.rect(surf, (100, 100, 100), (0, 0, width, height))
    asurf = pg.Surface(size, SRCALPHA)
    asurf.fill((255, 255, 255, 150))
    surf.blit(asurf, (0, 0), None, BLEND_RGBA_MULT)
    surf_rect = surf.get_rect()

    #main
    once = True
    running = [0]
    running[0] = True
    play_button_clicked = False
    while running[0]:
        for event in pg.event.get():
            if event.type == QUIT:
                pg.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_p or event.key == K_ESCAPE:
                    if status[0] == 'game': 
                        pausing[0] = True

        if status[0] == 'menu': #setting easy menu
            screen.fill((230, 230, 130))
            play_button = pg.image.load(os.path.join(path_buttons, 'play_button.png'))
            play_button_rect = play_button.get_rect()
            play_button_rect.center = (500, 350)
            screen.blit(play_button, play_button_rect)
            if play_button_rect.collidepoint(pg.mouse.get_pos()):
                if not pg.mouse.get_pressed()[0]:
                    play_button_clicked = True
                if pg.mouse.get_pressed()[0]:
                    if play_button_clicked:
                        status[0] = 'game'
                        time.sleep(0.1)
            else: play_button_clicked = False

        elif status[0] == 'game':
            screen.fill((230, 230, 130))
            if not answered[0]:
                if once: 
                    aflag = random.choice(flags) #elejir bandera
                    flags.remove(aflag)
                    answer = aflag.name #elejir los nombres que apareceran
                    countries.remove(answer)
                    names = random.sample(countries, 3)
                    names.append(answer)
                    countries.append(answer)
                    random.shuffle(names)
                    B1 = button((545, 30)) #reseteo de botones
                    B2 = button((545, 117))
                    B3 = button((545, 204))
                    B4 = button((545, 291))
                    once = False #para que no repita otra vez
                    right = [False]
                    flags_count = f'{str(75-len(flags))}/75'

                B1.choose(names[0], answer)
                B2.choose(names[1], answer)
                B3.choose(names[2], answer)
                B4.choose(names[3], answer)
            
            else: 
                B1.draw(names[0])
                B2.draw(names[1])
                B3.draw(names[2])
                B4.draw(names[3])
                BN.draw()

                if not once and not right[0]:
                    score -= 1/15
                    score = round(score, 2)
                    flags.append(aflag)
                once = True
            
            #mostrar bandera, puntos y cuenta
            screen.blit(aflag.image, aflag.rect)
            pg.draw.rect(screen, (0, 0, 0), aflag.rect, 4)
            score_text = sfont.render('Puntaje: ' + str(score), True, (0, 0, 0))
            flags_count_text = sfont.render(flags_count, True, (0, 0, 0))
            screen.blit(score_text, pg.Rect(30, 390, 0, 0))
            screen.blit(flags_count_text, pg.Rect(30, 440, 0, 0))

            #pausa el juego
            if pausing[0]: 
                screen.blit(surf, surf_rect)
                paused()
        
        pg.display.flip()
        clock.tick(50)

status = [0]
pausing = [0]
status[0] = 'menu'
pausing[0] = False
while __name__ == '__main__': #para que no se importe como modulo
    main()

#Ideas de palabras para el amongus
"""
- 'R.D.C. representa\nRupública Democrática del Congo'
- 'Ya vas con {attempt} intentos' (va sumando mientras el texto esta mostrandose)
- 'I Found Among Us'
- 'Recuerda echarle un vistazo a los creditos!'
- 'Un poco SUS no crees?'
- 'Sabias que el pais mas chico del mundo es el Vaticano?'
- 'Australia es mas ancha que la luna'

Sera un amongus que minimo se estara moviendo (agitando el trasero o caminando)
Para que sea divertido el jugador tendra que clickerarlo para que comienze a moverse
"""
