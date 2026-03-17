[[Aula 6 Arquitetura de Protocolo IP]]

Dentro de uma rede de computadores, cada dispositivo, ativo de rede para se comunicar com outro ativo e realizar o encaminhamento dos pacotes ou mesmo gerar pacotes, obrigatoriamente necessita possuir um IP.

`O que faz o IP?`
O endereço IP é responsável por realizar a sincronização entre os host's no sentido de que ambos estejam alocados próximos no sentido lógico da rede para que assim possam vir a se comunicar.

Sendo assim, cada ativo de rede deve possuir uma interface de rede, lógica ou física. Esta interface de rede é a fronteira entre o o host em si e camada de rede, e é ela que realizará toda a transferência do dado gerado pelo host em questão para o meio físico onde o mesmo está conectado. 

Cada endereço IP tem o comprimento de 32 bits (equivalente a 4 bytes). Portanto, há um total de 232 endereços IP possíveis. Fazendo uma aproximação de 210 por 103, é fácil ver que há cerca de 4 bilhões de endereços IP possíveis.

Esses endereços são escritos em notação decimal separada por pontos no qual cada byte do endereço é escrito em sua forma decimal e separado dos outros bytes do endereço por um ponto.

Sendo assim, cada interface de cada host, roteador ou qualquer outro ativo de rede deve possuir um endereço IP para que possa se comunicar com os demais equipamentos.

Porém, para adicionar um IP a uma interface, o mesmo não pode ser feito de forma aleatória: é preciso respeitar a Sub-rede em que o host está locado.

Os endereços IP são hierárquicos, diferentemente dos endereços Ethernet. Cada endereço de 32 bits é composto de uma parte de rede de tamanho variável nos bits superiores e uma parte de host nos bits inferiores.

A parte de rede tem o mesmo valor para todos os host's em uma única rede. Isso significa que uma rede corresponde a um bloco contínuo de espaços de endereços IP. Este bloco de endereço fixo e comum a todos os host's é denominado prefixo.

