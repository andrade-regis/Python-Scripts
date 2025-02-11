
## -*- coding: cp1252 -*-

import os
import json
import datetime

from smtplib import SMTP

class email:
    def __init__(self, key_path) -> None:

        with open(key_path, 'r') as file:
            self.credential = json.load(file)
            self.smtp = SMTP()


    def configure_smtp(self) -> None:

        self.smtp.set_debuglevel(0)
        
        self.smtp.connect(self.credential['server'], 
                          self.credential['port'])

        self.smtp.login(self.credential['address'],
                        self.credential['key'])


    def create_message(self) -> str:
        
        message = ''

        date = datetime.datetime.now().strftime('%Y/%m/%d %H:%M')

        subject = f'Monitora V-ray - {date}'

        content_message = 'Seu render já finalizou!!\nPode seguir com as demais atividades!'

        message = "From: %s\nTo: %s\nSubject: %s\nDate: %s\n\n%s" % (self.credential['from'],
                                                                     self.credential['to'],
                                                                     subject,
                                                                     date,
                                                                     content_message )

        return message


    def send_message(self, message) -> None:
        try:
            self.smtp.sendemail(self.credential['from'],
                                self.credential['from'],
                                message)

            self.smtp.quit()

        except:
            raise Exception('Erro ao enviar e-mail')


        


        
        

