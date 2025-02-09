## -*- coding: cp1252 -*-

import os

from sketchup.search_process import vray

image_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'image', 'finished_message.png')

# image_path = 'C:\\Users\\regis\\Documents\\teste.jpg'

def message_initial():
    print('---------------------------------')
    print('--- Acompanhando renderização ---')
    print('---------------------------------')


if __name__ == "__main__":

    message_initial()

    vray_value = vray(image_path)
    vray_value.try_located()



