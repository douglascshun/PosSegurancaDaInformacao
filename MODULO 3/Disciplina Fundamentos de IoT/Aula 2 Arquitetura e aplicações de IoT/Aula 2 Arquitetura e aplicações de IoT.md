[[IoT Security]]

**Introdução**

O objetivo deste módulo é apresentar os conceitos básicos sobre arquitetura e dispositivos IoT.

**Objetivos da aula**

- Discutir o ecossistema de serviços e endpoints;
- Compreender os desafios da IoT;
- Conhecer o relacionamento entre a IoT e a comunicação móvel;
- Apresentar os recursos dos dispositivos IoT;
- Apresentar algumas das aplicações mais comuns da IoT.

**Resumo**

A GSM Association (GSMA) publicou uma série de documentos tratando da IoT sob diferentes aspectos: do endpoint, das operadoras e da segurança.

Todos os documentos foram baseados em um modelo padrão de alto nível, ilustrado na figura 1:

Figura 1: Ecossistema IoT

![(Fonte: GSM ASSOCIATION. CLP.11 – Panorama das diretrizes de segurança para IoT. 2017. 45 p.)](https://paperx-dex-assets.s3.sa-east-1.amazonaws.com/images/1680628929289-lf3cmhfex9.png "(Fonte: GSM ASSOCIATION. CLP.11 – Panorama das diretrizes de segurança para IoT. 2017. 45 p.)")

(Fonte: GSM ASSOCIATION. CLP.11 – Panorama das diretrizes de segurança para IoT. 2017. 45 p.)

O ecossistema de serviços, mostrado na figura 1, representa o conjunto de serviços, plataformas, protocolos e todas as tecnologias necessárias para permitir a coleta de dados, a partir dos endpoints. O ecossistema de serviços faz a interface com os usuários, permitindo a coleta e envio de dados, e com a plataforma de serviços, armazenando e permitindo a análise no ambiente de servidores.

Já os ecossistemas de endpoints são compostos dos dispositivos finais e os gateways, que permitem a conexão do mundo físico com o mundo digital, utilizando atuadores e sensores que coletam e enviam dados por meio de redes de comunicação, com ou sem fio. Ou seja, os endpoints são os dispositivos que coletam métricas, enviam dados para o ecossistema de serviço, recebem instruções ou ações em resposta e podem até mesmo processar dados localmente.

**Desafios da IoT**

Com a explosão da internet, o mundo ficou cada vez mais conectado. Hoje não temos somente coisas conectadas: temos praticamente tudo conectado, inclusive nós mesmos! Esse fato, aliado a vários outros - o menor custo de componentes eletroeletrônicos, maior velocidade da rede, menor custo de conexão, baterias com maior durabilidade, mais serviços com maior integração – fez com que os desafios também aumentassem, proporcionalmente. Desta forma, é imperativo que os desafios da IoT sejam tratados, para que o seu crescimento não seja impactado.

Os principais desafios seriam:

**1- Disponibilidade**, ou seja, a garantia de acesso estável e constante ao ecossistema IoT, tratando especialmente:

- **A equidade das operadoras e tecnologias:** Como várias operadoras de comunicação móvel podem garantir o mesmo nível de segurança de rede quando os endpoints IoT passam entre uma rede/antena e outra?
- **A confiança da rede de comunicação:** Como garantir a confiança da rede de forma que os endpoints possam se comunicar efetivamente com os gateways e com o ecossistema de serviços?
- **A capacidade limitada dos endpoints:** Como garantir a segurança, dadas as limitações de capacidade de endpoints de baixa complexidade?

**2- Identidade**, de forma a garantir a autenticação mútua de dispositivos, serviços, clientes e usuários finais que operam o ecossistema, em especial:

- **A identificação segura do usuário,** é necessária a identificação do usuário na operação dos dispositivos? Há necessidade de associação do usuário ao dispositivo final?
- **A autenticação** de endpoints e serviços, de forma segura;
- **Gerenciamento de ameaças contra a identidade**, de forma que não seja possível que dispositivos falsos ou clonados possam imitar serviços e dispositivos autorizados, garantindo a proteção da identidade do endpoint contra adulteração ou manipulação;
- **A autorização**, como forma de garantir que um serviço tenha a devida autorização para acessar e controlar o endpoint.

**3- Privacidade**, sobretudo com a vigência da LGPD, de forma a proteger os dados pessoais e a privacidade dos indivíduos, levando em conta:

- **No endpoint,** se não é possível monitorar ou rastrear um indivíduo por meio dos identificadores IoT dos endpoints; se a identidade de um endpoint não está exposta indevidamente e se os dados IoT não podem ser associados a atributos físicos dos usuários;
- **O uso da criptografia,** para garantir a confidencialidade e integridade dos dados, bem como a atualização constante de chaves e algoritmos, se necessário;
- **As informações pessoais identificáveis ou dados pessoais,** verificando como os endpoints tratam esses dados pessoais, especialmente se o usuário tem o controle desse tratamento.

**4- Segurança**, garantindo a integridade e confidencialidade do ecossistema, com rastreabilidade e monitoramento constante, de forma a utilizar:

- **Privacy by design,** ou seja, incorporar as melhores práticas de segurança da informação desde a fase de projeto e concepção do produto ou serviço IoT.
- **Trusted Computing Base – TCB**, para garantir a utilização de uma base de software confiável e verificada;
- **Uma solução abrangente**, para garantir a segurança fim a fim no ecossistema IoT.

**IoT e a Comunicação Móvel**

As soluções de IoT são extremamente dependentes de tecnologias de conectividade. E com o avanço das tecnologias disponíveis, especialmente com o 5G, as redes móveis tendem a ser o padrão para conectividade no ecossistema IoT, pois são confiáveis, com alta disponibilidade, com segurança adequada e configurável e excelente custo-benefício.

Os protocolos de comunicação podem ser divididos em comunicações com fio e sem fio. Os protocolos de comunicação sem fio podem, ainda, serem subdivididos quanto ao alcance: curto, médio e longo alcance.

A figura 2 mostra os principais protocolos de comunicação sem fio de curto alcance:

Figura 2 - Protocolos de comunicação sem fio de curto alcance

![Fonte: autoral](https://paperx-dex-assets.s3.sa-east-1.amazonaws.com/images/1680629295784-tM9ciIkjav.png "Fonte: autoral")

Fonte: autoral

Da mesma forma, na figura 3 temos alguns protocolos de comunicação sem fio de médio alcance:

Figura 3

![Fonte: autoral](https://paperx-dex-assets.s3.sa-east-1.amazonaws.com/images/1680629348192-IEXCWKPQlL.png "Fonte: autoral")

Fonte: autoral

Por fim, os protocolos de comunicação sem fio de longo alcance seriam:

Figura 4

![Fonte: autoral](https://paperx-dex-assets.s3.sa-east-1.amazonaws.com/images/1680629412282-fC9HnveJC7.png "Fonte: autoral")

Fonte: autoral

Quanto aos protocolos com fio, os principais utilizados na IoT seriam:

Figura 5

![Fonte: autoral](https://paperx-dex-assets.s3.sa-east-1.amazonaws.com/images/1680630240681-hBybRlPufb.png "Fonte: autoral")

Fonte: autoral

Algumas tecnologias e características de redes sem fio de curto alcance:

1. Bluetooth: baixo consumo de energia com um número maior de nós e camada de aplicação padronizada.
2. Light-Fidelity (Li-Fi): semelhante ao Wi-Fi, mas usando _Visible Light Communication_ (luz visível), que gera maior largura de banda.
3. Near-field communication (NFC): comunicação com alcance de até 4 cm.
4. Identificação por radiofrequência (RFID - _Radio-frequency identification_): utiliza campos eletromagnéticos para ler dados armazenados em etiquetas embutidas.
5. Wi-Fi: Padrão de rede sem fio IEEE 802.11.
6. Zigbee: baseado no padrão IEEE 802.15.4, com baixo consumo de energia, baixa taxa de dados, baixo custo e alto _throughput_.
7. Z-Wave: protocolo de comunicação sem fio usado para automação residencial e aplicações de segurança.

Algumas tecnologias e características de redes sem fio de médio alcance:

- LTE-Advanced
- Alta velocidade para redes móveis.
- Maior taxa de transferência
- Menor latência
- 5G
- Grande número de dispositivos IoT, mesmo quando estão em movimento.
- Banda larga móvel aprimorada.
- Comunicações massivas de tipo de máquina.
- Comunicações ultra confiáveis ​​de baixa latência

Algumas tecnologias e características de redes sem fio de longo alcance:

Low-power wide-area networking (LPWAN)

- longo alcance
- taxa de dados baixa
- Baixo consumo de energia
- Baixo custo de transmissão
- Protocolos
- LoRaWan
- Sigfox
- NB-IoT, Weightless
- RPMA
- Very small aperture terminal (VSAT)
- Via satélite
- pequenas antenas parabólicas
- dados de banda estreita e banda larga

Já as redes com fio mais comuns são:

1) Ethernet

- Uso de pares trançados e links de fibra ótica
- Hubs ou switches

2) Power-line communication (PLC)

- Comunicação via rede elétrica para transportar energia e dados

**Recursos dos dispositivos IoT**

Um dispositivo IoT deve ter recursos ou funções próprias ou em conjunto com outros dispositivos para atingir seus objetivos. O dispositivo IoT é um equipamento de computação com pelo menos um transdutor (sensor ou atuador) e pelo menos um interface de rede. Os recursos podem ser divididos de forma macro nos seguintes itens:

**1. Recursos de transdutor,** que permitem a interação com o mundo físico, sendo a fronteira entre os ambientes digitais e físicos. Cada dispositivo IoT deve ter pelo menos um recurso de transdutor.

- **Características**
- Converte um tipo de energia em outro.
- Interação com o mundo físico.
- **Sensores**
- Detectam e convertem formas de energia em informações digitais. São capazes de coletar informações do mundo físico na forma de dados de medição. Alguns exemplos seriam a medição de temperatura, imagens radiográficas, sensoriamento óptico e detecção de áudio.
- **Atuadores**
- Recebe informações e emite alguma forma de energia física. Devem prover a capacidade de agir e atuar no mundo físico. Alguns exemplos seriam o acionamento de bobinas de aquecimento, entrega de choque elétrico cardíaco na área da saúde, fechaduras eletrônicas, operação de veículos aéreos não tripulados e braços robóticos.

**2. Recursos de Interface:** que fazem a interação entre dispositivos IoT e destes com o ecossistema IoT. O dispositivo IoT deve restringir o acesso lógico a interfaces locais e de rede – e a protocolos e serviços usados por essas interfaces – apenas a indivíduos, serviços e componentes de produtos de IoT autorizados. As interfaces podem ser subdivididas:

- **Interface de Aplicativo**
- Permite que outros dispositivos se comuniquem com um dispositivo IoT
- **Interface de usuário humana**
- Permite comunicação entre pessoas e IoT
- **Interface** **de Rede**
- Permite interação do IoT com uma rede de comunicação

**3. Recursos de Suporte,** que deve fornecem suporte a outros recursos de IoT, como

- Gerenciamento de dispositivos
- Segurança cibernética
- Privacidade

A figura 6 resume esses recursos dos dispositivos IoT: 

Figura 6

![Fonte: Adaptado de BOECKL, K. et al. Considerations for managing Internet of Things (IoT) cybersecurity and privacy risks. National Institute of Standards and Technology. 2019. Disponível em: <https://doi.org/10.6028/nist.ir.8228>. Acesso em 14/03/2023.](https://paperx-dex-assets.s3.sa-east-1.amazonaws.com/images/1680630618582-9gXy577HRZ.png "Fonte: Adaptado de BOECKL, K. et al. Considerations for managing Internet of Things (IoT) cybersecurity and privacy risks. National Institute of Standards and Technology. 2019. Disponível em: <https://doi.org/10.6028/nist.ir.8228>. Acesso em 14/03/2023.")

Fonte: Adaptado de BOECKL, K. et al. Considerations for managing Internet of Things (IoT) cybersecurity and privacy risks. National Institute of Standards and Technology. 2019. Disponível em: [https://doi.org/10.6028/nist.ir.8228](https://doi.org/10.6028/nist.ir.8228). Acesso em 14/03/2023.

**Aplicações comuns da IoT**

**1. Aplicação na Saúde**

Dados gerados por dispositivos vestíveis, como um smartwatch, permitem que as pessoas tenham uma melhor compreensão e possam monitorar sua saúde, com a possibilidade de compartilhamento com os médicos. A figura 7 mostra o ecossistema IoT para essa aplicação:

Figura 7

![Fonte: GSM ASSOCIATION. CLP.11 – Panorama das diretrizes de segurança para IoT. 2. 2017.](https://paperx-dex-assets.s3.sa-east-1.amazonaws.com/images/1680630676381-MBnqpMGHnD.png "Fonte: GSM ASSOCIATION. CLP.11 – Panorama das diretrizes de segurança para IoT. 2. 2017.")

Fonte: GSM ASSOCIATION. CLP.11 – Panorama das diretrizes de segurança para IoT. 2. 2017.

Outra aplicação na saúde seria para o monitoramento da glicose para pacientes diabéticos. Com um sensor afixado no paciente e um leitor que pode ser um equipamento específico ou um app no celular, é possível acompanhar instantaneamente o nível de glicose para que a dose de insulina possa ser melhor regulada. Além disso, esses dados podem ser compartilhados com o médico. As figuras 8 e 9 mostram essa solução de maneira macro:

Figura 8

![Fonte: o autor.](https://paperx-dex-assets.s3.sa-east-1.amazonaws.com/images/1680630704621-9gMpGFoIiU.png "Fonte: o autor.")

Fonte: o autor.

Figura 9

![Fonte: o autor.](https://paperx-dex-assets.s3.sa-east-1.amazonaws.com/images/1680630716261-ZCcyBOyzIJ.png "Fonte: o autor.")

Fonte: o autor.

**2. Aplicação na agricultura**

Dados gerados por rede de sensores na agricultura ajudam no monitoramento e automação do cultivo, coletando dados sobre temperatura, umidade, salinidade do solo, dentre outros. Dados de satélites com a previsão do tempo podem ser agregados a essa solução, além do uso de drones e telemetria de tratores. Assim, a irrigação, por exemplo, pode ser automatizada quando a umidade do solo estiver abaixo da adequada. As figuras 10 e 11 mostram o ecossistema IoT para essa aplicação:

Figura 10

![Fonte: o autor.](https://paperx-dex-assets.s3.sa-east-1.amazonaws.com/images/1680630764921-jYt1yPJ1Cw.png "Fonte: o autor.")

Fonte: o autor.

Figura 11

![Fonte: o autor.](https://paperx-dex-assets.s3.sa-east-1.amazonaws.com/images/1680630779803-rjNv5kjL7y.png "Fonte: o autor.")

Fonte: o autor.

**Conteúdo bônus**

**Tópicos avançados**

No meu artigo “**Como a tecnologia pode ajudar a melhorar a vida nas grandes metrópoles**”, publicado pela MIT Technology Review, eu trato como a tecnologia pode ajudar a melhorar a vida nas grandes metrópoles. O artigo aborda alguns dos desafios enfrentados pelos moradores urbanos, como congestionamentos, poluição do ar, desigualdade social e falta de serviços públicos. Ele também apresenta algumas das soluções que estão sendo desenvolvidas ou implementadas por pesquisadores, empreendedores e governos, como mobilidade inteligente, inclusão digital, agricultura urbana e governança participativa. Eu concluo o artigo refletindo como a tecnologia pode ser uma ferramenta poderosa para melhorar a qualidade de vida urbana, mas que também requer uma abordagem centrada no ser humano, que considere as necessidades e aspirações das pessoas que vivem nas cidades. Vale a pena dar uma olhada!

Referência Bibliográfica

BOECKL, K. et al. **Considerations for managing Internet of Things (IoT) cybersecurity and privacy risks**. National Institute of Standards and Technology. 2019. Disponível em: <[https://doi.org/10.6028/nist.ir.8228](https://doi.org/10.6028/nist.ir.8228)>. Acesso em 14/03/2023.

DURAES, Wellington; FERREIRA, Fernando Henrique Inocêncio Borba; MAZAN, Renato. **Arquitetura de soluções IoT: Desenvolva com Internet das Coisas para o mundo real**. Casa do Código, 2022. 80 p.

GSM ASSOCIATION. **CLP.11 – Panorama das diretrizes de segurança para IoT**. 2017. 45 p.

MICROSOFT. **IoT Signals**: summary of research learnings. 2019. 80 p. Disponível em: < [https://azure.microsoft.com/mediahandler/files/resourcefiles/iot-signals/IoT-Signals-Microsoft-072019.pdf](https://azure.microsoft.com/mediahandler/files/resourcefiles/iot-signals/IoT-Signals-Microsoft-072019.pdf) >. Acesso em: 14/03/2023.

MORAES, Alexandre de; TAKASHI, Victor. **Segurança em IoT: Entendendo os riscos e ameaças em IoT**. São Paulo: Alta Books, 2021. 197 p.

SINCLAIR, Bruce. **IoT: Como Usar a "Internet das Coisas" Para Alavancar Seus Negócios**. Autêntica Business, 2018. 272 p. Tradução de Afonso Celso da Cunha Serra.

[

Próxima aula

IoT sob ataque: visão geral

**Aula concluída**



](https://aulas.descomplica.com.br/pos/mba-em-seguranca-da-informacao-54164c/turma/iot-security/aula/iot-sob-ataque-visao-geral)