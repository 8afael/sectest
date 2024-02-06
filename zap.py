import subprocess

class owasp:
    test_zap = terminal_"docker run -v $(pwd):/zap/wrk/:rw owasp/zap2docker-stable zap-full-scan.py -t " +url_test+ " -g gen.conf -r report_dvwa_"+data_hora_f+".html -j"

    def testar_zap(url):
            session = requests.Session()
            retry = Retry(connect=3, backoff_factor=0.5)
            adapter = HTTPAdapter(max_retries=retry)
            session.mount('http://', adapter)
            session.mount('https://', adapter)
            response = session.get(url)
            if response.status_code == 200:
                print(f"A página {url} está acessível, Iniciando os testes com OWASP Zap ...  (aguarde)")
                process_test_zap = subprocess.Popen(test_zap, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                # for line in process_test_zap.stdout:
                #     print(line.decode().strip())
                process_test_zap.wait()
                print(f"Testes com OWASP Zap concluídos")

            else:
                print(f"Problemas ao acessar a url: {url} ")