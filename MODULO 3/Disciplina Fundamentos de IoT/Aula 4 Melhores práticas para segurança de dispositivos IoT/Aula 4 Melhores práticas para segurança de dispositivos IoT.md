[[IoT Security]]

**Introdução**

O objetivo deste módulo é apresentar as boas práticas em relação à segurança de IoT.

**Objetivos da aula**

- Apresentar os Princípios de arquitetura de Segurança IoT;
- Discutir a Segurança das operações de IoT;
- Entender os aspectos de Segurança do Usuário Final;
- Entender os aspectos de Segurança de Apps;
- Entender os aspectos de Segurança de Rede;
- Entender os aspectos de Segurança de Endpoint**.**

**Resumo**

A ISO (International Organization for Standardization) e IEC (International Electrotechnical Commission) formam um sistema especializado para padronização mundial. O padrão ISO/IEC 30141 propõe uma arquitetura de referência para a Internet das Coisas, abordando os sistemas IoT sob várias perspectivas: modelos conceituais, de sistema, de domínio, de rede, funcional e ecossistema de serviço intersetorial. O padrão ISO/IEC 30141 – Internet of Things (IoT) traz ainda uma avaliação de vulnerabilidades de segurança no domínio da entidade física e no domínio de detecção e controle, ou seja, o domínio dos dispositivos IoT. Neste último, a avaliação se dá nos seguintes aspectos: (i) o sistema operacional e de gestão; (ii) o sistema de recursos e intercâmbio; (iii) o sistema de serviço de aplicativos; e (iv) o domínio do usuário IoT. A figura a seguir ilustra esses conceitos:

Figura 1

![Fonte: ISO/IEC 30141:2018: Internet of Things (IoT) — Reference Architecture, 2018. Disponível em: https://www.iso.org/standard/65695.html. Acesso em: 22 mar. 2023.](https://paperx-dex-assets.s3.sa-east-1.amazonaws.com/images/1680633257752-eQ3tuVcghD.png "Fonte: ISO/IEC 30141:2018: Internet of Things (IoT) — Reference Architecture, 2018. Disponível em: https://www.iso.org/standard/65695.html. Acesso em: 22 mar. 2023.")

Fonte: ISO/IEC 30141:2018: Internet of Things (IoT) — Reference Architecture, 2018. Disponível em: [https://www.iso.org/standard/65695.html](https://www.iso.org/standard/65695.html). Acesso em: 22 mar. 2023.

É quase impossível garantir que não haja vulnerabilidades em uma solução de IoT. Existem vulnerabilidades na arquitetura da solução IoT e os hackers tentarão explorar suas fraquezas. Contudo, a partir da arquitetura de referência abordada na aula 1, vários princípios-chave de segurança podem ser considerados para orientar a segurança nas soluções de IoT. Assim, a segurança IoT deve ser considerada para os seguintes domínios:

- Camada de dispositivo IoT, que busca melhorar a segurança dos endpoints;
- Camada de comunicações/transporte, focando na segurança das comunicações entre dispositivos e em todo o ecossistema IoT;
- Camada de serviços em nuvem, considerando a segurança na plataforma de serviços IoT;
- Camada de usuário e aplicativos, melhorando a segurança para o usuário final e nos aplicativos que permitem a interação do usuário com o ecossistema IoT;
- Camada de processos de negócios, focando no compliance regulatório e legal.

A figura 2 ilustra a relação entre a arquitetura IoT apresentada na aula 1 com esses domínios de segurança: 

Figura 2 - Arquitetura IoT e domínios de segurança

![Fonte: autoral](https://paperx-dex-assets.s3.sa-east-1.amazonaws.com/images/1680634659712-BKACiHgLoi.png "Fonte: autoral")

Fonte: autoral

**Segurança das Operações de IoT**

Além da cibersegurança no nível técnico na rede, dispositivos, plataforma de nuvem e camadas de transporte, deve-se considerar também partes importantes, se não críticas, da garantia de segurança de uma solução de IoT: os aspectos de negócios, pessoas e processos.

Nesse sentido, a identificação das partes interessadas é um dos aspectos que deve ser considerado. Uma solução de IoT geralmente é composta por várias tecnologias, produtos e serviços e geralmente é uma parceria de vários participantes do ecossistema. Assim, uma solução de IoT precisaria considerar as seguintes partes interessadas:

- Fornecedor de dispositivos IoT, um provedor confiável de dispositivos IoT, que precisam estar em conformidade com um conjunto de requisitos de segurança;
- Provedor de serviços de conectividade, uma operadora e fornecedora de um serviço de conectividade para conectar dispositivos IoT a uma plataforma IoT central;
- Provedor de plataforma IoT, que poderia ser um SaaS, IaaS ou PaaS. Exemplos disso incluem plataforma de análise, plataforma de IA, banco de dados, plataforma de visualização, configuração de dispositivos e plataforma de gerenciamento.
- Demais partes interessadas, envolvidas no fornecimento de uma solução de IoT. O número de partes interessadas e o nível de seu envolvimento podem variar de acordo com o modelo de negócios adotado.

Indo além, é importante tratar a segurança para garantir a continuidade das operações dos negócios, ou seja, verificar a capacidade de uma organização responder rapidamente a um incidente de segurança. É preciso responder adequadamente algumas perguntas: como sua organização responderia a um incidente de segurança? Existe um plano de gerenciamento de riscos?

Nesse sentido, podemos novamente nos basear em padrões, recomendações e práticas recomendadas do setor. Dentre as várias opções, uma das mais implantadas é o modelo do National Institute of Standards and Technology (NIST). A estrutura de segurança cibernética do NIST, é formada por cinco funções principais:

**1. Identificar**

Esta função busca identificar e desenvolver uma compreensão abrangente de todos os aspectos de sua organização, como contexto de risco de segurança, recursos, riscos relacionados à segurança cibernética, governança de dados, gerenciamento de ativos e estratégias de gerenciamento de riscos.

**2. Proteger**

Função que tem como objetivo desenvolver e implementar salvaguardas apropriadas para garantir a prestação de serviços. A função dá suporte para minimizar o impacto de eventos de segurança cibernética por meio de gerenciamento de identidade, controle de acesso e segurança de dados.

**3. Detectar**

Aqui temos a função responsável por descobrir e identificar eventos de segurança cibernética. Facilita a detecção oportuna desses eventos por meio de anomalias e monitoramento contínuo.

**4. Responder**

Após a detecção de qualquer evento de segurança, esta função deve utilizar métodos adequados para minimizar o impacto do incidente nas operações de negócios. Isso pode incluir planejamento de resposta, estratégias de comunicação e análise estruturada.

**5. Recuperar**

Função responsável pelo desenvolvimento de planos de resiliência e implementação de restauração oportuna de serviços e capacidades prejudicadas por incidentes de cibersegurança.

A figura 3 consolida esses conceitos.

Figura 3

![Fonte: Fábio Correa Xavier, adaptado do NIST Cyber Security Framework](https://paperx-dex-assets.s3.sa-east-1.amazonaws.com/images/1680634795053-gtdpd2KthC.png "Fonte: Fábio Correa Xavier, adaptado do NIST Cyber Security Framework")

Fonte: Fábio Correa Xavier, adaptado do NIST Cyber Security Framework

**Segurança do Usuário Final**

A segurança do usuário final foca sua atenção aos usuários de uma solução ou aplicativo de IoT. Nesse sentido, a conscientização dos usuários sobre a necessidade de seguir os procedimentos de segurança apropriados é fator fundamental para garantir um nível adequado de segurança para todo o ecossistema IoT, de forma que os usuários sejam autenticados e acessem as informações com segurança. De maneira objetiva, a segurança do usuário final deve tratar:

- **Segurança Operacional**, definindo procedimentos de segurança para operação dos dispositivos IoT;
- **Segurança da Informação**, contemplando a Autenticação, Autorização, Confidencialidade, Integridade, Disponibilidade;
- **Identificação dos usuários finais**, que pode incluir a equipe técnica, as partes interessadas na solução de negócios, o suporte e administração do sistema ou seus contratados.

**Segurança de Apps e plataformas**

A segurança de aplicativos (apps) e plataformas de IoT deve tratar três elementos: (i) a proteção dos dados em seus 3 diferentes estados: em trânsito, em repouso ou em processamento; (ii) a segurança de acesso ao aplicativo, que envolve a proteção de segurança do perímetro de cada um dos aplicativos dentro de uma plataforma; (iii) a segurança de software e firmware, garantindo a integridade do software e hardware de vários aplicativos na plataforma.

E quais os pontos de atenção em uma plataforma IoT? A segurança da plataforma IoT pode ser bastante ampla, pois a definição de plataforma IoT pode variar de acordo com as funções, bem como com as ofertas do fornecedor. As plataformas IoT podem ter um ou todos esses conjuntos de funções, gerenciamento de conectividade, gerenciamento de dispositivos, habilitação de aplicativos e habilitação de inteligência. O gerenciamento de conectividade se preocupa, principalmente, com o gerenciamento de conectividade e gerenciamento de sessão. O gerenciamento de dispositivos envolve provisionamento, configuração e gerenciamento de dispositivos. A habilitação de aplicativos torna os dados de IoT acessíveis a sistemas e usuários externos. A capacitação de inteligência diz respeito a tornar a solução de IoT verdadeiramente inteligente por meio da aplicação de tecnologias de habilitação, como AI, Machine Learning, Deep Learning, Blockchain e assim por diante.

**Segurança de Rede**

Um dos protocolos da camada de transporte mais comuns em aplicações IoT é o MQTT - _Message Queuing Telemetry Transport_. O MQTT, que já era comum em aplicações IoT industriais, está sendo implementado em produtos domésticos inteligentes. A maioria dos dispositivos inteligentes é conectada a um hub central inteligente em casa ou na empresa, para fins de comunicação. Esse hub inteligente, geralmente, é implementado com software de automação que possui rotinas lógicas, que acionam determinadas ações quando uma condição é atendida. O MQTT, geralmente, é implementado em todos os produtos inteligentes, e o hub inteligente serve como um dispositivo intermediário, que recebe todas as mensagens MQTT de dispositivos inteligentes.

Em relação à conectividade nas camadas física e de enlace, há uma grande variedade de soluções de conectividade disponíveis, que conectam dispositivos IoT a plataformas IoT, como Wi-Fi, Bluetooth, LoRaWAN, Sigfox, redes celulares. A segurança na camada de conectividade, às vezes, pode não ser clara, dependendo do tipo de rede de conectividade. Se uma solução de IoT usar Cat-M1 ou NB-IoT, a conectividade e a segurança dependerão do provedor de rede celular. Na maioria dos casos, as redes Cat-M1 e NB-IoT têm seu próprio mecanismo de segurança e os dados são transportados por meio de um canal VPN seguro de dispositivos IoT para uma plataforma IoT. Isso faz com que uma rede celular seja, em princípio, mais segura do que muitas outras opções de rede de comunicação sem fio, especialmente se estiverem implantados com a possibilidade de identificação do assinante ou cartões SIM, que aproveitam a cifragem de hardware e as trocas de chaves criptografadas para garantir a autenticação entre o dispositivo e a rede celular, como 3G e 4G.

Contudo, ainda existem riscos de segurança que precisam ser resolvidos, como sinais de telefone celular bloqueados, ataques do tipo _man-in-the-middle,_ por meio de estações base desonestas capazes de interceptar dados, adulteração física de dispositivos IoT, software infectado com malware.

**Segurança de endpoint**

Grande parte dos dispositivos IoT são para consumidores finais, ou seja, para uso pessoal ou doméstico. A tendência é que o número de dispositivos aumente a cada ano, de forma que todos os produtos no futuro, especialmente os produtos de consumo, tenham a possibilidade de conexão com a Internet. Nesse cenário, os consumidores apenas irão ligar o produto e esperar que ele funcione de maneira adequada, sem precisar configurá-lo, deixando o equipamento vulnerável e um alvo perfeito para ataques cibernéticos.

Nesse sentido, é preciso endereçar algumas perguntas, quando se fala em segurança do endpoint:

- Como evitar a clonagem do endpoint? Ou seja, como diferenciar os dispositivos legítimos fabricados pelo provedor de serviços de IoT daqueles que são reproduções ou cópias?
- **Garantir a autenticação da Identidade do Endpoint**
- Implementar uma base de computação confiável (Trusted Computing Base - TCB), que pode ser definido como um conjunto de hardware, software, protocolos e políticas que deve definir o ambiente adequado para que uma aplicação possa ser executada de forma confiável, segura e com alta qualidade.
- Utilizar uma âncora de confiança, ou seja, um certificado ou sistema baseado em chave pública para autenticar entidades de plataforma de computação em uma organização.
- Usar uma senha segura, complexa, longa e com caracteres especiais.
- Usar uma API segura para a TCB, de forma que toda verificação de assinatura seja verificada pela TCB e que nenhuma chave privada seja exposta. A TCB deve controlar todo o processo de criptografia.
- Usar um gerador confiável de números aleatórios, em caso de necessidade
- Aplicar os conceitos de Confidencialidade e Integridade na âncora de confiança
- **Implementar mecanismos de autenticação mútua entre dispositivos e serviços**
- Como minimizar os riscos de ataque a âncora de confiança?
- **Fazer a validação da segurança da cadeia de fornecedores da solução**
- Antes de colocar o endpoint em produção, personalizar a configuração de segurança do dispositivo, especialmente com ativação de identidades exclusivas de criptografia para cada dispositivo; deve-se, ainda, garantir que um dispositivo seja ativado, atualizado e associado a uma identidade específica do ecossistema onde será instalado.
- Aplicar os conceitos de privacidade e utilizar identificadores únicos para cada endpoint.

3. Como reduzir a possibilidade de falsificação do endpoint?

- Utilizar o modelo criptográfico PFS - Perfect Forward Secrecy, no qual as chaves produzidas para comunicação entre as partes são temporárias.
- Bloquear o acesso às áreas críticas da memória do dispositivo.

4. Como impedir a falsificação de serviços ou pares?

- Utilizar somente protocolos seguros nas comunicações no endpoint.
- Utilizar o modelo criptográfico PFS - Perfect Forward Secrecy, no qual as chaves produzidas para comunicação entre as partes são temporárias.
- Verificar se o TCB é realmente capaz de gerar números aleatórios para garantir que o processo de verificação criptográfica seja adequado. Se isso não for garantido, os dados criptografados podem se tornar previsíveis, o que vai enfraquecer a segurança.
- Verificar detalhadamente as configurações de utilização de atualizações sem fio - over the air (OTA).
- Implementar mecanismos de autenticação mútua entre dispositivos e serviços.
- Impedir a coleta não autorizada de metadados.

5. Como impedir a falsificação de firmware e software?

- Implantar uma plataforma de execução mínima viável, que permita o roll-back de aplicação, definindo a quantidade mínima de configurações para garantir um ambiente de execução minimamente confiável.
- Utilizar somente imagens de aplicações criptograficamente assinadas, pois todas as aplicações que estão fora da EEPROM principal de uma CPU devem ser autenticadas com criptografia.
- Bloqueio de acesso às áreas críticas de memória (read-only), como inicializadores e TCB, de forma a proteger o equipamento contra aplicações nocivas ou comprometidas.
- Não utilizar nunca carregadores de inicialização (boot loaders) inseguros ou desconhecidos.

6. Como reduzir a possibilidade de execução remota de códigos maliciosos?

- Bloqueio de acesso às áreas críticas de memória (read-only), como inicializadores e TCB, de forma a proteger o equipamento contra aplicações nocivas ou comprometidas.
- Fazer uma gestão forte das atualizações _over the air,_ especialmente em caso de falhas.
- Rodar aplicativos com níveis apropriados de privilégios, sempre configurando o menor privilégio possível.
- Utilizar a segregação de tarefas na arquitetura de aplicativos.
- Revisar e aplicar as otimizações de segurança no nível do sistema operacional e na interface de usuário.
- Auditar sempre os códigos de terceiros.

7. Como detectar endpoints comprometidos?

- Monitorando e identificando anomalias no comportamento do dispositivo.

**Conteúdo bônus**

**Tópicos avançados**

A norma ISO 65695, também conhecida como ISO/IEC 30141:2018, é a primeira norma internacional que fornece uma arquitetura de referência harmonizada para o Internet of Things (IoT), incluindo princípios, modelos e terminologias comuns. Ela usa uma abordagem de cima para baixo, começando com a coleta das características mais importantes do IoT, abstraindo-as em um modelo conceitual genérico do IoT, derivando uma referência baseada em sistema de alto nível com subsequente dissecção desse modelo em cinco visões de arquitetura de diferentes perspectivas. A norma tem como objetivo facilitar o desenvolvimento, implantação e operação de sistemas IoT seguros, confiáveis e interoperáveis, bem como promover a inovação e a colaboração no domínio do IoT.

As cinco visões de arquitetura do IoT são: visão empresarial, visão funcional, visão operacional, visão técnica e visão de informação. Cada uma dessas visões descreve um aspecto diferente do sistema IoT e seus requisitos. A visão empresarial define os objetivos estratégicos e os benefícios esperados do sistema IoT. A visão funcional descreve as funções principais e os fluxos de informação entre as entidades do sistema IoT. A visão operacional especifica os processos operacionais e as responsabilidades dos participantes do sistema IoT. A visão técnica detalha os componentes técnicos e as interfaces do sistema IoT. A visão de informação modela os dados gerados e consumidos pelo sistema IoT.

A norma ISO 65695 também define um conjunto de protocolos e padrões que suportam a comunicação entre as entidades do sistema IoT. Esses protocolos e padrões abrangem diferentes camadas da pilha tecnológica do IoT, desde a camada física até a camada aplicacional. Alguns exemplos desses protocolos e padrões são: MQTT, CoAP, HTTP/HTTPS, WebSocket, Bluetooth Low Energy (BLE), Zigbee, LoRaWAN, IPv6 over Low-Power Wireless Personal Area Networks (6LoWPAN), Constrained Application Protocol (CoAP), Lightweight Machine-to-Machine (LwM2M), OneM2M.

Uma explicação detalhada da norma ISO 65695 pode ser encontrada no documento oficial da norma disponível no site da ISO.

**Perfect Forward Secrecy**

O Perfect Forward Secrecy (PFS) é um protocolo de criptografia que garante que as chaves de criptografia utilizadas em uma comunicação sejam únicas e efêmeras, ou seja, uma chave diferente é gerada para cada sessão de comunicação e nunca é reutilizada. Isso impede que um invasor possa acessar o conteúdo de uma comunicação anterior, mesmo que tenha tido acesso à chave de criptografia.

O PFS é importante para a segurança em um ecossistema IoT, porque muitos dispositivos IoT são vulneráveis a ataques, como sniffing, interceptação de tráfego e injeção de pacotes, que podem expor informações confidenciais e comprometer a privacidade dos usuários. Ao utilizar o PFS, a comunicação entre dispositivos IoT e servidores é protegida por uma camada adicional de segurança, que torna muito mais difícil para um invasor interceptar e decifrar o conteúdo da comunicação.

A implementação do PFS em um ecossistema IoT pode ser realizada por meio do uso de algoritmos de criptografia que suportem a geração de chaves efêmeras e a troca de chaves segura. Um exemplo de protocolo de criptografia que suporta o PFS é o Transport Layer Security (TLS), que é amplamente utilizado para proteger as comunicações na Internet.

Para implementar o PFS em um ecossistema IoT, é necessário seguir as diretrizes estabelecidas pelas normas ISO, como a ISO/IEC 27001, que define os requisitos para um sistema de gestão de segurança da informação. Além disso, também é recomendável seguir as melhores práticas de segurança, como o uso de certificados digitais, a autenticação de usuários e dispositivos, a implementação de políticas de segurança adequadas e a realização de testes de segurança regulares para identificar possíveis vulnerabilidades.

Referência Bibliográfica

BOECKL, K. et al. **Considerations for managing Internet of Things (IoT) cybersecurity and privacy risks**. National Institute of Standards and Technology. 2019. Disponível em: <[https://doi.org/10.6028/nist.ir.8228](https://doi.org/10.6028/nist.ir.8228)>. Acesso em 14/03/2023.

DURAES, Wellington; FERREIRA, Fernando Henrique Inocêncio Borba; MAZAN, Renato. **Arquitetura de soluções IoT: Desenvolva com Internet das Coisas para o mundo real**. Casa do Código, 2022. 80 p.

GSM ASSOCIATION. **CLP.11 – Panorama das diretrizes de segurança para IoT**. 2017. 45 p.

GSM ASSOCIATION. **CLP.13 – Diretrizes de segurança em IoT para o ecossistema de endpoints**. 2017. 90 p.

MICROSOFT. **IoT Signals**: summary of research learnings. 2019. 80 p. Disponível em: [https://azure.microsoft.com/mediahandler/files/resourcefiles/iot-signals/IoT-Signals-Microsoft-072019.pdf](https://azure.microsoft.com/mediahandler/files/resourcefiles/iot-signals/IoT-Signals-Microsoft-072019.pdf). Acesso em: 15/03/2023.

MORAES, Alexandre de; TAKASHI, Victor. **Segurança em IoT: Entendendo os riscos e ameaças em IoT**. São Paulo: Alta Books, 2021. 197 p.

NATIONAL INSTITUTE OF STANDARDS AND TECHNOLOGY. **NISTIR 8228**: Considerações para gerenciar Riscos de segurança cibernética e privacidade da Internet das Coisas (IoT). Gaithersburg: Nist, 2019. 44 p.

SINCLAIR, Bruce. **IoT: Como Usar a "Internet das Coisas" Para Alavancar Seus Negócios**. Autêntica Business, 2018. 272 p. Tradução de Afonso Celso da Cunha Serra.