[[Aula 6 Segurança de Endpoint]] 

TCB (Trusted Computing Base) ou Base de Computação Confiável 

- Conjunto de Hardware, firmware e/ou software que são críticos para sua segurança.
- Bugs ou vulnerabilidades dentro do TCB podem comprometer a segurança de todo o ecossistema.
- Falhas de segurança fora do TCB não devem ser capazes de vazar mais privilégio do que os concedidos a eles para o funcionamento do ecossistema.
![[TCB.png]]

O que é?
Conjunto de Hardware, software e protocolos que garantem a integridade do endpoint
	Executa autenticação, mutua com redes pareadas e gerencia a segurança das comunicações e das aplicações


Funções principais
	- Validação de imagem para execução
	- Autenticação mútua de redes pareadas
	- Separação de tarefas dentro da arquitetura de segurança em IoT
	- Provisionamento e personalização
	- Segurança de ambientes isolados

# Implementar uma TCB

Modelos de âncoras de confiança
	Tecnologias de hardware seguro que armazena e processa senhas criptografadas
		- Texto claro 
		- Chave Pré-compartilhada (PSK) -Criptografia Assimétrica 
		- Chave Pública/Privada (Criptografia Simétrica)

Por que é importante?
	Garante que as comunicações entre a âncora de confiança, a aplicação principal e as redes pareadas sejam seguras, protegidas e atualizadas

# Utilizar uma âncora de confiança

O que é?
	- Hardware seguro, um chip físico segregado ou um núcleo seguro dentro de uma CPU
	- Capaz de armazenar e processar com segurança senhas criptografadas

Funções principais
	- Determinar com segurança se as mensagens e identidades podem ser autenticadas 
	- Ser capaz de informar com segurança à TCB o resultado de todas as operações de autenticação ou criptografia

Porque é importante?
	- Possibilidade de um invasor roubar chaves relevantes para todo o ecossistema de IoT
		- Clonar identidades de endpoint 
		- Falsificar serviços de IoT
		- Distribuir serviços de IoT
		- Distribuir patches e atualizações maliciosas
		- Fazer alterações não autorizadas no software do endpoint 

# Utilizar uma API para o TCB

O que é?
	Serviço para acessar as funções do TCB

Por que é importante?
	Garante a integridade do ecossistema 

Funções principais, garantem que:
	- Toda verificação de assinatura é executada pelo TCB
	- Nenhuma chave privada do TCB é exposta 
	- Troca de chaves pode ser realizado pelo TCB em nome da aplicação
	- Criptografia e descriptografia de devem ser rexecutadaos pelo TCB
	- A assinatura de mensagens deve ser executado no TCB
	- O preenchimento seguro de mensagens deve ser realizado no TCB
	-  Confidencialidade e integridade entre o TCB e a aplicação

# Ameaças

Ameaça de Falsificação
![[Ameaça de Falsificação.png]]


Ameaça de Adulteração
![[Ameaça de Adulteração.png]]


Ameaça de Repúdio
![[Ameaça de Repúdio.png]]


Ameaça de Violação de dados (Divulgar informações)
![[Ameaça de Violação de dados.png]]


Ameaça de Negação de Serviço (DOS - Denial of Service)
![[Ameaça de Negação de Serviço.png]]


Ameaça de Elevação de Privilégios
![[Ameaça de Elevação de Privilégios.png]]


Ameaça do gerenciamento de endpoints sem suporte
![[Ameaça do gerenciamento de endpoints sem suporte.png]]