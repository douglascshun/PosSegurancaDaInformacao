[[Aula 4 Modelos de rede]]

## Funcionalidades de Cada Camada 

Entre o modelo TCP/IP e o modelo OSI existem semelhanças e diferenças, portanto, vamos compreender esta dinâmica na construção de redes.

## modelos de referência para Redes:

	 OSI
	 TCP/IP

## Camadas do Modelo TCP/IP

### Camada Internet: 

Toda a evolução das redes de computadores, com a interligação das redes, tornou necessário o desenvolvimento de uma forma com que host's pudessem vir a se comunicar com todos os host's conectados em qualquer rede à qual estivessem conectados.

### Camada de transporte: existe nos dois modelos: OSI E TCP/IP

É ela que é responsável pela comunicação fim a fim existente entre os host's de uma rede, ou seja, é esta camada que realiza a sincronização de conexão e determina como serão realizadas as transmissões entre os host's envolvidos.

Para tanto, foram desenvolvidos dois protocolos de comunicação utilizados por esta camada, o protocolo TCP (Transmission Control Procolo)
 e o protocolo UDP (User Datagram Procol).

### Camada de Acesso à Rede:

A camada de acesso à rede é responsável pela conexão física do dispositivo, ou seja faz a inserção das informações a serem transmitidas dentro do meio de comunicação, realizando as funções das camadas de enlace e física do modelo OSI.

Conexão física entre os elementos de rede!

## Camada Física:

Coordena as funções exigidas com a finalidade de transportar um fluxo determinado de bits em meio físico. 

## Camada de enlace:

Codifica a camada anterior de um recurso de transmissão bruto em um link confiável. A partir dos dados emitidos pela camada anterior, ela codifica os dados para que a próxima camada se utilize dos dados que foram fornecidos na sequência. 

## Camada de Rede:

Envia um pacote desde a sua origem até o seu destino. Possivelmente esse envio passará por diversas redes (links). Enquanto a camada de enlace monitora o envio de pacote no sistema, a camada de rede deve assegurar-se de que os dados sairão do seu destino e chegarão ao local necessário. 

## Camada de Sessão:

Realiza o diálogo que há na rede. Também é sua função estabelecer, manter e sincronizar a interação que existe entre os sistemas que se comunicam. 

## Camada de Aplicação:

Permite acesso à rede, portanto para usuário final quanto para o software. Esta camada fornece também uma interface tanto de usuário como de suporte para serviços como correio eletrônico, gerenciamento de dados compartilhados, entre outros. 