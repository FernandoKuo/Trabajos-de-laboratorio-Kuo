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

    #classes
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
        def choose(self, name, answer, answered, right):
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
        def draw(self, answered):
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
            self.trect.topleft = (789, 409.5)
            screen.blit(self.image, self.rect)
            screen.blit(self.text, self.trect)

    class flag(pg.sprite.Sprite):
        def __init__(self, name):
            super().__init__()
            self.name = name
            self.image = pg.image.load(os.path.join(path_flags, f'{self.name}.png'))
            self.image = pg.transform.scale(self.image, (500, 333))
            self.rect = self.image.get_rect()
            self.rect.topleft = (30, 30)

    flags = []
    for country in countries:
        flags.append(flag(country))

    BN = next_button((730, 390))

    #main
    once = True
    running = True
    play_button_clicked = False
    while running:
        for event in pg.event.get():
            if event.type == QUIT:
                pg.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_p or event.key == K_ESCAPE:
                    if status == 'game': status = 'pause'
                    elif status == 'pause': status = 'game'

        screen.fill((230, 230, 130))

        if status == 'menu': #setting easy menu
            play_button = pg.image.load(os.path.join(path_buttons, 'play_button.png'))
            play_button_rect = play_button.get_rect()
            play_button_rect.center = (500, 350)
            screen.blit(play_button, play_button_rect)
            if play_button_rect.collidepoint(pg.mouse.get_pos()):
                if not pg.mouse.get_pressed()[0]:
                    play_button_clicked = True
                if pg.mouse.get_pressed()[0]:
                    if play_button_clicked:
                        status = 'game'
                        time.sleep(0.1)
            else: play_button_clicked = False

        elif status == 'pause':
            pass


        elif status == 'game':
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

                B1.choose(names[0], answer, answered, right)
                B2.choose(names[1], answer, answered, right)
                B3.choose(names[2], answer, answered, right)
                B4.choose(names[3], answer, answered, right)
            
            else: 
                B1.draw(names[0])
                B2.draw(names[1])
                B3.draw(names[2])
                B4.draw(names[3])
                BN.draw(answered)

                if not once and not right[0]:
                    score -= 1/15
                    score = round(score, 2)
                    flags.append(aflag)
                once = True
            
            #mostrar bandera, puntos y cuenta
            screen.blit(aflag.image, aflag.rect)
            pg.draw.rect(screen, (0, 0, 0), aflag.rect, 4)
            score_text = sfont.render('Puntaje: '+str(score), True, (0, 0, 0))
            flags_count_text = sfont.render(flags_count, True, (0, 0, 0))
            screen.blit(score_text, pg.Rect(30, 390, 0, 0))
            screen.blit(flags_count_text, pg.Rect(30, 440, 0, 0))

            """surf = pg.Surface(size, SRCALPHA)
            pg.draw.rect(surf, (100, 100, 100), (0, 0, width, height))
            asurf = pg.Surface(size, SRCALPHA)
            asurf.fill((255, 255, 255, 100))
            surf.blit(asurf, (0, 0), None, BLEND_RGBA_MULT)
            surf_rect = surf.get_rect()
            screen.blit(surf, surf_rect)"""
        
        pg.display.flip()
        clock.tick(60)

if __name__ == '__main__': #para que no se importe como modulo
    answered = [False]
    score = 10
    status = 'menu'
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
