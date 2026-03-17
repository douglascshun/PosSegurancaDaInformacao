[[Networking Essentials]]
## Gerenciamento de rede

**Introdução**

Redes de computadores são estruturas complexas que devem ser constantemente monitoradas para minimizar problemas como indisponibilidade de rede, lentidão e congestionamento. Esse monitoramento de rede é chamado de gerenciamento de rede. Consiste em monitorar todos os ativos existentes no ambiente e conhecer suas características técnicas, capacidades, aplicabilidade e desempenho.

Além dos hardwares e softwares existentes na rede, a tarefa do gerenciamento da rede é entender todos os tipos de informações que circulam nessa rede e, consequentemente, a quantidade total de dados que circulam no ambiente. Trata-se de saber a quantidade.

**Objetivos da aula**

- Compreender os principais conceitos sobre o gerenciamento de rede;
- Conhecer o histórico do gerenciamento de redes;
- Compreender a importância da análise de protocolos;
- Conhecer os tipos de analisadores de protocolo.

**Resumo**

**Fundamentos de gerenciamento de rede**

Portanto, o gerenciamento de redes também permite dimensionar corretamente os componentes de sua rede para evitar possíveis problemas. Para Kurose (2010, Apud Bay e Bluning 2016, p.178), a ISO (International Organization for Standardization), desenvolveu um modelo de gerenciamento de rede que consiste em:

- **Gerenciamento de desempenho** → Possui principalmente funções para medir, quantificar, notificar, analisar e controlar o desempenho de links como roteadores e terminais.
- **Gerenciamento de erros →** Registra, detecta e responde a condições de erro de rede. Trate os erros que ocorrem na rede imediatamente. • Gerenciamento de configuração → Os administradores podem ver todos os dispositivos na rede e suas configurações de hardware e software.
- **Gerenciamento de Contas** → Registra e controla o acesso de usuários e dispositivos aos recursos de rede. Por exemplo, se você usar cotas de uso, calcule o uso.
- **Gerenciamento de segurança** → Controle o acesso aos recursos da rede de acordo com as políticas definidas. (BAY; BLUNING 2016, p.179). Desta forma, todos os ativos existentes na rede tornam-se aparentes como sendo de suma importância para o bom desempenho geral da rede. Portanto, cada nó deve ser devidamente rastreado e monitorado. Um administrador de rede deve ter um bom conhecimento de cada hardware incluído no ambiente, suas capacidades, vantagens, desvantagens e limitações para dimensionar corretamente cada equipamento incluído na rede de comunicações. (BAY; BLUNING 2016, p.179).

Existem algumas ferramentas de rede que suportam as tarefas do administrador de rede, mas não assumem o trabalho do administrador. Eles servem como base para decisões e ações dentro do ambiente específico que está sendo monitorado. As ferramentas sozinhas não podem resolver interrupções e interrupções de serviço. Muitas ferramentas auxiliam os administradores, mas os administradores devem saber como e onde aplicá-las para obter o máximo de eficiência e eficácia em seu ambiente de computação. (BAY; BLUNING 2016, p.179).

**Histórico do gerenciamento de redes**

Uma rede de computadores consiste em hardware, como computadores, roteadores e outros dispositivos físicos, e software que interage entre si para estabelecer conexões. Mas não se esqueça do referido protocolo que existe no software. Esses protocolos traduzem todas essas informações confusas em algo que o usuário final possa entender. (BAY; BLUNING 2016, p.179) p.177).

Essa combinação de componentes cria uma rede de computadores. Quanto mais componentes você incluir em seu ambiente, maior será a largura e o tamanho de sua rede existente. Portanto, estamos preocupados com o potencial de problemas e falhas neste ambiente e, em última análise, precisamos entender a complexidade do ambiente, processar e monitorar o ambiente e entender quais problemas e problemas futuros podem surgir no futuro.

A Necessidade de profissionais altamente qualificados que possam evitar a Interrupção de mídia não programada. Os administradores de rede nasceram desse requisito. A primeira intervenção dos administradores de rede ocorreu na década de 1980, quando as redes de computadores deram seus primeiros passos. Conhecida como ARPANET, essa primeira rede de computadores foi projetada e construída com base na experimentação.

Como tal, não havia especialistas no assunto e caracterizava-se por vários problemas e obstáculos. O problema mais grave ocorreu em 27 de outubro de 1981, quando a rede em questão falhou. Este momento foi crucial para o surgimento do conceito de gerenciamento de rede. Porque até aquele momento nenhum componente, software ou hardware era controlado ou monitorado.

De acordo com Bay e Bluning (2016, p.178)., como resultado, descobriu-se que o incidente não pôde ser diagnosticado rapidamente, resultando em uma interrupção prolongada das operações. Apenas horas após a descoberta do problema (um erro de comunicação entre os protocolos de rede), ele foi resolvido e corrigido pelos especialistas envolvidos.

Portanto, os administradores de rede são definidos como obrigados a monitorar, gerenciar e controlar todos os componentes presentes em seu ambiente de computação para antecipar incidentes e minimizar possíveis interrupções de serviço. Os administradores de rede devem lembrar que suas tarefas administrativas afetam diretamente a vida diária de todos ao seu redor. Se o trabalho não for feito de forma eficiente, alguns pontos de rede (nós) podem não conseguir se comunicar e alguns usuários podem perder a conectividade.

Transferir essa ideia para o ambiente corporativo facilita o relacionamento. Porque hoje uma empresa sem conectividade é totalmente pouco comunicativa, o que aumenta muito os indicadores negativos da organização. As ferramentas de gerenciamento de rede evoluíram ao longo dos anos e cada ferramenta é especializada em uma área de gerenciamento específica. (Bay; BLUNING 2016, p.180)

**Análise de protocolos**

Um analisador de protocolo é uma ferramenta para observar o tráfego de informações dentro da rede na qual este software está integrado. Com esse tipo de aplicativo, a interface de rede do dispositivo passará a capturar todos os pacotes que circulam na rede. Dessa forma, qualquer pacote válido ou transmitido presente no meio físico de comunicação pode ser interceptado pelo seu host e analisado pela aplicação. Conforme mostrado na Figura 1. (BAY; BLUNING 2016, p.181).

Figura 1: Analisador de Protocolos

![Fonte: Bay e Bluning (2016, p.181).](https://paperx-dex-assets.s3.sa-east-1.amazonaws.com/images/1677705379858-4nvYjgYFdb.png "Fonte: Bay e Bluning (2016, p.181).")

Fonte: Bay e Bluning (2016, p.181).

Na imagem você pode ver todos os pacotes circulando na rede. O próprio aplicativo já realiza o pré-agrupamento dos dados com base no protocolo de comunicação para que os administradores de rede possam interpretar os dados coletados pela ferramenta.

Essa manipulação de dados é comumente conhecida como "escova de bits". Isso ocorre porque o administrador precisa coletar pacotes somente de bits na rede e preparar os dados coletados de maneira útil. (BAY; BLUNING 2016, p.181).

Os analisadores de protocolo permitem que os gestores das redes sejam capazes de medir com grande precisão e em tempo real, o tráfego médio da rede, para que os usuários estão usando a rede e quais hosts estão movendo mais informações no momento. Com base nessas informações, decisões administrativas podem ser tomadas, como expansão de rede, bloqueio de conteúdo e opções para garantir a segurança da informação.

Esses analisadores são importantes ferramentas de gerenciamento. Isso dá aos administradores de rede uma visão completa do que está acontecendo na rede, a partir da qual decisões corretivas e ações preventivas podem ser tomadas para antecipar e minimizar problemas futuros, como apresenta Bay e Bluning (2016, p.182).

Um analisador de protocolo só pode ser usado se estiver conectado diretamente à rede que você deseja espionar (capturar pacotes). Qualquer forma de coleta não pode ser realizada a menos que o host que coleta os dados estejam na mesma rede física que os outros hosts envolvidos no processo. Um software bastante utilizado é o Wireshark, mas existem outras ferramentas semelhantes como TCPDUMP e IPTRAF. A maioria dessas ferramentas são downloads gratuitos. (BAY; BLUNING 2016, p.182).

**Tipos de analisadores de protocolo**

O Wireshark é um analisador de protocolo de rede amplamente utilizado, com versões para plataformas WINDOWS, MAC OS X, LINUX e UNIX fornecidas com software livre. O Wireshark é um analisador de protocolo de rede e também possui um recurso de sniffer que permite capturar pacotes em tempo real dentro da ferramenta para análise posterior.

Os arquivos capturados são processados ​​no formato pcap, pois também são baseados em libcap (WIRESHARK, 2016; LEAL 2017, p.27) e tcpdump. O Wireshark funciona em todas as camadas da pilha TCP/IP. A principal vantagem de usar o Wireshark como um sniffer e analisador de pacotes é a capacidade de monitorar os pacotes capturados. Isso é detalhado pela ferramenta em uma interface gráfica em tempo real. Além disso, possui diversos recursos como inspeção profunda de toras e registro em tempo real (CHAPPEL, 2013; LEAL 2017, p. 27).

Na maioria dos casos, não é recomendado usar o recurso de captura do Wireshark ao mesmo tempo que a análise de pacotes. Isso porque pode afetar os recursos da máquina utilizada. A Figura 2 mostra, de forma clara, a coleta de dados em andamento:

Figura 2: Coleta de dados com Wireshark

![Fonte: Leal (2017, p.28).](https://paperx-dex-assets.s3.sa-east-1.amazonaws.com/images/1677705417576-NH3UEf5wh4.png "Fonte: Leal (2017, p.28).")

Fonte: Leal (2017, p.28).

No diagrama, você pode ver todo o tráfego fluindo pela sua rede em tempo real através da interface gráfica do Wireshark. Tcpdump é um programa executável que roda na linha de comando de sistemas baseados em Unix e é usado para capturar pacotes de tráfego de rede TCP/IP. Neste trabalho, o Tcpdump foi utilizado para capturar o tráfego analisado para treinamento/validação da rede neural.

O tcpdump foi executado por cerca de uma hora em um computador contendo um executável conectado a uma porta específica de um switch em execução na rede (de preferência o switch principal onde todo o tráfego está concentrado). Após esta etapa, todas as portas necessárias neste switch foram espelhadas para aquelas que o tcpdump estava "escutando". Esse fluxo é mostrado na Figura 3. (OLIVEIRA; SA 2018, p.142).

Figura 3: Demonstração de captura de tráfego de rede pelo tcpdump

![Fonte: Oliveira e Sá (2018, p142).](https://paperx-dex-assets.s3.sa-east-1.amazonaws.com/images/1677705662897-7dFanDOK0s.png "Fonte: Oliveira e Sá (2018, p142).")

Fonte: Oliveira e Sá (2018, p142).

A execução do Tcpdump com os parâmetros mínimos necessários para operar coloca a placa de rede do seu computador em modo promíscuo e começa a capturar todo o tráfego que passa por ela. tcpdump então executa uma "tradução" em todos os dados que passam por esta porta. A Figura 4 mostra a linha de comando e os parâmetros usados ​​para essa captura de tráfego. (OLIVEIRA; SA 2018, p.142).

De acordo com Oliveira e Sá (2018, p.143), podemos demonstrar a captura de tráfego de rede pelo tcpdump ao utilizar o seguinte código:

**# tcpdump -i ens33 -c 200 -nn tcp or udp > trafegoDeRede**

O tráfego capturado é armazenado em um arquivo para que possa ser padronizado e encaminhado para um banco de dados relacional, facilitando a localização das informações necessárias para posterior análise dos dados. (OLIVEIRA; SA 2018, p.143).

O IPTraf é uma plataforma projetada para atuar como fonte de consulta sobre as características dos fluxos de rede em backbones IP. A arquitetura da plataforma inclui módulos coletores e ferramentas de análise associadas, conforme mostrado na Figura 2. Os roteadores de borda da Rede Rio/FAPERJ exportam o fluxo de dados coletados para o módulo Collector do servidor IPTraf. O fluxo é processado para gerar metadados que podem ser usados ​​por ferramentas de análise de anomalias. Por fim, o sistema Guardian integra alertas e ferramentas de detecção de anomalias que fornecem uma única interface de monitoramento. (ASSIS et al. 2021, p.03).

**Conteúdo bônus**

**Tópicos avançados**

A revolução das redes de computadores com o aprendizado de máquina

Para que as redes tenham sempre o melhor desempenho e a melhor segurança está cada vez mais necessário o uso de inovações como a inteligência artificial e o aprendizado de máquina, e desta forma começam a surgir redes com estas tecnologias que são capazes de tomar suas próprias decisões, quase que se auto gerenciando.

Obviamente que esse não é um daqueles temas que surgem para amedrontar profissionais da área, apenas estão oferecendo melhores ferramentas de correção de erros e segurança e que vão demandar novas habilidades aos seus gestores, portanto vale a pena conhecer melhor.

Disponível em: <[https://www.linkedin.com/pulse/como-o-aprendizado-de-m%C3%A1quina-pode-ser-aplicado-aos-redes-almeida/?trk=pulse-article_more-articles_related-content-card&originalSubdomain=pt](https://www.linkedin.com/pulse/como-o-aprendizado-de-m%C3%A1quina-pode-ser-aplicado-aos-redes-almeida/?trk=pulse-article_more-articles_related-content-card&originalSubdomain=pt)> Acesso em 01/02/2023

Observação: Este conteúdo não será cobrado nas avaliações e estará, obrigatoriamente, presente nas videoaulas. Fique tranquilo(a)!

Referência Bibliográfica

ASSIS. Felipe M.F. de... [et al.]. IPTraf: **Coleta e Detecção de Anomalias em Fluxos de Rede.** (ANAIS DO XXVI WORKSHOP DE GERÊNCIA E OPERAÇÃO DE REDES E SERVIÇOS) 2021. Disponível em: < [https://sol.sbc.org.br/index.php/wgrs/article/view/17188](https://sol.sbc.org.br/index.php/wgrs/article/view/17188)> Acesso em: 02/11/2022).

BAY; Edemilson; BLUNING, Paulo Henrique. **Fundamentos de redes de computadores**:- UNIASSELVI, 2016.

LEAL. Tiago Silva. **Detecção e análise proativa de anomalias no tráfego de rede**. Santa Cruz do Sul. 2017. Disponível em: <[https://repositorio.unisc.br/jspui/bitstream/11624/2156/1/Tiago%20Silva%20Leal.pdf](https://repositorio.unisc.br/jspui/bitstream/11624/2156/1/Tiago%20Silva%20Leal.pdf)>Acesso em: 02/11/2022.

OLIVEIRA, Diego José, SÁ, Angela Abreu Rosa de. **Redes Neurais Aplicadas à Classificação de Tráfego de Redes de Computadores Utilizando os Protocolos TCP e UDP**. Revista de Sistemas e Computação, Salvador, v. 8, n. 1, p. 135-152, jan./jun. 2018. Disponível em: <[https://core.ac.uk/download/pdf/234559717.pdf](https://core.ac.uk/download/pdf/234559717.pdf)> Acesso em: 02/11/2022.