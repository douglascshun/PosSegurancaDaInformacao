[[IoT Security]]

**Introdução**

O objetivo deste módulo é identificar os modelos de segurança de endpoint.

**Objetivos da aula**

- Apresentar os principais desafios para a segurança de endpoint
- Descrever os tipos de ataques aos endpoints
- Entender a segurança mínima de endpoint
- Conhecer as recomendações de segurança no endpoint

**Resumo**

Como aumentar a segurança nos dispositivos IoT, dadas suas características e limitações?

Figura 1

![Fonte: autoral](https://paperx-dex-assets.s3.sa-east-1.amazonaws.com/images/1680636631759-2vPWcvB15N.png "Fonte: autoral")

Fonte: autoral

Para isso, devemos considerar os tipos de endpoints, descritos a seguir:

**Endpoints de Baixa Complexidade,** como um sensor ou dispositivo mais simples (interruptor de luz, wearables, tomadas ou fechaduras), que buscam têm um objetivo geralmente único e principalmente de coleta de métricas ao ecossistema IoT. As principais características seriam:

- Dispositivos simples, com poucas funções: métricas e indicadores
- CPU de baixa capacidade
- Equipamentos baratos
- Utilização de protocolo de comunicação de curta distância, como Bluetooth Low Energy (BLE) ou Zigbee
- Utilização de gateway para conexão ao ecossistema IoT
- Recursos de segurança limitados, em função da simplicidade de sua construção
- Baixa potência, com utilização de pilha, baterias pequenas ou energia solar.

**Endpoints de Alta complexidade,** com funções mais avançadas, como sistemas de iluminação avançados, eletrodomésticos, sistemas de controle indústria e veículos, com as seguintes caraterísticas:

- Podem possuir conexão direta com o servidor backend e todo o ecossistema IoT, seja por meio de um protocolo de comunicação de longa distância, como uma rede celular, ou uma rede Wi-Fi ou Ethernet via Gateway,
- São dispositivos que possuem uma unidade de processamento mais robusta;
- Melhores recursos de segurança

**Gateways,** dispositivos com maior poder de processamento que gerenciam a comunicação entre endpoints e os sistemas de back-end. Geralmente possuem fonte de alimentação dedicada. Algumas características adicionais seriam:

- Gerenciamento da comunicação entre endpoints de baixa complexidade (EBC) e backend
- Gerenciamento de links de longa distância
- Roteamento de mensagens
- Outras funções de descoberta e gestão de endpoints

**Tipos de ataques aos endpoints**

Nos endpoints, os tipos de ameaças que podem ser exploradas podem ser classificados em camadas, conforme mostrado na figura 2:

Figura 2

![Fonte: autoral](https://paperx-dex-assets.s3.sa-east-1.amazonaws.com/images/1680636681018-8PmDc5R4RK.png "Fonte: autoral")

Fonte: autoral

Os **ataques às comunicações de rede** são o primeiro passo e o mais simples em um ataque ao endpoint. Os objetivos são a captura de credenciais de login, de tokens de comunicação e identificadores, por meio da utilização de softwares como sniffers de rede e interceptação – como o ataque do tipo _man-in-the-middle_, no qual um agente mal-intencionado se colocar entre dois dispositivos que tentam se comunicar e intercepta as mensagens enviadas, permitindo que o atacante se passe por uma das partes legítimas.

Em seguida, o atacante mira a **identificação dos serviços de rede** que estão abertos. Para isso, utiliza técnicas como:

1. Reconhecimento, para fazer a detecção e o mapeamento, não autorizado, de serviços, softwares e vulnerabilidades.

2. Captura de mensagens na rede, para identificar se os dados utilizáveis estão acessíveis nas mensagens, para reduzir a quantidade de trabalho para extrair dados do próprio endpoint.

3. Exploração dos serviços vulneráveis, de forma a identificar se é possível acessar ou manipular o sistema operacional do endpoint pela rede de comunicação.

4. Envio de mensagens ao endpoint, para descobrir se é possível executar comandos ou obter acesso remoto ao console do sistema operacional (via SSH, Telnet). Para isso, pode fazer uso de credenciais roubadas na primeira etapa ou mesmo credenciais padrões.

5. Exploração de serviços Web, onde comandos podem ser injetados em scripts CGI (Common Gateway Interface) vulneráveis, que não tratam de forma adequada caracteres de controle nos campos de entrada disponibilizados para preenchimento pelo usuário do serviço, resultando na execução de código no sistema operacional local.

O **acesso ao terminal**, então, acaba sendo mais uma estratégia do que um ataque em si. Com esse acesso ao prompt de comando do terminal, o atacante obtém informações valiosas que podem ajudar o invasor. Contudo, esse tipo de ação requer o acesso físico ao endpoint, com a utilização de equipamentos adicionais, para se obter o acesso ao prompt de comando do dispositivo.

Caso o invasor tenha acesso ao dispositivo, mas não consiga o acesso ao prompt de comando, ele pode verificar vulnerabilidades no hardware. Para isso, é possível tentar alterar uma eventual mídia gravável que esteja presente no equipamento. Outra possibilidade é verificar se os dados criptográficos trafegam em texto claro e desprotegidos no barramento do hardware. Além disso, pode-se tentar injetar mensagens maliciosas no circuito de hardware de forma a alterar o sistema.

O tipo de ataque mais complexo seria tentar comprometer o chip do endpoint. Para isso, são necessárias ferramentas especializadas e um conhecimento técnico avançado para tentar extrair dados da EEPROM interna ou NVRAM, interceptar mensagens internas da SRAM ou executar uma análise Raio X ou engenharia reversa.

**Segurança mínima no endpoint**

Para garantir um nível mínimo de segurança no endpoint, se faz necessário verificar se algumas recomendações vitais estão implementadas, de forma a minimizar a chance de comprometimento do equipamento.

O primeiro passo seria a definição da Base de Computação Confiável (TCB – Trusted Computing Base). Uma TCB é o conjunto de hardware, software e protocolos que objetivam manter a integridade do endpoint. Para isso, há a autenticação mútua com redes pareadas e gerenciamento adequado da segurança das comunicações e das aplicações que rodam no endpoint. Para isso, a âncora de confiança - tecnologia de hardware protegido com a função de armazenar e processar senhas e chaves criptográficas - é a base do TCB. Bugs ou vulnerabilidades no TCB podem comprometer a segurança de todo o ecossistema. Por outro lado, falhas de segurança fora do TCB não devem ser capazes de vazar mais privilégios do que os concedidos a eles para o funcionamento do ecossistema. A figura 3 ilustra o conceito de TCB:

Figura 3

![Fonte: autoral](https://paperx-dex-assets.s3.sa-east-1.amazonaws.com/images/1680636714578-Vs79QYieP7.png "Fonte: autoral")

Fonte: autoral

De maneira esquematizada, podemos pensar o TCB da seguinte maneira:

**O que é?**

- Conjunto de hardware, software e protocolos que garantem a integridade do endpoint,
- Executa autenticação mútua com redes pareadas e gerencia a segurança das comunicações e das aplicações

**Funções principais**

- Validação de imagem do sistema operacional e aplicações, antes da execução;
- Autenticação mútua de redes pareadas, garantindo a segurança das comunicações;
- Separação de tarefas dentro da arquitetura de segurança em IoT;
- Provisionamento e personalização de forma a garantir uma identidade criptograficamente exclusiva para o endpoint;
- Segurança de ambiente isolado, como políticas e procedimentos para validar a autenticidade dos endpoints, além de garantir também a confidencialidade dos dados coletados e enviados para o back-end.

**Modelos de âncoras de confiança**

- Tecnologia de hardware seguro que armazena e processa senhas criptografadas;
- Texto Claro;
- Chave pré-compartilhada (PSK) – criptografia simétrica;
- Chave Pública/Privada (criptografia assimétrica).

**Por que é importante?**

- Garante que as comunicações entre a âncora de confiança, a aplicação principal e as redes pareadas sejam seguras, protegidas e atualizadas.

Quanto à âncora de confiança, podemos destacar:

**O que é?**

- Hardware seguro, um chip físico segregado ou um núcleo seguro dentro de uma CPU
- Capaz de armazenar e processar com segurança senhas criptografadas

**Funções principais**

- Determinar com segurança se as mensagens e identidades podem ser autenticadas
- Ser capaz de informar com segurança à TCB o resultado de todas as operações de autenticação ou criptografia.

**Por que é importante?**

- Minimiza a possibilidade de um invasor de roubar chaves relevantes para todo o ecossistema de IoT;
- Clonar identidades de endpoints;
- Falsificar serviços de IoT;
- Distribuir patches e atualizações não autorizadas;
- Fazer alterações não autorizadas no software do endpoint.

Outra recomendação para a segurança do endpoint, seria disponibilizar serviços para acessar as funções do TCB, por meio de uma API.

**O que é?**

- Serviço seguro disponibilizado para permitir o acesso às funções do TCB.

**Funções principais, garantir que**

- Toda verificação de assinatura é executada pela TCB;
- Nenhuma chave privada da TCB é exposta;
- A troca de chaves pode ser realizada pela TCB em nome da aplicação;
- A criptografia e descriptografia devem ser executadas pela TCB;
- A assinatura de mensagens deve ser executada na TCB;
- O preenchimento seguro de mensagens deve ser realizado na TCB;
- Confidencialidade e Integridade entre a TCB e a aplicação.

**Por que é importante?**

- Garantia de integridade do ecossistema.

Dentre as ameaças que podem afetar os endpoints, destacam-se:

**1. Falsificação (spoofing)**

Consiste no envio de pacotes falsificados para influenciar o funcionamento de um dispositivo (por exemplo, parar, iniciar ou modificar a coleta e a transferência de dados). Assim, um usuário pode ser direcionado para um site falsificado de um provedor de serviços.

**Baseline de segurança:**

- Implementar **gateways e firewalls** para identificar tráfego suspeito;
- Utilizar **âncoras de confiança** para oferecer suporte a identidade e acesso confiáveis ;
- **Atualizar e corrigir** dispositivos para impedir a exploração de vulnerabilidades;
- **Gerenciar a identidade** do dispositivo, para dar suporte aos privilégios de autorização e acesso de um dispositivo comprometido e ao provisionamento em fim de vida útil.

**2. Adulteração (Tampering)**

Consiste em modificar secretamente as permissões de compartilhamento de dados de um sensor. Pode também adulterar softwares para modificar permissões, instalar spyware ou malware.

**Baseline de segurança:**

- Gerenciamento forte e seguro de controles de acesso;
- Inicialização e atualização seguras para garantir que o software e o hardware sejam modificados por fontes confiáveis;
- Usar âncoras de confiança para apoiar o não repúdio;
- Monitorar o status do dispositivo e o fluxo de tráfego para identificar atividades não autorizadas.

**3. Repúdio**

Neste caso, os dados do sensor são modificados em trânsito para o serviço de nuvem e as métricas domésticas são afetadas. Por exemplo, o dispositivo A recebe um comando aparentemente do dispositivo B, mas ele foi enviado na verdade por uma fonte desconhecida e leva a um mau funcionamento. Isso também poderia ocorrer quando um grupo de usuários compartilha uma senha/processo de autenticação de grupo para acessar um sistema.

**Baseline de segurança:**

- Práticas recomendadas de segurança da informação – gerenciamento de controles de acesso de usuários individuais;
- Uso de certificados digitais para oferecer suporte à identidade segura de usuários e dispositivos;
- Uso de âncoras de confiança para apoiar o não-repúdio;
- Infraestrutura de chave pública para gerenciar e revogar certificados digitais e âncoras de confiança;
- Inicialização e atualização seguras para garantir apenas a modificação autorizada de software e hardware.

**4. Violação de dados (Divulgação não autorizada de Informação)**

- Acesso não autorizado a câmeras de segurança;
- Vazamentos de senha ou modificação não autorizada de senha/credencial;
- Captura de pacotes por meio de ataques man-in-the-middle ou de tipo semelhante.

**Baseline de segurança:**

- Separar redes domésticas da rede utilizada por dispositivos IoT;
- Adotar práticas recomendadas de gerenciamento de segurança da informação;
- Gerenciamento de autorização baseado em privilégios ou outro método com refinamento de permissões/privilégios;
- Utilizar criptografia de dados;
- Monitorar e auditar o tráfego dentro e fora da rede IoT local;
- Alertas para tráfego de dados suspeitos.

**5. Negação de Serviço (DOS - Denial of Service)**

- Uso de exploits em dispositivos conectados para interromper as funções normais dos sistemas conectados em um ecossistema IoT;
- Uso de exploits em dispositivos conectados para executar um ataque DoS ou DDoS em uma rede ou site de terceiros.

**Baseline de segurança:**

- Bloquear a comunicação de dispositivos fora da LAN ou da Página Inicial;
- Uso de gateways e firewalls para monitorar, gerenciar e bloquear o tráfego;
- Restringir o acesso às funções de comando/controle dos dispositivos;
- Tirar dispositivos comprometidos e irreparáveis do ecossistema de IoT com segurança.

**6. Elevação de Privilégio**

- Por meio de uma exploração de dia zero de dispositivo inteligente que permite que terceiros entrem na LAN, ou acesso não autorizado do sistema de um provedor de serviços em nuvem, permitindo o acesso às redes domésticas, para obter privilégios de alto nível que permitem o comando e controle de um endpoint.

**Baseline de segurança:**

- Separação das redes de usuários IoT e outras redes para desencorajar usuários privilegiados de acessar informações não relevantes;
- Gerenciamento de autorização de usuário baseado em privilégios ou outro granular para impedir o acesso a informações não necessárias, especialmente controles de endpoints;
- Gerenciamento do ciclo de vida e desativação de dispositivos antigos ou comprometidos.

**7. Falta de suporte para o correto gerenciamento do endpoint**

**Principais causas:**

- Dispositivos desatualizados com explorações ou bugs conhecidos sendo explorados para acessar redes ou dispositivos IoT;
- Dispositivos com software ou firmware desatualizados;
- Incapacidade de criptografar dados ou atribuir uma âncora de confiança;
- Incapacidade de gerenciar remotamente;
- Fim da vida útil do endpoint.

**Baseline de segurança:**

- Criar um ambiente seguro para esses dispositivos separados das redes de usuários;
- Monitorar o tráfego de dados e habilitar alertas para tráfego suspeito;
- Gerenciar autorização e acesso a dispositivos;
- Gerenciar fisicamente as atualizações ou enviar atualizações por push onde for possível.

**Recomendações de alta prioridade**

Além das configurações e recomendações anteriores, há outras que merecem a atenção de quem trabalha com IoT. As recomendações de alta prioridade são mostradas nas tabelas a seguir:

Figura 4

![Fonte: autoral](https://paperx-dex-assets.s3.sa-east-1.amazonaws.com/images/1680636908559-wqttHltkjQ.png "Fonte: autoral")

Fonte: autoral

Figura 5

![Fonte: autoral](https://paperx-dex-assets.s3.sa-east-1.amazonaws.com/images/1680636928552-9r9iuXq4xH.png "Fonte: autoral")

Fonte: autoral

Figura 6

![Fonte: autoral](https://paperx-dex-assets.s3.sa-east-1.amazonaws.com/images/1680636942883-NxqhN8tqXR.png "Fonte: autoral")

Fonte: autoral

Figura 7

![Fonte: autoral](https://paperx-dex-assets.s3.sa-east-1.amazonaws.com/images/1680636957944-ABCqkl2oiK.png "Fonte: autoral")

Fonte: autoral

Por fim, outras recomendações para aumentar a segurança dos endpoints e que merecem destaque seriam as seguintes:

Figura 8

![Fonte: autoral](https://paperx-dex-assets.s3.sa-east-1.amazonaws.com/images/1680636981599-XF6xIS9YJf.png "Fonte: autoral")

Fonte: autoral

![Fonte: autoral](https://paperx-dex-assets.s3.sa-east-1.amazonaws.com/images/1680636993069-hNmpZiaCbg.png "Fonte: autoral")

Fonte: autoral

Figura 10

![Fonte: autoral](https://paperx-dex-assets.s3.sa-east-1.amazonaws.com/images/1680637035500-rgkIlGFXQu.png "Fonte: autoral")

Fonte: autoral

Figura 11

![Fonte: autoral](https://paperx-dex-assets.s3.sa-east-1.amazonaws.com/images/1680637048421-X21XNSeCft.png "Fonte: autoral")

Fonte: autoral

**Conteúdo bônus**

**Tópicos avançados**

Os endpoints de um ecossistema IoT (Internet das Coisas) são os dispositivos que coletam dados, realizam análises e tomam decisões com base nas informações obtidas. Esses dispositivos incluem sensores, atuadores e outros dispositivos conectados à Internet.

Embora a Internet das Coisas ofereça muitos benefícios, como maior eficiência, produtividade e economia de custos, ela também apresenta muitas vulnerabilidades, que podem ser exploradas por atacantes cibernéticos, para acessar dados confidenciais ou controlar dispositivos. Algumas das vulnerabilidades mais comuns que podem ser exploradas em endpoints de um ecossistema IoT incluem:

- Senhas fracas ou padrões de autenticação inseguros: muitos dispositivos IoT possuem senhas padrão ou previsíveis, o que facilita o acesso não autorizado ao sistema.
- Falhas de segurança em dispositivos: dispositivos IoT podem possuir vulnerabilidades que permitem que um invasor assuma o controle desses dispositivos e, consequentemente, dos processos controlados por eles.
- Falhas de segurança na rede: muitos sistemas IoT utilizam redes de comunicação vulneráveis, como a Internet, sem proteções adequadas, o que pode permitir que um invasor tenha acesso aos dispositivos conectados.

Para mitigar os riscos de ataques em endpoints IoT, é importante adotar medidas de segurança efetivas, como:

- Utilização de criptografia de dados para proteger as informações transmitidas entre os dispositivos.
- Implementação de políticas de segurança adequadas para a gestão de senhas e acesso aos dispositivos.
- Atualização regular dos dispositivos e softwares utilizados pelo sistema IoT.
- Implementação de procedimentos de backup e recuperação em caso de falha ou ataque.

Alguns exemplos de ataques em endpoints IoT, alguns serão abordados no último módulo, incluem:

- Ataque Mirai: esse ataque, descoberto em 2016, visou dispositivos IoT, explorando senhas fracas ou padrões de autenticação inseguros. Os atacantes utilizaram o malware Mirai para criar uma rede de bots que poderiam ser usados em ataques de negação de serviço (DDoS) em sites e servidores.
- Ataque aos carros conectados: em 2015, um grupo de pesquisadores mostrou que era possível assumir o controle de um carro conectado e realizar ações perigosas, como desligar o motor ou controlar os freios.
- Ataque ao sistema de monitoramento de pacientes: em 2020, foi descoberto que um dispositivo usado para monitorar pacientes em hospitais possuía uma vulnerabilidade que permitia que um invasor assumisse o controle do dispositivo e acessasse informações sensíveis dos pacientes. Esse tipo de ataque pode colocar em risco a vida dos pacientes e violar sua privacidade.

Referência Bibliográfica

BOECKL, K. et al. **Considerations for managing Internet of Things (IoT) cybersecurity and privacy risks**. National Institute of Standards and Technology. 2019. Disponível em: <[https://doi.org/10.6028/nist.ir.8228](https://doi.org/10.6028/nist.ir.8228)>. Acesso em 14/03/2023.

DURAES, Wellington; FERREIRA, Fernando Henrique Inocêncio Borba; MAZAN, Renato. **Arquitetura de soluções IoT: Desenvolva com Internet das Coisas para o mundo real**. Casa do Código, 2022. 80 p.

GSM ASSOCIATION. **CLP.11 – Panorama das diretrizes de segurança para IoT**. 2017. 45 p.

GSM ASSOCIATION. **CLP.13 – Diretrizes de segurança em IoT para o ecossistema de endpoints**. 2017. 90 p.

MICROSOFT. **IoT Signals**: summary of research learnings. 2019. 80 p. Disponível em: [https://azure.microsoft.com/mediahandler/files/resourcefiles/iot-signals/IoT-Signals-Microsoft-072019.pdf](https://azure.microsoft.com/mediahandler/files/resourcefiles/iot-signals/IoT-Signals-Microsoft-072019.pdf). Acesso em: 14/03/2023.

MORAES, Alexandre de; TAKASHI, Victor. **Segurança em IoT: Entendendo os riscos e ameaças em IoT**. São Paulo: Alta Books, 2021. 197 p.

NATIONAL INSTITUTE OF STANDARDS AND TECHNOLOGY. **NISTIR 8228**: Considerações para gerenciar Riscos de segurança cibernética e privacidade da Internet das Coisas (IoT). Gaithersburg: Nist, 2019. 44 p.

SINCLAIR, Bruce. **IoT: Como Usar a "Internet das Coisas" Para Alavancar Seus Negócios**. Autêntica Business, 2018. 272 p. Tradução de Afonso Celso da Cunha Serra.