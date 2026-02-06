[[Aula 6 Arquitetura de Protocolo IP]]

# Sumário
### 1 - O Protocolo IP  e seu Datagrama
Muito além do CPF dos computadores

### 2 - IPv4 e IPv6 
Existem dois padrões, mas um deve aposentar em breve 

### 3 - IPv4: Endereçamento 
Qual a limitação do IPv4 determinou sua aposentadoria?

### 4 - Sub-redes 
Conceito e aplicações das sub-redes.

### 5 - Implementação do IPv6 
Como está sendo migrado o IP para a versão IPv6?




# O protocolo IP e seu datagrama

O protocolo de internet ou Internet Protocol (IP), em inglês, é um mecanismo de comunicação que é utilizado em todas as máquinas que estão conectadas em rede por meio dos protocolos TCP/IP para efetuar encaminhamento de dados.

Nos protocolos TCP/IP, o protocolo IP fica situado na camada que é chamada de camada de rede.

# Posição do protocolo IP dentro dos protocolos TCP/IP

![[Posição do protocolo IP dentro dos protocolos TCP IP.png]]

O Protocolo IP é um serviço de envio de dados que utiliza a regra do melhor esforço, ou seja, `seu datagrama é sem conexão e não confiável.` Quando se fala em melhor esforço, o que pretende dizer é que o protocolo IP  não oferece nenhum tipo de verificação ou validação de entrega, tampouco oferece monitoramento para os erros. 

Ao utilizar o protocolo IP, sabe-se que não existe uma garantia de confiabilidade e que, apesar de esse protocolo fazer o possível para que o pacote seja transmitido desde o remetente até o seu destinatário, não haverá garantias de que isso acontecerá de forma íntegra.

	se a entrega tem que ser garantida, o protocolo IP deve ser combinado com outro protocolo do tipo confiável.

No protocolo IP, cada datagrama é trabalhado de maneira independente, podendo tomar rumos diferentes até encontrar o seu destinatário. Isso significa dizer que datagramas que forem enviados do mesmo remetente podem chegar de maneira desordenada ao seu destinatário.

Um datagrama consiste em um pacote que tem comprimento variável e é formado por duas partes, que são o cabeçalho e os dados. O cabeçalho pode ter de 20 a 60 bytes de comprimento e deve conter informações fundamentais para o roteamento e para o envio do pacote.

