import subprocess
import requests
from requests.adapters import HTTPAdapter
from urllib3 import Retry
from data import Data

class Owasp(Data):
    def __init__(self, url, dataHora):
         super().__init__(url, dataHora)
         
    def testar_zap(self):
            urlTest = Data.urlTest(self)
            dataH = Data.dataHoraAtual(self)
            test_zap = "docker run -v $(pwd):/zap/wrk/:rw owasp/zap2docker-stable zap-full-scan.py -t " +urlTest+ " -g gen.conf -r report_owaspZap_"+dataH+".html -j"
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
                print(f"Testes com OWASP Zap concluídos")
            else:
                print(f"Problemas ao acessar a url: {urlTest} ")

