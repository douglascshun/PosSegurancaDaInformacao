[]
**Introdução**

O objetivo deste módulo é apresentar as peculiaridades das redes e nuvem para suporte à IoT.

**Objetivos da aula**

- Apresentar os Recursos e Princípios de Segurança de Rede IoT;
- Descrever os processos de Identificação e autenticação no ecossistema IoT;
- Identificar os Canais de Comunicação Seguros;
- Discutir a Disponibilidade de canais;
- Entender o processo de Gerenciamento de endpoints e gateways;
- Revisar outras medidas de segurança.

**Resumo**

Podemos entender que é responsabilidade do provedor de serviços de soluções IoT aplicar e manter um processo de avaliação de risco e implementar técnicas e procedimentos de segurança da informação para proteger os dados e a privacidade do ecossistema IoT, especialmente dos titulares. Tal responsabilidade engloba também as operadoras de rede e telecomunicações, responsáveis pela comunicação dentro de uma solução IoT. A figura 1 ilustra as responsabilidades de cada ator em um ecossistema IoT:

Figura 1

![Fonte: autoral](https://paperx-dex-assets.s3.sa-east-1.amazonaws.com/images/1680637447065-tftfeYqVVX.png "Fonte: autoral")

Fonte: autoral

Os ataques à infraestrutura de rede e nuvem pode ter vários impactos no ecossistema IoT, como:

- **Impacto físico**, como o acionamento retardado ou falha no acionamento programado dos endpoints IoT - o que pode causar danos, inclusive letais, especialmente em ambientes críticos com atuadores – e a violação da privacidade física, dando ao agente mal-intencionado acesso indevido a residências e instalações industriais.
- **Impacto cibernético**, violando os princípios da confidencialidade, integridade, disponibilidade e autenticação.
- **Impacto na vida cotidiana** dos beneficiários e usuários da IoT, que fazem uso de plataformas das áreas de saúde, financeira e de segurança.

Para evitar esses impactos, alguns princípios de segurança de rede devem ser respeitados pelos provedores e operadoras:

- Identificação e autenticação
- **Identificação**: que deve fornecer identificadores únicos para as entidades dentro do serviço de IoT e correlacionar essas identidades eletrônicas com identidades reais e juridicamente vinculativas;
- **Autenticação**: confirmação da identidade das entidades participantes do ecossistema IoT;
- **Boas práticas:** IMSI, ICCID, EID ou IMEI (celular). Uso do UICC para identificar de forma segura o endpoint. Single sign-on.
- Controle de acesso, para todas as entidades que participam do ecossistema IoT, aplicando sempre as políticas de menor privilégio e segregação de tarefas.
- Proteção de dados, objetivando garantir a segurança (confidencialidade, integridade, disponibilidade, autenticidade) e privacidade das informações da rede para o serviço de IoT.
- Processos e mecanismos para garantir a disponibilidade com segurança de recursos de rede e protegê-los de ataques, como por exemplo, a utilização de firewall apropriado, prevenção de intrusão e tecnologias de filtragem de dados.

**Recomendações para um ecossistema IoT Seguro**

Podemos agrupar as recomendações para garantir a segurança IoT em algumas categorias, descritas a seguir:

- **Segurança de Hardware**, categoria que concentra recomendações para projetar dispositivos IoT com base no conceito Root of Trust (RoT). Uma RoT é uma unidade que consiste em um mecanismo de computação, código de baixo nível e dados (por exemplo, chaves criptográficas). Ele fornece serviços/recursos de segurança necessários para estabelecer confiança e segurança dentro da plataforma da qual faz parte. A RoT tem dois fundamentos basilares: imutabilidade e previsibilidade, ou seja, os resultados produzidos devem ser consistentes para os mesmos dados de entrada. A implementação em hardware de uma RoT permite o cumprimento dessas condições.

Assim, a Root of Trust pode fornecer os seguintes serviços de segurança independentes - identificação, autenticação, confidencialidade, integridade e medição (estado da plataforma), bem como serviços compostos (dependendo dos independentes) - autorização, verificação, relatórios, armazenamento seguro e atualizar. Principais características:

- Utilização de Raiz de Confiança de Hardware **imutável** (HWRoT—Trust Anchor) — um componente confiável que estende a cadeia de confiança para outros componentes de hardware, firmware e softwares.
- Hardware com recursos de segurança - Bloqueio de memória, Armazenamento de chaves criptográficas, Inicialização segura, Autenticação de dispositivo, Confidencialidade e integridade de comunicação)
- Medidas para proteção e detecção de violação no dispositivo
- Gerador de número aleatório de qualidade (baseada em hardware), para utilização em processos de criptografia.

**Gestão de confiança e integridade,** concentrando os requisitos para estabelecimento de confiança e garantia de integridade, fundamentais para manter a segurança do dispositivo IoT. Para isso, deve-se considerar um processo de inicialização seguro baseado uma raiz de confiança inerentemente confiável e imutável (em hardware, Hardware Root of Trust - HWRoT) como a âncora de confiança, a partir da qual a confiança é estendida a toda a plataforma por meio de um processo de inicialização seguro, verificando o código executado para garantir que o ambiente está em um estado esperado e não comprometido. O software deve ser assinado e verificado na instalação ou execução, com a capacidade de restauração para o último estado seguro conhecido. Deve-se ter um rígido controle de instalação de software em sistemas operacionais (SO).

**Proteção de dados e Design de Software**, englobando as recomendações sobre tratamento de dados, além dos princípios da arquitetura de software. Como regra fundamental, a confidencialidade dos dados deve ser protegida por criptografia. Além disso, o processo de desenvolvimento de software deve garantir que os aplicativos que processam dados tenham apenas os privilégios mínimos para tal, e que sejam isolados uns dos outros, aplicando técnicas como a compartimentalização da memória. É importante, também, ter a possibilidade de bloquear ou apagar remotamente o conteúdo do dispositivo.

**Configuração do dispositivo e atualização de software**, pois não ter ou aplicar correções de vulnerabilidade identificadas, acaba deixando os dispositivos à mercê de ameaças mais recentes, sendo um grande risco de segurança na IoT. O dispositivo deve ter suporte à atualização do software com segurança, obrigatoriamente por uma entidade autorizada, preferencialmente de forma automática – ativada por padrão – e/ou remotamente. O arquivo de atualização deve ser criptografado e assinado, de forma que o dispositivo possa verificar sua integridade antes da aplicação. A verificação de atualização deve ser em intervalos frequentes, mas irregulares e deve manter compatibilidade com versões anteriores de atualizações e não alterar as configurações das interfaces e protocolos de rede. Por fim, a atualização não deve alterar as preferências configuradas pelo usuário, nem as configurações de segurança e/ou privacidade.

**Interfaces e comunicações seguras**, englobando as diretrizes e boas práticas sobre comunicação segura, incluindo as interfaces do dispositivo, protocolos utilizados, e os dados. A utilização das interfaces do dispositivo deve ser configurável – de forma a permitir a desabilitação ou limitação lógica de acesso a qualquer interface local e de rede – e, por padrão, apenas as obrigatórias devem estar ativas. Os sistemas devem utilizar protocolos de segurança padronizados e de última geração, com ênfase, se existente, no uso das versões destinadas a IoT. Preferencialmente, o dispositivo não deve possuir interfaces de depuração, diagnóstico ou teste que possam ser exploradas. Quanto à segurança dos protocolos, deve-se utilizar somente protocolos de segurança padronizados e atuais, com autenticação mútua e somente devem ser aceitas conexões intencionais. Os dispositivos devem notificar e/ou solicitar uma confirmação do usuário ao emparelhar, integrar e/ou conectar-se. Por fim, em relação à segurança de dados, deve-se garantir sempre os pilares da segurança da informação - confidencialidade, integridade e disponibilidade – para os dados transmitidos.

**Monitoramento e registro de eventos de segurança cibernética**, como um requisito fundamental para o ter um nível de gerenciamento de segurança adequado para todo o ecossistema IoT. Deve-se gerar detalhes suficientes para permitir a resolução de problemas criados por incidentes de segurança, de forma a minimizar o impacto e a exposição de informações confidenciais. Para que os logs sejam confiáveis, deve-se garantir a confidencialidade e a integridade desses registros e somente entidades autorizadas devem ter acesso para análise. A modificação dos arquivos de log deve ser proibida para qualquer entidade. O registro deve conter eventos de segurança do Hardware, Firmware e Software. As mensagens de erro devem fornecer/exibir informações concisas e necessárias, sem expor informações confidenciais. Os dispositivos devem ser monitorados constantemente e ter seu funcionamento comparado com um baseline para permitir a detecção de anomalias.

**Uso de criptografia e processos de Gerenciamento de Chaves**, sendo recomendável o uso de algoritmos criptográficos padronizados e com eficiência comprovada, por meio de implementações seguras e comprimentos de chave suficientes para garantir um nível mínimo de segurança. As implementações devem ser revisadas de forma independente, considerando também o desempenho do algoritmo, uma vez que os dispositivos têm recursos limitados. Deve-se considerar a capacidade de alterar o algoritmo ou usá-lo apenas com uma chave mais longa, em caso de comprometimento do dispositivo. Uma política de gerenciamento de chaves segura e escalável deve ser aplicada no sistema IoT – geração, armazenamento, distribuição e revogação de chaves -, de forma que cada dispositivo IoT tenha uma chave privada exclusiva. Essa abordagem faz com que o comprometimento de um dispositivo não afete todo o ecossistema.

**Identificação do dispositivo, autenticação e forte segurança padrão**, que define que o dispositivo deve possuir identificadores físico e lógico exclusivos acessíveis somente por entidades devidamente autorizadas, uma vez que, geralmente, irá operar em um grande ecossistema. O dispositivo também deve ser protegido contra acesso indesejado e ter mecanismos de segurança para os dados do usuário. Quanto ao desenvolvedor de software e ao usuário, esta categoria inclui orientações sobre gerenciamento de senhas e procedimentos gerais de autenticação. O dispositivo também deve ter esquemas robustos de autenticação e autorização, obrigando a sua identificação inequívoca e mútua, por meio de senhas e chaves fortes e individuais por dispositivo. Para evitar ataques de força bruta ou outros ataques abusivos de login, deve-se limitar o número de tentativas de login, por meio de atrasos de novas tentativas ou uso de autenticação multifator (MFA). E como regra geral, a configuração de segurança deve ser a mais forte possível, privilegiando o conceito de Security by default.

**Conteúdo bônus**

**Tópicos avançados**

Uma infraestrutura de rede e cloud de um ecossistema de serviços IoT (Internet das Coisas) é responsável por conectar dispositivos, coletar e processar dados e fornecer serviços aos usuários finais. Essa infraestrutura é essencial para garantir o funcionamento correto de um sistema IoT, mas também apresenta várias vulnerabilidades que podem ser exploradas por atacantes cibernéticos. Algumas dessas vulnerabilidades incluem:

- Senhas fracas ou padrões de autenticação inseguros: muitas infraestruturas de IoT utilizam senhas padrão ou previsíveis, o que torna mais fácil para os atacantes descobrirem e acessarem as informações do sistema.
- Ataques de negação de serviço (DDoS): ataques DDoS podem ser usados para sobrecarregar a infraestrutura de rede e cloud do sistema IoT, tornando-o inoperante.
- Falhas na configuração de segurança: muitos sistemas IoT não têm as configurações de segurança adequadas, o que pode levar à exposição de informações confidenciais e ataques maliciosos.
- Falhas de segurança em dispositivos: os dispositivos IoT conectados à infraestrutura também podem ter vulnerabilidades que podem ser exploradas por atacantes cibernéticos.

Para mitigar os riscos de ataques em infraestruturas de rede e cloud de sistemas IoT, é importante adotar medidas de segurança efetivas, como:

- Utilização de criptografia de dados para proteger as informações transmitidas entre os dispositivos e a infraestrutura de rede e cloud.
- Implementação de políticas de segurança adequadas para a gestão de senhas e acesso à infraestrutura.
- Atualização regular dos dispositivos e softwares utilizados pelo sistema IoT.
- Utilização de ferramentas de segurança de rede, como firewalls, para monitorar e bloquear possíveis ataques.

Alguns exemplos de ataques em infraestruturas de rede e cloud de sistemas IoT incluem:

- Ataque à empresa Dyn: em 2016, a empresa de gerenciamento de DNS (Sistema de Nomes de Domínios) Dyn foi alvo de um ataque DDoS, que tornou inoperante vários sites populares, como o Twitter e o Spotify. O ataque foi realizado por meio de uma rede de dispositivos IoT infectados com o malware Mirai.
- Ataque ao sistema de controle de tráfego de uma cidade: em 2019, um ataque de ransomware comprometeu o sistema de controle de tráfego de uma cidade na Austrália. O ataque levou ao fechamento de semáforos e causou congestionamentos em várias vias.
- Ataque à infraestrutura de cloud da Capital One: em 2019, a Capital One, uma das maiores empresas de cartão de crédito nos Estados Unidos, sofreu um ataque cibernético que expôs informações confidenciais de mais de 100 milhões de clientes. O ataque foi realizado por meio da exploração de uma vulnerabilidade na infraestrutura de cloud da empresa.

Esses exemplos destacam a importância de adotar medidas de segurança efetivas em infraestruturas de rede e cloud de sistemas IoT para garantir a proteção dos dados e a continuidade dos serviços oferecidos.

**Referência Bibliográfica**

BOECKL, K. et al. **Considerations for managing Internet of Things (IoT) cybersecurity and privacy risks**. National Institute of Standards and Technology. 2019. Disponível em: <[https://doi.org/10.6028/nist.ir.8228](https://doi.org/10.6028/nist.ir.8228)>. Acesso em 14/03/2023.

DURAES, Wellington; FERREIRA, Fernando Henrique Inocêncio Borba; MAZAN, Renato. **Arquitetura de soluções IoT: Desenvolva com Internet das Coisas para o mundo real**. Casa do Código, 2022. 80 p.

GSM ASSOCIATION. **CLP.11 – Panorama das diretrizes de segurança para IoT**. 2017. 45 p.

GSM ASSOCIATION. **CLP.14 – Diretrizes de segurança em IoT para Operadoras de Rede**. 2017. 32 p.

MICROSOFT. **IoT Signals**: summary of research learnings. 2019. 80 p. Disponível em: [https://azure.microsoft.com/mediahandler/files/resourcefiles/iot-signals/IoT-Signals-Microsoft-072019.pdf](https://azure.microsoft.com/mediahandler/files/resourcefiles/iot-signals/IoT-Signals-Microsoft-072019.pdf). Acesso em: 14/03/2023.

MORAES, Alexandre de; TAKASHI, Victor. **Segurança em IoT: Entendendo os riscos e ameaças em IoT**. São Paulo: Alta Books, 2021. 197 p.

NATIONAL INSTITUTE OF STANDARDS AND TECHNOLOGY. **NISTIR 8228**: Considerações para gerenciar Riscos de segurança cibernética e privacidade da Internet das Coisas (IoT). Gaithersburg: Nist, 2019. 44 p.

SINCLAIR, Bruce. **IoT: Como Usar a "Internet das Coisas" Para Alavancar Seus Negócios**. Autêntica Business, 2018. 272 p. Tradução de Afonso Celso da Cunha Serra.