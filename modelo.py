import os
import json
import glob
import requests
from data import Data
from os import PathLike
from pathlib import Path
from jsonpath_rw import parse
from pprint import pprint
from glom import glom
from glom.tutorial import *
from bs4 import BeautifulSoup
    
class Report:

    def __init__(self):
        lstVulnerabilites = []

    async def gerarReportOwasp(self):       
        url = 'https://www.zaproxy.org/docs/alerts/'
        response = requests.get(url)
        html_content = response.content
        soup = BeautifulSoup(html_content, "html.parser")
        table = soup.find("table")
        lstSiteOwasp = []
        for row in table.find_all("tr")[1:]:
            codigos = row.find_all('td')[0]
            lstSiteOwasp.append(codigos.text)

        caminho = Data.caminhoAtual(self)
        padrao = caminho+"/reports/report_owaspZap*"
        lstJson = glob.glob(padrao)
        target = Path(lstJson[0])
        with open(target, 'r') as f:
            owaspJson = json.load(f)

        spec = ('site', ['alerts'], [['alert']])
        lstJsonOwasp = (glom(owaspJson, spec))

        toolName = f'Owasp\n'
        
        self.lstVulnerabilites = [valor for valor in lstSiteOwasp if valor in lstJsonOwasp[1]]
        
        #pprint(self.lstVulnerabilites)

    async def gerarReportNikto(self):
        caminho = Data.caminhoAtual(self)
        padrao = caminho+"/reports/report_nikto*"
        lstJson = glob.glob(padrao)
        target = Path(lstJson[0])
        with open(target, 'r') as f:
            niktoJson = json.load(f)
        #print(niktoJson)

        spec = (['vulnerabilities'], [['msg']])
        lstJsonNikto = (glom(niktoJson, spec))

        self.lstVulnerabilites = self.lstVulnerabilites+[valor for valor in lstJsonNikto[0]]
        #pprint(self.lstVulnerabilites)

    async def gerarReportWapiti(self):
        caminho = Data.caminhoAtual(self)
        padrao = caminho+"/reports/report_wapiti*"
        lstJson = glob.glob(padrao)
        target = Path(lstJson[0])
        with open(target, 'r') as f:
            wapitiJson = json.load(f)
        #print(niktoJson)

        spec = 'classifications.**.ref'
        lstJsonWapiti = (glom(wapitiJson, spec))

        self.lstVulnerabilites = self.lstVulnerabilites+[valor for valor in lstJsonWapiti]
        #pprint(lstVul)   

    async def gerarReportArachni(self):
        caminho = Data.caminhoAtual(self)
        padrao = caminho+"/reports/report_arachni*"
        lstJson = glob.glob(padrao)
        target = Path(lstJson[0])
        with open(target, 'r') as f:
            arachniJson = json.load(f)
        spec = ('issues.**.references')
                #('issues.**.references.OWASP')       
        lstJsonArachni = (glom(arachniJson, spec))
        self.lstVulnerabilites = self.lstVulnerabilites+[valor for valor in lstJsonArachni]
        #pprint(lstVul)    

    async def runReport(self):
        nome_arquivo = "dados.json"

        with open(nome_arquivo, "w") as arquivo:
            json.dump(self.lstVulnerabilites, arquivo)
        
        pprint('Arquivo Json Salvo')

    # async def gerarDicionario(self, ferramenta):
    #     caminho = Data.caminhoAtual(self)
    #     padrao = caminho+"/reports/report_"+ferramenta+"*"
    #     lstJson = glob.glob(padrao)
    #     arquivo = lstJson[0]
    #     pathFile = str(arquivo)
    #     #print(pathFile+' \n')
    #     print(ferramenta+' tests:\n')
    #     with open(pathFile, 'r') as f:
    #         exist_json = json.load(f)
    #     file_path = '/home/rafa/Documents/agap_PI/sectest/report.json'
    #     result = ''
    #     if ferramenta == 'owaspZap':
    #         result = glom(exist_json, ("site", ["alerts", "alert", "desc", "confidence"]))
    #         #strFerramenta = f'"Resultado dos testes executados com: '+ferramenta+'"'+'.\n' 
    #         nomeFerramenta = glom(exist_json, ("@programName"))
    #         json_str = json.dumps(nomeFerramenta, indent=3)
    #         json_data = json.dumps(result, indent=4)
    #         with open(file_path, "w") as json_file:
    #             json_file.write(json_str)
    #             json_file.write(json_data)
    #     elif ferramenta == 'nikto':
    #         result = glom(exist_json, ("site", ["alerts", "alert", "desc", "confidence"]))
    #     elif ferramenta == 'wapiti':
    #         result = glom(exist_json, ("site", ["alerts", "alert", "desc", "confidence"]))
    #     elif ferramenta == 'arachni':
    #         #referring_page = glom(exist_json, ("issues", ["referring_page": ("referring_page", omit=True)]))
    #         result = glom(exist_json, ("issues"))
    #     else:
    #         result = 'Não foi encontrada a ferramenta'
    #     pprint(result)

        
    # async def gerarJson(self, ferramenta):
    #     caminho = Data.caminhoAtual(self)
    #     padrao = caminho+"/reports/report_"+ferramenta+"*"
    #     lstJson = glob.glob(padrao)
    #     arquivo = lstJson[0]
    #     pathFile = str(arquivo)
    #     print(ferramenta+' tests:\n')
    #     with open(pathFile, 'r') as f:
    #         exist_json = json.load(f)
    #     file_path = '/home/rafa/Documents/agap_PI/sectest/report.json'
    
    # async def getCodigosJsonOwasp(self):
    #     caminho = Data.caminhoAtual(self)
    #     padrao = caminho+"/reports/report_owaspZap*"
    #     lstJson = glob.glob(padrao)
    #     target = Path(lstJson[0])
    #     with open(target, 'r') as f:
    #         owaspJson = json.load(f)
    #     spec = ('site', ['alerts'], [['alertRef']])
    #     lista = (glom(owaspJson, spec))
    #     result = list(lista)
    #     print(result)
    #     return(result)
 
    # async def listaVulnOwasp(self):
    #     lstOwasp = self.getCodigosOwasp()
    #     jsonOwasp = self.getCodigosJsonOwasp()
    #     lista1 = list(lstOwasp)
    #     lista2 = list(jsonOwasp)
    #     print(f'Codigos Owasp')
    #     pprint(lstOwasp)
    #     print(f'Codigos Json Owasp')
    #     pprint(jsonOwasp)
                          
    # async def teste(self, ferramenta):

    #     result = ''
    #     if ferramenta == 'owaspZap':
    #         codigosOwasp = self.getCodigos(ferramenta)
    #         codigoJson = glom(exist_json, ('site.alerts', [('alertRef')]))
    #         pprint(codigoJson)
    #         result = glom(exist_json, ("site", ["alerts", "alert", "desc", "confidence"]))
    #         nomeFerramenta = glom(exist_json, ("@programName"))
    #         json_str = json.dumps(nomeFerramenta, indent=3)
    #         json_data = json.dumps(result, indent=4)
    #         with open(file_path, "w") as json_file:
    #             json_file.write(json_str)
    #             json_file.write(json_data)
    #     elif ferramenta == 'nikto':
    #         result = glom(exist_json, ("site", ["alerts", "alert", "desc", "confidence"]))
    #     elif ferramenta == 'wapiti':
    #         result = glom(exist_json, ("site", ["alerts", "alert", "desc", "confidence"]))
    #     elif ferramenta == 'arachni':
    #         #referring_page = glom(exist_json, ("issues", ["referring_page": ("referring_page", omit=True)]))
    #         result = glom(exist_json, ("issues"))
    #     else:
    #         result = 'Não foi encontrada a ferramenta'
    #     #pprint(result)

       



