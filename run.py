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

class Sectest:   
    #  def __init__(self, url, dataHora) :
    #       self.url = url
    #       self.dataHora = dataHora
    #Comando gerais:
    # data_hora = datetime.
    # dataHora = data_hora.strftime("%Y-%m-%d_%H:%M")
    # terminal = "gnome-terminal --tab --working-directory=/home/rafa/Documents/agap_PI/sectest -- bash -c '"
    # terminal2 = "; exec $SHELL'"
    # remover_report = "docker exec con_cypress rm /e2e/cypress/downloads/*.*"
    # copy_report_arachni = "docker cp con_cypress:/e2e/cypress/downloads/ ."
    # remove_container_cypress = "docker stop con_cypress && docker rm con_cypress"
    # mover_reports = "mv report*.* reports && mv -t final report*"

    # URL's a serem testadas
    # url_test = "http://172.17.0.2/"
    # url = "http://172.17.0.2/"

    # Montar e atualizar imagens com docker
    # atualizar_imagens = terminal+"docker-compose up -d"+terminal2

    # Montar container do honeypot (DVWA)

    # honeypot_dvwa = terminal+"docker run -it --rm --name honeypot web-dvwa"+terminal2

    # User do Arachni Web:
    # E-mail: admin@admin.admin
    # Password: administrator

    # Executar OWASP Zap na URL indicada
    # test_zap = "docker run -v $(pwd):/zap/wrk/:rw owasp/zap2docker-stable zap-full-scan.py -t " +url_test+ " -g gen.conf -r report_dvwa_"+dataHora+".html -j"

    # Executar Arachni na URL indicada

    # arachni_test = "docker run -it --rm ajunneti/arachni-docker ./bin/arachni "+url_test+remover_report+" && docker run -it -v $PWD:/e2e -w /e2e --name con_cypress cypress"
    # arachni_web = terminal+"docker run -it ajunneti/arachni-docker ./bin/arachni_web -o 0.0.0.0"+terminal2
    # #arachni_cypress = terminal+"docker run -it -v $PWD:/e2e -w /e2e --name con_cypress cypress"+terminal2
    # # report_arachni = "cd downloads/ && unzip -o 172_17_*.* && rm *.zip && cd .. && mv downloads report_arachni_"+dataHora
    # arachni_test_docker = "./bin/arachni "+url_test+" --report-save-path=/arachni"
    # arachni_rename = "mv *.afr teste.afr"
    # arachni_json = "./bin/arachni_reporter teste.afr --reporter=json"
    # # arachni_report = "mv *.json report_arachni_"+dataHora+".json"
    # arachni_mv_home = "mv *.json /home"
    # arachni_docker_cp = "docker cp c348cdbe28d4:/home/report_arachni_data_hora_.json /home/rafa/Documents/agap_PI/sectest"
    

    # # Atualizar e executar Wapiti na URL indicada
    # wapiti_update = "docker run -it wapiti_docker --update"
    # wapiti_test = "docker run -v $(pwd):/home/:rw -it --rm wapiti_docker -u "+url_test+" -o /home"
    # wapiti_report_json = "docker run -v $(pwd):/home/:rw -it --rm wapiti_docker -u http://172.17.0.2 -f json -o /home/report_wapiti_"+dataHora+".json"
    # wapiti_ren_report = "mv 172.* report_wapiti_"+dataHora+".html"

    # Executar Nikto na URL indicada
    # nikto_test = "docker run -v $(pwd):/tmp:rw -it --rm secsi/nikto -h "+url_test+" -o /tmp/report_nikto_"+dataHora+".htm -Format htm"

    #Executar a criação das imagens e do honeypot exibindo as saídas no terminal
    # process_imagens = subprocess.Popen(atualizar_imagens, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    # for line in process_imagens.stdout:
    #     print(line.decode().strip())
    # process_imagens.wait()

    # process_honeypot = subprocess.Popen(honeypot_dvwa, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    # for line in process_honeypot.stdout:
    #     print(line.decode().strip())
    # process_honeypot.wait()

    # process_web_arachni = subprocess.Popen(arachni_web, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    # for line in process_web_arachni.stdout:
    #     print(line.decode().strip())
    # process_web_arachni.wait()

    # def testar_zap(url):
    #         session = requests.Session()
    #         retry = Retry(connect=3, backoff_factor=0.5)
    #         adapter = HTTPAdapter(max_retries=retry)
    #         session.mount('http://', adapter)
    #         session.mount('https://', adapter)
    #         response = session.get(url)
    #         if response.status_code == 200:
    #             print(f"A página {url} está acessível, Iniciando os testes com OWASP Zap ...  (aguarde)")
    #             process_test_zap = subprocess.Popen(test_zap, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    #             # for line in process_test_zap.stdout:
    #             #     print(line.decode().strip())
    #             process_test_zap.wait()
    #             print(f"Testes com OWASP Zap concluídos")

    #         else:
    #             print(f"Problemas ao acessar a url: {url} ")

    # def testar_arachni(url):
    #         session = requests.Session()
    #         retry = Retry(connect=3, backoff_factor=0.5)
    #         adapter = HTTPAdapter(max_retries=retry)
    #         session.mount('http://', adapter)
    #         session.mount('https://', adapter)
    #         response = session.get(url)
    #         if response.status_code == 200:
    #             print(f"A página {url} está acessível, Iniciando os testes com Arachni ...  (aguarde)")
    #             process_test_arachni = subprocess.Popen(arachni_test, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    #             process_test_arachni.wait()
    #             process_report1_arachni = subprocess.Popen(copy_report_arachni, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    #             process_report1_arachni.wait()
    #             process_report2_arachni = subprocess.Popen(report_arachni, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    #             process_report2_arachni.wait()
    #             process_end_arachni = subprocess.Popen(remove_container_cypress, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    #             process_end_arachni.wait()
    #             print(f"Testes com Arachni concluídos")            

    #         else:
    #             print(f"Problemas ao acessar a url: {url} ")

    # def updating_wapiti():
    #         update_wapiti = subprocess.Popen(wapiti_update, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    #         update_wapiti.wait()

    # def testar_wapiti(url):
    #         session = requests.Session()
    #         retry = Retry(connect=3, backoff_factor=0.5)
    #         adapter = HTTPAdapter(max_retries=retry)
    #         session.mount('http://', adapter)
    #         session.mount('https://', adapter)
    #         response = session.get(url)
    #         if response.status_code == 200:
    #             print(f"A página {url} está acessível, Iniciando os testes com Wapiti ... (aguarde)")
    #             test_wapiti = subprocess.Popen(wapiti_test, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    #             test_wapiti.wait()
    #             rename_report = subprocess.Popen(wapiti_ren_report, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    #             rename_report.wait()
    #             print(f"Testes com Wapiti concluídos") 

    #         else:
    #             print(f"Problemas ao acessar a url: {url} ")

    # def testar_nikto(url):
    #         session = requests.Session()
    #         retry = Retry(connect=3, backoff_factor=0.5)
    #         adapter = HTTPAdapter(max_retries=retry)
    #         session.mount('http://', adapter)
    #         session.mount('https://', adapter)
    #         response = session.get(url)
    #         if response.status_code == 200:
    #             print(f"A página {url} está acessível, Iniciando os testes com Nikto ... (aguarde)")
    #             test_nikto = subprocess.Popen(nikto_test, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    #             test_nikto.wait()
    #             print(f"Testes com Nikto concluídos") 

    #         else:
    #             print(f"Problemas ao acessar a url: {url} ")

    # def reports():
    #     reports = subprocess.Popen(mover_reports, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    #     for line in reports.stdout:
    #         print(line.decode().strip())
    #     reports.wait()

    async def main():
        honeypot = Alvo()
        honeypot.montarContainer()
        arachniTest = Arachni(Data.dataHoraAtual, Data.urlTest)
        wapitiTest = Wapiti(Data.dataHoraAtual, Data.urlTest)
        zapTest = Owasp(Data.dataHoraAtual, Data.urlTest)
        #await arachniTest.testar_arachni()
        #await wapitiTest.testar_wapiti()
        await zapTest.testar_zap()
        print(f"Todos testes concluídos com sucesso, verificar relatórios na pasta /sectest/reports") 
    
    asyncio.run(main())

    # zapTest = Owasp(Data.dataHoraAtual, Data.urlTest)
    # zapTest.testar_zap()
    
    #arachniTest.montar_Arachni()
    #arachniTest.testar_arachni()
    #arachniTest.gerar_Report()
    # thread1 = threading.Thread(target=arachniTest.testar_arachni())
    # thread2 = threading.Thread(target=arachniTest.gerar_Report())
    # thread1.start()
    # thread1.join()
    # thread2.start()
    # thread2.join()

    
    #testar_zap(url_test)
    #testar_arachni(url_test)
    #updating_wapiti()
    #testar_wapiti(url_test)
    #testar_nikto(url_test)
    #reports()
    