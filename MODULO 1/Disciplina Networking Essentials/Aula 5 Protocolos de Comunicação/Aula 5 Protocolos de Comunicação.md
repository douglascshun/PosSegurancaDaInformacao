[[Networking Essentials]]
## Protocolos de comunicação

**Introdução**

O mundo tornou-se cada vez mais globalizado com as redes de computadores, principalmente a Internet, e a distância física entre as pessoas não é mais um obstáculo para uma comunicação efetiva e troca de dados e dispositivos de informação. Esse padrão, chamado de protocolo, é um conjunto de regras que diferentes dispositivos devem seguir para poder trocar pacotes perfeitamente.

Quando se trata de comunicação entre computadores que fazem parte de uma rede, o estabelecimento dessa comunicação deve ser feito de forma padronizada para que diferentes dispositivos possam trocar informações entre si.

**Objetivos da aula**

- Conhecer os fundamentos dos protocolos de comunicação;
- Compreender as principais funcionalidades dos protocolos de comunicação;
- Conhecer e compreender a aplicabilidade dos protocolos de rede;
- Conhecer os principais serviços dos protocolos de rede.

**Resumo**

**Fundamentos dos protocolos de comunicação**

As redes são compostas por muitos componentes físicos e lógicos e, portanto, são representadas por camadas de modelos funcionais executados por programas chamados protocolos. Os protocolos são responsáveis ​​por desempenhar as funções de cada camada como se fossem especialistas nessas tarefas. (BARRETO; ZANIN; SARAIVA, 2018, p.96).

Depois que todas as camadas concluírem as atividades pelas quais são responsáveis, os dados são encapsulados para formar um pacote. Esses pacotes realizam a comunicação entre os computadores conectados à rede. Esta comunicação é bidirecional.

Em outras palavras, um computador pode ser tanto o remetente quanto o destinatário de pacotes. Portanto, cada camada da rede e cada protocolo específico devem ser capazes de realizar atividades em ambas as direções. (BARRETO; ZANIN; SARAIVA 2018, p.96) Relembrando os modelos de redes, temos:

- **Modelo Open Systems Interconnect (OSI):** esse modelo é referência da ISO e é formado por sete camadas de funções, sendo que nunca foi aceito na prática. Apesar disso, os nomes das camadas deste modelo são bastante utilizados. Nesse modelo, cada protocolo realiza uma atividade, que corresponde a uma camada. (BARRETO; ZANIN; SARAIVA, 2018, p.96).
- **Modelo Transmission Control Protocol/Internet Protocol (TCP/IP):** esse modelo foi baseado no modelo OSI, mas possui menos camadas que ele. Ele envolve um conjunto de protocolos que são utilizados para realizar a comunicação entre computadores de uma rede. Sua criação aconteceu em um cenário onde os equipamentos e as conexões eram muito diferentes entre si, mas havia a necessidade de enviar dados de um equipamento para outro, independentemente de como isso acontecesse. Foi nesse ambiente que o TCP/IP surgiu e acabou por se firmar como o padrão no qual a Internet se desenvolveu. (BARRETO; ZANIN; SARAIVA, 2018, p.96).

Sobre as funcionalidades dos protocolos, podemos afirmar que realizam as seguintes funções para efetivar a comunicação entre dispositivos de uma rede:

- **Endereçamento:** define o ponto de destino do pacote.
- **Numeração:** identifica cada pacote por meio de uma numeração sequencial.
- **Conexão:** estabelece a conexão por meio de um túnel lógico fechado que liga o remetente e o destinatário do pacote.
- **Controle de erros:** identifica os erros da comunicação e faz a correção. 
- **Confirmação:** envia um sinal informando quando cada segmento da mensagem é recebido de maneira íntegra.
- **Conversão:** converte o código e o adapta às características do dispositivo destinatário. (BARRETO; ZANIN; SARAIVA, 2018, p.97).

Uma rede ou protocolo de Internet é usado para comunicação e inclui um conjunto de regras projetadas para controlar e regular comunicações, conexões e transferências de dados entre dispositivos e/ou sistemas de computador. Qualquer tipo de comunicação precisa de regras estabelecidas para que as partes envolvidas possam se entender e entender o que estão falando.

A definição do idioma utilizado para comunicação é um exemplo das regras que devem ser estabelecidas ao falar com amigos que moram no exterior, por exemplo. Em outras palavras, os protocolos são usados ​​nas redes para permitir que máquinas e sistemas se comuniquem, mesmo que tenham diferentes configurações que definem como a comunicação e a troca de dados são realizadas. (BARRETO; ZANIN; SARAIVA, 2018, p.98).

Em outras palavras, os protocolos são usados ​​nas redes para permitir que máquinas e sistemas se comuniquem, mesmo que tenham diferentes configurações que definem como a comunicação e a troca de dados são realizadas. Você pode compartilhar recursos existentes em sua máquina, seja em sua rede local ou na World Wide Web (Internet). Por exemplo, os usuários podem compartilhar arquivos, pastas, impressoras, etc. em uma rede local sem acesso à Internet.

O uso da Internet criou uma oportunidade cada vez maior de compartilhamento de recursos entre máquinas em uma rede de computadores, permitindo a troca de informações com qualquer computador conectado no mundo. Todos esses recursos são fornecidos por meio de protocolos instalados e configurados por profissionais de TI. (BARRETO; ZANIN; SARAIVA, 2018, p.99).

**Utilização dos protocolos de rede**

As redes de computadores são compostas de vários componentes físicos e lógicos. Portanto, eles são divididos em camadas para fornecer uma melhor compreensão de como eles funcionam. Como vimos, essas camadas possuem funções distintas desempenhadas por elementos denominados protocolos, conforme defendem Forouzan e Mosharraf (2013 apud Barreto, Zanin e Saraiva 2018, p. 99).

Em cada camada da rede, o protocolo atua como se fosse um especialista realizando todas as atividades de cada camada. Para entender o uso desses protocolos em cada camada, observe que, embora existam dois modelos de divisão de redes em camadas, OSI e TCP/IP, o modelo TCP/IP tornou-se o padrão da Internet.

O nome TCP/IP vem dos nomes dos protocolos mais utilizados neste modelo de referência: TCP (Transmission Control Protocol ou Transmission Control Protocol) e IP (Internet Protocol ou Internet Protocol). O modelo TCP/IP é dividido em diferentes camadas, onde cada uma executa tarefas de comunicação. Conforme apresentam Forouzan e Mosharraf (2013 apud Barreto, Zanin e Saraiva 2018, p.99), dentro das camadas, os protocolos são chamados de pilhas de protocolos, com cada camada interagindo com a camada acima e abaixo.

**Camada de aplicação**

Em uma rede, a camada de aplicação é a camada mais próxima do usuário. Isso ocorre porque o aplicativo do usuário usa o protocolo nessa camada para os propósitos do programa do usuário. Reuniões, redes sociais, editores de texto. Essa camada é responsável por garantir que os usuários tenham uma experiência de uso bem-sucedida do programa, apesar de todas as diferenças entre os dispositivos distribuídos na Internet.

Como resultado, muitos novos protocolos foram criados e os antigos caíram em desuso. Um protocolo requer uma porta para habilitar a conectividade. As portas são os elementos responsáveis ​​por adaptar os aplicativos para serem executados em dispositivos executados em diferentes plataformas de computação. (BARRETO; ZANIN; SARAIVA 2018, p.100).

A maioria dos sistemas operacionais vem com um arquivo contendo números de porta e os serviços que correspondem a cada porta. Esses números de porta nem sempre são os mesmos. Eles dependem da plataforma em que o sistema operacional está sendo executado e do hardware e software usados ​​para executar o protocolo TCP. (BARRETO; ZANIN; SARAIVA 2018, p.100).

Na camada de transporte ocorre o processamento de uma solicitação de programa, o protocolo da camada de aplicação se comunica com o protocolo da camada de transporte, geralmente TCP ou UDP (User Datagram Protocol). A seguir podemos compreender melhor o que são os protocolos TCP e UDP:

- **Protocolo TCP:** esse protocolo é utilizado para fazer a entrega confiável dos dados, excluir segmentos de dados duplicados e também recuperar dados corrompidos. O encaminhamento de pacotes feito utilizando o protocolo TCP é mais lento do que quando é feito utilizando o protocolo UDP, mas ele assegura garantia e ordenação na entrega dos segmentos. (BARRETO; ZANIN; SARAIVA, 2018, p.101).
- **Protocolo UDP:** normalmente se diz que esse protocolo não é orientado à conexão, ou seja, ele faz uma entrega não confiável de pacotes, não exclui pacotes duplicados nem faz o controle de dados corrompidos. Além disso, ele não faz uma confirmação de que os dados chegaram de maneira integral no seu destinatário e também não faz a ordenação das mensagens. Nesse sentido, existe grande possibilidade de os pacotes serem perdidos, alterados, duplicados ou desordenados. Como o protocolo UDP não tem a mesma preocupação com integridade e confiabilidade que o protocolo TCP tem, o encaminhamento de pacotes feito por ele é bem mais rápido. (BARRETO; ZANIN; SARAIVA, 2018, p.101).

Em uma rede, a camada de aplicação é a camada mais próxima do usuário. Isso ocorre porque o aplicativo do usuário usa o protocolo nessa camada para os propósitos do programa do usuário. Reuniões, redes sociais, editores de texto. Essa camada é responsável por garantir que os usuários tenham uma experiência de uso bem-sucedida do programa, apesar de todas as diferenças entre os dispositivos distribuídos na Internet.

Como resultado, muitos novos protocolos foram criados e os antigos caíram em desuso. Um protocolo requer uma porta para habilitar a conectividade. As portas são os elementos responsáveis ​​por adaptar os aplicativos para serem executados em dispositivos executados em diferentes plataformas de computação. (BARRETO; ZANIN; SARAIVA 2018, p.100).

A maioria dos sistemas operacionais vem com um arquivo contendo números de porta e os serviços que correspondem a cada porta. Esses números de porta nem sempre são os mesmos. Eles dependem da plataforma em que o sistema operacional está sendo executado e do hardware e software usados ​​para executar o protocolo TCP. (BARRETO; ZANIN; SARAIVA 2018, p.100).

Camada de transporte, após o processamento de uma solicitação de programa, o protocolo da camada de aplicação se comunica com o protocolo da camada de transporte, geralmente TCP ou UDP (User Datagram Protocol).3

**Serviços dos protocolos de rede**

Existem muitos serviços que os protocolos de rede podem fornecer e que podem ser classificados da seguinte forma: Serviço de Rede Internet, Serviço de Rede Cliente-Servidor e Serviço de Rede WAN. A Internet oferece muitos recursos e usos, desde acesso a e-mails e websites até vídeo em tempo real e compartilhamento de arquivos em sistemas peer-to-peer. Todos esses usos são baseados em conceitos relativamente simples.

Um serviço de rede pode ser considerado como um aplicativo distribuído, cujos microsserviços estão mantidos em diferentes hosts, e executado em dois ou mais computadores conectados por uma rede. Todos os serviços de rede consistem em pelo menos quatro elementos a seguir:

- **Servidor**: computador que realiza a parte principal do serviço, usando seus recursos locais e/ou outros serviços.
- **Cliente**: computador que solicita o serviço através da rede; geralmente o cliente age a pedido de um ser humano, através de uma interface de usuário, mas ele também pode ser o representante de outro sistema computacional.
- **Protocolo**: é a definição do serviço propriamente dito, ou seja, os passos, o conjunto de mensagens e os formatos de dados que definem o diálogo necessário entre o cliente e o servidor para a realização do serviço.
- **Middleware**: é o suporte de execução e de comunicação que permite a construção do serviço. Em geral o _middleware_ é composto por sistemas operacionais e protocolos de rede encarregados de encaminhar os pedidos do cliente para o servidor e as respostas de volta ao cliente. (MAZERO 2021, DOCUMENTO ONLINE).

Se o cliente exibir apenas dados, ele é chamado de thin cliente, mas se for responsável por parte da lógica do aplicativo, é chamado de cliente gordo. Desta forma os clientes gordos atuam como sistemas de e-mail convencionais (não _webmail_); Mas com uma futuridade

De acordo com Mazero (2021, DOCUMENTO ONLINE), temos que o _Three-Tier_, representa de uma arquitetura com três componentes: o cliente, responsável pela interface com o usuário, o servidor, responsável pela lógica da aplicação, e os repositórios de dados.

Figura 1: _Three-Tier_

![Fonte: Maziero (2021, Documento Online).](https://paperx-dex-assets.s3.sa-east-1.amazonaws.com/images/1677703693770-h9aHtdS3OL.png "Fonte: Maziero (2021, Documento Online).")

Fonte: Maziero (2021, Documento Online).

Desta forma, o Peer-to-Peer é uma arquitetura onde todos os participantes são ao mesmo tempo servidores (oferecem serviços e recursos) e clientes (usam serviços e recursos) uns dos outros. Muitos serviços de compartilhamento de arquivos e de comunicação entre usuários se estruturam dessa forma:

Figura 2: Peer-to-Peer

![Fonte: Maziero (2021, Documento Online).](https://paperx-dex-assets.s3.sa-east-1.amazonaws.com/images/1677703724348-Z5L73F7YZO.png "Fonte: Maziero (2021, Documento Online).")

Fonte: Maziero (2021, Documento Online).

Existem muitos serviços de rede, para as mais diversas finalidades. Eis alguns exemplos:

Quadro 1: Serviços de Rede

![Fonte: Adaptado de MAZERO (2021, DOCUMENTO ONLINE).](https://paperx-dex-assets.s3.sa-east-1.amazonaws.com/images/1677703808221-eMiAJdNzIW.png "Fonte: Adaptado de MAZERO (2021, DOCUMENTO ONLINE).")

Fonte: Adaptado de MAZERO (2021, DOCUMENTO ONLINE).

Os serviços mais comuns em redes IP usam TCP ou UDP como suporte de comunicação. Isso se aplica a serviços como WWW, e-mail, sistemas peer-to-peer e Voz sobre IP. Esses serviços são implementados basicamente por um processo do lado do servidor que possui um número de porta aberta e um protocolo de transporte (TCP ou UDP) dependendo do serviço oferecido.

Qualquer serviço pode ser executado em qualquer porta, mas a maioria dos serviços legados estabelece portas padrão para simplificar as conexões entre clientes e servidores. Alguns protocolos e números de porta padrão são (MAZERO, 2021, documentação online).

Figura 3: Portas padrão

![Fonte: Maziero (2021, Documento Online).](https://paperx-dex-assets.s3.sa-east-1.amazonaws.com/images/1677703867141-YwVxPym00Y.png "Fonte: Maziero (2021, Documento Online).")

Fonte: Maziero (2021, Documento Online).

Alguns serviços de rede podem usar suporte de comunicação mais avançado construído como uma camada sobre TCP ou UDP. É o caso de RPC (Remote Call Procedure), serviços da Web e serviços baseados em ambientes de objetos distribuídos, como Java RMI (Remote Method Invocation) e CORBA.

Nesse caso, os aplicativos cliente e servidor se comunicam por TCP/IP usando chamadas de procedimento ou métodos remotos criados por bibliotecas específicas. Nesse caso, vários processos podem estar envolvidos na construção do serviço, tanto cliente quanto servidor. Pode ser difícil criar regras de filtragem (firewalls) para esses serviços, pois os números de porta usados ​​geralmente não são padronizados e podem variar de versão para versão. (MAZERO, 2021, documentação online).

**Conteúdo bônus**

**Tópicos avançados**

Como são os protocolos de comunicação na Indústria?

Em uma era de Indústria 4.0 é de se esperar que a conectividade das máquinas e ferramentas seja cada vez maior, e para que tudo seja orquestrado de forma harmoniosa existem protocolos especiais industriais de comunicação. 

De acordo com Wilson (2012, online), existe a necessidade por uma “capacidade de se comunicar com a instrumentação instalada no chão de fábrica não é mais apenas um luxo. A necessidade de monitorar, controlar e armazenar dados de processo automaticamente é agora um requisito para muitos dos clientes.”

Quer saber mais sobre a comunicação industrial? Leia o artigo a seguir:

Disponível em: <[https://www.aquecimentoindustrial.com.br/protocolos-de-comunicacao-industrial-comuns/#:~:text=O%20Modbus%20%C3%A9%20atualmente%20o,para%20protocolos%20de%20comunica%C3%A7%C3%A3o%20industrial](https://www.aquecimentoindustrial.com.br/protocolos-de-comunicacao-industrial-comuns/#:~:text=O%20Modbus%20%C3%A9%20atualmente%20o,para%20protocolos%20de%20comunica%C3%A7%C3%A3o%20industrial).> Acesso em 30/01/2023.

Observação: Este conteúdo não será cobrado nas avaliações e estará, obrigatoriamente, presente nas videoaulas. Fique tranquilo(a)!

Referência Bibliográfica

BARRETO, Jeanine dos Santos; ZANIN, Aline; SARAIVA, Maurício de Oliveira. **Fundamentos de redes de computadore**s. – Porto Alegre: SAGAH, 2018.

MAZERO, Carlos. **Introdução aos Serviços de Rede**. 2021. Disponível em: < [http://wiki.inf.ufpr.br/maziero/doku.php?id=espec:introducao](http://wiki.inf.ufpr.br/maziero/doku.php?id=espec:introducao)> Acesso em: 28/10/2022.