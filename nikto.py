import subprocess
import requests
from requests.adapters import HTTPAdapter
from urllib3 import Retry
from data import Data

class Nikto(Data):
    def __init__(self, url, dataHora):
         super().__init__(url, dataHora)
         
    async def testar_nikto(self):
            urlTest = Data.urlTest(self)
            dataH = Data.dataHoraAtual(self)
            nikto_test = "docker run -v $(pwd):/tmp:rw -it --rm secsi/nikto -h "+urlTest+" -o /tmp/report_nikto_"+dataH+".json -Format json"
            mover_report = "mv report_nikto*.* reports" 
            session = requests.Session()
            retry = Retry(connect=3, backoff_factor=0.5)
            adapter = HTTPAdapter(max_retries=retry)
            session.mount('http://', adapter)
            session.mount('https://', adapter)
            response = session.get(urlTest)
            if response.status_code == 200:
                print(f"A página {urlTest} está acessível, Iniciando os testes com Nikto ... (aguarde)")
                test_nikto = subprocess.Popen(nikto_test, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                # for line in test_nikto.stdout:
                #     print(line.decode().strip())                 
                test_nikto.wait()
                report = subprocess.Popen(mover_report, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                report.wait()                
                print(f"Testes com Nikto concluídos") 
                

            else:
                print(f"Problemas ao acessar a url: {urlTest} ")