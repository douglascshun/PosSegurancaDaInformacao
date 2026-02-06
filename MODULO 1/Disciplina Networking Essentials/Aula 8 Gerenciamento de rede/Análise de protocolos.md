[[Aula 8 Gerenciamento de rede]]

# Análise de protocolos

Os analisadores de protocolo são ferramentas que observam o tráfego de informações dentro da rede em que estes softwares estão conectados. Ao utilizar aplicações desse tipo, a interface de rede do dispositivo passa a capturar todos os pacotes que estão circulando dentro da rede. 

## WireShark:

![[WireSharkExemploScanner.png]]


	Na imagem, é possível perceber todos os pacotes que estão circulando dentro da rede. A própria aplicação já realiza um pré-agrupamento dos dados baseado no seu protocolo de comunicação, com a finalidade de auxiliar o administrador de rede no momento da interpretação dos dados colhidos pela ferramenta.


Essa manipulação de dados é popularmente conhecida como `escovar os bits`, pois o administrador está colhendo pacotes dentro da rede, os quais são formados somente por bits e, dessa maneira, precisa tratar os dados colhidos para que os mesmos venham a ser úteis.

Ao utilizar um analisador de protocolos, o administrador pode medir seu tráfego de rede médio, para que seus usuários estão utilizando a rede, quais host's estão realizando maior movimentação de informações no momento, entre outras funcionalidades.

`Baseando-se nestas informações`, é possível tomar decisões administrativas com a intenção de expansão de rede, bloqueis de conteúdo e formas de garantir a segurança da informação.

Estes analisadores são importantes ferramentas de gestão, pois através delas o administrador de rede tem total conhecimento do que está acontecendo dentro de sua rede e a partir daí pode tomar decisões para correções de problemas e ações preventivas para antecipar e minimizar possíveis problemas futuros.

