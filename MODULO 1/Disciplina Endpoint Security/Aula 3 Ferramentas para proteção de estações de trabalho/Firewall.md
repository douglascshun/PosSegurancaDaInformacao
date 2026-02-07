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

As decisões de filtragem são tomadas de acordo com as regras definidas pelo administrador e com o contexto, o que significa o uso de informações de conexões e pacotes anteriores que pertencem à mesma conexão.


# Firewall de gerenciamento unificado de ameaças (UTM)

Normalmente, um dispositivo UTM combina, de maneira flexível, as funções de um firewall com inspeção de estado e prevendo contra intrusões e antivírus.

Ele também pode incluir serviços adicionais e, às vezes, gerenciamento em nuvem. O UTM concentra-se em simplicidade e facilidade de uso.


# Firewall de próxima geração (NGFW)

- Recursos padrão de firewall, como inspeção statefull.
- Prevenção de invasão integrada.
- Reconhecimento e controle da aplicação para detectar e bloquear aplicativos nocivos.
- Atualização de caminhos para incluir feeds futuros de informação.
- Técnicas para lidar com as ameaças à segurança em evolução.
- Saber quais recursos sofrem um risco maior com reconhecimento completo de contexto.
- Reagir rapidamente a ataques com automação de segurança inteligente que define políticas e fortalece suas defesas de forma dinâmica. 
- Detectar melhor as atividades evasivas e suspeitas com correlação de eventos de rede e endpoint.
- Reduz expressivamente o tempo entre a detecção e a limpeza com segurança retrospectiva que monitoram continuamente atividades e comportamentos suspeitos mesmo após a inspeção inicial.
- Facilita a administração e reduz a complexidade com `políticas unificadas`  que oferecem proteção durante todo o ciclo de ataque.


# Firewall

A filtragem de tráfego por meio de um firewall utiliza regras predefinidas ou dinamicamente aprendidas para permitir e negar tentativas de 