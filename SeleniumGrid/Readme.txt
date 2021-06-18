Requisitos:
Java jdk 8+

Inicialização do hub:

java -jar selenium-server-standalone-<version>.jar -role hub

Inicialização Node:

java -jar selenium-server-standalone-<version>.jar -role node -hub https://localhost:4444/grid/register


Help: https://www.browserstack.com/guide/selenium-grid-tutorial

