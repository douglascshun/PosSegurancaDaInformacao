[[Aula 7 Camada de aplicação]]

No modelo TCP/IP, essa camada é equivalente à combinação das camadas de sessão, de apresentação e de aplicação no modelo OSI. É a partir dela que muitos protocolos são definidos.

Antes de falar da camada de aplicação é preciso mencionar que entre essa camada e a de transporte existem, no modelo OSI, outras duas camadas, responsáveis pelo gerenciamento de uma sessão (a camada de sessão) e pelo gerenciamento do perfil dessa sessão (a camada de apresentação).

## Transferência de arquivos

O serviço de transferências de arquivos permite aos usuários movimentar (carregar ou depositar) arquivos de uma máquina para outra. Aplicativos dessa categoria incluem o ftp (ou sftp por razões de segurança) e, hoje em dia, navegadores web.


## Troca de mensagens

Esse serviço consiste em permitir que usuários se comuniquem de forma assíncrona através de mensagens de texto (com ou sem imagens ou outros arquivos anexados). Esse serviço é provido por aplicativos como e-mail, usenet news(muito tempo atrás) e twitter, entre outros.

Para e-mails o envio de uma mensagem exige que as máquinas que representam os endereços fonte e destino se conectem para que o envio da mensagem ocorra de fato.

## Acesso remoto 

Permite aos usuários acessarem máquinas remotamente.

Os maiores problemas de acesso remoto estão ligados à `segurança e ao fornecimento de um ambiente de trabalho confortável ao usuário.` A segurança envolve aspectos bastante específicos e não serão tratados aqui e o ambiente de trabalho envolve o fornecimento de características de conversão entre terminais gráficos, que serão tratados no próximo item. Aplicativos desse tipo incluem telnet (que deve ser evitado) e ssh, entre outros.

## Execução remota 

Serviços de execução remota são, na realidade, uma especialização do serviço de acesso remoto em que o usuário apenas solicita que ma determinada tarefa seja executada remotamente.

Eles são uma das características determinantes de sistemas distribuídos, sendo representados, por exemplo pelo serviço de RPC (Remote Procedure Call) ou de RMI (Remote Method Invocation em Java).

## Terminal virtual

Como dito acima, o serviço de terminal virtual consiste em fornecer ao usuário um ambiente em que ele possa fazer acesso remoto à uma determinada máquina, através da conversão de controles específicos de interface (tela, teclado, mouse, etc..) da maquina em que está fisicamente o usuário e a máquina que ele acessa remotamente. Terminais virtuais incluem xterm, vt100, etc.

## Segurança 

Fornecimento de meios de controle de acesso aos serviços de rede. Isso implica em controlar a autenticação dos usuários e das permissões de acesso que esses usuários terão aos conteúdos disponíveis na rede.