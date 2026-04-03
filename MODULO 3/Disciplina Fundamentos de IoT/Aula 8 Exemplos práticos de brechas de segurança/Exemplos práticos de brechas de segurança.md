[[IoT Security]]

**Introdução**

O objetivo deste módulo é apresentar ataques feitos a IoT e as suas consequências.

**Objetivos da aula**

- Apresentar as características dos ataques Mirai Botnet, VPNFilter Malware, Tesla Model X e câmeras da Verkada;
- Discutir vulnerabilidades exploradas e consequências;
- Entender as formas de mitigação que poderiam ter sido utilizadas para se evitar esses ataques.

**Resumo**

Como vimos, os dispositivos IoT são vulneráveis a vários tipos de ataques. Neste módulo, vamos apresentar os principais ataques que já ocorreram nos últimos anos.

**2016: Ataque Mirai Botnet.**

Como vimos, o principal componente de uma solução de IoT são coisas ou dispositivos de IoT implantados para detectar, medir, executar ações e gerar dados sobre seu ambiente. Em pouco tempo, teremos dezenas de bilhões de dispositivos conectados à Internet e a maior parte será de dispositivos de baixa complexidade. Esses dispositivos têm preços acessíveis, e geralmente são caracterizados por usar CPU menos potente, ter menos memória integrada, gerar pequenas quantidades de dados por vez e consumir menos energia. A consequência é que para manter os dispositivos com um baixo custo e lançá-los no mercado em um ritmo mais rápido implica que geralmente não há um cuidado adequado em relação à segurança cibernética.

Ter dispositivos IoT não seguros conectados à Internet os expõe a ataques cibernéticos de grande impacto. Um exemplo de ataque DDOS ocorreu em 2016. Os invasores exploraram uma vulnerabilidade de segurança – o uso de uma versão simplificada do SO Linux, com usuário e senha padrão - em um grande número de dispositivos IoT e os transformaram em bots para o ataque de botnet Mirai, que acabou sobrecarregando e causando interrupções nos serviços de internet. O Mirai é um tipo de **malware – worm autopropagável -** que visa dispositivos IoT de uso doméstico transformando-os em uma rede zumbi de bots controlados remotamente. Os botnets Mirai são usados ​​por agentes mal-intencionados para obter o controle de sistemas de computador e usá-los em ataques massivos de negação de serviço (DDoS). O destaque é que o malware Mirai afeta principalmente dispositivos de casas inteligentes. Em 2016, uma botnet criada pelo malware, com 150 mil dispositivos, foi utilizada para atacar a OVH, uma empresa de tecnologia francesa, a OVH. O tráfego gerado por essa botnet foi de 1Tbps.

A figura 1 ilustra o funcionamento desse malware:

Figura 1

![Fonte: autoral](https://paperx-dex-assets.s3.sa-east-1.amazonaws.com/images/1680637735212-byrkHPtMux.png "Fonte: autoral")

Fonte: autoral

O Mirai funciona em três etapas de alto nível:

**1. Reconhecimento**, que busca identificar possíveis novos dispositivos vulneráveis para agregação ao botnet. Nessa fase, podemos distinguir três atividades principais:

- SYN Port Scan – que varre a internet para identificar possíveis alvos
- Autenticação de força bruta - realizando correspondências de padrão simples
- Relatório de sucesso – onde há o envio de resultados para um servidor de relatórios centralizado

A figura 2 mostra essa etapa:

Figura 2

![Fonte: autoral](https://paperx-dex-assets.s3.sa-east-1.amazonaws.com/images/1680637861412-Jtnz8TEq7g.png "Fonte: autoral")

Fonte: autoral

**2. Infecção**, etapa em que o malware Mirai é instalado nos dispositivos IoT. O código do malware é compilado em várias arquiteturas. O Malware Loader (Carregador) tenta identificar a arquitetura do dispositivo vulnerável e carregar o executável apropriado. Uma vez que o executável esteja em execução, o dispositivo se torna um novo nó da botnet e começa a realizar as mesmas atividades de varredura e ataque que qualquer outro nó na botnet. De forma resumida, o fluxo de infecção segue os seguintes passos.

- Identificação dos dispositivos vulneráveis, por meio do servidor de relatórios.
- Malware loader (Carregador) recebe dados dos dispositivos.
- Malware loader (Carregador) envia malware e infecta o dispositivo.

A figura 3 ilustra essa etapa:

Figura 3

![Fonte: autoral](https://paperx-dex-assets.s3.sa-east-1.amazonaws.com/images/1680637890573-L6pvho8SIv.png "Fonte: autoral")

Fonte: autoral

**3. Ataque**, onde a funcionalidade responsável por ativar os ataques DDoS nos nós dentro da botnet é iniciado. O processo consiste em três atividades principais.

- O mestre da botnet envia um comando de ataque ao servidor de comando e controle.
- O sistema de comando e controle envia para cada nó da botnet o comando para lançar um ataque, informando os com detalhes necessários.
- O nó, ao receber a mensagem do sistema de comando e controle, executa o ataque desejado, enviando pacotes o mais rápido possível, sem limitação de taxa de transmissão.

Neste ataque, uma versão limitada do SO Linux com usuários e contas padrões foram exploradas para criar novos nós para a bot net. Alterações ou bloqueios dessas contas padrões poderiam mitigar ou mesmo evitar esse tipo de ataque.

A figura 4 ilustra a etapa de ataque: 

Figura 4

![Fonte: autoral](https://paperx-dex-assets.s3.sa-east-1.amazonaws.com/images/1680637978154-eauwqKLSeV.png "Fonte: autoral")

Fonte: autoral

**Malware VPNFilter**

Muitas das plataformas domésticas inteligentes dependem da casa gateway de internet para acessar a nuvem para poder funcionar. Caso os invasores tenham sucesso conseguem comprometer o gateway de internet, eles podem obter controle total de todos os dispositivos domésticos conectados à plataforma. Esse é o objetivo do malware VPNFilter. Projetado para infectar roteadores (especialmente domésticos) e dispositivos de armazenamento conectados à internet, o VPNFilter é um malware que pode roubar dados, desativar o roteador infectado, e consegue se manter no equipamento, mesmo se o usuário reiniciar o roteador infectado. Desde 2018, estima-se que o VPNFilter tenha infectado aproximadamente 500.000 roteadores em todo o mundo.

O ataque pode ser iniciado quando o cliente acessa um site infectado, que executa automaticamente um applet Java no código do dispositivo. Este script irá identificar os endereços IP usados na rede interna do roteador de internet doméstico.

Tendo informações completas relacionadas ao roteador, o invasor tenta fazer login usando as credenciais padrão do fornecedor. Após o login bem-sucedido, o invasor modifica as definições de configuração para obter acesso completo ao gateway de internet doméstico. Assim, o atacante pode interceptar o tráfego de internet do usuário – roubando informações sensíveis, incluindo senhas -, além de manipular as páginas visitadas por ele, criando páginas falsas. Além disso, é possível que o atacante deixe o roteador sem funcionar ou mesmo inutilizá-lo.

O malware é uma plataforma modular com 3 estágios, descritos a seguir:

- **Estágio 1 -** o malware tenta baixar uma imagem de dos sites photobucket ou tokonowall, a partir da qual ele consiga extrair o endereço IP do servidor do estágio 2 oculto nos metadados EXIF da imagem. O objetivo deste estágio é garantir que o malware continue no dispositivo infectado, mesmo após a reinicialização do equipamento para encontrar o endereço IP do servidor do estágio 2.
- **Estágio 2** - o malware então executa o download de um módulo não persistente do servidor do invasor. Este módulo opera por meio de um diretório de trabalho local e se comunica com o servidor de comando e controle (C&C) para executar os comandos.
- **Estágio 3** - a instalação de um módulo de detecção de pacotes não persistentes será feita para estender a funcionalidade do malware. Esse módulo é capaz de interceptar o tráfego para tentar extrair _strings_ de autenticação HTTP, além de instalar um plug-in de comunicação que permita a comunicação remota usando a rede Tor. Esse estágio funciona como plug-ins de estágio 2 e inclui um rastreador de pacotes para espionar o tráfego roteado pelo dispositivo.

A figura 5 ilustra o VPNFilter:

Figura 5

![Fonte: autoral](https://paperx-dex-assets.s3.sa-east-1.amazonaws.com/images/1680638015856-w2gu5pBvhK.png "Fonte: autoral")

Fonte: autoral

**Tesla Model X**

Uma falha no processo de atualização de firmware do sistema da chave keyless do Tesla Model X, usado para destravar as portas, possibilita um ataque e posterior roubo do veículo.

Para que essa falha possa ser explorada, é necessário que o atacante tenha uma unidade de controle eletrônico (ECU - _Electronic Control Unit_) de um veículo Modelo X mais antigo, que pode ser adquirido online em sites como o eBay ou em qualquer loja ou fórum que venda peças usadas de carros Tesla.

Os atacantes, então, modificam a ECU mais antiga para enganar a chave keyless do alvo, de forma que ela fique visível como um dispositivo Bluetooth conectável. Em seguida, o atacante envia uma atualização de firmware maliciosa para a chave keyless, por meio do protocolo BLE (_Bluetooth Low Energy_), assumindo o controle remoto dessa chave. Assim, o atacante obtém os códigos de desbloqueio para abrir a porta e, após isso, tem acesso à interface de diagnóstico do veículo, para emparelhar uma nova chave keyless.

De forma resumida, as etapas desse ataque seriam:

1. Atacante se aproxima da vítima (distância máxima de 5 metros) para permitir que a ECU modificada se conecte com a chave keyless da vítima.
2. O atacante envia a atualização de firmware maliciosa para a chave keyless da vítima, processo que demanda cerca de 1,5 minutos para conclusão. Porém, nesta fase, a distância para a vítima pode ser de até 30 metros.
3. Depois que um chaveiro é hackeado, o invasor consegue extrair as mensagens de desbloqueio para abrir as portas do carro.
4. O invasor usa essas mensagens de desbloqueio para entrar no carro da vítima.
5. O invasor conecta a ECU mais antiga à interface de diagnóstico do carro para emparelhar sua própria chave keyless, de forma que ele consiga ligar o veículo e ir embora.

Neste caso, uma falha conhecida foi explorada, por meio do acesso físico (ou próximo) da vítima. Claro que esse tipo de ataque necessita de conhecimentos avançados e o uso de equipamento volumoso. O vídeo [https://youtu.be/clrNuBb3myE](https://youtu.be/clrNuBb3myE) mostra como é feito esse ataque.

**Câmeras Verkada**

Em 2021, um grupo de hackers teve acesso indevido a um banco de dados contendo feeds de câmeras de segurança coletados pela Verkada Inc., uma startup do Vale do Silício. O banco de dados continha feeds ao vivo de 150.000 câmeras de vigilância dentro de hospitais, organizações, departamentos de polícia, prisões e escolas. Segundo a própria Verkada, os invasores comprometeram a sua plataforma e acessaram dados de 97 clientes, que tiveram suas câmeras acessadas e dados de vídeo ou imagem visualizados. Além disso, oito desses clientes tiveram dados de produtos de controle de acesso acessados, incluindo credenciais de crachá. Outros clientes tiveram suas credenciais de rede wi-fi comprometidas. Os invasores também baixaram uma lista de usuários, incluindo nomes e endereços de e-mail, e uma lista de pedidos de vendas da Vergada.

O vetor de entrada dos invasores foi por meio de um servidor de suporte ao cliente mal configurado, exposto na Internet. Depois que os invasores acessaram esse servidor, eles encontraram as credenciais do administrador de suporte ao cliente e as usaram para fazer login em uma interface da Web do sistema de suporte ao cliente. Neste ponto, eles acessaram os dispositivos do cliente usando a funcionalidade de suporte interno que emulava as sessões do usuário.

A figura 6 ilustra esse caso:

Figura 6

![Fonte: autoral](https://paperx-dex-assets.s3.sa-east-1.amazonaws.com/images/1680638082198-pJORgy8mbk.png "Fonte: autoral")

Fonte: autoral

Neste caso, houve exploração de uma conta com excesso de privilégio, que eram divulgadas na Internet.

**Conteúdo Bônus**

**Tópicos avançados**

**Mais sobre o botnet Miraí**

O ataque botnet Mirai foi uma das maiores ameaças de segurança da Internet das Coisas (IoT) até o momento. Ele se originou em agosto de 2016 e foi responsável por derrubar vários sites populares, como Twitter, Reddit e Spotify.

O Mirai explorou vulnerabilidades em dispositivos IoT, como câmeras de segurança, DVRs e roteadores, para infectá-los com malware e criar uma botnet. Uma botnet é uma rede de dispositivos infectados que podem ser controlados remotamente por um atacante cibernético.

O ataque Mirai foi possível devido a duas vulnerabilidades nos dispositivos IoT: senhas fracas e padrões de autenticação previsíveis. Essas vulnerabilidades permitiram que o malware Mirai se espalhasse rapidamente pela Internet.

O malware Mirai foi projetado para explorar a falta de segurança nos dispositivos IoT. Ele se conecta aos dispositivos por meio de telnet, usando uma lista de senhas comuns para tentar adivinhar a senha de administrador dos dispositivos. Uma vez conectado, o malware executa um comando que instala o malware na memória do dispositivo.

Uma vez instalado, o malware se comunica com o servidor de comando e controle (C&C) para receber instruções. O C&C é o sistema usado pelos atacantes para controlar a botnet. Os atacantes podem enviar comandos para os dispositivos infectados na botnet para executar atividades maliciosas, como ataques DDoS.

Uma vez que um grande número de dispositivos IoT foi infectado, a botnet Mirai foi usada para realizar ataques de negação de serviço distribuído (DDoS) contra os alvos escolhidos. O ataque DDoS consiste em enviar um grande número de solicitações ao servidor de um site ou serviço, com o objetivo de sobrecarregá-lo e torná-lo inoperante. No caso do ataque Mirai, a botnet foi capaz de gerar um tráfego de mais de 1 terabyte por segundo, o que é suficiente para derrubar a maioria dos sites e serviços na Internet.

Os autores do Mirai foram identificados e condenados em 2018. No entanto, o ataque revelou a vulnerabilidade de dispositivos IoT e a necessidade de implementar medidas de segurança adequadas para protegê-los contra ataques cibernéticos.

Algumas formas de mitigação para evitar ataques como o Mirai incluem a implementação de senhas fortes e exclusivas em dispositivos IoT, a desativação de serviços desnecessários em dispositivos IoT e a instalação de atualizações de segurança regularmente. Também é recomendável utilizar soluções de segurança avançadas, como firewalls e sistemas de detecção de intrusão, para monitorar e proteger os dispositivos IoT contra possíveis ameaças.

**Mais sobre o ataque às câmeras Verkada**

Como já visto, em março de 2021, ocorreu um ataque cibernético às câmeras de segurança da empresa Verkada. Esse ataque permitiu que os invasores acessassem feeds de câmeras em todo o mundo, incluindo hospitais, escolas e prisões. Vamos trazer aqui uma análise das técnicas, comandos, vulnerabilidades exploradas no ataque e o que poderia ter sido feito para evitá-lo.

**Técnicas Utilizadas**

Os invasores utilizaram várias técnicas para obter acesso às câmeras Verkade, incluindo:

- **Força Bruta**: Os invasores usaram uma técnica de ataque conhecida como "força bruta" para obter as credenciais de login do servidor de gerenciamento de vídeo Verkada. Eles usaram um script automatizado que tentava várias combinações de nome de usuário e senha até que a combinação correta fosse encontrada.
- **Injeção de Comando**: Os invasores se aproveitaram de outras vulnerabilidades em sistemas de segurança conectados à Internet, como roteadores, para obter acesso às câmeras Verkada. Eles usaram a técnica de "injeção de comando" para enviar comandos maliciosos a esses dispositivos, permitindo que eles desativassem os firewalls de segurança e acessassem as câmeras Verkade sem detecção.
- **Exploração de Vulnerabilidades**: Os invasores também exploraram vulnerabilidades em dispositivos de segurança conectados à Internet, como servidores expostos à Internet, para obter acesso às câmeras Verkada.

**Vulnerabilidades Exploradas**

Os invasores exploraram várias vulnerabilidades para obter acesso às câmeras Verkade, incluindo:

- **Servidor de Gerenciamento de Vídeo Exposto à Internet**: O servidor de gerenciamento de vídeo Versada foi exposto à Internet sem a proteção adequada, permitindo que os invasores obtivessem acesso às credenciais de login do servidor.
- **Senhas Fracas**: As senhas utilizadas para proteger os dispositivos de segurança, incluindo as câmeras Verdade, eram fracas e fáceis de adivinhar.
- **Falta de Atualizações de Segurança**: Alguns dispositivos de segurança conectados à Internet, como roteadores, não foram atualizados com as últimas atualizações de segurança, tornando-os vulneráveis ​​a ataques cibernéticos.

**Formas de Mitigação**

Para evitar ataques como o Vergada, é importante implementar medidas de segurança adequadas em dispositivos conectados à Internet, como câmeras de segurança. Isso inclui:

- **Proteção Adequada de Servidores Expostos à Internet**: Servidores expostos à Internet, como servidores de gerenciamento de vídeo, devem ser protegidos com medidas de segurança adequadas, como firewalls de segurança.
- **Senhas Fortes e Exclusivas**: Senhas fortes e exclusivas devem ser usadas para proteger os dispositivos de segurança.
- **Atualizações de Segurança**: Dispositivos.

**Outros ataques**

**Ataque Blue Borne (2017)**

**Causa**: O ataque Blue Borne explorou uma série de vulnerabilidades na pilha de protocolos Bluetooth.

**Vulnerabilidades exploradas**: O ataque explorou a vulnerabilidade CVE-2017-1000251, que permitiu que um invasor executasse código remoto em um dispositivo Bluetooth afetado. O ataque também explorou outras vulnerabilidades, incluindo CVE-2017-0781 e CVE-2017-0782, que permitiram que um invasor executasse código arbitrário no dispositivo.

**Consequências**: O ataque Blue Borne afetou milhões de dispositivos IoT conectados, incluindo smartphones, laptops e dispositivos IoT. Como resultado, os dispositivos comprometidos poderiam ser usados para espionagem, roubo de dados e outros ataques cibernéticos.

**Formas de mitigação**: Para mitigar o risco de um ataque BlueBorne, é essencial manter os dispositivos IoT atualizados com as últimas correções de segurança. Também é importante desativar o Bluetooth em dispositivos quando não estiver em uso.

**Ataque ao protocolo TCP/IP Nucleus**

Em julho de 2021, um relatório chamado NUCLEUS:13 identificou 13 vulnerabilidades no protocolo TCP/IP Nucleus, que é um sistema operacional em tempo real usado em sistemas para aplicações aeroespaciais, industriais e médicas. Essas vulnerabilidades permitem aos hackers executar código arbitrário nos dispositivos afetados ou causar negação de serviço (DoS). A causa desse ataque foi a falta de atualização do protocolo TCP/IP Nucleus por parte dos fabricantes dos dispositivos IoT que o utilizam. O protocolo TCP/IP Nucleus foi desenvolvido há mais de 20 anos e não recebeu manutenção adequada desde então. As consequências desse ataque podem ser graves para os setores críticos que dependem desses dispositivos IoT para operações vitais ou sensíveis. Por exemplo, os hackers podem comprometer o funcionamento dos equipamentos médicos ou interferir nos sistemas industriais ou aeroespaciais. As formas de mitigação desse ataque são aplicar os patches disponibilizados pelos fabricantes dos dispositivos IoT afetados ou substituir esses dispositivos por outros mais modernos e seguros.

**Ataque aos dispositivos IoT domésticos**

No primeiro semestre de 2021, houve 1.5 bilhão de ataques aos dispositivos IoT domésticos conectados à internet, como roteadores, câmeras, smart TVs, assistentes virtuais e termostatos. Os hackers tentaram infectar esses dispositivos com malware, roubar dados pessoais, minerar criptomoedas ou construir botnets. A causa desses ataques foi a falta de proteção adequada dos dispositivos IoT domésticos por parte dos usuários finais. Muitos desses dispositivos vêm com configurações padrão inseguras, como senhas fracas ou nulas, portas abertas ou serviços desnecessários habilitados. Além disso, muitos usuários não alteram essas configurações ou não atualizam seus dispositivos regularmente.

Referência Bibliográfica

BOECKL, K. et al. **Considerations for managing Internet of Things (IoT) cybersecurity and privacy risks**. National Institute of Standards and Technology. 2019. Disponível em: <[https://doi.org/10.6028/nist.ir.8228](https://doi.org/10.6028/nist.ir.8228)>. Acesso em 14/03/2023.

DURAES, Wellington; FERREIRA, Fernando Henrique Inocêncio Borba; MAZAN, Renato. **Arquitetura de soluções IoT: Desenvolva com Internet das Coisas para o mundo real**. Casa do Código, 2022. 80 p.

GSM ASSOCIATION. **CLP.11 – Panorama das diretrizes de segurança para IoT**. 2017. 45 p.

GSM ASSOCIATION. **CLP.14 – Diretrizes de segurança em IoT para Operadoras de Rede**. 2017. 32 p.

MICROSOFT. **IoT Signals**: summary of research learnings. 2019. 80 p. Disponível em: [https://azure.microsoft.com/mediahandler/files/resourcefiles/iot-signals/IoT-Signals-Microsoft-072019.pdf](https://azure.microsoft.com/mediahandler/files/resourcefiles/iot-signals/IoT-Signals-Microsoft-072019.pdf). Acesso em: 15/03/2023.

MORAES, Alexandre de; TAKASHI, Victor. **Segurança em IoT: Entendendo os riscos e ameaças em IoT**. São Paulo: Alta Books, 2021. 197 p.

NATIONAL INSTITUTE OF STANDARDS AND TECHNOLOGY. **NISTIR 8228**: Considerações para gerenciar Riscos de segurança cibernética e privacidade da Internet das Coisas (IoT). Gaithersburg: Nist, 2019. 44 p.

SINCLAIR, Bruce. **IoT: Como Usar a "Internet das Coisas" Para Alavancar Seus Negócios**. Autêntica Business, 2018. 272 p. Tradução de Afonso Celso da Cunha Serra.