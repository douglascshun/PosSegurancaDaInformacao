[[Networking Essentials]]

## Camada de aplicação

**Introdução**

A camada de aplicação é responsável por abrigar os sistemas e apps que o usuário final entra em contato quando navega na internet, dentre outras atividades, desta forma, no modelo TCP/IP, essa camada corresponde às camadas combinadas de sessão, apresentação e aplicação do modelo OSI.

Muitos protocolos ainda precisam ser definidos, mas antes de falar da camada de aplicação, entre esta camada e a camada de transporte do modelo OSI está o gerenciamento da sessão (camada de sessão) e o gerenciamento do perfil dessa sessão (camada). apresentação). Nesta aula vamos conhecer melhor a camada de aplicação!

**Objetivos da aula**

- Compreender as funções da camada de aplicação;
- Conhecer detalhes da arquitetura da aplicação de rede;
- Conhecer os principais protocolos da camada de aplicação.

**Resumo**

**A camada de aplicação**

Que tal falar um pouco de endereçamento IP? Como a camada de aplicação concentra os pedidos que os usuários fazem em seus navegadores, ela é a primeira a usar o endereço de IP, e com isso temos a importância da criação de sub-redes, que podem ser identificadas pela máscara de rede identificada e pelo número de hosts em cada nova sub-rede.

Observe que um valor de 0 (zero) conta como um endereço de rede. É assim que a tabela de rede é organizada. Começando com o endereço de rede, sempre adicione 32 para identificar a próxima rede, subtraia 1 do valor inicial da próxima rede para obter o endereço de broadcast da rede anterior e identifique-a como a próxima rede. visível da mesa. ((Bay; BLUNING 2016, S.112):

Figura 1: Redirecionamento de gravação de arquivo.

![Fonte: Adaptado de Tannenbaum 2007.](https://paperx-dex-assets.s3.sa-east-1.amazonaws.com/images/1677704491059-0Wlv5LwokP.png "Fonte: Adaptado de Tannenbaum 2007.")

Fonte: Adaptado de Tannenbaum 2007.

De acordo com Bay e Bluning (2016, p.81), a camada de aplicação é conhecida por ter muitos protocolos familiares aos usuários. Entre eles estão HTTP, SSH, POP e SMTP. Dessa forma, a camada de aplicação realiza as interações entre os usuários e os serviços que desejam utilizar. É o usuário quem processa as informações e encaminha a solicitação às pessoas autorizadas.

Um exemplo bem simples desses protocolos é o HTTP (Hyper Text Transfer Protocol), onde um usuário envia o nome da página que deseja acessar para o servidor que possui aquela página. O servidor então recebe essa transmissão e envia as informações da página para que o navegador do usuário possa renderizar o site. Todo esse processo é feito usando o protocolo HTTP.

**Funcionalidades da camada de aplicação**

A camada de aplicação é responsável por especificar vários serviços de comunicação a serem disponibilizados aos usuários da rede. Com efeito, a funcionalidade descrita a seguir encapsula um conjunto de aplicativos de rede que permitem que os usuários desses serviços executem uma variedade de tarefas.

 Portanto, a camada de aplicação não possui serviços com a mesma funcionalidade dos serviços existentes na camada anterior. Para cada aplicação é definido um protocolo específico para a aplicação que possui apenas uma interface em comum com a camada inferior (representação em protocolo OSI ou transporte em TCP/IP).

Dessa forma, uma investigação da camada de aplicação pode ser entendida (e, portanto, também pode ser realizada) como uma investigação de cada aplicação existente. Claro, é preciso muito esforço para fazer isso de forma eficaz neste ponto do curso. Portanto, listaremos apenas alguns dos aplicativos existentes e suas principais funções, e discutiremos os aplicativos de segurança com um pouco mais de detalhes no próximo capítulo.

Os serviços de transferência de arquivos permitem que os usuários movam (carreguem ou soltem) arquivos de um computador para outro. Os aplicativos nesta categoria incluem ftp (ou sftp por motivos de segurança) e navegadores modernos. Os serviços prestados consistem em estabelecer conexões entre duas máquinas, detectar permissões e transferir arquivos entre máquinas por meio de pacotes de mensagens.

Este serviço consiste em permitir que os usuários se comuniquem de forma assíncrona por meio de mensagens de texto (com ou sem imagem ou outros anexos de arquivos). Este serviço é fornecido por aplicativos como e-mail, Usenet News (velhos tempos) e Twitter. Para enviar uma mensagem por e-mail, os computadores que representam os endereços de e para devem estabelecer uma conexão para realmente enviar a mensagem. Se não for possível estabelecer uma conexão, a mensagem é colocada na fila e tentada várias vezes durante vários dias.

Nos serviços de notícias, as mensagens não são enviadas para um usuário específico (ou lista de usuários), mas para um mural que qualquer um pode ver. Funciona como um quadro de avisos, postando notas que só as pessoas interessadas podem ler. Esta é uma forma mais eficiente de trabalhar com listas de distribuição, mas requer um servidor (e muitos espelhos) para a parede.

Existem também serviços que trocam mensagens em tempo real, como o chat na Internet, mas estes não são muito diferentes dos mecanismos anteriores, exceto que a troca é mais instantânea.

O acesso remoto permite que os usuários acessem computadores remotamente. Os maiores problemas de acesso remoto estão ligados à segurança e ao fornecimento de um ambiente de trabalho confortável ao usuário. A segurança envolve aspectos bastante específicos e não serão tratados aqui e o ambiente de trabalho envolve o fornecimento de características de conversão entre terminais gráficos, que serão tratados no próximo item.

Importante para a computação em nuvem, o terminal virtual é um serviço que consiste em fornecer ao usuário um ambiente em que ele possa fazer acesso remoto à uma determinada máquina, através da conversão de controles específicos de interface (tela, teclado, mouse, etc.) da máquina em que está fisicamente o usuário e a máquina que ele acessa remotamente.

Já a execução remota representa uma especialização do serviço de acesso remoto em que o usuário apenas solicita que uma determinada tarefa seja executada remotamente. Eles são uma das características determinantes de sistemas distribuídos, sendo representados, por exemplo, pelo serviço de RPC (Remote Procedure Call) ou de RMI (Remote Method Invocation em Java);

**Arquitetura da aplicação de rede**

Essa arquitetura consiste em aplicativos distribuídos que compartilham tarefas e cargas de trabalho entre provedores de recursos (ou seja, servidores) e consumidores de serviços (ou seja, clientes). Ou seja, o cliente solicita informações do servidor e o servidor compartilha recursos para responder ao cliente. Essa estrutura geralmente emprega um paradigma de solicitação/resposta para comunicação. Ele mostra solicitações e respostas de serviço, tal como apresenta Tanenbaum e Wetherall (2011 _apud_ Quincozes, Quincozes E Kazienko 2022, p.257].

Este paradigma também é conhecido como peer-to-peer ou peer-to-peer (P2P). Nela, cada dispositivo que compõe a rede atua tanto como cliente quanto como servidor. Desta forma, dados e serviços podem ser compartilhados sem a necessidade de um servidor central. Um exemplo de aplicativo P2P puro é o Gnutella, uma rede de compartilhamento de arquivos em que as solicitações de pesquisa são roteadas entre os nós.

Isso elimina a necessidade de um servidor central. No entanto, é importante enfatizar o potencial de arquiteturas híbridas que consistem em arquiteturas cliente/servidor e peer-to-peer. O Torrent é um exemplo de aplicativo que utiliza uma arquitetura híbrida. Por exemplo, torrents permitem que vários usuários se conectem e transfiram arquivos sem a necessidade de uma fonte intermediária para baixar os arquivos (Tanenbaum e Wetherall 2011 apud Quincozes, Quincozes E Kazienko 2022, p.257).

Também conhecido como publicar/assinar, esse paradigma consiste em três componentes principais: Editores, assinantes e servidores centralizados (brokers). Basicamente, os corretores são organizados em temas. Os dispositivos do editor são responsáveis ​​por alimentar os tópicos intermediários. Os assinantes, por outro lado, são dispositivos que se interessam pelas informações contidas nos tópicos que assinam e recebem essas informações.

**Protocolos da camada de aplicação**

A camada de aplicação realiza a mediação entre as solicitações dos usuários e os recursos dos microsserviços demandados, desta forma , quando um sistema é construído de forma a se comunicar com outro, é necessário que sejam especificados detalhes como:

- A sintaxe e a semântica da mensagem que pode ser trocada.
- O iniciador da interação, que é ou o cliente ou o servidor.
- As ações a serem realizadas em caso de erro.
- Como os dois lados sabem quando a comunicação termina. (COMER 2016, p.46).

Ao especificar os detalhes de comunicação, os programadores definem os protocolos da camada de aplicação. Existem dois tipos gerais de protocolos da camada de aplicação, dependendo de seu uso.

- **Serviço privado.** Um programador ou uma empresa cria um par de aplicativos que se comunicam por meio da Internet com a intenção de que nenhum outro crie software cliente ou servidor para esse serviço. Não existe necessidade de publicar e distribuir uma especificação formal para definir a interação, porque nenhuma aplicação externa precisaria entender os detalhes de protocolo. De fato, se a interação entre os dois aplicativos é suficientemente simples, pode até não haver um documento de protocolo interno.
- **Serviço padronizado.** Um serviço da Internet é definido com a expectativa de que muitos programadores criem o software servidor que oferece o serviço ou o software cliente para acessar o serviço. Em tais casos, o protocolo da camada de aplicação deve ser documentado independentemente de qualquer implementação. Além disso, a especificação deve ser precisa, e não ambígua, para que aplicativos cliente-servidor possam ser construídos de tal modo que se interoperem corretamente. (COMER 2016, p.46).

O comprimento de uma especificação de protocolo depende da complexidade do serviço. Uma especificação de serviço trivial cabe em uma página de texto. Por exemplo, o Internet Protocol inclui um serviço de aplicativo padronizado chamado DAYTIME que permite aos clientes consultar datas, locais e horários nos locais do servidor. O protocolo é simples:

Um cliente se conecta e desconecta de um servidor que envia uma representação ASCII da data e hora. Por exemplo, um servidor pode enviar uma string como essa: “Mon Sep 9 20:18:37 2013”. O cliente lê os dados de conexão até que um caractere de fim de arquivo seja encontrado.

Quadro 2: Principais protocolos da camada de aplicação

![Fonte: Bay e Bluning (2016 p.98).](https://paperx-dex-assets.s3.sa-east-1.amazonaws.com/images/1677704650029-JVtPclvKjt.png "Fonte: Bay e Bluning (2016 p.98).")

Fonte: Bay e Bluning (2016 p.98).

Um protocolo de camada de aplicativo padrão é criado para que os aplicativos de serviço padronizados trabalhem juntos, independentemente da implementação. Os aplicativos são a principal razão pela qual as redes de computadores existem. Para garantir que todos os aplicativos funcionem corretamente, foram desenvolvidos protocolos de comunicação para dar suporte aos aplicativos existentes. (Bay e Bluning, 2016)

**Conteúdo bônus**

**Tópicos avançados**

Recursos para a camada de aplicação: Firewall

Com um número cada vez maior de aplicações, a camada de aplicações tende a concentrar mais usuários que as demais camadas, o que a torna mais atrativa a ataques. Desta forma é preciso investigar, avaliar e assim poder elencar quais serão as táticas para que sejam protegidos os recursos oferecidos nesta camada.

Assim, fica claro que o uso de um bom firewall, em conjunto com outros sistemas, é cada vez mais necessário. Desta forma vamos conhecer mais sobre as opções de firewall e como são capazes de proteger as empresas e seus ativos digitais.

Disponível em: <[https://www.blockbit.com/pt/blog/firewall-de-rede-ou-de-aplicacao/](https://www.blockbit.com/pt/blog/firewall-de-rede-ou-de-aplicacao/)> Acesso em 31/01/2023

Observação: Este conteúdo não será cobrado nas avaliações e estará, obrigatoriamente, presente nas videoaulas. Fique tranquilo(a)!

Referência Bibliográfica

BARRETO, Jeanine dos Santos; ZANIN, Aline; SARAIVA, Maurício de Oliveira. **Fundamentos de redes de computadore**s. – Porto Alegre: SAGAH, 2018.

BAY; Edemilson; BLUNING, Paulo Henrique. **Fundamentos de redes de computadores**. UNIASSELVI, 2016.

COMER. Douglas. **Redes de computadores e internet**. – 6. ed. – Porto Alegre: Bookman, 2016.

QUINCOZEs, Vagner E; QUINCOZES, Silvio E; KAZIENKO, Juliano F. **Desvendando a Camada de Aplicação na Internet das Coisas: Teoria, Prática e Tendências**. 2022. Disponível em: <[https://sol.sbc.org.br/livros/index.php/sbc/catalog/download/78/338/595-1](https://sol.sbc.org.br/livros/index.php/sbc/catalog/download/78/338/595-1)> Acesso em: 01/10/2022.

VENTURY, Sidney Nicolau. **Fundamentos de rede de computadores**. Rio de Janeiro: SESES, 2016.