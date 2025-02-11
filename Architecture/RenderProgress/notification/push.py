
## -*- coding: cp1252 -*-

import os
import sys
import json
import datetime

from smtplib import SMTP_SSL as SMTP
from typing import final

class email:
    def __init__(self, key_path) -> None:

        with open(key_path, 'r') as file:
            self.credential = json.load(file)

        self.smtp = SMTP(self.credential['server'])


    def configure_smtp(self) -> None:

        try:

            self.smtp.set_debuglevel(False)
            
            self.smtp.login(self.credential['address'],
                            self.credential['password'])
        except Exception as e:
            error = e.message
            error.capitalize()


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
            self.smtp.sendmail(self.credential['from'],
                                self.credential['to'],
                                message.encode('utf-8'))

        except Exception as error:
            raise Exception('Erro ao enviar e-mail')

        finally:
            self.smtp.quit()



        


        
        

