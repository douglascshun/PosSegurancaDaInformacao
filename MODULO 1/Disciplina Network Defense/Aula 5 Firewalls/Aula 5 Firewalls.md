[[Network Defense]]

**Introdução**

O objetivo deste módulo é explicar o funcionamento de um firewall, apresentar os diferentes tipos e como atuam em cada camada de rede.

**Objetivos da aula**

- O que é um firewall?
- IDS e IPS
- Microsegmentação
- Firewall de Camada 1 e 2
- Firewall de Camada 3 e 4
- Firewall de Camada 7 e Última Geração

**Resumo**

![Fonte: Autoria Própria, 2023.](https://paperx-dex-assets.s3.sa-east-1.amazonaws.com/images/1678142966629-u5iRC5VUHP.png "Fonte: Autoria Própria, 2023.")

Fonte: Autoria Própria, 2023.

Vamos observar o seguinte cenário: temos nosso computador, e contratamos um link de internet para acessar a rede mundial. A operadora vem até a minha residência, instala um cabo e coloca um modem. Plugamos um cabo que liga o nosso computador e agora podemos nos conectar a um computador que se encontra em algum lugar do mundo. Contudo, em compensação, estes computadores em qualquer lugar do mundo também podem se conectar ao meu computador. Ou seja, para a minha segurança, devo instalar um Firewall entre o modem e minha máquina.

No Brasil utilizamos o termo firewall como tradução de parede de fogo, mas a tradução correta seria parede corta-fogo, pois é uma comparação a um dispositivo físico que impede que as chamas se alastrem em caso de incêndio, impedindo a passagem do fogo. Além disso, representa uma proteção que impede o fogo de entrar em um determinado ambiente, mas em redes representa um equipamento físico (hardware) ou software que tem a função de aplicar políticas de segurança a algum ponto da rede. A combinação de software e hardware dedicados à proteção recebe o nome de “appliance”.

Historicamente, surgiram no final da década de 80, por conta da necessidade de se controlar o acesso às redes, e a implementação de políticas de segurança, principalmente para controlar os protocolos de rede que estavam em crescimento e sendo adotados em massa, o nosso famoso TCP/IP, pois essas redes passaram a ser alvo dos primeiros hackers.

O filme “Jogos de Guerra" (War Games) foi lançado em 1983 e já retratava invasões de redes e fraudes em redes de telefonia. Sendo em 1988, identificada a primeira infestação por vírus de computador, que se disseminou por todos os sistemas então existentes, causando o primeiro “apagão” na internet.

O termo firewall foi criado em inglês, fazendo referência a uma função desempenhada pela porta corta-fogo, evitando que os incêndios se alastrem entre os andares de um prédio. Elas deveriam impedir que um novo vírus passasse de uma rede para outra, evitando a sua propagação.

A Primeira Geração de firewalls fazia apenas a filtragem de pacotes. Sua tecnologia foi promovida pela DEC, sendo muito disseminada a partir de 1988. A primeira implementação foi feita por Bill Cheswick e Steve Bellovin e tratava-se de um filtro de pacotes para o conjunto TCP/IP.

Uma das críticas a este modelo é o fato do TCP, que é o principal protocolo de transporte, ser orientado à conexão, e o filtro de pacotes não. Por isso, são chamados de stateless, ou seja, sem conexão.

Estes firewalls de primeira geração basicamente controlavam o tráfego baseando-se em endereços IP de origem e/ou destino, ou por portas TCP/UDP também de origem e/ou destino.

Os primeiros firewalls considerados de segunda geração, que surgiram no começo da década de 1990, tinham a capacidade de criar uma tabela de conexões. Aproveitando do protocolo TCP ser orientado à conexão, eram muito superiores e podiam implementar novas funcionalidades, pois implementavam filtros por sessão e não por pacote, o que é muito mais eficiente. Eles foram considerados firewalls do tipo statefull, ou seja, com estado de conexão.

Os Firewalls continuaram evoluindo saindo versões de 3º e 4ª gerações.

**IDS x IPS**

O **IDS** (_Intrusion Detection System_) e o **IPS** (_Intrusion Prevention System_) são ferramentas que ajudam na segurança de rede. Possuem um banco de dados com a assinatura de várias ameaças e comparam os pacotes passando na rede em busca destas assinaturas. No caso do IDS, se encontrar, avisa. Já no caso do IPS, bloqueia.

O IDS trabalha como uma câmera de segurança, monitorando e registrando tudo o que está acontecendo, mas não impede qualquer ação ofensiva, ou seja, caso haja um furto, podemos verificar nas imagens quem foi o responsável. Contudo, não impedirá o crime, mas ajudará a solucioná-lo.

Já o IPS seria uma câmera com uma pessoa 24hs por dia assistindo as imagens, ou seja, na hora em que a pessoa furtou o item da loja, o vigilante vê pela câmera e aciona um segurança na porta para interceptar o indivíduo, impedindo que o produto seja levado.

Figura: Firewall, IPS e IDS

![Fonte: Autoria Própria, 2023.](https://paperx-dex-assets.s3.sa-east-1.amazonaws.com/images/1678143007682-zPjOecd1dt.png "Fonte: Autoria Própria, 2023.")

Fonte: Autoria Própria, 2023.

**Microsegmentação**

Em cenários simples como uma microempresa com apenas dois computadores temos o dono da empresa e um funcionário, que fazem juntos todas as atividades da empresa, por exemplo, o financeiro, a cobrança e as vendas. Logo, só existe um segmento de rede e uma única política que será implementada para todos os dispositivos, neste caso, com apenas dois computadores. Porém, quando a empresa crescer e prosperar, terá vários departamentos, um comercial, outro de suporte, um de marketing, e o dono vai perceber que a produtividade do comercial, por exemplo, está muito baixa. Ao analisar o problema percebe que estão gastando muito tempo em redes sociais durante o expediente e decide aplicar uma política diretamente no firewall bloqueando as redes sociais. Quando faz isso, o pessoal do marketing reclama na mesma hora, pois tem várias campanhas da empresa nas redes sociais, sendo necessário acompanhar as postagens dos clientes, com os comentários da empresa. O dono percebe que precisa segmentar as políticas, uma para o comercial, outra para o marketing, uma terceira para o suporte, e uma quarta para a rede sem fio que é aberta para os clientes e que não deve se comunicar com os servidores da empresa, de forma que a solução é segmentar a rede e implementar vários firewalls: um controlando cada segmento e com as políticas específicas de cada uma. Assim, ele vai ficar com um firewall central que se liga até a internet e atua em toda a empresa com regras gerais, além de vários firewalls, com as políticas específicas de cada segmento.

Contudo, conforme a rede cresce, aumenta sua complexidade e com os novos serviços e opções de implantação a segurança implementada da forma tradicional não se aplica mais. Nós temos hoje containers, máquinas virtuais, serviços em nuvem, o que nos obriga a segmentar ainda mais o sistema, nos levando ao conceito de microssegmentação, que pode chegar ao ambiente, tipo de aplicativo por camada, baseado no perfil de usuário.

Figura: Rede com um segmento e com vários segmentos.

![Fonte: Autoria Própria, 2023.](https://paperx-dex-assets.s3.sa-east-1.amazonaws.com/images/1678143037179-t0F4xDqNeO.png "Fonte: Autoria Própria, 2023.")

Fonte: Autoria Própria, 2023.

![Fonte: Autoria Própria, 2023.](https://paperx-dex-assets.s3.sa-east-1.amazonaws.com/images/1678143065960-SsQaGn8lbz.png "Fonte: Autoria Própria, 2023.")

Fonte: Autoria Própria, 2023.

**Firewalls de última geração**

Os melhores firewalls de próxima geração oferecem cinco benefícios principais para as organizações, desde pequenas e médias empresas até as grandes. Certifique-se de que o seu forneça:

**1- Prevenção de violação e segurança avançada**

O trabalho número 1 de um firewall deve ser prevenir violações e manter sua organização segura. Porém, como as medidas preventivas nunca serão 100% eficazes, seu firewall também deve ter recursos avançados para detectar rapidamente malware avançado, caso ele escape de suas defesas de linha de frente. O ideal é que tenha os seguintes recursos:

- Prevenção para interromper os ataques antes que eles entrem.
- Um IPS de última geração integrado para detectar ameaças furtivas e detê-las rapidamente.
- Filtragem de URL para impor políticas em centenas de milhões de URLs.
- Integração com um Sandbox a fim de promover uma proteção avançada contra malware, e que seja capaz de analisar de forma contínua o comportamento de arquivos, detectando e eliminando ameaças rapidamente.
- Uma organização de inteligência de ameaças de abrangência mundial para fornecer ao firewall a inteligência mais recente para impedir ameaças emergentes.

**2- Visibilidade abrangente da rede**

Você não pode se proteger contra o que não pode enxergar. Você precisa monitorar o que está acontecendo em sua rede em todos os momentos para que possa identificar o mau comportamento e interrompê-lo rapidamente. Seu firewall deve fornecer uma visão total da atividade e consciência contextual completa para ver:

- Atividade de ameaças entre usuários, dispositivos, hosts e redes.
- Onde e quando uma ameaça foi originada, onde mais ela esteve em sua rede estendida e o que está fazendo agora.
- Aplicativos e sites ativos.
- Comunicações entre máquinas virtuais, transferências de arquivos e muito mais.

**3- Opções flexíveis de implantação e gerenciamento**

Quer você seja uma empresa de pequeno ou médio porte ou uma grande empresa, seu firewall deve atender aos seus requisitos exclusivos:

- Gerenciamento para cada caso de uso - escolha entre um gerenciador na caixa ou gerenciamento centralizado em todos os dispositivos.
- Implante no local ou na nuvem por meio de um firewall virtual.
- Personalize com recursos que atendam às suas necessidades - basta ativar as assinaturas para obter recursos avançados.
- Escolha entre uma ampla gama de velocidades de produção.

**4- Tempo mais rápido para detecção**

O tempo padrão atual do setor para detectar uma ameaça é muito longo. Um firewall de última geração deve ser capaz de:

- Detectar ameaças em segundos.
- Detectar a presença de uma violação bem-sucedida rapidamente.
- Priorizar alertas para que você possa tomar medidas rápidas e precisas para eliminar ameaças.
- Facilitar sua vida implantando políticas fáceis de manter e consistentes, com aplicação automática em todas as diferentes facetas de sua organização.  
     

**5- Automação e integrações de produtos**

Seu firewall de próxima geração não deve ser uma ferramenta isolada. Ele deve trabalhar em conjunto com o restante de sua arquitetura de segurança. Escolha um firewall que:

- Integre-se perfeitamente com outras ferramentas do mesmo fornecedor.
- Compartilhe automaticamente informações sobre ameaças, dados de eventos, políticas e informações contextuais com ferramentas de segurança de e-mail, web, endpoint e rede.
- Automatize tarefas de segurança, gerencie e faça ajuste de políticas e identificação de usuários, além de poder fazer avaliação de impacto.

**Como aplicar na prática o que aprendeu**

No seu computador, seja ele Windows, Linux ou Mac, existe um sistema de firewall. Você já o explorou? Verifique suas características e funcionalidades, explorando e testando as configurações disponíveis.

**Conteúdo bônus**

**Tópicos avançados**

Se quiser aprender mais sobre o assunto desta aula, sugiro as indicações abaixo:

[www.checkpoint.com](http://www.checkpoint.com/) 

[www.kaspersky.com](http://www.kaspersky.com/) 

[www.sonicwall.com](http://www.sonicwall.com/) 

[www.fortinet.com](http://www.fortinet.com/) 

[www.cloudflare.com](http://www.cloudflare.com/) 

Referência Bibliográfica

BEAL, Adriana. **Segurança da informação: princípios e melhores práticas para proteção dos ativos de informação nas organizações.** São Paulo: Atlas, 2005.

CHAPMAN D. BRENT; ZWICKY, ELIZABETH D. - **Building Internet Firewalls**. O’Reilly & Associates Inc., 2st Edition, 2000.

DIAS, Cláudia. **Segurança e auditoria da tecnologia da informação.** Rio de janeiro: Axcel Books do Brasil, 2000.

KIZZA, Joseph Migga. **Computer network security and cyber ethics.** 4th ed. Jefferson: McFarland & Company, 2014.

KUROSE, James F.; ROSS, Keith W. **"Computer Networking".** Pearson Education, 2012.

SCHNEIER, Bruce. **Segurança.com: segredos e mentiras sobre a proteção na vida digital.** Rio de Janeiro: Campus, 2001.

STALLINGS, W; **"Cryptography and Network Security"**; Prentice Hall, 4th Edition, 2005.

STALLINGS, William. **Criptografia e segurança de redes: princípios e práticas.** São Paulo: Pearson Education do Brasil, 2010.

**s e mentiras sobre a proteção na vida digital.** Rio de Janeiro: Campus, 2001.

TANENBAUM, Andrew S.; FEAMSTER, Nick; WETHERALL, David J.; **Computer Network**. Rio de Janeiro: Pearson, 2020.