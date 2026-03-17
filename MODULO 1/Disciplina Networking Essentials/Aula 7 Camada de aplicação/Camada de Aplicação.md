[[Aula 7 Camada de aplicação]]

A primeira camada do ponto de vista do usuário.


# Sumário
##  1 - A camada de Aplicação
Principais conceitos de comunicação de dados.

##  2 - Funcionalidades da Camada de Aplicação
Como os dados são transmitidos?
Assim, nascem as redes!


##  3 -  Arquitetura da Aplicação de Rede
Diferentes conceitos e formas de transmissão.

##  4 - Protocolos da Camada de Aplicação
Como é construída a velocidade e o ping das conexões?


##   5 - Exemplos de Sistemas 
Observando as diferentes situações e seu impacto em relação a velocidade de transmissão.

# A camada de aplicação

A camada de aplicação é a camada mais próxima do usuário!

A camada de aplicação não fornece serviços a nenhuma outra camada, no entanto ela forne serviços aos processos de aplicação de usuários como programas de planilhas, programas de processamento de textos e programas de terminais bancários.

Em um ambiente LAN,  suporte de rede de aplicações indiretas é uma função cliente-servidor.

Se um cliente quiser salvar um arquivo de processador de texto em um servidor da rede, o redirecionador permitirá que a aplicação processadora de texto se torne um cliente da rede.

O `redicionador` é um protocolo que trabalha com sistemas operacionais de computadores e clientes de rede ao invés de programas de aplicações específicos. O processo do redirecionador é o seguinte:

- 1. O cliente solicita que o servidor de arquivo da rede permita que o arquivo de dados seja armazenado.

- 2. O servidor responde salvando o arquivo no seu disco ou rejeitando a solicitação do cliente.

O redirecionador permite que um administrador de rede atribua recursos remotos a nomes lógicos no cliente local.

Quando você selecionar um desses nomes lógicos para realizar uma operação, como salvar ou imprimir um arquivo, o redirecionador da rede enviará o arquivo selecionado ao recurso remoto apropriado na rede para o processamento. Se o recurso estiver em um computador local, o redirecionador ignorará a solicitação e permitirá que o sistema operacional local processe a solicitação.

A vantagem de usar um redirecionador de rede em um cliente local é que as aplicações no cliente nunca precisam reconhecer a rede.

Além disso, a aplicação que solicita serviço está localizada no computador local e o redirecionador rodeia novamente a solicitação para o recurso de rede apropriado, enquanto a aplicação trata-a como uma solicitação local.

A camada de Aplicação usa o HTTP para encaminhar as solicitações dos usuários:

O HTTP (Hyper Text Transfer Protocol), o qual o envia o nome da página que o usuário deseja acessar para o servidor detentor da página. Então, o servidor recebe esta transmissão e envia as informações da página para que o navegador do usuário possa realizar a apresentação do site. Todo este processo ocorre utilizando o protocolo HTTP.

Nome vira IP, Localiza o servidor, o servidor envia o pacote de exibição do site e a pessoa exibe o site em sua tela..