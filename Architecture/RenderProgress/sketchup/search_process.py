## -*- coding: cp1252 -*-

import pyautogui as pyauto
from PIL import Image
import time

class vray:
    def __init__(self, image_path):

        self.image_path = image_path

    def message_searching_on_screen(self):
        print('')
        print('--- Procurando no V-ray ---')
        print('')

    def message_waiting(self):
        print('')
        print('--- Aguardando Finalização ---')
        print('')


    def try_located(self):
        
        try:
            location = pyauto.locateOnScreen(self.image_path, confidence=0.9)
                    
        except:
            location = None


        return location



        
