
[[IoT Security]]

**Introdução**

O objetivo deste módulo é apresentar os riscos de segurança relacionados a IoT.

**Objetivos da aula**

- Apresentar os desafios de segurança na Iot;
- Compreender as ameaças e riscos do IoT;
- Descrever os riscos em IoT nas Interações do dispositivo com o mundo físico;
- Descrever os riscos em IoT nas operações de acesso, gerenciamento e monitoramento;
- Descrever os riscos em IoT em relação à disponibilidade, eficiência e segurança;
- Entender os desafios da segurança no endpoint.

**Resumo**

Como vimos, o principal componente de uma solução de IoT são os dispositivos de IoT implantados para detectar, medir, executar ações e gerar dados sobre seu ambiente. Analistas do setor previram que até 2025 teremos dezenas de bilhões de dispositivos conectados à Internet. A maioria desses dispositivos certamente serão dispositivos de baixa potência, com preços acessíveis, CPU menos potente, menos memória integrada, baixo consumo de energia e que geram pequenas quantidades de dados. Infelizmente, manter os dispositivos de baixo custo e lançá-los no mercado em um ritmo mais rápido também significa que esses dispositivos de baixa potência geralmente não são projetados com a segurança adequada. Ter dispositivos IoT não seguros conectados à Internet os expõe a ataques cibernéticos.

Figura 1

![Fonte: autoral](https://paperx-dex-assets.s3.sa-east-1.amazonaws.com/images/1680630934028-6TsTi4zZLq.png "Fonte: autoral")

Fonte: autoral

Para equilibrar essa balança, é importante aumentar a confiabilidade de um sistema IoT. Isso pode ser feito por meio de considerações dos cinco aspectos principais a seguir:

Figura 2

![Fonte: autoral](https://paperx-dex-assets.s3.sa-east-1.amazonaws.com/images/1680630961783-J5iHaFo2Dm.png "Fonte: autoral")

Fonte: autoral

1. **Segurança – _safety_:** O termo segurança aqui está associado à operação adequada dos sistemas IoT e/ou dispositivos IoT em relação ao risco de causar lesões físicas ou até mesmo a morte de seus operadores. No caso de dispositivos IoT, que podem ser implantados na comunidade, a possibilidade de que eles possam causar riscos à segurança é real.
2. **Resiliência**: característica de um sistema para se manter funcionando mesmo em condições diferentes das condições normais de operação.
3. **Confiabilidade**: refere-se à capacidade de um sistema IoT desempenhar suas funções durante todo o período de tempo definido em seu projeto.
4. **CiberSegurança**: proteção do sistema contra acesso não intencional ou não autorizado, alteração ou destruição. Em suma, garantir o CID: confidencialidade, integridade e disponibilidade.
5. **Privacidade:** sistemas IoT têm forte relação com dados, inclusive dados pessoais. Aqui a preocupação é o tratamento adequado dos dados em relação à privacidade, especialmente dos dados pessoais de forma a garantir os direitos dos titulares em relação à LGPD.

**Ameaças e riscos da IoT**

A avaliação de risco é o primeiro passo para a identificação e mitigação de ameaças. É um procedimento bem conhecido no mercado de segurança da informação, e não é diferente quando pensamos em IoT. De acordo com a GSM Association (2017), as seguintes perguntas devem orientar o processo de avaliação de risco:

Que recursos (digitais ou físicos) precisam ser protegidos?

- Que grupos de pessoas (tangíveis ou intangíveis) são potenciais agentes de ameaças?
- O que se caracteriza como uma ameaça para a organização?
- O que é uma vulnerabilidade?
- Qual seria o resultado se um recurso protegido fosse comprometido?
- Qual a probabilidade de o recurso ser comprometido?
- Qual seria o resultado em um contexto com diferentes grupos de hackers?
- Qual é o valor do recurso para a organização e seus parceiros?
- Qual é a relevância do recurso que está sendo comprometido na segurança?
- O que pode ser feito para remediar ou mitigar a possibilidade de vulnerabilidade?
- Como novas ou emergentes lacunas na segurança podem ser monitoradas?
- Quais riscos não podem ser resolvidos e o que eles significam para a organização?
- Que orçamento deve ser aplicado para a resposta a incidentes, monitoramento e redução de risco?

Assim, o objetivo principal de uma avaliação de risco é orientar a criação de um conjunto de políticas, procedimentos e controles que possam corrigir, monitorar e responder aos problemas de segurança e ameaças identificadas na organização (GSM Association, 2017).

Existem alguns modelos de referência que podem ser utilizados para um processo de avaliação de riscos, como a estrutura de gerenciamento de riscos do National Institute of Standards and Technology (NIST) e o modelo OCTAVE do Computer Emergency Response Team (CERT).

**Riscos em IoT**

**1. Riscos nas Interações do dispositivo com o mundo físico**

Dispositivos IoT têm uma grande interação com o mundo físico, diferentemente dos dispositivos de TI convencionais. Consequentemente, há riscos envolvidos nessa maior interação. Assim, devem ser tratados os seguintes pontos:

- Gerenciamento da qualidade dos dados;
- Dados dos sensores, podem ter incertezas, de forma que é importante um gerenciamento eficaz garantir sua exatidão e qualidade antes analisar os dados;
- Cuidado com dados pessoais, uma vez que os sensores podem estar coletando dados sensíveis e revelando informações indevidas, além de os dados levarem a tomada de decisões equivocadas;
- Cuidado especial com atuadores, que podem trazer danos reais no mundo físico;
- Deve-se avaliar a qualidade e significado dos dados;
- Deve-se buscar formas de mitigar ataques físicos à tecnologia dos sensores e atuadores, especialmente:
- Ataques à comunicação sem fio
- Adulteração de dados
- Acesso indevido
- Danificação de equipamentos e instalações
- Ataques DOS
- Roubo de dados
- Acesso não autorizado aos ambientes físicos
- Confidencialidade, integridade e disponibilidade
- Em IoT, Disponibilidade e a integridade podem ser mais importantes do que a confidencialidade devido ao impacto potencial no mundo físico.
- Um invasor **que pode exibir os dados armazenados** ou transmitidos do dispositivo IoT pode não obter nenhuma vantagem ou valor com isso.
- Mas um invasor **que pode alterar** os dados pode disparar uma série de eventos que causam um incidente.

**2. Recursos de acesso, gerenciamento e monitoramento dos dispositivos**

Dispositivos IoT não podem ser acessados, gerenciados ou monitorados da mesma forma que os dispositivos de TI convencionais, uma vez que são dispositivos que fornecem pouca ou nenhuma visibilidade sobre seu funcionamento, seu status e dados sobre sua composição. Ou seja, os dispositivos IoT podem ter limitações quanto aos dados para gerenciamento e monitoramento. Alguns dos desafios neste quesito seriam:

- **Falta de recursos de gerenciamento**, o que leva à impossibilidade de gerenciar plenamente o firmware, SO e apps:
- Adquirir, verificar a integridade, instalar, configurar, armazenar, recuperar, executar, encerrar, remover, substituir, atualizar e corrigir software.
- Software de um dispositivo IoT pode ser reconfigurado automaticamente quando ocorre um evento adverso, como uma falha de energia ou uma perda de conectividade de rede.
- **Falta de interfaces** de usuário, de aplicativos e/ou humanos para uso e gerenciamento de dispositivos:
- Como solicitar o consentimento dos usuários sobre o processamento de suas informações pessoais?
- Falta de padrões universalmente aceitos para interfaces de aplicativos IoT, para:
- Formatação de dados
- Emissão de comandos
- Interoperabilidade
- **Dificuldade no Gerenciamento em escala,** por falta de suporte a mecanismos de gerenciamento centralizado, em função da variedade de softwares, que leva a:
- Dificuldade no gerenciamento do **ciclo de vida** do dispositivo IoT
- Gerenciamento de **configuração**
- Gerenciamento de **atualização e patches**
- **Diferentes expectativas de tempo de vida,** gerando diferenças entre a expectativa do cliente e a expectativa do fabricante quanto à:
- Segurança – vulnerabilidades sem patchs
- Falta de suporte
- Confiabilidade
- **Gestão do Hardware**
- Dificuldade de Inventário
- Heterogeneidade do parque
- Hardware não reparável

**3. Disponibilidade, Eficiência e Segurança** dos recursos de segurança cibernética e privacidade geralmente são diferentes para dispositivos IoT do que para dispositivos de TI convencionais, devido a:

- Uso de dispositivos IoT “caixa preta”
- Há registro de eventos de segurança e privacidade?
- É possível acesso aos registros de eventos?
- Efetividade e desempenho
- Criptografia forte?
- Autenticação MFA?
- Atrasos x segurança
- Impossibilidade de instalação de soluções de terceiros
- Capacidade de processamento
- Esforço excessivo para gerenciamento, proteção e monitoramento, em função da existência de dispositivos IoT sem suporte à funcionalidade de gerenciamento centralizado, levando à necessidade de:
- Implantação de mecanismos de proteção de cada dispositivo, levando à uma configuração complexa pela diversidade e limitações de cada dispositivo;
- Busca de uma solução de mercado para proteger os dispositivos IoT, especialmente nos gateways IoT;
- Verificar adequação dos sistemas de proteção convencionais ao ambiente IoT, analisando:
- Protocolos diversos para comunicação e como se dá a comunicação entre dispositivos.
- Adequação da solução à realidade e limitação dos dispositivos IoT:
- É necessária a proteção de dados em repouso?
- Proteção das interações com o mundo físico?

**4. Desafio da segurança no endpoint,** que acaba sendo impactado e diretamente relacionado às características específicas de cada dispositivo IoT, como:

- Baixo consumo de energia, para aumentar a vida útil do endpoint e por, em muitos casos, o equipamento ser instalado em local inacessível ou remoto. Além disso, a fonte de alimentação deve ser permanente e pode ser limitada, como o uso de energia solar
- Limitação na capacidade de processamento e baixa largura de banda, o que pode inviabilizar algumas _features_ de segurança, como o uso de algoritmos de criptografia avançada.
- Equipamentos de baixo custo, baixa capacidade de processamento, pouca memória e Sistema Operacional simples e limitado.
- Pode ser um requisito de negócio que o endpoint tenha uma vida longa útil, maior que 10 anos, o que gera as seguintes questões:
- Como fazer com que as features de criptografia e segurança sejam duradouras, uma vez que o poder de processamento aumenta 16 vezes em 10 anos?
- Durante o ciclo de vida do endpoint, o poder de processamento do endpoint permanece o mesmo.
- Como tratar e corrigir adequadamente as vulnerabilidades?

A figura 3 mostra os desafios ao tratar a segurança do endpoint: 

Figura 3

![Fonte: autoral](https://paperx-dex-assets.s3.sa-east-1.amazonaws.com/images/1680631879269-HM5NWyZ9Ya.png "Fonte: autoral")

Fonte: autoral

**Classificação dos endpoints**

Os endpoints podem ser classificados de acordo com suas capacidades e complexidade de construção. Teríamos então:

**Endpoint de baixa complexidade**

- Principais características
- Simples, com poucas funções, para coleta de métricas e indicadores
- Utilização de CPU de baixa capacidade
- Baixo custo
- Utilização de protocolo de comunicação de curta distância, como PAN, Bluetooth Low Energy, Threa ou Zigbee
- Uso de gateway para funções mais complexas
- Recursos de segurança limitados
- Baixa potência, privilegiando o baixo consumo de energia
- Exemplos
- Dispositivos Wearables
- Sensores para segurança residencial
- Sensores de proximidade

**2) Endpoint de alta complexidade**

- Características
- Conexão direta com o servidor backend
- Utilização de protocolo de comunicação de média e longa distância, como rede Celular, Wifi e Ethernet por meio de um Gateway CPE
- Trabalha com uma unidade de processamento mais robusta
- Melhores recursos de segurança, como criptografia de chave compartilhada (PSK) e Trusted Computing Base - TCB
- TCB é um conjunto de hardware, software e protocolos que **garantem a integridade do endpoint**, fazendo a autenticação mútua e comunicação segura.
- Possuem fonte de alimentação AC ou bateria com sistema de recarga
- Exemplos
- Sistemas de iluminação
- Eletrodomésticos
- Sistemas de controle industrial
- Veículos conectados

Além dos dispositivos IoT, temos também o gateway, que é um hub centralizado, que conecta dispositivos e sensores IoT à computação e processamento de dados baseados em nuvem. Os gateways IoT modernos geralmente permitem o fluxo de dados bidirecional entre a nuvem e os dispositivos IoT. As principais características do Gateway em relação à segurança seriam:

- Fonte de alimentação dedicada
- Gerenciamento da comunicação entre endpoints de baixa complexidade e backend
- Gerenciamento de links de longa distância, como Celular, Satélite, conexões por cabo de cobre e fibra, redes Ethernet
- Roteamento de mensagens, recebendo comandos do backend e enviando para os endpoints
- Outras funções como descoberta de dispositivos, implantação do driver de rede no dispositivo, gerenciamento e monitoramento, autenticação e segurança e maior poder de processamento.
- Tipos de gateways:
- Gateway de Serviço, que seria um hub para conectar os endpoints entre si;
- Gateway CPE, que funciona com um roteador de banda larga para os endpoints.

**Conteúdo bônus**

**Tópicos avançados**

Um processo de avaliação de risco de um ecossistema IoT é uma parte importante da gestão de risco, que visa identificar, analisar e avaliar os riscos que podem afetar a segurança, a privacidade e a confiabilidade dos dispositivos conectados e dos ambientes em que eles são implantados. Um processo de avaliação de risco de um ecossistema IoT baseado nas normas ISO segue as diretrizes da ISO/IEC 30141:2018, que fornece uma arquitetura de referência harmonizada para o Internet of Things (IoT), incluindo princípios, modelos e terminologias comuns.

Um processo de avaliação de risco de um ecossistema IoT baseado nas normas ISO envolve as seguintes etapas:

- **Definir o escopo e os critérios da avaliação**: isso inclui estabelecer o contexto do ecossistema IoT, os objetivos da avaliação, os critérios para avaliar a significância dos riscos e os recursos necessários para realizar a avaliação.
- **Identificar os riscos**: isso consiste em identificar as fontes, causas, eventos e consequências potenciais dos riscos que podem afetar o ecossistema IoT, considerando os aspectos técnicos, organizacionais e regulatórios.
- **Analisar os riscos**: isso envolve estimar a probabilidade e o impacto dos riscos identificados, considerando as medidas existentes para controlá-los ou mitigá-los.
- **Avaliar os riscos:** isso implica comparar os níveis de risco com os critérios definidos anteriormente e priorizar os riscos que requerem atenção ou tratamento.
- **Comunicar e consultar**: isso significa envolver as partes interessadas relevantes no processo de avaliação de risco, compartilhar informações sobre os resultados da avaliação e obter feedbacks.

Algumas técnicas para realizar a avaliação de risco podem ser encontradas na norma IEC 31010:2019, que fornece orientação sobre a seleção e aplicação de técnicas para avaliar o risco em uma ampla gama de situações. Algumas dessas técnicas são:

- **Análise SWOT**: uma técnica para identificar as forças (strengths), fraquezas (weaknesses), oportunidades (opportunities) e ameaças (threats) relacionadas ao ecossistema IoT.
- **Análise FMEA**: uma técnica para identificar as falhas potenciais nos componentes ou funções do ecossistema IoT, seus modos (formas), causas e efeitos nas operações ou nos requisitos do usuário.
- **Análise Bow-tie**: uma técnica para analisar as relações entre causas, eventos iniciadores, barreiras preventivas ou mitigadoras.

Referência Bibliográfica

BOECKL, K. et al. **Considerations for managing Internet of Things (IoT) cybersecurity and privacy risks**. National Institute of Standards and Technology. 2019. Disponível em: <[https://doi.org/10.6028/nist.ir.8228](https://doi.org/10.6028/nist.ir.8228)>. Acesso em 14/03/2023.

DURAES, Wellington; FERREIRA, Fernando Henrique Inocêncio Borba; MAZAN, Renato. **Arquitetura de soluções IoT: Desenvolva com Internet das Coisas para o mundo real**. Casa do Código, 2022. 80 p.

GSM ASSOCIATION. **CLP.11 – Panorama das diretrizes de segurança para IoT**. 2017. 45 p.

MICROSOFT. **IoT Signals: summary of research learnings**. 2019. 80 p. Disponível em: [https://azure.microsoft.com/mediahandler/files/resourcefiles/iot-signals/IoT-Signals-Microsoft-072019.pdf](https://azure.microsoft.com/mediahandler/files/resourcefiles/iot-signals/IoT-Signals-Microsoft-072019.pdf). Acesso em: 14/03/2023.

MORAES, Alexandre de; TAKASHI, Victor. **Segurança em IoT: Entendendo os riscos e ameaças em IoT**. São Paulo: Alta Books, 2021. 197 p.

NATIONAL INSTITUTE OF STANDARDS AND TECHNOLOGY. **NISTIR 8228**: Considerações para gerenciar Riscos de segurança cibernética e privacidade da Internet das Coisas (IoT). Gaithersburg: Nist, 2019. 44 p.

SINCLAIR, Bruce. **IoT: Como Usar a "Internet das Coisas" Para Alavancar Seus Negócios**. Autêntica Business, 2018. 272 p. Tradução de Afonso Celso da Cunha Serra.