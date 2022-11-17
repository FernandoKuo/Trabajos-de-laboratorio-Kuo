#importar librerias
import sys, random, time
import pygame as pg
from os import path
from pygame.locals import *
from pygame import image
from FG_data import *

pg.init() #inicializacion de pygame

def main(): #funcion principal
    global status, pausing, score

    #setup
    clock = pg.time.Clock() #fps
    size = width, height = 1000, 500
    screen = pg.display.set_mode(size)
    path_images = 'images'
    path_buttons = 'images/buttons' #path para entrar a los archivos
    path_countries = 'images/flags/countries'
    path_provinces = 'images/flags/provinces'
    path_amo = 'images/Among_Us'
    pg.display.set_caption('Flags Guess')
    icon = image.load(path.join(path_images, 'FG icono.png')) #icono del juego
    pg.display.set_icon(icon)
    logo = image.load(path.join(path_images, 'FG logo.png')) #logo del juego
    logo = pg.transform.scale(logo, (650, 140))

    bfont = pg.font.Font(None, 100) #default font: freesansbold
    font = pg.font.Font(None, 60)
    sfont = pg.font.Font(None, 45)
    ssfont = pg.font.Font(None, 25)
    lfont = pg.font.Font(None, 20)
    credits_text = lfont.render('Credits: Tonanyulo3', True, (0, 0, 0))

    #variables
    score = [10]
    over = [False]
    once = [True]
    answered = [False]
    running = [True]
    play_button_clicked = [False]
    attempts = [0]

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
        
    def guess_countries():
        global score, B1, B2, B3, B4, names, aflag, flags_count, answer, right
        
        if status[0] == 'game':
            if not answered[0]:
                if once[0]: 
                    try:
                        aflag = random.choice(flags) #elejir bandera
                        flags.remove(aflag)
                        answer = aflag.name #elejir los nombres que apareceran
                        countries.remove(answer)
                        names = random.sample(countries, 3)
                        names.append(answer)
                        countries.append(answer)
                        random.shuffle(names)
                    except: over[0] = True
                    B1 = button((545, 30)) #reseteo de botones
                    B2 = button((545, 117))
                    B3 = button((545, 204))
                    B4 = button((545, 291))
                    once[0] = False #para que no repita otra vez
                    right = [False]
                    flags_count = f'{str(75-len(flags))}/75'

                B1.motion_draw(names[0])
                B2.motion_draw(names[1])
                B3.motion_draw(names[2])
                B4.motion_draw(names[3]) #funcionan ya que las variables son globales
            
            else: 
                B1.draw(names[0])
                B2.draw(names[1])
                B3.draw(names[2])
                B4.draw(names[3])
                BN.motion_draw()

                if not once[0] and not right[0]:
                    score[0] -= 1/15
                    score[0] = round(score[0], 2)
                    flags.append(aflag)
                    over[0] = False
                once[0] = True
            
            #mostrar bandera, puntos y cuenta
            pg.draw.rect(screen, (255, 255, 255), (30, 30, 500, 333))
            aflag.draw()
            pg.draw.rect(screen, (0, 0, 0), (30, 30, 500, 333), 4)
            score_text = sfont.render('Puntaje: ' + str(score[0]), True, (0, 0, 0))
            flags_count_text = sfont.render(flags_count, True, (0, 0, 0))
            screen.blit(score_text, pg.Rect(30, 390, 0, 0))
            screen.blit(flags_count_text, pg.Rect(30, 440, 0, 0))

    def guess_provinces():
        global score, B1, B2, B3, B4, names, aflag, flags_count, answer, right
        
        if status[0] == 'game':
            if not answered[0]:
                if once[0]: 
                    try:
                        aflag = random.choice(cflags) #elejir bandera
                        cflags.remove(aflag)
                        answer = aflag.name #elejir los nombres que apareceran
                        provinces.remove(answer)
                        names = random.sample(provinces, 3)
                        names.append(answer)
                        provinces.append(answer)
                        random.shuffle(names)
                    except: 
                        over[0] = True
                    B1 = button((545, 30)) #reseteo de botones
                    B2 = button((545, 117))
                    B3 = button((545, 204))
                    B4 = button((545, 291))
                    once[0] = False #para que no repita otra vez
                    right = [False]
                    flags_count = f'{str(24-len(cflags))}/24'

                B1.motion_draw(names[0])
                B2.motion_draw(names[1])
                B3.motion_draw(names[2])
                B4.motion_draw(names[3]) #funcionan ya que las variables son globales
            
            else: 
                B1.draw(names[0])
                B2.draw(names[1])
                B3.draw(names[2])
                B4.draw(names[3])
                BN.motion_draw()

                if not once[0] and not right[0]:
                    score[0] -= 1/4.8
                    score = [round(score[0], 2)]
                    cflags.append(aflag)
                    over[0] = False
                once[0] = True
            
            #mostrar bandera, puntos y cuenta
            pg.draw.rect(screen, (255, 255, 255), (30, 30, 500, 333))
            aflag.draw()
            pg.draw.rect(screen, (0, 0, 0), (30, 30, 500, 333), 4)
            score_text = sfont.render('Puntaje: ' + str(score[0]), True, (0, 0, 0))
            flags_count_text = sfont.render(flags_count, True, (0, 0, 0))
            screen.blit(score_text, pg.Rect(30, 390, 0, 0))
            screen.blit(flags_count_text, pg.Rect(30, 440, 0, 0))

    #classes
    class button(pg.sprite.Sprite): #se divide en boton de choose y next
        global answer, right
        def __init__(self, pos, kind='choose'):
            super().__init__()
            if kind=='next': self.image = image.load(path.join(path_buttons, 'default_next_button.png'))
            elif kind=='choose': self.image = image.load(path.join(path_buttons, 'default_button.png'))
            self.rect = self.image.get_rect()
            self.rect.topleft = pos
            self.ischoose = True if kind=='choose' else False
            self.clicked = False
        def draw(self, name='NEXT'):
            self.text = font.render(name, True, (0, 0, 0))
            self.trect = self.text.get_rect()
            if self.ischoose: self.trect.topleft = (self.rect.x + (self.rect.width-self.trect.width)/2, 
                                                    self.rect.y + (self.rect.height-self.trect.height)/2)
            else: self.trect.topleft = (789, 410)
            screen.blit(self.image, self.rect)
            screen.blit(self.text, self.trect) #mostrar texto sobre el boton
        def motion_draw(self, name='NEXT'):
            #"si la posicion del mouse esta dentro del area del boton"
            if self.rect.collidepoint(pg.mouse.get_pos()):
                if self.ischoose:
                    if not answered[0]: 
                        self.image = image.load(path.join(path_buttons, 'hover_button.png'))
                else: self.image = image.load(path.join(path_buttons, 'hover_next_button.png'))
                if not pg.mouse.get_pressed()[0]: self.clicked = True
                if pg.mouse.get_pressed()[0]:
                    if self.clicked:
                        if self.ischoose:
                            if name == answer: 
                                self.image = image.load(path.join(path_buttons, 'right_button.png'))
                                right[0] = True
                            else:
                                self.image = image.load(path.join(path_buttons, 'wrong_button.png'))
                            answered[0] = True
                            attempts[0] += 1
                        else: 
                            self.image = image.load(path.join(path_buttons, 'default_next_button.png'))
                            answered[0] = False
            else:
                if self.ischoose: self.image = self.image = image.load(path.join(path_buttons, 'default_button.png'))
                else: self.image = image.load(path.join(path_buttons, 'default_next_button.png'))
                self.clicked = False
            self.draw(name)

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
                        if self.word == 'Países' or self.word == 'Provincias': 
                            mode[0] = self.word
                            status[0] = 'game'
                            option[0] = 'menu'
                        else:
                            pausing[0] = False
                            if self.word == 'Creditos':
                                pass
                            elif not self.word == 'Resumir':
                                running[0] = False
                                if self.word == 'Ir al menu':
                                    status[0] = 'menu'
                            time.sleep(0.1)
            else: 
                self.surface.fill(self.default_color)
                self.clicked = False
            self.text = sfont.render(self.word, True, (0, 0, 0))
            self.trect = self.text.get_rect()
            self.trect.topleft = (self.rect[0] + (self.rect[2] - self.trect.width)/2, 
                                  self.rect[1] + (self.rect[3] - self.trect.height)/2)
            screen.blit(self.surface, self.rect)
            screen.blit(self.text, self.trect)
            pg.draw.rect(screen, (0, 0, 0), self.rect, 3)

    class flag(pg.sprite.Sprite):
        def __init__(self, name, kind):
            super().__init__()
            self.name = name
            if kind == 'country': self.image = image.load(path.join(path_countries, f'{self.name}.png'))
            elif kind == 'province': self.image = image.load(path.join(path_provinces, f'{self.name}.png'))
            self.rect = self.image.get_rect()
            self.rect.topleft = (30, 30)
        def draw(self):
            if self.rect.height > self.rect.width: #la bandera es mas alta que ancha
                new_width = self.rect.width/(self.rect.height/333) #newX = 333*X/Y
                self.image = pg.transform.scale(self.image, (new_width, 333))
            else: self.image = pg.transform.scale(self.image, (500, 333))
            screen.blit(self.image, self.rect)

    #banderas
    flags = []
    for country in countries:
        flags.append(flag(country, 'country'))
    cflags = []
    for province in provinces:
        cflags.append(flag(province, 'province'))

    #setup de muchos botones
    BN = button((730, 390), 'next')
    pausa_titulo = draw_button('Juego en pausa', (360, 100, 280, 70), (200, 180, 100), (200, 200, 100))
    pausa_resumir = draw_button('Resumir', (400, 180, 200, 50), (0, 128, 255), (51, 153, 255))
    pausa_reiniciar = draw_button('Reiniciar', (400, 250, 200, 50), (0, 128, 255), (51, 153, 255))
    pausa_irmenu = draw_button('Ir al menu', (400, 320, 200, 50), (0, 128, 255), (51, 153, 255))
    menu_countries = draw_button('Países', (225, 310, 220, 60), (0, 255, 0), (100, 255, 100))
    menu_provinces = draw_button('Provincias', (525, 310, 220, 60), (0, 255, 0), (100, 255, 100))
    gm_irmenu = draw_button('Ir al menu', (400, 360, 200, 50), (0, 128, 255), (51, 153, 255))
    play_button = image.load(path.join(path_buttons, 'play_button.png'))
    play_button_rect = play_button.get_rect()
    play_button_rect.topleft = (400, 300)
    
    #fondo oscuro invisible del menu de pausa
    surf = pg.Surface(size, SRCALPHA)
    pg.draw.rect(surf, (100, 100, 100), (0, 0, width, height))
    asurf = pg.Surface(size, SRCALPHA)
    asurf.fill((255, 255, 255, 180))
    surf.blit(asurf, (0, 0), None, BLEND_RGBA_MULT)
    surf_rect = surf.get_rect()

    #configuracion del amongus
    amocount = 0
    amoimage = None
    amotext = None
    amotext = ssfont.render(random.choice(amowords), True, (0, 0, 0))
    amowalking = [pg.transform.scale(image.load(path.join(path_amo, 'Walkmogus1.png')), (120, 120)), 
                  pg.transform.scale(image.load(path.join(path_amo, 'Walkmogus2.png')), (120, 120)), 
                  pg.transform.scale(image.load(path.join(path_amo, 'Walkmogus3.png')), (120, 120)), 
                  pg.transform.scale(image.load(path.join(path_amo, 'Walkmogus4.png')), (120, 120))]
    amorect = amowalking[0].get_rect()
    amorect.topleft = (220, 365)
    amoclicked = False

    #main
    option = ['menu']
    while running[0]:
        screen.fill((230, 230, 130))

        if over[0]:
            big_mode = bfont.render(f'Modo: {mode[0]}', True, (0, 0, 0))
            big_score = bfont.render(str(score[0]), True, (0, 0, 0))
            bigs_rect = big_score.get_rect()
            bigs_rect.center = (500, 240)
            screen.blit(big_mode, (200, 80))
            screen.blit(big_score, bigs_rect)
            gm_irmenu.draw()

        elif status[0] == 'menu': #setting easy menu
            screen.blit(logo, (175, 70)) #siempre muestran en el menu
            screen.blit(credits_text, (870, 481))
            if option[0] == 'menu':
                screen.blit(play_button, play_button_rect)
                #para que funcione correctamente el boton de jugar
                if play_button_rect.collidepoint(pg.mouse.get_pos()):
                    if not pg.mouse.get_pressed()[0]:
                        play_button_clicked[0] = True
                    if pg.mouse.get_pressed()[0]:
                        if play_button_clicked[0]:
                            option[0] = 'choose'
                else: play_button_clicked[0] = False
            elif option[0] == 'choose':
                menu_countries.draw()
                menu_provinces.draw()

        #Among Us (muy importante)
        elif status[0] == 'game':
            screen.blit(amoimage, amorect)
            screen.blit(amotext, (320, 400))
            if pg.Rect(240, 380, 80, 100).collidepoint(pg.mouse.get_pos()):
                if not pg.mouse.get_pressed()[0]: amoclicked = True
                if pg.mouse.get_pressed()[0]:
                    if amoclicked: pausing[0] = True
            else: amoclicked = False
        
        #main part
        if not over[0]:
            if mode[0] == 'Países': guess_countries()
            elif mode[0] == 'Provincias': guess_provinces()

        #pausa el juego
        if pausing[0]: 
            screen.blit(surf, surf_rect)
            paused()
        
        for event in pg.event.get():
            if event.type == QUIT:
                pg.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_p or event.key == K_ESCAPE:
                    if status[0] == 'game': 
                        pausing[0] = True
            if event.type == amowalk:
                amoimage = amowalking[amocount]
                amocount += 1
                if amocount > 3: amocount = 0
            if event.type == amosay:
                amotext = ssfont.render(random.choice(amowords), True, (0, 0, 0))
                amoattemptword = ssfont.render(f'Ya vas con {attempts[0]} intentos', True, (0, 0, 0))
                amotext = random.choices([amotext, amoattemptword], [5, 1])[0]

        pg.display.flip()
        clock.tick(50)

status = ['menu']
pausing = [False]
mode = [None]
amowalk = USEREVENT
amosay = USEREVENT + 1
pg.time.set_timer(amowalk, 400)
pg.time.set_timer(amosay, 6000)
#el juego se reinicia cuando pongo reiniciar o ir al menu
while __name__ == '__main__': #para que no se importe como modulo
    main()

#Ideas de palabras para el amongus
"""
- 'R.D.C. representa\nRupública Democrática del Congo'
- 'Ya vas con {attempt} intentos' (va sumando mientras el texto esta mostrandose)
- 'I Found Among Us'
- 'Recuerda echarle un vistazo a los creditos!'
- 'Un poco SUS no crees?'
- 'Sabias que el pais mas chico del mundo es Vaticano?'
- 'Australia es mas ancha que la luna'

Sera un amongus que minimo se estara moviendo (agitando el trasero o caminando)
Para que sea divertido el jugador tendra que clickerarlo para que comienze a moverse
"""
