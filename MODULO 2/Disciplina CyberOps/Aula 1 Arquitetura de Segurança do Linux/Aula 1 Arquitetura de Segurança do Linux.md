[[CyberOps]]


**Introdução**

O módulo Arquitetura de Segurança do Linux apresenta conceitos básicos dos artefatos e tecnologias de segurança em sistemas Linux, inicialmente abordando os pontos elementares de administração do sistema, juntamente com a abordagem de uso do shell nesses processos administrativos. Na sequência foram estudados os fundamentos e segurança do sistema de arquivos do Linux. Em continuidade aos temas abordados, foram vistas as funcionalidades de segurança do Linux, bem como seu firewall nativo e outras versões. A evolução desse estudo aborda estratégias de proteção de conta root, uso de ssh com mais segurança, compreensão da importância de monitoramento de Logs e ACLs.

**Objetivos da aula**

- Compreender as características de administração básica do Linux, bem como o uso do shell do Linux em tarefas gerais administrativas.
- Analisar o funcionamento do sistema arquivos e features de segurança presentes no SELinux de algumas distribuições Linux.
- Entender como de se dá o mecanismo de proteção da conta root, firewall e elevação no nível de segurança no SSH (Secure Shell Protocol), abordando a importância do monitoramento de logs e ACLs

**Resumo**

Nesse módulo foram contemplados os conceitos iniciais de administração básica do Linux e o uso do shell, pois através deste conseguimos aplicar de forma direta e prática os conceitos supracitados. Na sequência foram revelados os elementos estruturantes de segurança do sistema de arquivos de Linux e seus princípios de funcionamento respectivamente. O fechamento dos conceitos iniciais apresentou o mecanismo de proteção da conta root, bem como o processo necessário na elevação do nível segurança do SSH e firewall Linux, com destaque para os processos de monitoramento de logs, configuração e administração de Access Control Lists (ACLs).

Historicamente, é importante destacar que Linus Torvalds utilizou o Minix, do professor Andrew S. Tanenbaum, em seus estudos na disciplina de Sistemas Operacionais, ainda na Universidade de Helsinki na Finlândia. Buscando ampliar algumas funcionalidades e entendendo que, ao criar o Linux, este poderia figurar como uma alternativa acessível, em contraponto aos sistemas da família Unix, que eram e ainda são muito onerosos.

Em um momento histórico anterior, especificamente no ano de 1984, Richard Stallman cria o projeto GNU (Gnu's Not Unix), segundo seu próprio relato, após perceber que o desenvolvimento tecnológico poderia seguir um caminho ruim, pois em sua necessidade de acesso ao código fonte de um drive para um impressora recém adquirida pelo laboratório de inteligência artificial do MIT, onde trabalhava, deve esse acesso negado e assim não pode executar as melhorias que julgava pertinente ao uso daquela impressora.

O GNU/Linux passou a indicar a junção dos aplicativos e programas desenvolvidos no projeto GNU, com o kernel Linux, que se mostrou mais rápido e eficiente com sua arquitetura de kernel monolítico. Logo após, aconteceu o fenômeno do surgimento das distribuições Linux que passaram a oferecer pacotes de aplicativos e funcionalidades direcionadas a necessidades individuais e de mercado, assim passou-se a ter distribuições Linux especializadas para soluções de segurança, armazenamento de banco de dados, controle de domínio, serviços web e de rede, como pode ser visto no site <[https://distrowatch.com/](https://distrowatch.com/)> **(Acesso em 16/02/2023)** que ranqueia e atua como observatório de distribuições.

O fato do sistema operacional Linux ser um sistema multiusuário possibilita controle de permissão e privilégios ao sistema de arquivos, impedindo que arquivos e personalizações sejam acessíveis por outros usuários do sistema. O usuário root é o administrador do sistema com permissão total de manipulação de arquivos de configuração do sistema. A hierarquia do sistema de arquivo no Linux segue a seguinte estrutura:

- / - é o diretório raiz.
- /bin – é o diretório onde ficam os arquivos binários.
- /dev – é o diretório dos arquivos especiais associados aos dispositivos do sistema.
- /etc – é o diretório onde ficam os arquivos de configuração do sistema.
- /home – é o diretório dos arquivos pessoais de um usuário do sistema.
- /lib – é o diretório das bibliotecas do sistema
- /mnt – é o diretório onde encontram-se os pontos de montagem
- /proc – é o diretório com arquivos associados aos processos do sistema.
- /root – é o diretório home do root.
- /sbin – é o diretório dos arquivos binários do root.
- /tmp – é o diretório dos arquivos temporários do sistema.
- /usr – é o diretório dos arquivos e programas usados por usuários do sistema.
- /var – é o diretório dos arquivos de dados das contas de usuários.
- /boot – é o diretório dos arquivos utilizados para o processo de boot do sistema.
- /log – é o diretório dos arquivos de log do sistema.

Os diretórios citados acima podem ser considerados os principais do sistema Linux. Contudo, temos outros diretórios que possuem aplicações específicas.

Security Enhanced Linux é um sistema de controle de acesso que foi introduzido em algumas distribuições Linux que constituí uma interface de segurança que estabelece regras para autorizar ou proibir certas operações, bem como uma ampla gestão dos processos de permissão.

Entre algumas medidas reconhecidas como estratégias de elevação no nível de segurança do sistema Linux, podemos destacar a proteção da conta root, ssh hardening e utilização de firewall Linux nativo.

ACLs são utilizadas para obter controle mais refinado das permissões do sistema de arquivos do Linux. Em sistemas UNIX ou GNU/Linux, arquivos de log são compostos de informações em texto puro e são continuamente acrescidos de novas informações.

**Como aplicar na prática o que aprendeu**

Uma distribuição Linux (muitas vezes abreviada como distro) é um sistema operacional feito de uma coleção de software que inclui o kernel do Linux e, muitas vezes, um sistema de gerenciamento de pacotes. Os usuários do Linux geralmente obtêm seu sistema operacional baixando uma das distribuições do Linux, que estão disponíveis para uma ampla variedade de sistemas, desde dispositivos embarcados (por exemplo, OpenWrt) e computadores pessoais (por exemplo, Linux Mint) até poderosos supercomputadores (por exemplo, Rocks Cluster Distribution). Acesse o site <[https://distrowatch.com/](https://distrowatch.com/)> e acompanhe por alguns dias o ranking das distribuições Linux.

**Conteúdo bônus**

**Tópicos avançados**

Revolution OS é um documentário de 2001 que traça a história de vinte anos do GNU, Linux, código aberto e o movimento do software livre. Dirigido por J. T. S. Moore, o filme apresenta entrevistas com hackers e empresários proeminentes, incluindo Richard Stallman, Michael Tiemann, Linus Torvalds, Larry Augustin, Eric S. Raymond, Bruce Perens, Frank Hecker e Brian Behlendorf. O documentário vai apresentar uma série de eventos históricos que irão ampliar seu entendimento sobre sistemas open source.

Referência Bibliográfica

**Bibliografia Básica**

RICCI, Bruno. **Rede Segura:** VPN Linu**x**, Editora Ciência Moderna, 2007.

TANENBAUM, A. S., **Redes de Computadores**. Rio de Janeiro, Campus, 2003.

COSTA, Daniel Gouveia. **Administração de Redes com Scripts**, 2ª Edição, Editora Brasport, 2010.

**Bibliografia Complementar**

SMITH, Rodercik W**. Linux:** Ferramentas Poderosas, 1ª Edição, 2004, Editora Ciência Moderna.

NAKAMURA, E. T., e GEUS, P. L., **Segurança de Redes em Ambientes Cooperativos**, 2 ed. Ed. Berkley, São Paulo, 2007.

MORAES, Alexandre F. **Redes de Computadores**. 7ª Edição, Editora Érica, 2008.

MENDES, Douglas Rocha, **Redes de Computadores**, Ed. Novatec, 1ª Edição, 2007

STARLIN, Gorki, **Conceitos, Protocolos e Uso Tcp/Ip: Redes de Computadores.** 1ª Edição, Alta Books, 2004.