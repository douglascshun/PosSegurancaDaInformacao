[[IoT Security]]

**Introdução**

O objetivo deste módulo é identificar em detalhes as principais ameaças ao IoT.

**Objetivos da aula**

- Apresentar as metas para a mitigação dos riscos em IoT;
- Discutir os aspectos para aumentar a confiabilidade de um ecossistema IoT;
- Entender os tipos de ataques à infraestrutura;
- Entender como são os ataques às casas Inteligentes;
- Entender os ataques baseados no hub central;
- Entender os ataques baseados na segurança física.

**Resumo**

Os riscos de segurança cibernética e privacidade em um ecossistema IoT podem ser tratados objetivando a mitigação de riscos em três frentes:

- **Proteger a segurança do dispositivo**, impedindo que um dispositivo seja usado para realizar ataques. Aqui, devemos tratar especialmente os seguintes pontos:
- **Gerenciamento de ativos**, para manter um inventário atualizado e preciso, incluindo as características relevantes ao longo dos ciclos de vida dos dispositivos, para alimentar o processo de gerenciamento de riscos de segurança cibernética e privacidade.
- **Gerenciamento de vulnerabilidades**, para identificar e eliminar vulnerabilidades conhecidas no software e firmware de dispositivos IoT, reduzindo a probabilidade de exploração e comprometimento.
- **Gerenciamento de acesso**, com a implementação de soluções de controle de identidade/autorização para acesso físico e lógico, para evitar o uso e a administração de dispositivos IoT por pessoas, processos e outros dispositivos de computação não autorizados.
- **Detecção de Incidentes**, para monitorar e analisar a atividade do dispositivo IoT em busca de sinais de incidentes envolvendo a segurança do dispositivo.

- **Proteger a segurança dos dados,** garantindo o atendimento aos pilares da segurança da informação, ou seja, a confidencialidade, a integridade e a disponibilidade de dados (incluindo dados pessoais) coletados, armazenados, processados ou transmitidos de ou para o dispositivo IoT, incluindo:
- **Segurança dos dados,** para impedir o acesso e a adulteração de dados em repouso ou em trânsito que possam expor informações confidenciais ou permitir a manipulação ou interrupção das operações do dispositivo IoT.
- **Detecção de incidentes com dados**, para monitorar e analisar a atividade do dispositivo IoT em busca de sinais de incidentes envolvendo segurança de dados.

- **Proteger a privacidade das pessoas,** especialmente quando do tratamento de dados pessoais, aplicando os meios adequados para a proteção desses dados. Aqui deve-se abordar:
- **Gerenciamento do fluxo de informações**, mapeando e atualizando com precisão o ciclo de vida dos dados pessoais;
- **Permissão de processamento de Dados Pessoais**, gerenciando adequadamente as permissões para o processamento de Dados Pessoais;
- **Tomada de decisão informada**, para permitir que os indivíduos entendam os efeitos do processamento de Dados Pessoais e das interações com o dispositivo, de forma que o titular tenha participação efetiva na tomada de decisões sobre o processamento dos Dados Pessoais;
- **Gerenciamento de dados desassociados**, de forma a identificar o processamento autorizado e determinar como os dados pessoais podem ser minimizados ou desassociados do titular e endpoints;
- **Detecção de violação**, para monitorar e analisar a atividade do dispositivo IoT em busca de sinais de violações envolvendo a privacidade dos indivíduos.

**Aspectos para aumentar a confiabilidade de um ecossistema IoT**

Toda implantação de IoT deve ter um documento abrangente de arquitetura, procedimentos, protocolos, funções e responsabilidades, ou seja, um processo de governança de segurança de IoT. Embora existam diferentes maneiras de implementar a governança de segurança de IoT, um modelo de governança de segurança de IoT deve incluir os seguintes princípios: estratégia de segurança de IoT, processos de IoT, estratégia de dados, monitoramento e geração de relatórios, gerenciamento do ciclo de vida e gerenciamento de melhores práticas de segurança de IoT. Assim, o plano de governança de segurança IoT deve incluir os seguintes aspectos:

- **Treinamento e conscientização**, que seja adequado ao público-alvo e o grau de envolvimento no ecossistema IoT – usuário ou técnico - , abordando temas como segurança IoT, arquitetura de segurança IoT, políticas de segurança IoT, procedimentos de integração de dispositivos IoT, auditoria de segurança IoT, detecção de ameaças IoT, vulnerabilidades de segurança de dispositivos IoT, vulnerabilidades de segurança de soluções IoT, segurança de aplicativos em nuvem, segurança de aplicativos, segurança de rede IoT, ameaças e ataques comuns de segurança IoT, recomendações e melhores práticas de segurança IoT, métodos e procedimentos para identificação de vulnerabilidades IoT, detecção de ameaças, mecanismo de proteção e procedimentos de recuperação, responsabilidades compartilhadas de segurança de IoT entre diferentes partes interessadas e parceiros, dentre outros.
- **Plano de Gerenciamento de Riscos**, que contemple o gerenciamento de dispositivos e dispositivos IoT, gerenciamento do ciclo de vida do dispositivo, interfaces de dispositivo como dispositivo para nuvem, os riscos associados aos acessos como gateway de API, portais e aplicativos da Web, riscos em relação à conectividade de rede, plataformas, produtos e serviços, riscos associados aos usuários de IoT, cadeia de suprimentos e cadeia de valor, o adequado gerenciamento de software e firmware, além da segurança física e proteção e gerenciamento de dados, incluindo compartilhamento e privacidade.
- **Documentação de processos IoT**, uma vez que documentar processos e procedimentos é uma medida proativa para prevenir ou mitigar problemas de segurança. Os processos de documentação e execução de IoT devem incluir: planos de prontidão operacional de IoT, auditorias de segurança, protocolos de integração de dispositivos IoT, protocolos de teste e certificação de dispositivos IoT, planos de gerenciamento de segurança, incluindo patches de software, planos de gerenciamento de dados, processos operacionais de segurança e planos de automação de processos.
- **Plano de Estratégia de Dados**, pois o principal valor de uma solução de IoT são os dados que ela gera e como eles podem fornecer informações sobre problemas existentes, ajudar a descobrir padrões potenciais, criar novas soluções, prever novos resultados, desafiar e moldar nosso pensamento. Uma estratégia de dados, portanto, é outro elemento-chave de uma governança de segurança de IoT na busca da melhor maneira para fazer a gestão de dados confidenciais e sensíveis, como se dará o tratamento de dados pessoais e a coleta e compartilhamento dos dados coletados e tratados. Deve-se, ainda, observar sempre as regulamentações e Legislações aplicáveis.
- **Plano de monitoramento e relatórios**, para possibilitar o diagnóstico preventivo de equipamentos de rede e endpoints, registrar eventos incomuns, capturar eventos que sirvam de gatilhos para o acionamento de ações automatizadas com base em regras de negócios definidas. Permite ainda entender o desempenho de sua solução de IoT, incluindo a verificação da disponibilidade de dispositivos e detecção de acesso não autorizado, desenvolvendo um conhecimento e compreensão do funcionamento normal de todo o ecossistema, de forma a prever incidentes que possam impactar os negócios, permitindo ações e tomadas de decisão apropriadas.
- **Plano de Gestão do Ciclo de Vida**, que deve incluir protocolos de documentação para a execução de teste de integração de dispositivos IoT durante o seu ciclo de vida, gestão de patches de software e atualizações de firmware, gerenciamento de ativos e processos de alienação de ativos.

**Ataques à infraestrutura**

Os sistemas IoT são baseados em dois componentes principais: **hardware** do sistema e **software** do sistema; ambos têm falhas de design com bastante frequência. As vulnerabilidades de hardware são muito difíceis de identificar e também difíceis de corrigir, mesmo que a vulnerabilidade tenha sido identificada devido à compatibilidade e interoperabilidade do hardware e também ao esforço necessário para corrigi-la. As vulnerabilidades de software podem ser encontradas em sistemas operacionais, software de aplicativo e software de controle, como protocolos de comunicação e unidades de dispositivos. Por sua vez, ataques são ações realizadas para prejudicar um sistema ou interromper as operações normais, explorando vulnerabilidades usando várias técnicas e ferramentas.

Os tipos de ataques mais comuns seriam:

- **Ataques físicos**, que adulteram componentes de hardware dos dispositivos. O ecossistema IoT é altamente vulnerável a esse tipo de ataque, pois a maioria dos dispositivos IoT opera em ambientes externos.
- **Ataques de reconhecimento**, que fazem a descoberta e mapeamento não autorizado de sistemas, serviços ou vulnerabilidades, para posterior exploração.
- **Negação de serviço (DoS),** ataque que tenta assumir o controle de um dispositivo ou recurso de rede, tornando-o indisponível para os usuários legítimos. Como os dispositivos IoT, em geral, possuem recursos limitados, como pouca memória e CPU limitada, todo o ecossistema acaba sendo vulnerável a esse tipo de ataque.
- **Ataques de acesso**, no qual pessoas não autorizadas obtêm acesso a redes ou dispositivos aos quais não têm direito de acesso. Há dois tipos diferentes de ataque de acesso: o primeiro é o **acesso físico**, pelo qual o atacante obtém esse acesso fisicamente ao dispositivo; e o **acesso remoto**, que é realizado por meio da rede e/ou Internet.
- **Ataques à privacidade**: proteger a privacidade é um desafio cada vez maior, especialmente em IoT, dada a grande quantidade de informações coletadas e tratadas. Nesse sentido, os ataques mais comuns à privacidade do usuário, em ambientes IoT, seriam:
- **Mineração de dados**: com acesso indevido e descoberta de informações em determinados bancos de dados.
- **Espionagem cibernética**: quando se utiliza técnicas de cracking e software malicioso para espionar ou obter informações secretas de indivíduos, organizações ou do governo.
- **Espionagem**: interceptando e ouvindo conversa entre duas partes, de forma não autorizada.
- **Rastreamento de usuários**: por meio do número de identificação exclusivo (UID) do dispositivo associados ao usuário ou mesmo pela localização georreferenciada.
- **Ataques baseados em senha**: para obter acesso indevido com senhas comprometidas ou de baixa complexidade.
- **Meio para cibercrimes**: os dispositivos IoT conectados à Internet podem ser utilizados para explorar usuários e dados para ganho material, como roubo de propriedade intelectual, roubo de identidade, roubo de marca e fraude [[6](https://journals.riverpublishers.com/index.php/JCSANDM/article/download/6087/4527?inline=1#bib6), [7](https://journals.riverpublishers.com/index.php/JCSANDM/article/download/6087/4527?inline=1#bib7), [44]](https://journals.riverpublishers.com/index.php/JCSANDM/article/download/6087/4527?inline=1#bib44). 
- **Ataques destrutivos**: uso do ecossistema IoT, especialmente atuadores, para criar perturbações e destruição em larga escala de vidas e propriedades.
- **Ataques de controle de supervisão e aquisição de dados** (SCADA - _Supervisory Control and Data Acquisition_): Como qualquer outro sistema TCP/IP, o sistema SCADA é vulnerável a muitos ataques cibernéticos, incluindo: (i) uso de negação de serviço para indisponibilizar o sistema e (ii) uso de cavalos de Tróia ou vírus para assumir o controle do sistema.

**Casas inteligentes sob ataque**

Os dispositivos domésticos inteligentes facilitam nossa vida; a automação pode tornar nossa rotina mais confortável e nossa casa mais segura. No entanto, todos esses dispositivos podem apresentar uma grande ameaça se forem atingidos por ataques cibernéticos, como vírus, ataques maliciosos, ataques da Web, dentre outros. Esses ataques podem ser classificados em:

- Ataques baseados na **arquitetura;**
- Ataques baseados no **hub central;**
- Ataques baseados na **segurança física.**

Os ataques baseados na arquitetura podem ser subdivididos em:

- **Ataques na camada de Aplicação**
- **Code Injection**, onde há a injeção de dados em aplicativos Web, gerando a interpretação e execução de dados maliciosos de maneira inesperada, como forma de explorar erros e vulnerabilidades de programas.
- **Buffer Overflow**, quando um programa deliberadamente tenta ocupar mais espaço de armazenamento do que o buffer pode suportar, de forma que os dados extras transbordem para outra área de memória, com o objetivo de fazer a exploração de vulnerabilidades
- **Data Manipulation**, para obter acesso ilegal para explorar falhas de projeto no modelo de permissão
- **Autenticação**, para explorar e descobrir brechas de segurança em aplicativos da web em relação ao processo de autenticação
- **Ataques na camada de Middleware**
- **Flooding**, um tipo de ataque de negação de serviço em que uma rede ou um serviço fica tão sobrecarregado com pacotes iniciando solicitações de conexão incompletas que não pode mais processar solicitações de conexão genuínas, afetando a disponibilidade e qualidade do serviço
- **Cloud Malware**, no qual o invasor tenta injetar um serviço malicioso na nuvem e cria seu próprio módulo de implementação de serviço malicioso e tenta adicioná-lo ao sistema de nuvem. Em caso de sucesso do ataque, a nuvem irá redirecionar automaticamente a solicitação do usuário válido para que o código do invasor comece a ser executado
- **SQL Injection**, no qual instruções SQL são utilizadas para gravar, excluir operações e ler quando o aplicativo da Web está sendo invadido por injeção de SQL. As páginas mostram resultados diferentes em comparação com as informações reais na rede.
- **Signature Wrapping**, que usa a assinatura XML para garantir a integridade do serviço. Os invasores podem facilmente modificar a comunicação entre os nós nesta camada espionando sem invalidar a assinatura
- **Ataques à camada de Rede**
- **DOS**, forma de ataque bem conhecida, que gera uma grande quantidade de dados, fazendo com que o serviço seja impactado
- **Sybil**, onde o invasor subverte o sistema de reputação de um serviço de rede criando muitas identidades pseudônimas e as usa para obter uma influência desproporcionalmente grande.
- **Sinkhole**, no qual um nó comprometido atrai o fluxo de dados de nós próximos de forma que o invasor pode usar o nó malicioso para atrair tráfego de rede e, em seguida, os dados do sensor podem ser operados arbitrariamente
- **Man-in-the-Middle**, onde dados trocados entre duas partes são de alguma forma interceptados, registrados e, possivelmente, alterados pelo atacante sem que as vítimas percebam
- **Ataques à camada de Percepção**
- **Spoofing**, no qual o invasor usa muitos endereços de origem falsos diferentes, enviando pacotes pela rede. Ao amplificar o ataque, o atacante disfarça um tag como um tag válido, que ganha a mesma permissão e serviço que o tag válido
- **Sleep Deprivation**, para prolongar a vida útil da bateria, muitos endpoints acabam “hibernando” quando não estão em operação. Esse tipo de ataque tenta subverter esse processo, controlando e enviando constantemente informações aos dispositivos da rede
- **Eavesdropping**, quando diferentes sistemas de e-mail, mensagens instantâneas e telefonia, e outros serviços de internet, são utilizados para roubar credenciais de usuários para posterior utilização indevida
- **Radio Frequency jamming**, que mira a camada física da comunicação sem fio dos endpoints, impedindo o envio de dados.

Já os ataques baseados no hub central ou roteador de uma casa inteligente podem ser divididos em:

- **Ataque de Software**, que exploram as vulnerabilidades no software do hub ou roteador por meio de sua interface de comunicação, que pode ser feito por meio de vírus, negação de serviço, worms e ataque de filtro VPN que permite a injeção de um código malicioso no sistema
- **Ataque DoS**, onde o invasor usa várias solicitações de série para inundar o roteador com solicitações de mensagens usando pacotes ICMP
- **Ataque de tratamento incorreto de pacote**, que pode ocorrer durante qualquer transmissão de dados, pois um agente mal-intencionado pode capturar os pacotes de dados e alterar a formatação deles, dificultando e até impossibilitando o correto tratamento deles. O ataque pode gerar congestionamento, redução da taxa de transferência e ataques de negação de serviço.
- **Ataque VPNFilter**, no qual um malware, uma plataforma modular, com várias fases e recursos que permitem operações de coleta de informações e ataques cibernéticos.

Por sua vez, os ataques baseados na segurança física, podem ser dos seguintes tipos:

- **Ataque de fonte de tensão**, que modifica afeta o funcionamento do dispositivo interrompendo o fornecimento de energia; e
- **Ataque de adulteração**, que ocorre quando o invasor está próximo do dispositivo e consegue alterar o hardware sem autorização.

**Conteúdo bônus**

**Tópicos avançados**

**Ataques SCADA**

SCADA é a sigla em inglês para _Supervisory Control and Data Acquisition_, que se refere a sistemas utilizados para monitorar e controlar processos industriais e infraestruturas críticas, como usinas de energia, sistemas de distribuição de água e redes de transporte. Esses sistemas são compostos por um conjunto de dispositivos interconectados, como sensores, atuadores e controladores, que coletam dados e enviam comandos para controlar os processos.

Um ataque SCADA é um ataque cibernético que tem como alvo esses sistemas, visando a interrupção ou manipulação dos processos controlados pelos dispositivos conectados. Esses ataques podem ser realizados por meio da exploração de vulnerabilidades nos dispositivos, nas redes de comunicação ou em softwares utilizados pelos sistemas.

Existem diversas vulnerabilidades que podem ser exploradas para realizar um ataque SCADA, tais como:

- **Senhas fracas ou padrões de autenticação inseguros**: muitos dispositivos SCADA possuem senhas padrão ou previsíveis, o que facilita o acesso não autorizado ao sistema.
- **Falhas de segurança em dispositivos**: dispositivos SCADA podem possuir vulnerabilidades que permitem que um invasor assuma o controle desses dispositivos e, consequentemente, dos processos controlados por eles.
- **Falhas de segurança na rede**: muitos sistemas SCADA utilizam redes de comunicação vulneráveis, como a Internet, sem proteções adequadas, o que pode permitir que um invasor tenha acesso aos dispositivos conectados.

Para mitigar os riscos de ataques SCADA, é importante adotar medidas de segurança efetivas, como:

- Utilização de firewalls e sistemas de detecção de intrusão para monitorar e controlar o tráfego na rede.
- Utilização de criptografia de dados para proteger as informações transmitidas entre os dispositivos.
- Implementação de políticas de segurança adequadas para a gestão de senhas e acesso aos dispositivos.
- Atualização regular dos dispositivos e softwares utilizados pelo sistema SCADA.
- Implementação de procedimentos de backup e recuperação em caso de falha ou ataque.

Alguns exemplos de ataques SCADA incluem:

- **Ataque Stuxnet**: esse ataque, descoberto em 2010, visou a infraestrutura de enriquecimento de urânio do Irã, utilizando um malware que se propagava por dispositivos USB e comprometia os sistemas SCADA.
- **Ataque à usina de energia ucraniana**: em 2015, um grupo de hackers comprometeu a rede de computadores da usina de energia ucraniana e interrompeu o fornecimento de energia elétrica para centenas de milhares de pessoas.
- **Ataque à rede de distribuição de água em Israel**: em 2020, um grupo de hackers comprometeu a rede de distribuição de água em uma cidade em Israel, tentando elevar a concentração de cloro na água para níveis perigosos. O ataque foi detectado a tempo e não causou danos significativos.

Referência Bibliográfica

BOECKL, K. et al. **Considerations for managing Internet of Things (IoT) cybersecurity and privacy risks**. National Institute of Standards and Technology. 2019. Disponível em: <[https://doi.org/10.6028/nist.ir.8228](https://doi.org/10.6028/nist.ir.8228)>. Acesso em 14/03/2023.

DURAES, Wellington; FERREIRA, Fernando Henrique Inocêncio Borba; MAZAN, Renato. **Arquitetura de soluções IoT: Desenvolva com Internet das Coisas para o mundo real**. Casa do Código, 2022. 80 p.

GSM ASSOCIATION. **CLP.11 – Panorama das diretrizes de segurança para IoT**. 2017. 45 p.

GSM ASSOCIATION. **CLP.13 – Diretrizes de segurança em IoT para o ecossistema de endpoints**. 2017. 90 p.

MICROSOFT. **IoT Signals**: summary of research learnings. 2019. 80 p. Disponível em: [https://azure.microsoft.com/mediahandler/files/resourcefiles/iot-signals/IoT-Signals-Microsoft-072019.pdf](https://azure.microsoft.com/mediahandler/files/resourcefiles/iot-signals/IoT-Signals-Microsoft-072019.pdf). Acesso em: 14/03/2023.

MORAES, Alexandre de; TAKASHI, Victor. **Segurança em IoT: Entendendo os riscos e ameaças em IoT**. São Paulo: Alta Books, 2021. 197 p.

NATIONAL INSTITUTE OF STANDARDS AND TECHNOLOGY. **NISTIR 8228**: Considerações para gerenciar Riscos de segurança cibernética e privacidade da Internet das Coisas (IoT). Gaithersburg: Nist, 2019. 44 p.

SINCLAIR, Bruce. **IoT: Como Usar a "Internet das Coisas" Para Alavancar Seus Negócios**. Autêntica Business, 2018. 272 p. Tradução de Afonso Celso da Cunha Serra.