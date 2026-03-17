[[Networking Essentials]]
## Componentes de rede

**Introdução**

Para que uma rede de computadores funcione corretamente, ela deve ter um conjunto mínimo de componentes instalados e funcionando, ou seja, devidamente configurados e ativados. Desta forma, as mídias físicas, o hardware de rede e o software de rede são os grupos de componentes básicos das redes de computadores.

Assim, podemos dizer que os meios físicos atuam no transporte dos sinais contendo informações a serem entregues em seu destino. O hardware de rede inclui todos os dispositivos de rede, como hubs, switches, roteadores, servidores e computadores clientes. Software de rede é o conjunto de programas responsáveis ​​pela troca de informações entre máquinas, constituído por um sistema operacional de rede e protocolos de arquitetura de comunicação de rede. (BAY; BLUNING 2016, p.48).

**Objetivos da aula**

- Conhecer os conceitos sobre os meios físicos guiados;
- Compreender a diferença de aplicação de redes em meios físicos não guiados;
- Conhecer os principais componentes e conceitos sobre o hardware de rede;
- Compreender os detalhes sobre as funções dos softwares de rede.

**Resumo**

**Meios físicos guiados**

Os meios de transmissão guiados podem ser divididos em dois grupos: o grupo de meios de cobre e o grupo de meios ópticos. No grupo de meios que utilizam fio de cobre, o cabo coaxial e o par trançado são os principais, enquanto no grupo de meios ópticos, o cabo de fibra ótica está em primeiro plano.

Um cabo coaxial é formado por um condutor interno e um condutor externo, sendo este último uma trança de cobre trançada, separados fisicamente por um material isolante. Há uma cobertura flexível para proteção física e resistência ao fogo sobre a trança para evitar interferências externas. (BAY; BLUNING 2016, p.49).

Embora o cabo coaxial já tenha sido obsoleto e substituído por par trançado, ele ainda tem usos como serviços oferecidos por empresas de televisão a cabo (CATV). Esses cabos podem ser usados ​​para transmitir sinais analógicos em distâncias típicas de vários quilômetros usando repetidores ou sinais digitais usando repetidores de sinal a cada quilômetro. Vale ressaltar que quanto maior a frequência analógica ou a taxa de transmissão digital utilizada, menor o alcance. (BAY; BLUNING 2016, p.49).

O par trançado é o meio de transmissão mais simples e substituiu o cabo coaxial desde o início dos anos 90. O cabo de par trançado é mais flexível, mais rápido, mais fácil de instalar e mais barato do que o cabo coaxial.

Os cabos de fibra óptica não transmitem energia elétrica (na forma de elétrons) como cabos coaxiais ou de par trançado, mas transmitem energia luminosa (na forma de fótons). A composição de uma fibra óptica é simples: o cilindro interno, chamado de núcleo, é muito fino, flexível e capaz de guiar os raios de luz. Feito de quartzo, vidro ou plástico. É coberto com uma casca de material com um índice de refração diferente do núcleo.

**Meios físicos não guiados**

Existem basicamente três grupos na categoria de meios não guiados, meios de transmissão que não necessitam de fios ou cabos. Alguns são baseados em RF (rádio frequência), alguns são baseados em infravermelho, alguns são baseados em laser. A mídia não-guiada, portanto, usa o próprio ar (ou espaço livre) como meio físico de transmissão. (BAY; BLUNING 2016, p.54).

Segundo Amaral (2012, Apud Bay e Bluning 2016, p. 54), a comunicação sem fio é possível por meio de transmissores e receptores acoplados a antenas de tamanho adequado que se comunicam por meio de frequências aéreas. Frequência é o número de ciclos por segundo de uma onda eletromagnética medida em hertz (Hz).

Em relação ao uso de meios físicos de rede, devemos dar prioridade a meios de roteamento com baixo atraso, baixo custo e imunidade a interferências externas. Recursos não guiados devem ser usados ​​onde o uso de recursos guiados é proibido. Por exemplo, quando a instalação de cabos não é (ou é) permitida por algum motivo legal, como transmissão em desertos, pântanos ou cidades.

A mídia baseada em RF (Radio Frequencies) é predominante e possui dois modos de transmissão. O primeiro modo é a transmissão omnidirecional, na qual as ondas de rádio se propagam em todas as direções ao redor de uma antena transmissora, permitindo que diferentes antenas receptoras dentro do alcance captem as informações. Portanto, este modo não é seguro, mas aplicável quando as informações são públicas. Se a segurança for necessária, um sistema de criptografia de informações pode ser ativado. (BAY; BLUNING 2016, p.54).

O modo de transmissão direcional utiliza duas antenas formando um único link, onde somente um sistema receptor registra as informações, e, portanto, este método é consideravelmente mais seguro, embora demande que as duas antenas estejam perfeitamente alinhadas.

Sistemas baseados em infravermelho não necessitam de licença para operar, ao contrário de alguns sistemas de RF que requerem licença da Anatel para operar. O infravermelho, invisível para os humanos, é usado para comunicação entre dispositivos. As frequências infravermelhas estão acima das micro-ondas e abaixo da luz visível. É usado principalmente em televisores domésticos e equipamentos de áudio, mas também pode ser usado para redes de computadores em pequenos dispositivos, como smartphones.

As desvantagens são as limitações de distância e o fato de que a luz infravermelha não pode penetrar em barreiras rígidas, como paredes. O alcance do infravermelho chega a 30 metros na linha de visão, e o aparelho tem capacidade para até 15.

Por outro lado, os sistemas baseados em laser que usam tecnologia semelhante ao infravermelho, mas operam em diferentes faixas de frequência, são altamente direcionais. Isso significa que os dispositivos de envio e recebimento não devem apenas ser fixos, mais precisamente alinhados entre si para que o alinhamento e a comunicação não sejam perdidos.

Também não é necessária licença da Anatel. Por exemplo, uma aplicação pode ser uma interligação LAN entre edifícios, desde que a vista seja perfeita. A vantagem dos sistemas de laser sobre o infravermelho é que alcances muito maiores podem ser alcançados devido à potência e diretividade do transmissor. Os sistemas a laser, por outro lado, são altamente sensíveis às condições climáticas, como chuva e neblina, que podem afetar a mira e interferir nas comunicações.

**Hardware de rede**

Hardware de rede é um grupo de componentes de rede, incluindo dispositivos ou equipamentos usados ​​para habilitar fisicamente as comunicações de rede. Eles são responsáveis ​​por transportar sinais físicos (elétricos, ópticos, eletromagnéticos) entre dispositivos e não devem ser confundidos com caminhos físicos de transmissão. Os principais dispositivos no grupo de hardware de rede são hubs, switches, roteadores, modems, placas de rede, estações de trabalho e servidores. (BAY; BLUNING 2016, p.56).

Um hub é um dispositivo mais antigo que foi usado pela primeira vez para implementar uma rede local (LAN) de topologia em estrela e conectar computadores entre si usando cabos de par trançado. Funciona na camada física e é basicamente um repetidor com capacidade de regenerar, amplificar e retransmitir um sinal recebido em uma porta para todas as outras portas.

Dessa forma, os pacotes que chegam em uma porta do hub são enviados para todas as outras portas do hub, de modo que todos os segmentos da LAN recebam esses pacotes. No entanto, apenas o computador com o endereço de destino do pacote é processado; os outros computadores ignoram o pacote. (BAY; BLUNING 2016, p.57).

Os hubs são muito rápidos porque executam apenas uma iteração de hardware do sinal, mas degradam o desempenho da rede porque todos os dispositivos conectados ao hub compartilham a mesma velocidade. Portanto, se três dispositivos estiverem conectados a um hub de 10 Mbps, cada dispositivo terá apenas 3,33 Mbps se estiverem transmitindo ao mesmo tempo.

Os switches, por outro lado, não operam em velocidade compartilhada. Em outras palavras, se três dispositivos estiverem conectados a um switch de 10 Mbps, todos os três poderão usar a velocidade de 10 Mbps. Como o switch opera na camada de enlace do modelo OSI [...], os pacotes recebidos são enviados apenas para a porta à qual o computador que recebe o pacote está conectado. Isso reduz ou elimina substancialmente o número de colisões que podem ocorrer na rede e melhora o desempenho. (BAY; BLUNING 2016, p.57).

Outro importante componente dos projetos de redes é o roteador, um dispositivo de conexão de rede que implementa funções até a camada de rede. Ao contrário dos switches, os roteadores usam endereçamento lógico para separar o tráfego entre os segmentos. (VENTURY 2016, p.143).

Estes são "computadores" dedicados conectados a múltiplas redes físicas, e uma de suas funções é atribuir pacotes à rede apropriada. Eles conhecem os endereços de algumas redes e os caminhos que os pacotes percorrem até elas. A vantagem de usar um roteador dedicado é que ele foi construído para fazer exatamente isso. Como um computador normal, não há outros processos competindo com a tarefa de roteamento. Os roteadores hoje operam com vários protocolos e oferecem suporte a várias tecnologias de conectividade para redes locais (LANs) e redes de longa distância (WANs). (VENTURY 2016, p.143).

Para Bay e Bluning (2016, p.58), os roteadores também podem controlar o comportamento de determinados protocolos que geram grandes quantidades de tráfego ou broadcasts na rede, fornecendo serviços de proxy (proxy) aos hosts que os utilizam. Um modem, cujo nome representa a abreviação de modulador/demodulador, tem a função de adaptar e transmitir dados por uma linha de transmissão física. Se a mídia for de fibra óptica, um modem óptico é usado. Se o meio for uma rede de metal, um modem de par de metal é usado. Se o meio for de radiofrequência, um modem de rádio é usado.

Para os serviços ADSL (ou banda larga) que usamos em casa, costumamos usar modems analógicos que compartilham serviços de voz (telefonia tradicional) e dados (ADSL - Asymmetric Digital Subscriber Line). Atualmente, os serviços ADSL utilizando pares metálicos atingem velocidades de até 30 Mbit/s, enquanto utilizando a fibra óptica como meio de transmissão já é possível atingir 100 Mbit/s. Nesse caso, a operadora vai levar a fibra até a casa do usuário, o que obviamente encarece o serviço. (BAY; BLUNING 2016, p.58).

Uma placa de rede, também conhecida como interface de rede ou NIC (Network Interface Card), é necessária para permitir que um computador se conecte a uma rede local. As informações enviadas pela rede devem ser condicionadas, os quadros devem ser montados de acordo com o protocolo de rede utilizado e enviados pela rede.

O processo inverso também é realizado. Ou seja, quando as informações chegam pela rede, o cartão usa seu endereço MAC (endereço MAC) para determinar se deve receber essas informações do computador em que está localizado e direcioná-las de acordo. Ele usa protocolos de rede para enviar mais informações ao nível superior, que é um computador. (BAY; BLUNING 2016, p.58).

Um endereço MAC ou endereço MAC é o endereço que existe em cada placa de rede (ou dispositivo de rede) para identificar seu hardware. É composto por 6 octetos, os primeiros 3 octetos identificam o fabricante do hardware e os restantes 3 octetos referem-se a um ID interno definido pelo fabricante do hardware. Não há dois endereços MAC iguais no mundo. (BAY; BLUNING 2016, p.58).

As placas de rede se comunicam com o computador no qual estão instaladas por meio de drivers de comunicação, que se comunicam com o sistema operacional no qual estão instaladas. Existem placas com diferentes padrões de rede, sendo as mais importantes 10 Mbit/s Ethernet, 10 ou 100 Mbit/s Fast Ethernet, 1 Gbit/s Gigabit Ethernet, 10 Gbit/s 10 Gigabit Ethernet, etc. (BAY; BLUNING 2016, p.59).

Servidores e estações de rede nada mais são [...] do que computadores que executam diversas funções definidas em uma rede do tipo cliente/servidor. Um servidor (arquivo, impressão, aplicativo, e-mail, etc.) se dedica apenas à sua função principal e espera que os clientes da rede solicitem os serviços fornecidos pelo servidor. Eles normalmente têm melhor poder de processamento, maior capacidade de disco e RAM e hardware interno mais robusto e tolerante a falhas, como fontes de alimentação duplas e placas de processador duplo. A parte mais pesada do software aplicativo é executada no servidor. (BAY; BLUNING 2016, p.59).

Uma estação de rede, estação de trabalho ou estação cliente, por outro lado, é simplesmente um computador que usa recursos de rede solicitando serviços de um servidor e aguardando uma resposta. As peças mais simples de software aplicativo são executadas em estações de trabalho clientes. Você pode estar com pouco espaço no disco rígido e memória RAM. Como vimos, não podemos esquecer que também existem redes peer-to-peer (P2P) onde os computadores podem ser clientes e servidores. As necessidades dos computadores, as necessidades de outras estações e as necessidades de todos os usuários Os recursos disponíveis de uma estação (BAY; BLUNING 2016, p.59).

**Software de rede**

O software de rede é um grupo de componentes de rede que consiste principalmente em sistemas operacionais de rede (ORS) e protocolos de comunicação. Existem também aplicativos de software de rede e segurança e aplicativos de acesso à rede, mas estão fora do escopo deste folheto. (BAY; BLUNING 2016, p.59).

Quando se trata de comunicação entre computadores que fazem parte de uma rede, o estabelecimento dessa comunicação deve ser feito de forma padronizada para que diferentes dispositivos possam trocar informações entre si. (BARRETO; ZANIN; SARAIVA 2018; BAY; BLUNING 2016, p.95).

As redes são compostas por muitos componentes físicos e lógicos e, portanto, são representadas por camadas de modelos funcionais executados por programas chamados protocolos. Os protocolos são responsáveis ​​por desempenhar as funções de cada camada como se fossem especialistas nessas tarefas.

Assim, segundo Amaral (2012, p. 49), o SOR é responsável por duas funções principais, onde a primeira é atuar como um sistema operacional regular e controlar os recursos do computador do servidor, como o acesso ao Disco Rígido ou Memória Principal. A segunda função é controlar o uso das redes instaladas. Por exemplo, o SOR pode controlar se os usuários da rede podem acessar arquivos no disco rígido de um servidor. (Amal 2012; Zanin; Saraiba 2018, p.60)

Os sistemas operacionais de rede podem ser classificados como ponto a ponto ou cliente/servidor. Em redes ponto a ponto, o tipo de cliente é o SOR instalado. Em todos os computadores, porque essas redes não possuem servidores dedicados. Não use em redes com mais de 20 computadores, pois a configuração e a segurança da rede são difíceis de controlar. Por outro lado, também tem a vantagem de ser mais fácil de instalar e configurar.

Segundo Amaral (2012 apud Zain e Saraiva 2018, p. 60), em uma rede cliente/servidor existem computadores clientes que possuem um SOR cliente e solicitam serviços do servidor. O servidor possui um SOR de servidor semelhante a este: B. Uma distribuição Windows Server 2012 ou Linux para servidores, atendendo a solicitações de clientes. Essas redes são mais complexas e mais caras porque requerem servidores SORs e exigem pessoal técnico especializado para instalar, configurar e manter os serviços prestados pelos servidores.

Um protocolo de rede é um conjunto de políticas que permitem que os computadores em rede se comuniquem entre si. Por exemplo, se você pode enviar uma mensagem, fazer uma solicitação a um servidor, baixar um arquivo ou realizar uma ação interativa na Internet, você está (sem saber) usando um protocolo de rede.

**Conteúdo bônus**

**Tópicos avançados**

CES – porquê acompanhar esta feira de tecnologia?

Ano a ano as maiores empresas de tecnologia se reúnem para organizar feiras onde apresentam seus novos produtos, conceitos e novas tecnologias. A CES (_Consumer Electronics Show_) é considerada a maior feira de tecnologia do planeta e em 2023 apresentou inúmeras tecnologias.

É importante acompanhar feiras como esta para que saibamos as direções que as empresas estão tomando, pois além de novos componentes, novos padrões e protocolos surgem de tempos em tempos e saber qual está sendo adotado pelas maiores empresas ajuda a planejar melhor o tão necessário upgrade da rede da empresa, não é mesmo?

Disponível em: <[https://www.pichauarena.com.br/hardware/principais-novidades-ces-2023/](https://www.pichauarena.com.br/hardware/principais-novidades-ces-2023/)> Acesso em 01/02/2023

Observação: Este conteúdo não será cobrado nas avaliações e estará, obrigatoriamente, presente nas videoaulas. Fique tranquilo(a)!

Referência Bibliográfica

BARRETO, Jeanine dos Santos; ZANIN, Aline; SARAIVA, Maurício de Oliveira. **Fundamentos de redes de computadore**s. – Porto Alegre: SAGAH, 2018.

BAY; Edemilson; BLUNING, Paulo Henrique. **Fundamentos de redes de computadores**. UNIASSELVI, 2016.

VENTURY, Sidney Nicolau. **Fundamentos de rede de computadores**. Rio de Janeiro: SESES, 2016.

[

Próxima aula

Modelos de rede

**Aula concluída**



](https://aulas.descomplica.com.br/pos/mba-em-seguranca-da-informacao-54164c/turma/networking-essentials-461344/aula/modelos-de-rede)
