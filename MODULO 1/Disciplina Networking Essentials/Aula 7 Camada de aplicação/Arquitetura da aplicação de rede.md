[[Aula 7 Camada de aplicação]]

## Arquitetura da Aplicação de Rede

Segundo `kurose and Ross 2010 apud Quincozes, quincozes E kazlenko 2022, p.257`, uma arquitetura de aplicação de rede determina a forma como a aplicação é organizada nos sistemas finais, além de ser projetada pelo desenvolvedor da aplicação.

É diferente de arquitetura de rede, que é algo engessado do ponto de vista do desenvolvedor, fornecendo um conjunto específico de serviços às aplicações.

Essas arquiteturas definem a forma de comunicação entre as partes envolvidas. As arquiteturas de aplicação de rede mais adotadas na camada de aplicação são da IoT.

`Cliente - Server`
Em português, é denominado como cliente-servidor. Essa arquitetura consiste em uma aplicação distribuída que compartilha tarefas e cargas de trabalho entre os provedores de recursos (i. e servidores) e os (i. e. clientes).

`peer-to-peer` 
Esse paradigma também é conhecido como par-a-par (ou P2P). Nele, cada um dos dispositivos que compõem a rede funciona tanto como cliente quanto como servidor.

Por exemplo, no torrent vários usuários podem realizar a conexão e transmitir arquivos, sem a necessidade de uma fonte intermediária para baixar os arquivos.

`Pulish-subscribe`
Também conhecido por publicação-assinatura, esse paradigma é composto por três componentes principais, sendo eles um `publicador`, um `assinante` e um `servidor centralizado (ou broker)`. Basicamente, o broker é composto por tópicos.

Os dispositivos publicadores são responsáveis por alimentar os tópicos do broker. Já os assinantes, são dispositivos interessados nas informações contidas nos tópicos, que assinam os mesmo para receber tais informações.

Vale ressaltar que um broker pode conter múltiplos tópicos. Cada um deles pode receber mensagens de diversos dispositivos publicadores, as quais são entregues para todos os dispositivos que assinam aquele tópico.

	Os protovolos da camada de aplicação podem utilizar tais arquiteturas. Desse modo, é de extrema importância, entendê-las para auxiliar na tomada de decisões no momento da implementação de novas aplicações IoT.

Por exemplo, o protocolo MQTT é baseado na arquitetura publish-subscribe.