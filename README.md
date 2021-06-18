# atvidades

# automation test
Casos de teste automatizados para criar usuario, efetuar login e comprar item

#tecnologia utilizadas
*selenium
*selenium grid
*pytest

#instalação
instale os pacotes descritos em requiriments.txt

#instalação e configuração selenium grid
**necessita jdk 8+ instalado

execute o comando para iniciar o hub: java -jar selenium-server-standalone-<version>.jar -role hub
execute o comendo para cria um node: java -jar selenium-server-standalone-<version>.jar -role node -hub https://localhost:4444/grid/register
para executar em mais de um navegador passe por parametro as especificações dos brows depois da tag -broser, por exemplo: -browser browserName=firefox,version=3.6,firefox_binary=/home/myhomedir/firefox36/firefox,maxInstances=5,platform=WINDOWS -browser browserName=firefox,version=4,firefox_binary=/home/myhomedir/firefox4/firefox,maxInstances=4,platform=WINDOWS
  
Help: https://www.browserstack.com/guide/selenium-grid-tutorial

#instruções de execução
digite o comando pytest no console para rodar todos os testes
  

 #autor 
 Thiago Miranda
