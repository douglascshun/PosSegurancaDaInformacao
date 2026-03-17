[[Aula 8 Gerenciamento de rede]]


# Tipos de analisadores de protocolo

O WireShark, é um analisador de protocolos de rede bastante utilizado, pode ser encontrado versões para as plataformas Windows, Mac OS, Linux e Unix, além disso trata-se de um software livre.

O WireShark é um analisador de protocolos de rede que também possuí, a funcionalidade de sniffer, que consistem em permitir realizar a captura dos pacotes em tempo real diretamente na ferramenta para realizar análises posteriormente.

`A principal vantagem de utilizar o Wireshark` como sniffer e analisador de pacotes é a possibilidade de acompanhamento em tempo real, em sua interface gráfica, dos pacotes capturados que são detalhadamente pela ferramenta.

`Além disso`, apresenta vários recursos que incluem inspeções detalhadas de protocolos, capturas em tempo real entre outros fatores.

`Não é conselhável` utilizar na maioria dos casos a funcionalidade de captura do WireShark simultaneamente à análise dos pacotes, pois pode comprometer os recursos da máquina que está sendo utilizada.

# Coleta de dados com WireShark:
![[Coleta de dados com WireShark.png]]

Na Figura podemos verificar todo o tráfego que está passando em tempo real em nossa rede, através da interface gráfica do WireShark.


# TCPDUMP

O `TCPDUMP` é um programa executável que roda em linha de comando de sistemas com base em Unix, utilizado para captura de pacotes em tráfego de redes TCP/IP.

O TCPDUMP foi utilizado neste trabalho para fazer a captura do tráfego que foi analisado para treinamento/validação da rede neural.

Quando o TCPDUMP é executado com o mínimo de parâmetros necessários para seu funcionamento, a placa de rede do computador em questão é colocada em modo promiscuo, onde passa a capturar todo o tráfego que passa por ela.

Então o TCPDUMP faz a "tradução" de todos os dados que transitam por esta porta.

