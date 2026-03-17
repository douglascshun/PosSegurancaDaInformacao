[[Aula 5 Protocolos de Comunicação]]

# Principais funções dos protocolos na comunicação de rede

- `Endereçamento:` Define o ponto de destino do pacote.
Ex: 192.168.... para www.pipipipopopo.com

- `Numeração:` Identifica cada pacote por meio de uma numeração sequencial.
Para reconstrução do que foi baixado, ou enviado.

- `Conexão:` Estabelece a conexão por meio de um túnel lógico fechado que liga o remetente e o destinatário do pacote.

- `Controle de erros:` Identifica os erros da comunicação e faz a correção.

- `Confirmação:` Envia um sinal informando quando cada segmento da mensagem é recebido de maneira íntegra.
Feito pelo TCP e não é feito pelo UDP, não esquecer Douglas!!!!

- `Conversão:` Converte o código e o adapta às características do dispositivo destinatário.

Os protocolos de rede, ou de internet, são utilizados na comunicação e envolvem conjuntos de regras que servem para controlar e regular a comunicação, a conexão e a transferência de dados entre dispositivos e/ou sistemas computacionais.

Protocolos criam regras na comunicação de rede, mas isso é importante pense em um idioma...

A definição do idioma no qual a comunicação vai ser feita é um exemplo de regra que é preciso estabelecer, por exemplo, ao conversar com um amigo que mora no exterior. 

Em outras palavras, os protocolos são utilizados na rede para que as máquinas e os sistemas possam se comunicar, por mais que elas tenham configurações diferentes entre si, definindo a maneira como a comunicação e a troca de dados vai ser realizada.

Em uma rede local que não tenha acesso à Internet, por exemplo, os usuários podem compartilhar seus arquivos, pastas, impressoras, entre outros Com a utilização da Internet, as possibilidades de compartilhamento de recursos entre as máquinas de das redes de computadores só aumentaram, possibilitando a troca de informações com qualquer computador do mundo que esteja conectado a ela.

Toda essa estrutura e essas funcionalidades são possíveis devido aos protocolos de rede!

# Camada de Aplicação

Em uma rede, a camada de aplicação é aquela que fica mais perto do usuário, pois as aplicações utilizadas por ele utilizam os protocolos que ficam nessa camada, de acordo com a finalidade do programa que o usuário estão utilizando, seja correio eletrônico, videoconferência, rede social, editor de texto, entre outras...

# Camada de Transporte 

Depois que a requisição de um programa é processada, o protocolo da camada de aplicação vai se comunicar com o protocolo da camada de transporte, que geralmente é o TCP, UDP, ou protocolo de data-gramas do usuário.

`Protocolo TCP:` Após montar o pacote recebido, envia confirmação de entrega.

`Protocolo UDP:` Usado em Streaming onde não é preciso confirmar entregas "não confiável".

# Camada de Internet

Nessa camada, o principal protocolo é o IP. Ele é utilizado para incluir, nos segmentos recebidos da camada de transporte, tanto o endereço do computador remetente de um pacote como também o endereço do computador destinatário do pacote. Isso é feito porque, para que um dispositivo tenha acesso à internet, é preciso que ele tenha um endereço IP. Depois disso, os pacotes são enviados para a camada de interface de rede.

# Camada de Interface de Rede 

Essa camada é responsável por receber os pacotes enviados pela camada de Internet, enviando-os para a rede ou recebendo-os da rede, caso o dispositivo seja o destinatário dos dados. Nessa camada, também são identificados e corrigidos os erros do nível físico e é feito o controle de fluxo entre a transmissão e a recepção dos pacotes.


