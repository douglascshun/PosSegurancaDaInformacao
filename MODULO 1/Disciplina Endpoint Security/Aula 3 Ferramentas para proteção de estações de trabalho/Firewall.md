[[Aula 3 Ferramentas para proteção de estações de trabalho]]


# O que é firewall?

Um firewall (Muro de fogo) é um sistema de segurança de rede de computadores que protege o tráfego da internet para a rede privada. Esse software ou hardware funciona bloqueando ou permitindo pacotes de dados.

![[Illustracao de firewall.png]]

Os firewalls têm  sido a linha de frente da defesa na segurança de rede há mais de 25 anos.

Eles colocam uma barreira entre redes internas protegidas e controladas que podem ser redes externas confiáveis ou não, como a internet.


# Como funciona o firewall?

O firewall decide qual tráfego de rede pode passar e qual tráfego é considerado perigoso. Ele atua como um filtro, separando o que é bom do que é ruim, o confiável do não confiável. 

`No entando, antes de entrarmos em detalhes, é útil entender a estrutura das redes baseadas na Web.`


# Qual o objetivo do firewall?

É proteger as redes privadas e os dispositivos de endpoint contidos nelas, que são conhecidos como host's de redes.

Os host's de rede são dispositivos que "conversam" com outros host's na rede. Eles enviam e recebem entre redes internas, bem como saída e entrada entre redes externas.


# Firewall

- Redes públicas externas normalmente consistem na internet pública/global ou em várias extranet's.

- Rede privada interna define uma rede domestica, intranet's corporativas e outras redes "fechadas".

- Redes de perímetro detalham redes de fronteira que consistem de host's bastiões: host's de computador dedicados com segurança reforçada que estão prontos para resistir a ataques externos.

# Firewall de proxy

Um firewall de proxy é um dos primeiros tipos de firewall e funciona como a passagem de uma rede para outra de uma aplicação específica.

Servidores proxy podem oferecer recursos adicionais, como armazenamento em cache e segurança de conteúdo ao evitar conexões diretas de fora da rede No entanto, isso também pode afetar a capacidade de taxa de transferência e as aplicações que eles podem comportar.



# Firewall com inspeção de estado

Atualmente conhecido como firewall tradicional, um firewall com inspeção de estado permite ou bloqueia tráfego de acordo com o estado, a porta e o protocolo. Ele monitora toda atividade desde o momento em que uma conexão é aberta até que ela seja fechada.

As decisões de filtragem são tomadas de acordo com as regras definidas pelo administrador e com o contexto, o que significa o uso de informaçõ