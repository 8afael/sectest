import os
import subprocess
from datetime import datetime

class Data:
    def __init__(self, url, dataHora) :
        self.url = url
        self.dataHora = dataHora

    def dataHoraAtual(self):
        data_hora = datetime.now()
        dataHora = data_hora.strftime("%Y-%m-%d_%H:%M")
        return dataHora

    def urlTest(self):
        url = "http://172.17.0.2/"
        return url
    
    def caminhoAtual(self):
        caminho = os.getcwd()
        return caminho
    

