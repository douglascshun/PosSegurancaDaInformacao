[[Aula 8 Computação forense]]

	Cadeia de custódia de evidências

É um registro detalhado de como as evidências foram tratadas durante a análise forense, desde a coleta até os resultados finais.
Este registro deve conter informações sobre quem teve acesso ás evidências ou ás copias utilizadas.
Durante um processo judicial, este registro vai garantir que as provas não foram comprometidas. Cada evidência coletada deve ter um registro de custódia associada a ela.

Um registro deve conter pelo menos os seguintes itens:
- Data e hora de coleta da evidência
- De quem a evidência foi apreendida
- Informações sobre o hardware, como fabricante, modelo, numero de serie ...
- Nome da pessoa que coletou a evidência
- Descrição detalhada da evidência
- Nome e assinatura das pessoas envolvidas
- Identificação do caso e identificação de evidencia (tags)
- Assinatura MD5/SHA1 das evidências, se possível 
- Informações técnicas pertinentes


		Ordem de coleta de evidências:
	
	Registros de memória periférica, cache, etc...
	Memoria do Kernel e física
	Estado da rede, rotas, interfaces, etc..
	Processos em execução
	Discos, file systems, partições
	Floppies, fitas e outros meios magnéticos
	CD-ROMs, cópias impressas, etc...

		Ordem de pertubação do sistema computacional quando se executa um binario 
	
	Shell e variáveis de ambiente 
	Comando ou programa 
	Bibliotecas dinâmicas
	Device drivers
	Kernel 
	Controladoras
	Hardware

Entre os métodos a serem aplicados na correlação de eventos, pode-se citar, em ordem de importância, os seguintes procedimentos e técnicas, bem como algumas questões associadas a eles:
- Reconstrução do histórico dos usuários e suas operações
- Reconstrução do histórico dos processos executados, ou em execução
- Reconstrução da situação das conexões de rede e roteamento 
- Arquivos dos registros de auditoria (logs)
- Horários de acesso (ou modificação) de arquivos ou diretórios
- Network Sniffing (se possível)


		Reconstrução do histórico dos usuários e suas operações
	- Quais usuários acessaram o sistema numa determinada hora?
	- Qual foi o padrão de uso de uma conta em particular?
	- Qual o Username, terminal e hora de inicio da sessão de cada processo?
	- Qual a quantidade de uso de memória e CPU?
	- Quais as linhas de comando de chamada do processo?
	- Qual o estado do processo no momento ? (running, sleeping, suspended, dead, etc...)?
	- Quais os comando executados por um processo específico?

		`Reconstrução da situação das conexões de rede e roteamento
	- Qual a data, horário e destino da conexão?
	- Qual nome do processo de rede e seu ID?
	- Qual o host cliente?

		`Arquivos dos registros de auditoria (logs)
	- Quais as conexões de, e para, um site específico?
	- Quais as conexões para um serviço específico (exemplo telnet ou ftpd)?
	- Quais as sequências sucessivas de conexão de um site (exemplo, finger seguido de telnet)?
	- Quais as conexões ocorridas num intervalo de tempo?

	`Horários de acesso (ou modificação) de arquivos ou diretórios (M/A/C/times)
	- mtime = modification time
	- ctime = access time
	- ctime = status change time 
	- dtime = deletion time (presente em alguns linux)