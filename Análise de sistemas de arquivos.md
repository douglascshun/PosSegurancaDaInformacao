[[Aula 8 Pensamento crítico]]

Sistemas de arquivos é um método e estrutura de dados que o sistema operacional usa para controlar como os dados são armazenados e recuperados.


	Dados não voláteis 

São dados que podem podem permanecer na máquina durante longos períodos de tempo e podem ser recuperados mesmo após a mesma ser deligada.


	MACtimes são informações cronológicas e atributos de tempo de um arquivo

mtime (Modification time): Mostra a última data e hora em que o arquivo foi modificado.

atime (Access time): mostra a última data e hora em que um diretório ou arquivo foi acessado/lido.

ctime (Creation time): mostra a data e a hora que o arquivo foi criado

	MACtimes podem ser coletados bastante tempo depois de um incidente, porém são muito efêmeros.

![[MACtime.png]]

A simples abertura de um diretório ou arquivo mudará o seu atime, assim como algumas ferramentas de gerenciamento de arquv