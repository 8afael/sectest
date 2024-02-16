import os
import json
import glob
import jq
from data import Data
from os import PathLike
from pathlib import Path
    
class Report:
    dirFinal = "reports"
    nomeArquivo = "report_wapiti"
    
    async def gerar_relatorio(self):     
        caminho = Data.caminhoAtual(self)
        padrao = caminho+"/reports/report_wapiti*"
        lstJson = glob.glob(padrao)
        arquivo = lstJson[0]
        pathFile = str(arquivo)
        secao = "vulnerabilities"
        print(f'Wapiti Tests:\n')
        g = open(pathFile)
        data = json.load(g)
        chave = "[{"
      
        for i in data[secao].items():
                print(i)

        g.close()

