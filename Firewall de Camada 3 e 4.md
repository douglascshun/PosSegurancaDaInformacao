[[Aula 5 Firewalls]]

![[Camadas 1  2  3  e  4 p firewall.png]]

Como descrito anteriormente sobre a camada 1 ela atua diretamente na parte física portas, e cabos. Já a Camada 2 analisa os pacotes com uma certa profundidade, lendo os cabeçalhos e permitindo que sejam impostas políticas de gerenciamento com base em endereços MAC por exemplo. Agora chegando nas novas camadas, camada 3 e camada 4:

# Camada 3:
A camada 3, trás novidades em relação as anteriores. Está camada permite a implementação de ferramentas de gerenciamento de IPv4 e IPv6, essa camada permite impor políticas de qualquer tipo de protocolos existentes na camada de Internet, como endereço de origem, endereço de destino, DSCP que é um campo de 6 bits no cabeçalho IP do IPv4 ou do IPv6 usado para classificar o tráfego de rede, também TPL que no caso de congestionamento na rede, os dispositivos utilizam ele  para decidir quais pacotes devem ser descartados primeiro.

# Camada 4:
Essa camada é a Camada de Transporte no modelo OSI, os principais protocolos presentes nessa camada são o TCP e o UDP, eles são representados e endereçados com um número de porta 