import subprocess
import requests
from requests.adapters import HTTPAdapter
from urllib3 import Retry
from data import Data

class Wapiti(Data):
    def __init__(self, url, dataHora):
         super().__init__(url, dataHora)
         
    async def testar_wapiti(self):
            urlTest = Data.urlTest(self)
            dataH = Data.dataHoraAtual(self)
            test_wapiti = "docker run -v $(pwd):/home/:rw -it --rm wapiti_docker -u "+urlTest+" -f json -o /home/report_wapiti_"+dataH+".json"
            report = "mv report_wapiti*.* reports"
            session = requests.Session()
            retry = Retry(connect=3, backoff_factor=0.5)
            adapter = HTTPAdapter(max_retries=retry)
            session.mount('http://', adapter)
            response = session.get(urlTest)
            if response.status_code == 200:
                print(f"A página {urlTest} está acessível, Iniciando os testes com Wapiti ...  (aguarde)")
                process_test_wapiti = subprocess.Popen(test_wapiti, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                # for line in process_test_wapiti.stdout:
                #     print(line.decode().strip())
                process_test_wapiti.wait()
                process_report = subprocess.Popen(report, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                for line in process_report.stdout:
                    print(line.decode().strip())
                process_report.wait()
                print(f"Testes com Wapiti concluídos, continuando para o próximo teste")

            else:
                print(f"Problemas ao acessar a url: {urlTest} ")
