[[Aula 3 Infraestrutura de Segurança em Rede]]


## Vul da pilha TCP/IP

O TCP usa um handshake de três vias para estabelecer uma conexão confiável. A conexão é full duplex e ambos os lados sincronizam (SYN) e confirmam (ACK) um ao outro A troca desses quatro sinalizadores é realizada em três etapas SYN,  SYN-ACK e ACK.

![[Handshack.png]]



## IP Address spoofing

A falsificação de IP, ou falsificação de endereço IP, refere-se à criação de pacotes de Protocolo de Internet (IP) com um endereço de origem falso para se passar por outro dispositivo.

![[IP Address spoofing.png]]


# ARP Spoofing

A falsificação de ARP refere-se a um invasor com acesso à LAN fingindo ser o Host B. O invasor envia mensagens ao Host A com objetivo de engana-lo para que ele salve o endereço do invasor, com isso o Host A acabará por enviar dados destinados ao Host B para o invasor.
![[ARP Spoofing.png]]

# Port scanning

É uma aplicativo projetado para sondar um servidor ou host em busca de portas abertas.
Esse aplicativo pode ser usado por administradores para verificar as políticas de segurança de suas redes e por invasores para identificar serviços de rede em execução em um host e explorar vulnerabilidades.

![[Nmap.png]]



# ICMP attacks
Um ataque de DDoS de inundação do protocolo de mensagem de controle da internet (ICMP) é um atauqe comum de negação de serviço (DoS) no qual um invasor tente sobrecarregar um dispositivo de destino com solicitações de eco ICMP (ping)

![[DoS por ping.png]]

# Packet reassembly and sequence prediction

Uma ataque de previsão de sequência TCP é uma tentativa de prever o número de sequência usado para identificar os pacotes em uma conexão TCP, que pode ser usado para falsificar pacotes

![[Packet reassembly and sequence prediction.png]]



# Man-In-the-Middle Attacks

