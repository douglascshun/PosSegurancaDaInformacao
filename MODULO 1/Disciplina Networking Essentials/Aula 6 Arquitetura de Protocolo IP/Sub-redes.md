[[Aula 6 Arquitetura de Protocolo IP]]

`Todo dispositivo conectado é conectado a uma rede!`

Uma Sub-rede nada mais é do que uma rede que foi dividida diversas vezes, onde cada fragmento dessa divisão deu origem a uma nova rede, independentemente da quantidade de vezes em que a rede inicial foi dividida.

Este conceito de sub-rede surgiu com a necessidade de economizar os endereços de rede, onde é possível de uma rede fazer várias outras, e assim realizar a distribuição destas diferentes redes para diferentes locais sem que haja endereços IPs desperdiçados, ou seja alocando uma rede inteira para um ou dois host's.

Assim, as alterações somente terão efeito dentro da rede local, onde as subdivisões realmente terão o efeito programado, isolando o tráfego entre as redes criadas e não permitindo acesso direto entre as sub-redes, por mais que as mesmas estejam utilizando os mesmo meio físicos para realizar as transmissões dos seus dados.

Para implementar a divisão em sub-redes é necessária a utilização de uma máscara de Sub-rede, pois é ela que realiza a divisão entre o número de rede, mais Sub-rede e o host. Estas máscaras de Sub-rede também são escritas em notação decimal com pontos, com a inclusão de uma barra vertical seguida pelo número de bits na parte de rede mais Sub-rede.

Sendo assim, a subdivisão de uma rede acontece da seguinte forma: partindo da rede inicial 192.168.1.0/24, que baseado no que estudamos até o momento, sabemos que possuí 256 endereços, sendo 254 disponíveis para host, pede-se para dividir esta rede em seis novas Sub-redes quye possam alocar 30 host's em cada uma delas.

