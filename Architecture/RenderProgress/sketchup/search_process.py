## -*- coding: cp1252 -*-

import pyautogui as pyauto
from PIL import Image
import time

class vray:
    def __init__(self, image_path):

        self.image_path = image_path

    def message_progress(self):
        print('')
        print('--- Procurando no V-ray ---')
        print('')


    def finished(self) -> bool:
        
        try:
            location = pyauto.locateOnScreen(self.image_path, confidence=0.9)
        
        except pyauto.ImageNotFoundException:
            location = None

        return location


    def try_located(self):

        self.message_progress()

        locate = None

        while locate == None:
            
            locate = self.finished()
            
            if locate:
                print('')
                print('--- Render Finalizado ---')
                print('')

                pyauto.click(locate)
            
            else:
                print('')
                print('--- Render em Andamento ---')
                print('')

                time.sleep(5)



        
