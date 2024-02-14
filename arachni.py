import subprocess
import requests
from requests.adapters import HTTPAdapter
from urllib3 import Retry
from data import Data
import asyncio

terminal = "gnome-terminal --tab --working-directory=/home/rafa/Documents/agap_PI/sectest -- bash -c '"
terminal2 = "; exec $SHELL'"

class Arachni(Data):
    
    def __init__(self, url, dataHora):
         super().__init__(url, dataHora) 
    
    async def testar_arachni(self):
        dataH = Data.dataHoraAtual(self)
        path_linux = Data.caminhoAtual(self)
        urlTest = Data.urlTest(self)
        rodarArachni = "docker run -d -it --name arachni ajunneti/arachni-docker /bin/bash && docker exec -it arachni mkdir /arachni/report && docker exec -it arachni ./bin/arachni --output-verbose --scope-include-subdomains "+urlTest+" --report-save-path=/arachni/report/report.afr" 
        rodarBash = "docker cp report.sh arachni:/arachni/report.sh && docker exec -it arachni bash /arachni/report.sh && docker cp arachni:/arachni/report/. "+path_linux
        ajustarReport = "mv report.json reports && rm report.afr && cd reports && mv report.json report_arachni_"+dataH+".json && docker stop arachni $$ docker rm arachni && docker container prune -f"
        session = requests.Session()
        retry = Retry(connect=3, backoff_factor=0.5)
        adapter = HTTPAdapter(max_retries=retry)
        session.mount('http://', adapter)
        response = session.get(urlTest)
        if response.status_code == 200:
            print(f"A página {urlTest} está acessível, Iniciando os testes com Arachni ...  (aguarde)")
            process_rodar_arachni = subprocess.Popen(rodarArachni, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            for line in process_rodar_arachni.stdout:
                print(line.decode().strip())                
            process_rodar_arachni.wait()
            print(f"Testes com Arachni concluídos, gerando relatório")
            process_report1 = subprocess.Popen(rodarBash, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            for line in process_report1.stdout:
                print(line.decode().strip())                
            process_report1.wait()      
            process_report2 = subprocess.Popen(ajustarReport, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            for line in process_report2.stdout:
                print(line.decode().strip())                
            process_report2.wait()
            print(f"Testes com Arachni concluídos, relatório gerado na pasta reports")        
        else:
                print(f"Problemas ao acessar a url: {urlTest} ")
    

