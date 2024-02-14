import datetime
import subprocess
import requests
import time
import threading
import asyncio
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
from data import Data
from zap import Owasp
from honeypot import Alvo
from arachni import Arachni
from wapiti import Wapiti
from nikto import Nikto

class Sectest:   
    
    async def main():
        honeypot = Alvo()
        honeypot.montarContainer()
        arachniTest = Arachni(Data.dataHoraAtual, Data.urlTest)
        wapitiTest = Wapiti(Data.dataHoraAtual, Data.urlTest)
        zapTest = Owasp(Data.dataHoraAtual, Data.urlTest)
        niktoTest = Nikto(Data.dataHoraAtual, Data.urlTest)
        await arachniTest.testar_arachni()
        await wapitiTest.testar_wapiti()
        await zapTest.testar_zap()
        await niktoTest.testar_nikto()
        await Data.clearDocker()
        print(f"Todos testes concluídos com sucesso, verificar relatórios na pasta /sectest/reports")
        
    asyncio.run(main())

 

    