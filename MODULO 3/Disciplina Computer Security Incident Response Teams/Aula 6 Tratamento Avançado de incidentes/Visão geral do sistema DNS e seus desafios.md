[[Aula 6 Tratamento Avançado de incidentes]]

DNS = Banco de dados
	O sistema DNS e os banco de dados Whois são 2 serviços de diretório amplamente usados na internet

Todo servidor de informações públicas deve ser considerado `não confivel`.
	É possível `disfarçar` um outro sistema como um servidor DNS.


Ataques de DNS
	`TUDO` é acessado pelo DNS quando recursos estão na nuvem

Ameaças com o Serviço DNS
![[Ameaças com o Serviço DNS.png]]

Principais Ataques de DNS inclem:
	- Envenenamento de DNS
	- DNS Spoofing
	- Sequestro de domínio 
	- Captura de domínio 
	- Cybersquatting

Como é envenenado o DNS
	- O DNS é enganado, fazendo-o acreditar que recebeu informações autênticas
	- As informações geralmente são armazenadas em cache por um tempo
	- Espalha os efeitos do ataque aos usuários do servidor
	- O Hacker pode usar o seu próprio domínio e DNS hackeado

Alguns métodos de defesa contra o envenenamento de DNS
	- DNSSEC e NXDOMAIN
	- Auditar servidores DNS por vulnerabilidades
	- Evitar porta de saída UDO 53

Sequestro de servidores DNS
	Redireciona os clientes para um site falso para a coleta de dados confif