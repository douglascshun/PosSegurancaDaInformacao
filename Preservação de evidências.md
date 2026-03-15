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
	Registros de memória periférica, cace, etc...
	Processos em execução
	Discos, filesystems, partições
	