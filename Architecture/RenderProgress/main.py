## -*- coding: cp1252 -*-

import os
import time

from pydoc import locate

from sketchup.search_process import vray
from notification.push import email

image_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'image', 'finished_message.png')
# key_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'keys', 'CREDENTIALS.json')
key_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'Example keys', 'EXAMPLE_CREDENTIAL.json')

def message_initial():
    print('---------------------------------')
    print('--- Acompanhando renderização ---')
    print('---------------------------------')


if __name__ == "__main__":

    message_initial()

    interface = vray(image_path)

    interface.message_searching_on_screen()

    locate = None

    while locate == None:
        
        time.sleep(5)

        interface.message_waiting()

        locate = interface.try_located()
                
    print('')
    print('--- Render Finalizado ---')
    print('')

    notification = email(key_path)

    notification.configure_smtp()

    message = notification.create_message()

    notification.send_message(message)

    print('')
    print('--- E-mail de notificação enviado! ---')
    print('')









