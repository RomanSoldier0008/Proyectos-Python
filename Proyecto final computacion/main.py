from Credits import *
from Game import *


class Main:
    def __init__(self):
        self.__opc = 0
        self.__start_music = True

    def get_listen(self):
        return self.__start_music

    def set_listen(self, listen):
        self.__start_music = listen

    def get_opc(self):
        return self.__opc

    def set_opc(self, opc):
        self.__opc = opc

    def select_option_menu_root(self):
        while True:
            if self.get_opc() == '0' or self.get_opc() == '2' or self.get_opc() == '4':
                self.clear()
            else:
                sleep(2)
                self.clear()

            if self.get_opc() != '2' and self.get_opc() != '3' and self.get_listen() == True:
                self.listen_music_menu()

            self.set_opc(str(input(OPTIONS_MENU_INPUT)))
            if self.get_opc() == "1":
                if len(characters_list) > 0:
                    juego = Game("Ninguna", characters_list)
                    juego.menu()
                    self.set_listen(True)
                else:
                    print(ERROR_NO_HEROS)
                    self.set_listen(False)

            elif self.get_opc() == "2":
                Character_controller(None).assign_breed_and_name()

            elif self.get_opc() == "3":
                Character_controller(None).delete_character()

            elif self.get_opc() == "4":
                self.clear()
                self.listen_music_credits()
                self.view_credits()
                self.set_listen(True)

            elif self.get_opc() == "5":
                break

            else:
                print(ERROR_IN_OPC_MENU)

    def view_credits(self):
        Credits().view_credits()

    def listen_music_menu(self):
        pygame.mixer.music.fadeout(4000)
        pygame.mixer.music.load('Sounds/Menu_principal.mp3')
        pygame.mixer.music.play(-1)

    def listen_music_credits(self):
        pygame.mixer.music.fadeout(4000)
        pygame.mixer.music.load('Sounds/creditos.mp3')
        pygame.mixer.music.play(1)

    def clear(self):
        print("""
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        """)


player = Main()
player.select_option_menu_root()
