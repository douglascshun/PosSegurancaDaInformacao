[[Aula 5 Protocolos de Comunicação]]

Muitos são os serviços que os protocolos de rede são capazes de oferecer. Basicamente, eles poder ser classificados em:
- Serviços de rede na Internet
- Serviços de rede Cliente-Servidor
- Serviços de rede WAN

A Internet oferece uma grande quantidade de recursos e possibilidades de uso que vão do e-mail e do acesso a páginas Web ao vídeo em tempo real e ao compartilhamento de arquivos de sistemas peer-to-peer. Todas essas possibilidades de uso são construídas  a partir de um conceito relativamente simples: o serviço de rede.

Um serviço de rede pode ser visto como uma aplicação distribuída, que executa em dois ou mais computadores conectados por uma rede 

Cada serviço de rede é composto por ao menos quatro elementos.

`Servidor:`  Computador que realiza a parte principal do serviço, usando seus recursos locais e /ou outros serviços.

`Cliente:` Computador que solicita o serviço através da rede geralmente o cliente age a pedido de um ser humano, através de uma interface de usuário, mas ele também pode ser o representante de outro sistema computacional.

`Protocolo:` É a definição do serviço propriamente dito, ou seja, os passos, o conjunto de mensagens e os formatos de dados que definem o diálogo necessário entre o cliente e o servidor para realização do serviço

`Middleware:` É o suporte de execução e de comunicação que permite a construção do serviço. Em geral o middleware é composto por sistemas operacionais e protocolos de rede encarregados de encaminhar os pedidos do cliente para o servidor e as respostas de volta ao cliente. 

### As arquiteturas de serviços de rede são:

- Two-Tier 
- Peer-to-Peer

### Arquitetura Two-Tier

Esta arquitetura tem dois componentes:
`Servidor`, responsável pela execução do serviço.
`Cliente`, responsável pela apresentação dos resultados e interação com o usuário.

Alguns clientes se preocupam somente com a apresentação dos dados e outros tem responsabilidades por parte lógica da aplicação.

Nesta arquitetura os participantes são ao mesmo tempo servidores (oferecem serviços e recursos) e clientes (usam serviços e recursos) uns dos outros. Muitos serviços de compartilhamento de arquivos e de comunicação entre usuários se estruturam dessa forma.

### Exemplo de rede ponto a ponto
![[Exemplo de rede ponto a ponto.png]]

A maioria dos serviços habituais em redes IP usa TCP ou uDP como suporte de comunicação. Esse é o caso de serviços como WWW, E-mail, sistemas peer-to-peer e de voz sobre IP.

Alguns serviços de rede podem fazer uso de suportes de comunicação mais sofisticados, construídos como camadas acima do TCP ou UDP. Esse é o caso dos serviços baseados em RPC (Remote Procedure Call), dos Web Services e dos ambientes de objetos distribuídos como Java RMI (Remote Method Invocation) e  CORBA.

Muitas vezes os números de portas usados não são padronizados e podem variar de uma execução para a outra, o que pode dificultar a criação de regras de filtragem (firewall) para esses serviços.