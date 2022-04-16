from const import*
import pygame, os, random, sys, ctypes
from win32api import GetSystemMetrics
myappid = 'mycompany.myproduct.subproduct.version'
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

from logicajogo import*

class Game:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        pygame.display.set_icon(pygame.image.load(os.path.join(os.getcwd(),"images", "icone.png")))
        self.jogando = False
        self.ligado = True
        self.twoplayers = False
        self.dificulty = 0
        self.partidas = 1
        self.selecionado  = False
        self.menu_options = False
        self.selecionando = False
        self.menu = False
        self.largura = 1280
        self.fimdejogo = False
        self.altura = 720
        self.mouse_hover = False
        self.tela = pygame.display.set_mode((self.largura, self.altura))
        pygame.display.set_caption("Jogo da Velha")
        self.relogio = pygame.time.Clock()       
        self.fonte = pygame.font.match_font(FONTE)        
        self.carregar_arquivos()
        self.tabuleiro_img = self.spritesheet.subsurface((0,0),(404,404))
        self.tab_rect = self.tabuleiro_img.get_rect()
        self.x = self.spritesheet.subsurface((808,404),(128,128))
        self.o = self.spritesheet.subsurface((936,404),(128,128))
        self.x2 = self.spritesheet2.subsurface((808,404),(128,128))
        self.o2 = self.spritesheet2.subsurface((936,404),(128,128))
        self.tabuleiro = [
            [" "," "," "],
            [" "," "," "],
            [" "," "," ",],
        ]
        self.jogador1 = "X"
        self.jogador2 = "O"
        self.contador = 1
        self.pontos1 = 0
        self.pontos2 = 0
        self.empates = 0
            
    def carregar_arquivos(self):
        self.spritesheet = os.path.join(os.getcwd(),"images", SPRITESHEET)
        self.spritesheet = pygame.image.load(self.spritesheet).convert_alpha()
        self.spritesheet2 = os.path.join(os.getcwd(),"images", "image4.png")
        self.spritesheet2 = pygame.image.load(self.spritesheet2).convert_alpha()
        

        self.back_button = os.path.join(os.getcwd(),"images", "image5.png")
        self.back_button = pygame.image.load(self.back_button).convert_alpha()
        self.onoff_button = os.path.join(os.getcwd(),"images", "onoff.png")
        self.onoff_button = pygame.image.load(self.onoff_button).convert_alpha()
        self.opt1_button = os.path.join(os.getcwd(),"images", "image7.png")
        self.opt1_button = pygame.image.load(self.opt1_button).convert_alpha()

        self.opt2_button = os.path.join(os.getcwd(),"images", "image6.png")
        self.opt2_button = pygame.image.load(self.opt2_button).convert_alpha()
        
        self.opt3_button = os.path.join(os.getcwd(),"images", "image8.png")
        self.opt3_button = pygame.image.load(self.opt3_button).convert_alpha()

        self.opt4_button = os.path.join(os.getcwd(),"images", "image101.png")
        self.opt4_button = pygame.image.load(self.opt4_button).convert_alpha()

        self.opt5_button = os.path.join(os.getcwd(),"images", "image9.png")
        self.opt5_button = pygame.image.load(self.opt5_button).convert_alpha()

        self.opt6_button = os.path.join(os.getcwd(),"images", "image11.png")
        self.opt6_button = pygame.image.load(self.opt6_button).convert_alpha()

        self.opt10_button = os.path.join(os.getcwd(),"images", "normal.png")
        self.opt10_button = pygame.image.load(self.opt10_button).convert_alpha()

        self.opt11_button = os.path.join(os.getcwd(),"images", "hard.png")
        self.opt11_button = pygame.image.load(self.opt11_button).convert_alpha()

    def eventos(self):
        while self.ligado:
            pos = pygame.mouse.get_pos()
            for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.jogando = False
                        self.menu_options = False
                        self.menu = False
                        self.mouse_hover = False
                        self.fimdejogo = False
                        self.selecionando = False
                        self.ligado = False
                        sys.exit()
                        
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            
                            self.jogando = False
                            self.menu_options = False
                            self.menu = False
                            self.mouse_hover = False
                            self.fimdejogo = False
                            self.selecionando = False
                            self.restart()
                            self.novo_jogo()
                            self.main_menu()
                        elif self.fimdejogo:
                                return "restart"
                    if event.type == pygame.MOUSEMOTION:
                        pos = pygame.mouse.get_pos()
                        if self.selecionando:
                            if self.opt10_button2.collidepoint(pos):
                                if not self.mouse_hover:
                                    self.mouse_hover = True
                                    self.opt10_button = os.path.join(os.getcwd(),"images", "normal2.png")
                                    self.opt10_button = pygame.image.load(self.opt10_button).convert_alpha()
                                    return
                            
                            elif self.opt11_button2.collidepoint(pos):
                                if not self.mouse_hover:
                                    self.mouse_hover = True
                                    self.opt11_button = os.path.join(os.getcwd(),"images", "hard2.png")
                                    self.opt11_button = pygame.image.load(self.opt11_button).convert_alpha()
                                    return
                            else:
                                self.mouse_hover = False
                                self.opt10_button = os.path.join(os.getcwd(),"images", "normal.png")
                                self.opt10_button = pygame.image.load(self.opt10_button).convert_alpha()
                                
                                self.opt11_button = os.path.join(os.getcwd(),"images", "hard.png")
                                self.opt11_button = pygame.image.load(self.opt11_button).convert_alpha()
                                
                                return
                        if self.menu_options:
                            if self.opt1_button2.collidepoint(pos):
                                if not self.mouse_hover:
                                    self.mouse_hover = True
                                    self.opt1_button = os.path.join(os.getcwd(),"images", "image72.png")
                                    self.opt1_button = pygame.image.load(self.opt1_button).convert_alpha()
                                    return
                            
                            elif self.opt2_button2.collidepoint(pos):
                                if not self.mouse_hover:
                                    self.mouse_hover = True
                                    self.opt2_button = os.path.join(os.getcwd(),"images", "image62.png")
                                    self.opt2_button = pygame.image.load(self.opt2_button).convert_alpha()
                                    return
                           
                            elif self.opt3_button2.collidepoint(pos):
                                if not self.mouse_hover:
                                    self.mouse_hover = True
                                    self.opt3_button = os.path.join(os.getcwd(),"images", "image82.png")
                                    self.opt3_button = pygame.image.load(self.opt3_button).convert_alpha()
                                    return
                            else:
                                self.mouse_hover = False
                                self.opt1_button = os.path.join(os.getcwd(),"images", "image7.png")
                                self.opt1_button = pygame.image.load(self.opt1_button).convert_alpha()
                                
                                self.opt2_button = os.path.join(os.getcwd(),"images", "image6.png")
                                self.opt2_button = pygame.image.load(self.opt2_button).convert_alpha()
                                
                                self.opt3_button = os.path.join(os.getcwd(),"images", "image8.png")
                                self.opt3_button = pygame.image.load(self.opt3_button).convert_alpha()
                                return
                        if self.menu:
                            if self.opt6_button2.collidepoint(pos):
                                if not self.mouse_hover:
                                    self.mouse_hover = True
                                    self.opt6_button = os.path.join(os.getcwd(),"images", "image12.png")
                                    self.opt6_button = pygame.image.load(self.opt6_button).convert_alpha()
                                    return
                            
                            elif self.opt5_button2.collidepoint(pos):
                                if not self.mouse_hover:
                                    self.mouse_hover = True
                                    self.opt5_button = os.path.join(os.getcwd(),"images", "image92.png")
                                    self.opt5_button = pygame.image.load(self.opt5_button).convert_alpha()
                                    return
                           
                            elif self.opt4_button2.collidepoint(pos):
                                if not self.mouse_hover:
                                    self.mouse_hover = True
                                    self.opt4_button = os.path.join(os.getcwd(),"images", "image102.png")
                                    self.opt4_button = pygame.image.load(self.opt4_button).convert_alpha()
                                    return
                            else:
                                self.mouse_hover = False
                                self.opt4_button = os.path.join(os.getcwd(),"images", "image101.png")
                                self.opt4_button = pygame.image.load(self.opt4_button).convert_alpha()
                                
                                self.opt6_button = os.path.join(os.getcwd(),"images", "image11.png")
                                self.opt6_button = pygame.image.load(self.opt6_button).convert_alpha()
                                
                                self.opt5_button = os.path.join(os.getcwd(),"images", "image9.png")
                                self.opt5_button = pygame.image.load(self.opt5_button).convert_alpha()
                                return
                        if self.jogando:
                            if self.buttons[0].collidepoint(pos):
                                if self.tabuleiro[0][0] == " ":
                                    if not self.mouse_hover:
                                        self.mouse_hover = True
                                        self.print_tabuleiro()
                                        if self.jogador_atual == self.jogador1:
                                            self.tela.blit(self.x2, (self.dicionario[f"L_{0}"],self.dicionario[f"C_{0}"]))
                                        else:
                                            self.tela.blit(self.o2, (self.dicionario[f"L_{0}"],self.dicionario[f"C_{0}"]))
                                        pygame.display.flip()
                            elif self.buttons[1].collidepoint(pos):
                                if self.tabuleiro[0][1] == " ":
                                    if not self.mouse_hover:
                                        self.mouse_hover = True
                                        self.print_tabuleiro()
                                        if self.jogador_atual == self.jogador1:
                                            self.tela.blit(self.x2, (self.dicionario[f"L_{0}"],self.dicionario[f"C_{1}"]))
                                        else:
                                            self.tela.blit(self.o2, (self.dicionario[f"L_{0}"],self.dicionario[f"C_{1}"]))
                                        pygame.display.flip()
                            elif self.buttons[2].collidepoint(pos):
                                if self.tabuleiro[0][2] == " ":
                                    if not self.mouse_hover:
                                        self.mouse_hover = True
                                        self.print_tabuleiro()
                                        if self.jogador_atual == self.jogador1:
                                            self.tela.blit(self.x2, (self.dicionario[f"L_{0}"],self.dicionario[f"C_{2}"]))
                                        else:
                                            self.tela.blit(self.o2, (self.dicionario[f"L_{0}"],self.dicionario[f"C_{2}"]))
                                        pygame.display.flip()
                            elif self.buttons[3].collidepoint(pos):
                                if self.tabuleiro[1][0] == " ":
                                    if not self.mouse_hover:
                                        self.mouse_hover = True
                                        self.print_tabuleiro()
                                        if self.jogador_atual == self.jogador1:
                                            self.tela.blit(self.x2, (self.dicionario[f"L_{1}"],self.dicionario[f"C_{0}"]))
                                        else:
                                            self.tela.blit(self.o2, (self.dicionario[f"L_{1}"],self.dicionario[f"C_{0}"]))
                                        pygame.display.flip()
                            elif self.buttons[4].collidepoint(pos):
                                if self.tabuleiro[1][1] == " ":
                                    if not self.mouse_hover:
                                        self.mouse_hover = True
                                        self.print_tabuleiro()
                                        if self.jogador_atual == self.jogador1:
                                            self.tela.blit(self.x2, (self.dicionario[f"L_{1}"],self.dicionario[f"C_{1}"]))
                                        else:
                                            self.tela.blit(self.o2, (self.dicionario[f"L_{1}"],self.dicionario[f"C_{1}"]))
                                        pygame.display.flip()
                            elif self.buttons[5].collidepoint(pos):
                                if self.tabuleiro[1][2] == " ":
                                    if not self.mouse_hover:
                                        self.mouse_hover = True
                                        self.print_tabuleiro()
                                        if self.jogador_atual == self.jogador1:
                                            self.tela.blit(self.x2, (self.dicionario[f"L_{1}"],self.dicionario[f"C_{2}"]))
                                        else:
                                            self.tela.blit(self.o2, (self.dicionario[f"L_{1}"],self.dicionario[f"C_{2}"]))
                                        pygame.display.flip()
                            elif self.buttons[6].collidepoint(pos):
                                if self.tabuleiro[2][0] == " ":
                                    if not self.mouse_hover:
                                        self.mouse_hover = True
                                        self.print_tabuleiro()
                                        if self.jogador_atual == self.jogador1:
                                            self.tela.blit(self.x2, (self.dicionario[f"L_{2}"],self.dicionario[f"C_{0}"]))
                                        else:
                                            self.tela.blit(self.o2, (self.dicionario[f"L_{2}"],self.dicionario[f"C_{0}"]))
                                        pygame.display.flip()
                            elif self.buttons[7].collidepoint(pos):
                                if self.tabuleiro[2][1] == " ":
                                    if not self.mouse_hover:
                                        self.mouse_hover = True
                                        self.print_tabuleiro()
                                        if self.jogador_atual == self.jogador1:
                                            self.tela.blit(self.x2, (self.dicionario[f"L_{2}"],self.dicionario[f"C_{1}"]))
                                        else:
                                            self.tela.blit(self.o2, (self.dicionario[f"L_{2}"],self.dicionario[f"C_{1}"]))
                                        pygame.display.flip()
                            elif self.buttons[8].collidepoint(pos):
                                if self.tabuleiro[2][2] == " ":
                                    if not self.mouse_hover:
                                        self.mouse_hover = True
                                        self.print_tabuleiro()
                                        if self.jogador_atual == self.jogador1:
                                            self.tela.blit(self.x2, (self.dicionario[f"L_{2}"],self.dicionario[f"C_{2}"]))
                                        else:
                                            self.tela.blit(self.o2, (self.dicionario[f"L_{2}"],self.dicionario[f"C_{2}"]))
                                        pygame.display.flip()
                                
                            else:
                                self.mouse_hover = False
                                self.print_tabuleiro()
                                
                    if event.type == pygame.MOUSEBUTTONDOWN:
                                                
                        if self.selecionando:
                            if self.back_rect.collidepoint(pos):
                                self.jogando = False
                                self.menu_options = False
                                self.menu = False
                                self.mouse_hover = False
                                self.fimdejogo = False
                                self.selecionando = False
                                self.restart()
                                self.novo_jogo()
                                self.main_menu()
                            if self.opt10_button_rect.collidepoint(pos):
                                self.dificulty = 1
                                self.selecionando = False
                                self.selecionado = True
                                return
                            if self.opt11_button_rect.collidepoint(pos):
                                self.selecionando = False
                                self.selecionado = True
                                self.dificulty = 2
                                return
                        if self.fimdejogo:
                            if self.back_rect.collidepoint(pos):
                                self.jogando = False
                                self.menu_options = False
                                self.menu = False
                                self.mouse_hover = False
                                self.fimdejogo = False
                                self.restart()
                                self.novo_jogo()
                                self.main_menu()
                            return "restart"
                        if self.menu:
                            if self.opt4_button_rect.collidepoint(pos):
                                self.jogando = False
                                self.menu_options = False
                                self.menu = False
                                self.mouse_hover = False
                                self.twoplayers = False
                                self.jogar()
                            if self.opt5_button_rect.collidepoint(pos):
                                self.jogando = False
                                self.menu_options = False
                                self.menu = False
                                self.mouse_hover = False
                                self.twoplayers = True
                                self.jogar()
                            if self.opt6_button_rect.collidepoint(pos):
                                self.jogando = False
                                self.menu_options = False
                                self.menu = False
                                self.mouse_hover = False
                                self.options()
                            if self.onoff_rect.collidepoint(pos):
                                pygame.quit()
                                self.jogando = False
                                self.menu_options = False
                                self.menu = False
                                self.mouse_hover = False
                                self.fimdejogo = False
                                self.selecionando = False
                                self.ligado = False
                                sys.exit()
                                return
                                
                        if self.menu_options:
                            if self.back_rect.collidepoint(pos):
                                self.jogando = False
                                self.menu_options = False
                                self.menu = False
                                self.mouse_hover = False
                                self.main_menu()
                            if self.opt1_button_rect.collidepoint(pos):
                                self.altura = 600
                                self.largura = 800
                                self.mouse_hover = False
                                self.tela = pygame.display.set_mode((self.largura, self.altura))
                                self.options()
                                return True
                            if self.opt2_button_rect.collidepoint(pos):
                                self.altura = 720
                                self.largura = 1280
                                self.mouse_hover = False
                                self.tela = pygame.display.set_mode((self.largura, self.altura))
                                self.options()
                                return True
                            if self.opt3_button_rect.collidepoint(pos):
                                self.altura = GetSystemMetrics(1)
                                self.largura = GetSystemMetrics(0)
                                self.mouse_hover = False
                                self.tela = pygame.display.set_mode((self.largura, self.altura),pygame.FULLSCREEN)
                                self.options()
                                return True
                        if self.jogando:
                            if self.back_rect.collidepoint(pos):
                                self.jogando = False
                                self.menu_options = False
                                self.menu = False
                                self.mouse_hover = False
                                self.fimdejogo = False
                                self.restart()
                                self.novo_jogo()
                                self.main_menu()
                        #coluna 1
                            
                            if self.buttons[0].collidepoint(pos):
                                if self.tabuleiro[0][0] == " ":
                                    recebendo_jogada = False
                                    return (0,0)

                                
                            if self.buttons[1].collidepoint(pos):
                                if self.tabuleiro[0][1] == " ":
                                    recebendo_jogada = False
                                    return (0,1)
                                
                            if self.buttons[2].collidepoint(pos):
                                if self.tabuleiro[0][2] == " ":
                                    recebendo_jogada = False
                                    return (0,2)
                            #coluna 2
                            if self.buttons[3].collidepoint(pos):
                                if self.tabuleiro[1][0] == " ":
                                    recebendo_jogada = False
                                    return (1,0)
                                
                            if self.buttons[4].collidepoint(pos):
                                if self.tabuleiro[1][1] == " ":
                                    recebendo_jogada = False
                                    return (1,1)
                                
                            if self.buttons[5].collidepoint(pos):
                                if self.tabuleiro[1][2] == " ":
                                    recebendo_jogada = False
                                    return (1,2)
                            #coluna 3
                            if self.buttons[6].collidepoint(pos):
                                if self.tabuleiro[2][0] == " ":
                                    recebendo_jogada = False
                                    return (2,0)
                                
                            if self.buttons[7].collidepoint(pos):
                                if self.tabuleiro[2][1] == " ":
                                    recebendo_jogada = False
                                    return (2,1)
                                
                            if self.buttons[8].collidepoint(pos):
                                if self.tabuleiro[2][2] == " ":
                                    recebendo_jogada = False
                                    return (2,2) 
                            

    def atualizar_pos(self):
        self.tab_rect.center = (self.largura//2,self.altura//2)
        self.buttons = [(pygame.Rect(self.tab_rect[0],self.tab_rect[1],128,128)),
        (pygame.Rect(self.tab_rect[0],self.tab_rect[1]+138,128,128)),
        (pygame.Rect(self.tab_rect[0],self.tab_rect[1]+138+138,128,128)),
        (pygame.Rect(self.tab_rect[0]+138,self.tab_rect[1],128,128)),
        (pygame.Rect(self.tab_rect[0]+138,self.tab_rect[1]+138,128,128)),
        (pygame.Rect(self.tab_rect[0]+138,self.tab_rect[1]+138+138,128,128)),
        (pygame.Rect(self.tab_rect[0]+138+138,self.tab_rect[1],128,128)),
        (pygame.Rect(self.tab_rect[0]+138+138,self.tab_rect[1]+138,128,128)),
        (pygame.Rect(self.tab_rect[0]+138+138,self.tab_rect[1]+138+138,128,128))
        ]
        self.dicionario = {"L_0" : self.tab_rect[0],
                            "L_1" : self.tab_rect[0]+138,
                            "L_2" : self.tab_rect[0]+138+138,

                            "C_0" : self.tab_rect[1],
                            "C_1" : self.tab_rect[1]+138,
                            "C_2" : self.tab_rect[1]+138+138}

        self.faixa = pygame.Rect(0,self.altura//10,self.largura,80)
        
        self.back_rect = self.back_button.get_rect()
        self.back_rect.center = (self.largura//15,self.altura//10+40)
        self.onoff_rect = self.onoff_button.get_rect()
        self.onoff_rect.center = (self.largura//25,self.altura//20)

        self.opt1_button_rect = self.opt1_button.get_rect()
        self.opt1_button_rect.center = (self.largura//2,self.altura//3+self.altura//15)

        self.opt2_button_rect = self.opt2_button.get_rect()
        self.opt2_button_rect.center = (self.largura//2,self.altura//3+self.altura//5+self.altura//15)
                
        self.opt3_button_rect = self.opt3_button.get_rect()
        self.opt3_button_rect.center = (self.largura//2,self.altura//3+self.altura//5*2+self.altura//15)
        
        self.opt1_button2 = pygame.Rect(0,0,400,100)
        self.opt1_button2.center = (self.largura//2,self.altura//3+self.altura//15)

        self.opt2_button2 = pygame.Rect(0,0,400,100)
        self.opt2_button2.center = (self.largura//2,self.altura//3+self.altura//5+self.altura//15)

        self.opt3_button2 = pygame.Rect(0,0,400,100)
        self.opt3_button2.center = (self.largura//2,self.altura//3+self.altura//5*2+self.altura//15)

        self.opt4_button_rect = self.opt4_button.get_rect()
        self.opt4_button_rect.center = (self.largura//2,self.altura//3+self.altura//15)

        self.opt5_button_rect = self.opt5_button.get_rect()
        self.opt5_button_rect.center = (self.largura//2,self.altura//3+self.altura//5+self.altura//15)
                
        self.opt6_button_rect = self.opt6_button.get_rect()
        self.opt6_button_rect.center = (self.largura//2,self.altura//3+self.altura//5*2+self.altura//15)

        self.opt6_button2 = pygame.Rect(0,0,400,100)
        self.opt6_button2.center = (self.largura//2,self.altura//3+self.altura//5*2+self.altura//15)

        self.opt4_button2 = pygame.Rect(0,0,400,100)
        self.opt4_button2.center = (self.largura//2,self.altura//3+self.altura//15)

        self.opt5_button2 = pygame.Rect(0,0,400,100)
        self.opt5_button2.center = (self.largura//2,self.altura//3+self.altura//5+self.altura//15)

        self.opt10_button_rect = self.opt10_button.get_rect()
        self.opt10_button_rect.center = (self.largura//2,self.altura//2 - self.altura//15)

        self.opt10_button2 = pygame.Rect(0,0,400,100)
        self.opt10_button2.center = (self.largura//2,self.altura//2 - self.altura//15)

        self.opt11_button_rect = self.opt11_button.get_rect()
        self.opt11_button_rect.center = (self.largura//2,self.altura//2 + self.altura//4)

        self.opt11_button2 = pygame.Rect(0,0,400,100)
        self.opt11_button2.center = (self.largura//2,self.altura//2 + self.altura//4)


    def mostrar_texto(self,texto,tamanho,cor,x,y):
        fonte = pygame.font.Font(self.fonte, tamanho)
        texto = fonte.render(texto, True, cor)
        texto_rect = texto.get_rect()
        texto_rect.center = (x,y)
        self.tela.blit(texto, texto_rect)

    def select_dificulty(self):
        self.novo_jogo()
        self.selecionando = True
        while self.selecionando:
            self.tela.fill(FUNDO)
            self.atualizar_pos()
            pygame.draw.rect(self.tela, LINHAS, self.faixa)
            self.mostrar_texto("DIFICULTY",80,COR_CIRC,self.largura//2,self.altura//10+43)
            self.tela.blit(self.back_button, (self.back_rect))
            self.tela.blit(self.opt10_button, (self.opt10_button_rect))
            self.tela.blit(self.opt11_button, (self.opt11_button_rect))
            pygame.display.flip()
            self.eventos()
            

    def jogar(self):
        if not self.twoplayers and not self.selecionado:
            self.select_dificulty()
    
        self.jogando =  True
        self.tela.fill(FUNDO)
        
        self.atualizar_pos()
        self.print_tabuleiro()
        
        
        pygame.display.flip()
        while self.jogando:
            if self.twoplayers:
                if self.contador%2 == 1:
                    self.jogador_atual = self.jogador1
                    jogada = self.eventos()
                else:
                    self.jogador_atual = self.jogador2
                    jogada = self.eventos()
            else:
                if self.contador%2 == 1:
                    self.jogador_atual = self.jogador1
                    jogada = self.eventos()
                else:
                    self.jogador_atual = self.jogador2
                    jogada = inteligencia(self.tabuleiro,"O","X","O",self.dificulty)

            if jogada == None:
                self.ligado = False
                sys.exit()
                break
            self.tabuleiro[jogada[0]][jogada[1]] = self.jogador_atual
            self.print_tabuleiro()
            self.contador +=1
            resultado = verificar_resultado(self.tabuleiro)
            if resultado != 0:
                self.verificar_local_vit(self.jogador_atual)
                self.jogando = False 
                self.acabou(resultado)
                

    def print_tabuleiro(self):
        self.tela.fill(FUNDO)

        self.mostrar_texto(f"VELHAS: {self.empates}",80,COR_X,self.largura//2,self.altura - self.altura//15)

        if self.twoplayers:
            self.mostrar_texto(f"X: {self.pontos1}",80,COR_X,self.largura//8,self.altura - self.altura//15)
            self.mostrar_texto(f"O: {self.pontos2}",80,COR_X,self.largura - self.largura//8,self.altura - self.altura//15)
        else:
            self.mostrar_texto(f"YOU: {self.pontos1}",80,COR_X,self.largura//8,self.altura - self.altura//15)
            self.mostrar_texto(f"A.I: {self.pontos2}",80,COR_X,self.largura - self.largura//10,self.altura - self.altura//15)
            if self.dificulty == 1:
                self.mostrar_texto("NORMAL",40,COR_X,self.largura - self.largura//12,self.altura//15)
            elif self.dificulty == 2:
                self.mostrar_texto("HARD",40,COR_X,self.largura - self.largura//12,self.altura//15)
        self.atualizar_pos()
        self.tela.blit(self.tabuleiro_img, (self.tab_rect))
        for i in range(3):
            for j in range(3):
                if self.tabuleiro[i][j] != " ":
                    if self.tabuleiro[i][j] == self.jogador1:                        
                        self.tela.blit(self.x, (self.dicionario[f"L_{i}"],self.dicionario[f"C_{j}"]))
                    elif self.tabuleiro[i][j] == self.jogador2: 
                        self.tela.blit(self.o, (self.dicionario[f"L_{i}"],self.dicionario[f"C_{j}"]))
        self.tela.blit(self.back_button, (self.back_rect))
        pygame.display.flip()        
       
    def verificar_local_vit(self,jogador):
        if jogador == self.jogador1:
            linha = self.spritesheet.subsurface((0,404),(404,128))
            coluna = self.spritesheet.subsurface((2020,0),(128,404))
            diagonal_1 = self.spritesheet.subsurface((808,0),(404,404))
            diagonal_2 = self.spritesheet.subsurface((404,0),(404,404))
        else:
            linha = self.spritesheet.subsurface((404,404),(404,128))
            coluna = self.spritesheet.subsurface((2148,0),(128,404))
            diagonal_1 = self.spritesheet.subsurface((1616,0),(404,404))
            diagonal_2 = self.spritesheet.subsurface((1212,0),(404,404))
        z = verificar_resultado(self.tabuleiro)
        if z != 0:
            if z == 2:
                #velha
                pass
            elif z[1] == "linha":           
                self.tela.blit(linha, (self.dicionario[f"L_{0}"],self.dicionario[f"C_{z[2]}"]))
            elif z[1] == "coluna":
                self.tela.blit(coluna, (self.dicionario[f"L_{z[2]}"],self.dicionario[f"C_{0}"]))
            elif z[1] == "diagonal_1":
                self.tela.blit(diagonal_1, (self.dicionario[f"L_{0}"],self.dicionario[f"C_{0}"]))
            elif z[1] == "diagonal_2":
                self.tela.blit(diagonal_2, (self.dicionario[f"L_{0}"],self.dicionario[f"C_{0}"]))
        pygame.display.flip()
    
    def novo_jogo(self):
        self.contador = 1
        self.pontos1 = 0
        self.pontos2 = 0
        self.partidas = 1
        self.empates = 0
        self.selecionado = False

    def acabou(self,resultado):
        self.fimdejogo = True
        self.partidas +=1
        while self.fimdejogo:
            if resultado == 2:
                a = random.randint(0,1)
                self.empates += 1
                if a == 0:
                    self.mostrar_texto("DEU VELHA",80,COR_CIRC,self.largura//2,self.altura//10)
                else:
                    self.mostrar_texto("DEU VELHA",80,COR_X,self.largura//2,self.altura//10)
            else:
                if self.jogador_atual == "O":
                    self.pontos2 += 1
                    self.mostrar_texto(f"VITORIA DE {self.jogador_atual}",80,COR_CIRC,self.largura//2,self.altura//10)
                else:
                    self.pontos1 += 1
                    self.mostrar_texto(f"VITORIA DE {self.jogador_atual}",80,COR_X,self.largura//2,self.altura//10)
            pygame.display.flip()
            a = self.eventos()
            if a == "restart":
                self.fimdejogo = False
                self.restart()
                self.jogar()

    def restart(self):
        self.tabuleiro = [
            [" "," "," "],
            [" "," "," "],
            [" "," "," ",],
        ]
        if self.partidas%2 != 0:
            self.contador = 1
        elif self.partidas%2 == 0:
            self.contador = 2

    def options(self):

        self.menu_options = True
        self.carregar_arquivos()
               

        while self.menu_options:
            self.tela.fill(FUNDO)
            self.atualizar_pos()
            pygame.draw.rect(self.tela, LINHAS, self.faixa)
            self.mostrar_texto("OPTIONS",80,COR_CIRC,self.largura//2,self.altura//10+43)
            self.tela.blit(self.back_button, (self.back_rect))
            self.tela.blit(self.opt1_button, (self.opt1_button_rect))
            self.tela.blit(self.opt2_button, (self.opt2_button_rect))
            self.tela.blit(self.opt3_button, (self.opt3_button_rect))
            
            pygame.display.flip()
            self.eventos()
            
    def main_menu(self):
        self.menu = True
        self.cor_button = LINHAS
        self.carregar_arquivos()
        self.novo_jogo()
        
        while self.menu:
            self.tela.fill(FUNDO)
            self.atualizar_pos()
            pygame.draw.rect(self.tela, LINHAS, self.faixa)
            self.mostrar_texto("JOGO DA VELHA",80,COR_CIRC,self.largura//2,self.altura//10+43)
            self.tela.blit(self.onoff_button, (self.onoff_rect))
            self.tela.blit(self.opt4_button, (self.opt4_button_rect))
            self.tela.blit(self.opt5_button, (self.opt5_button_rect))
            self.tela.blit(self.opt6_button, (self.opt6_button_rect))
            self.mostrar_texto("Developed by gbPagano",25,COR_X,self.largura//2,self.altura - self.altura//40)

            pygame.display.flip()
            self.eventos()

def main():
    jogo = Game()
    jogo.main_menu()

if __name__ == "__main__":
    main()