import subprocess
import requests
from requests.adapters import HTTPAdapter
from urllib3 import Retry
from data import Data

class Owasp(Data):
    def __init__(self, url, dataHora):
         super().__init__(url, dataHora)
         
    async def testar_zap(self):
            urlTest = Data.urlTest(self)
            dataH = Data.dataHoraAtual(self)
            test_zap = "docker run -v $(pwd):/zap/wrk/:rw owasp/zap2docker-stable zap-full-scan.py -t " +urlTest+ " -g gen.conf -J report_owaspZap_"+dataH+".json -j"
            mover_report = "mv report_owaspZap*.* reports" 
            session = requests.Session()
            retry = Retry(connect=3, backoff_factor=0.5)
            adapter = HTTPAdapter(max_retries=retry)
            session.mount('http://', adapter)
            response = session.get(urlTest)
            if response.status_code == 200:
                print(f"A página {urlTest} está acessível, Iniciando os testes com OWASP Zap ...  (aguarde)")
                process_test_zap = subprocess.Popen(test_zap, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                for line in process_test_zap.stdout:
                    print(line.decode().strip())
                process_test_zap.wait()
                report = subprocess.Popen(mover_report, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                report.wait() 
                print(f"Testes com OWASP Zap concluídos, continuando para o próximo teste")
            else:
                print(f"Problemas ao acessar a url: {urlTest} ")

