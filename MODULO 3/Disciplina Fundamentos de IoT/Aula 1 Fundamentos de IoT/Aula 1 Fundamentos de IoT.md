[[IoT Security]]

**Introdução**

O objetivo deste módulo é apresentar os principais conceitos de IoT.

**Objetivos da aula**

- Apresentar uma visão Geral da IoT
- Apresentar as principais características da IoT
- Conhecer as iniciativas globais de arquitetura de referência de IoT
- Entender a arquitetura de Referência IoT
- Identificar os facilitadores para IoT
- Conhecer as oportunidades e impacto social da IoT

**Resumo**

A Internet das Coisas, ou IoT (Internet of Things) como a conexão via Internet de bilhões de objetos, dispositivos ou coisas com capacidades de detecção e/ou ação. Esses objetos IoT são configurados para coletar dados de seu ambiente e compartilhá-los com outros sistemas. A força da IoT surge quando os dados coletados pelos objetos são analisados, aprendidos e transformados em _insights_, que permitem a tomada de decisões baseadas em dados. Os dispositivos conectados à Internet podem ser acessados e controlados de qualquer lugar e a qualquer momento e, juntamente com as percepções derivadas dos dados coletados, a Internet das Coisas oferece aos negócios e às empresas um incrível poder de inovação.

Embora não haja uma definição padrão acordada do que é IoT, as seguintes definições de órgãos globais podem melhorar nossa compreensão do que seria a IoT:

**O Instituto Nacional de Ciência e Tecnologia, NIST**, define IoT como um conceito baseado na criação de sistemas que interagem com o mundo físico, usando entidades em rede, como sensores, atuadores, recursos de informação e pessoas.

A **União Internacional de Telecomunicações, ITU**, por outro lado, define a IoT como uma infraestrutura global para a sociedade da informação, permitindo serviços avançados, interconectando coisas físicas e virtuais com base em tecnologias de informação e comunicação interoperáveis existentes e em evolução, TIC.

De acordo com os **US Computer Emergency Response Team**, US-CERT, a Internet das Coisas refere-se a qualquer objeto ou dispositivo que envia e recebe dados automaticamente, através da internet. Esse conjunto de coisas em rápida expansão inclui tags, também conhecidas como rótulos ou chips, que rastreiam automaticamente objetos, sensores e dispositivos que interagem com pessoas e compartilham informações de máquina para máquina.

O **IETF, Internet Engineering Taskforce**, define a Internet das Coisas como a rede de objetos físicos ou coisas incorporadas com eletrônicos, software, sensores e conectividade, para permitir que os objetos troquem dados com o fabricante, operador e/ou outros dispositivos conectados.

Como você verá ao longo do curso, embora não haja uma definição única do que é IoT, destaco que a Internet das Coisas não é uma tecnologia. A IoT envolve ecossistemas complexos compostos por uma variedade de tecnologias, produtos e serviços. A IoT pode ser utilizada em muitos setores da indústria, desde cidades inteligentes, empresas de consumo e domésticas, automotivas e de transporte, até agricultura, saúde, cadeia de suprimentos, varejo, gerenciamento de frota e manufatura. Esse ecossistema IoT apresenta desafios e oportunidades para inovações. Há uma série de características fundamentais no ecossistema de IoT:

- **Endpoints IoT**: termo usado genericamente para denotar um "dispositivo" IoT capaz de detectar (ou seja, sensor) e/ou executar uma ação conforme instruído (atuador). Um endpoint IoT pode ser um sensor simples, um dispositivo autônomo com sensor/atuador e capacidade de comunicação, ou como uma “função” IoT incorporada em um dispositivo/máquina maior, como carros e eletrodomésticos.
- **Sensores/Atuadores**: principais componentes de construção de um dispositivo/objeto/coisa IoT, permitindo que ele gere e/ou monitore dados de seu ambiente.
- **Conectividade:** refere-se à atividade de comunicação entre dispositivos/endpoints IoT e a plataforma de serviços IoT. Há uma variedade de tecnologias de conectividade que podem ser aplicadas para se ter essa conectividade.
- **Geração/Compartilhamento de Dados:** Fundamental para o conceito de IoT, pois é o que agrega valor à solução.
- **Tecnologias facilitadoras:** Em geral, refere-se ao uso de tecnologias de computação em nuvem que oferecem vários serviços, como armazenamento, análises, aplicativos, SaaS, IaaS e XaaS. Especificamente, as tecnologias emergentes que desempenham papéis cada vez mais significativos para tornar a IoT mais valiosa são: Big Data Analytics, Inteligência Artificial, Machine Learning, Deep Learning e Blockchain.
- **Insights baseados em dados:** podemos afirmar que a principal razão por trás da implementação de qualquer solução de IoT em qualquer setor da indústria é o desejo de gerar valor para o negócio, seja para fins comerciais ou pessoais, usando informações coletadas para gerar insights ou executar alguma ação. O resultado disso pode vir na forma de melhoria de produtividade, ganhos de eficiência, automação de processos, redução de custos, melhoria da qualidade de vida, monitoramento de ativos valiosos e assim por diante.
- **Segurança:** embora não seja um resultado ou uma característica de um aplicativo IoT, a segurança cibernética (incluindo privacidade, proteção de dados pessoais, confiabilidade e resiliência) é fundamental para o sucesso comercial da IoT, bem como para manter a privacidade e segurança dos usuários finais. Uma IoT vulnerável à exploração da segurança cibernética, pode prejudicar toda a rede IoT, tornando o negócio inoperável.

**Arquitetura IoT**

Há várias iniciativas para a criação de uma arquitetura de referência IoT. A figura 01 mostra algumas delas:

Figura 01

![Fonte: autoral](https://paperx-dex-assets.s3.sa-east-1.amazonaws.com/images/1680628529661-PvP6862lr7.png "Fonte: autoral")

Fonte: autoral

Se olharmos com cuidado, podemos notar que há vários pontos em comum. Todas as arquiteturas identificam relações e responsabilidade para cada participante no ecossistema IoT. Há, ainda, componentes e camadas que tratam de segurança da informação, privacidade, segurança física, confiabilidade e outros aspectos, que devem ser considerados desde a concepção da solução.

De maneira geral, podemos identificar as seguintes camadas em uma arquitetura IoT:

**1. Indústria e negócios**

Essa camada destaca que qualquer solução de IoT deve ser vista como parte de um ecossistema maior em um determinado setor da indústria. Isso obriga a solução a considerar uma série de questões e preocupações relativas a leis locais, regulamentos, conformidade, segurança, aquisição, privacidade de dados, segurança e infraestrutura crítica. Além disso, como negócio, destaca o relacionamento e a colaboração entre o proprietário/operador da solução IoT e as partes interessadas que fornecem serviços ou produtos relacionados à solução.

**2. Usuários e aplicativos**

O objetivo central de uma solução de IoT é resolver determinados problemas para os beneficiários da solução. Essa camada obriga o proprietário da solução a entender e/ou definir quem são seus clientes reais. Uma solução de IoT pode ter vários tipos de usuários, e cada tipo de usuário pode ter diferentes requisitos de uso ou consumo.Por exemplo, uma solução de IoT pode incluir equipe técnica e de operações, usuários de negócios como gerenciamento, patrocinadores da solução e aqueles que realmente usam as soluções para ajudar a melhorar seu trabalho/vida.

**3. Plataforma de gerenciamento e ativação de IoT**

Essa camada trabalha fornecendo as seguintes funcionalidades: Processamento, armazenamento e análise de dados;          Rede e segurança; Gerenciamento e configuração de dispositivos; mecanismo de regras; log de eventos; gerenciamento de identidade; funções avançadas que envolvam inteligência artificial, aprendizado de máquina (A.I.) e blockchain; Gerenciamento da interface do usuário, gateway de API, segurança do usuário, portal da Web, aplicativos, visualização; Protocolos de comunicação e gerenciamento; Dispositivo IoT e gerenciamento de endpoint;

Esses recursos e funções são realizados por diferentes meios. Algumas dessas funções podem ser implantadas próximas aos dispositivos finais e gateway, o que geralmente é chamado de processamento/computação de borda ou Mobile Edge Computing (MEC). Outros são baseados em nuvem ou SaaS, como aprendizado de máquina, big data ou armazenamento.

**4. Comunicações**

A chave para o conceito de IoT é a comunicação entre os endpoints de IoT e a plataforma de IoT. Existem muitas tecnologias e protocolos diferentes que podem ser implementados. As tecnologias de conectividade incluem: Ethernet com fio; Curto alcance sem fio – WiFi, Bluetooth, RFID; Longo alcance sem fio – conhecido como LPWAN (Low Power Wide Area Networks), que inclui LoRaWAN, SigFox, NB-IoT/Cat-M1 (celular), Weightless, Ingenu, WiSUN; Celular – inclui NB-IoT/Cat-M1, LTE, Cat-1, 3G, GSM.

Alguns dos protocolos de comunicação mais comuns usados em implantações de IoT atualmente são: MQTT, CoAP, HTTP, UDP, TCP,SOAP.

**5. Dispositivos IoT**

Essa camada trata os endpoints, dispositivos ou coisas de IoT. Os dispositivos IoT podem ser sensores simples que monitoram uma coisa específica, como temperatura ou umidade. Outras coisas da IoT também podem ser um produto autônomo, como um rastreador pessoal, um dispositivo ODB, uma câmera conectada ou um brinquedo. Dispositivos ou funções de IoT também podem ser incorporados a um item doméstico, como uma máquina de lavar, uma geladeira, um veículo ou um ar-condicionado.

A figura 02 ilustra as 5 camadas da arquitetura IoT:

Figura 02

![Fonte: autoral](https://paperx-dex-assets.s3.sa-east-1.amazonaws.com/images/1680628603468-lVKxoXNDYk.png "Fonte: autoral")

Fonte: autoral

**Facilitadores para IoT**

A Internet das Coisas (IoT) emergiu nos últimos anos como uma importante fonte de inovação e um motor de crescimento para a economia global. Os avanços na tecnologia significaram que os custos de sensores, hardware eletrônico, CPU e memória diminuíram muito, e o poder de computação aumentou aos trancos e barrancos. Como resultado, vimos avanços tecnológicos na Internet, computação em nuvem, big data, inteligência artificial, tecnologia digital emergente como Blockchain e inovações em redes e conectividade com a Internet. Serviços baseados em nuvem, como SaaS, IaaS e PaaS, tornaram-se muito acessíveis. Isso criou um ambiente perfeito para a IoT.

De uma maneira geral, os seguintes avanços tecnológicos e tendências estão impulsionando o mercado IoT:

**1- Redução de custos**

Os avanços tecnológicos e a redução dos custos de eletrônicos, especialmente relacionados ao armazenamento, da CPU, de memória e sensores, impulsionaram o crescimento da IoT.

**2- Computação em Nuvem**

A computação em nuvem oferece serviços incluindo armazenamento, bancos de dados, redes, big data e inteligência artificial, sendo responsável pelo ritmo acelerado de inovações e economias de escala.

**3- Tecnologia de Conectividade**

Novas tecnologias de conectividade projetadas especialmente para comunicação de máquinas ajudaram a impulsionar a implantação de IoT industrial e empresarial. Eles incluem Low Power Wide Area Network, LPWAN, como SigFox, LoRaWAN, Weightless, Cellular, como Cat-M1, NB-IoT ou mesmo LTE, e Nano-Satellite IoT, liderado por empresas como Myriota, Fleet Space Technologies, e Hiber.

**4- Grande ecossistema**

A IoT está sendo adotada em todos os setores da indústria: consumo, automação residencial, cidades inteligentes, empresas, agricultura, mineração e transporte, apenas para citar alguns. As oportunidades e demandas do mercado criaram um grande e variado ecossistema global de IoT de fornecedores de hardware, produtos, provedores de serviços, desenvolvedores e fabricantes.

**Oportunidade de negócios da IoT**

Em um relatório de 2019 sobre estratégias para implantação de IoT podemos encontrar os principais motivos para adoção da tecnologia, na visão das empresas. O gráfico abaixo mostra essas razões:

Figura 03

![Fonte: https://azure.microsoft.com/mediahandler/files/resourcefiles/iot-signals/IoT-Signals-Microsoft-072019.pdf. acesso em 14/03/2023.](https://paperx-dex-assets.s3.sa-east-1.amazonaws.com/images/1680628700887-tF5isdUTeR.png "Fonte: https://azure.microsoft.com/mediahandler/files/resourcefiles/iot-signals/IoT-Signals-Microsoft-072019.pdf. acesso em 14/03/2023.")

Fonte: [https://azure.microsoft.com/mediahandler/files/resourcefiles/iot-signals/IoT-Signals-Microsoft-072019.pdf](https://azure.microsoft.com/mediahandler/files/resourcefiles/iot-signals/IoT-Signals-Microsoft-072019.pdf). acesso em 14/03/2023.

De uma maneira geral, podemos concluir que os principais benefícios comerciais da IoT seriam:

1. **Otimização de processos de negócios** – Processos de negócios otimizados significam melhores operações de negócios. Simplificando, os aplicativos de IoT geram dados valiosos que podem permitir que as organizações ajustem suas operações de negócios por meio de uma melhor tomada de decisão baseada em dados coletados pelos endpoints IoT.
2. **Manutenção preditiva** – O uso de IoT em conjunto com a Inteligência Artificial permite que uma organização detecte problemas antes que eles ocorram e possam interromper as operações de negócios. Por exemplo, a solução pode identificar algum problema que possa causar a parada de uma máquina em uma fábrica, um veículo de frota ou uma bomba de água. Com isso, vários benefícios são conseguidos pelas organizações, como: (i) Economia de custos; (ii) Fortalecimento da segurança no local de trabalho; (iii) Menor tempo de indisponibilidade; (iv) Maior qualidade de produtos e processos por meio de aprendizado de máquina e detecção de problemas, aumentando a satisfação do cliente; (v) Maior eficiência e rendimento.

**Impacto Social da IoT**

A Internet das Coisas traz, também, vários impactos positivos para a sociedade por meio de aplicações em diversos setores da indústria, como Cidades Inteligentes, Saúde, Casas Inteligentes e Transporte, entre outros. Alguns desses benefícios seriam:

1. **Meio Ambiente**: há diversas formas pelas quais os aplicativos de IoT podem impactar direta ou indiretamente nosso meio ambiente, como a redução da poluição dos veículos. O transporte inteligente é uma área em que muitos aplicativos de IoT – monitoramento de tráfego, veículos conectados, gerenciamento de frota e otimização de rotas de tráfego – podem contribuir para reduzir as emissões de carbono. Os sistemas inteligentes de gerenciamento de edifícios são outra área em que os aplicativos de IoT podem otimizar o consumo de energia e o uso de água, reduzindo assim o desperdício e o consumo desnecessário de energia.
2. **Cuidados com a saúde**: os dados gerados por dispositivos vestíveis para o consumidor de IoT, como Smartwatches, permitem que as pessoas tenham uma compreensão e acompanhamento mais efetivo de sua saúde.
3. **Segurança**: a IoT fornece tecnologias assistivas para apoiar pessoas vulneráveis, como idosos ou pessoas com demência ou autistas. Alguns exemplos incluem dispositivos domésticos inteligentes, dispositivos de rastreamento de localização pessoal para pessoas autistas e demência e dispositivos de alerta de segurança pessoal para trabalhadores solitários. No mercado doméstico inteligente, a IoT pode fornecer uma sensação de segurança por meio do monitoramento remoto.
4. **Conveniência/Automação**: em uma casa inteligente, muitas tarefas e atividades domésticas demoradas estão sendo automatizadas. Os sistemas de irrigação do jardim já podem ser automatizados. Indo além, a IoT oferece mais flexibilidade para controlar e alterar as configurações do sistema de qualquer lugar e a qualquer momento. Com as fechaduras inteligentes, não precisamos mais procurar as chaves, não precisamos estar em casa para abrir a porta e deixar as pessoas entrarem, e podemos ver quem está na porta antes de deixá-los entrar. Aplicativos de IoT, como estacionamento inteligente, nos permitem encontrar vagas de estacionamento disponíveis rapidamente.
5. **Educação**: os dispositivos IoT estão sendo usados para fornecer experiências interativas de causa e efeito para ajudar os alunos com uma maneira mais envolvente de aprender.

**Conteúdo bônus**

**Tópicos avançados**

Para que você tenha uma visão aprofundada sobre o ecossistema IoT, é importante recorrer a pesquisas de empresas de tecnologia. Nesse sentido, a Microsoft realizou uma pesquisa extensa sobre a IoT, para dar uma visão holística para a indústria, de todo o ecossistema envolvido em soluções IoT, trazendo insights, oportunidades e desafios para quem deseja trabalhar nesse mercado. O relatório da Microsoft é intitulado **_IoT Signals – Summary of Research Learnings 2019_** e está disponível gratuitamente na Internet.

Referência Bibliográfica

DURAES, Wellington; FERREIRA, Fernando Henrique Inocêncio Borba; MAZAN, Renato. **Arquitetura de soluções IoT: Desenvolva com Internet das Coisas para o mundo real**. Casa do Código, 2022. 80 p.

MICROSOFT. **IoT Signals**: summary of research learnings. 2019. 80 p. Disponível em: < [https://azure.microsoft.com/mediahandler/files/resourcefiles/iot-signals/IoT-Signals-Microsoft-072019.pdf](https://azure.microsoft.com/mediahandler/files/resourcefiles/iot-signals/IoT-Signals-Microsoft-072019.pdf) >. Acesso em: 14/03/2023.

MORAES, Alexandre de; TAKASHI, Victor. **Segurança em IoT: Entendendo os riscos e ameaças em IoT**. São Paulo: Alta Books, 2021. 197 p.

SINCLAIR, Bruce. **IoT: Como Usar a "Internet das Coisas" Para Alavancar Seus Negócios**. Autêntica Business, 2018. 272 p. Tradução de Afonso Celso da Cunha Serra.