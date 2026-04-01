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
	Hardware seguro, um chip físico segregado ou um núcleo seguro dentro de uma CPU
