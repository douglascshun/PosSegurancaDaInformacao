[[Aula 5 Firewalls]]

![[Camadas 1  2  3  e  4 p firewall.png]]

Como descrito anteriormente sobre a camada 1 ela atua diretamente na parte física portas, e cabos. Já a Camada 2 analisa os pacotes com uma certa profundidade, lendo os cabeçalhos e permitindo que sejam impostas políticas de gerenciamento com base em endereços MAC por exemplo. Agora chegando nas novas camadas, camada 3 e camada 4:

# Camada 3:
A camada 3, trás novidades em relação as anteriores. Está camada permite a implementação de ferramentas de gerenciamento de IPv4 e IPv6, essa camada permite impor políticas de qualquer tipo de protocolos existentes na camada de Internet, como endereço de origem, endereço de destino, DSCP que é um campo de 6 bits no cabeçalho IP do IPv4 ou do IPv6 usado para classificar o tráfego de rede, também TPL que no caso de congestionamento na rede, os dispositivos utilizam ele  para decidir quais pacotes devem ser descartados primeiro. Ressaltando que essa camada permite filtrar a entrada por endereços específicos como bloquear endereços da Meta o que restringe o acesso a algumas redes sociais.

# Camada 4:
Essa camada é a Camada de Transporte no modelo OSI, os principais protocolos presentes nessa camada são o TCP e o UDP, eles são representados e endereçados com um número de port, como por exemplo a porta 80 que a porta do protocolo HTTP.  Essa camada diferentemente da camada anterior, bloqueia aplicações específicas de endereços, vamos supor que na camada anterior seja configurado o bloquei do IP do Youtube, o endereço do mesmo é igual ao endereço do de outras ferramentas do Google como o G-mail, o Mecanismo de pesquisa do Google entre diversas outras ferramentas que a empresa oferece, bloquear isso pode gerar uma situação gravíssima para a empresa, então a camada 4 vem como solução buscando oferecer o bloqueio de aplicações específicas ao invés do endereço inteiro.


# Firewall Stateless:
Tipo de firewall que não analisam o contexto o contexto de conexão.

# Firewall Statefull:
Analisam contexto ou seja o fluxo completo do conjunto de pacotes, o que os tornam mais eficientes e consomem menos recuros 

# Aplicação:
As aplicações como TeamViewer, Navegação WEB, Vídeo, WEB, precisam ser bloqueados fora do Firewall ou um firewall de camada 7