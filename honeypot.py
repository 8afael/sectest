import subprocess

class Alvo:

    def montarContainer(self):
        terminal = "gnome-terminal --tab --working-directory=/home/rafa/Documents/agap_PI/sectest -- bash -c '"
        terminal2 = "; exec $SHELL'"
        honeypot_dvwa = terminal+"docker run -it --rm --name honeypot web-dvwa"+terminal2
        listarContainers = "docker ps -a --format '{{.Names}}'"
        # Executar o comando e capturar a saída
        output = subprocess.check_output(listarContainers, shell=True)
        container_names = output.decode('utf-8').split('\n')
        # Nome do contêiner a ser verificado
        container_name = 'honeypot'
        # Verificar se o contêiner está em execução
        if container_name in container_names:
            print("O Honeypot já está em execução, continuando os testes")
        else:
            print("O Honeypot não está em execução, iniciando...")
            process_honeypot = subprocess.Popen(honeypot_dvwa, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            for line in process_honeypot.stdout:
                print(line.decode().strip())
            process_honeypot.wait()
            #subprocess.run(["docker", "run", container_name])

        