[[Aula 1 Monitoramento de redes]]

# Tipos de Monitoramento:

- `Ativo`
- `Passivo`


# Ativo:
  Fornece respostas instantâneas mas, não monitora a todo momento somente quando solicitado, é bom para monitoramento planejado e ao longo do tempo.
  
`Exemplos:`
- SNMP (Simple Network Protocolo)
Usado em monitoramento de redes fornece dados sobre como está o dispositivo, uso do processador, rede, hd. O protocolo funciona por meio de códigos, onde cada código fornece um dado, como código 1 para o status da CPU, código 2 para o status da conexão de rede e ai vai...

- ICMP (Internet Control Message Protocol)
Responsável por varias ferramentas uteis como o ping

- SSH
Usado para acessar maquinas, o que fornece ativamente dados de qualquer dispositivo que tenha conexão via SSH estabelecida


# Passivo: 

Fornece monitoramento contínuo, ou seja a todo momento.


 `Exemplos:`
- SNMP (Simple Network Protocolo)
 Sim novamente ele, ativo e passivo. Ele permite o uso do chamado trap SNMP, que faz com que ao chegar em determinado estado o servidor