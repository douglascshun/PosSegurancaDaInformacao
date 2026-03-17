[[Cybersecurity Essentials]]
## Resolução de Problemas usando Cisco Packet Tracer

**Introdução**

O Cisco Packet Tracer é uma ferramenta de simulação de redes que nos permite experimentar conceitos de comunicação e que são a base para compreender ataques de segurança que ocorrem em redes de computadores.

**Objetivos da aula**

- Instalar o Cisco Packet Tracer;
- Utilizar o Cisco Packet Tracer para construir um exemplo de rede com dois computadores;
- Utilizar o Cisco Packet Tracer para construir um exemplo de rede com quatro computadores.

**Resumo**

O Cisco Packet Tracer é um simulador de redes desenvolvido pela empresa Cisco com uso gratuito. Esta ferramenta permite a simulação de equipamentos de rede como roteadores, gerenciamento de dispositivos clientes como dispositivos móveis, _tablets_ e computadores. Para realizar uma simulação, é necessário adicionar os nós (equipamentos clientes e de rede) e como estes equipamentos se conectam para realizar uma comunicação, ou seja, devemos especificar a topologia da rede utilizada.

O uso de um simulador é justificado pelo seu baixo custo associado, facilidade de instalação, quando comparado com equipamentos reais, e facilidade de reprodução de resultados (também denominado reprodutibilidade). É um ambiente virtual que imita o comportamento real e pode ter limitações em relação a quão fidedigno é seu comportamento quando comparado ao real, mas de forma geral seus benefícios são maiores que suas limitações, principalmente, para iniciantes em redes e segurança da informação.

Mas afinal, o que redes e comunicação tem a ver com segurança da informação? Lembrando do cenário hipotético com Alice, Bob e Carlos com envio de e-mail, é possível observar que todos os cenários de ataque ocorreram durante uma comunicação, e isto não é por acaso. Entender a comunicação em uma rede e conseguir diagnosticar situações é um primeiro passo para entender os possíveis ataques e contramedidas.

Afinal de contas, não é possível compreender os ataques possíveis a um sistema de e-mail, se você não entender como o envio de um e-mail de Alice para Bob funciona.

Para instalar o Cisco Packet Tracer, acesse [https://netacad.com/pt-br](https://netacad.com/pt-br). 

Em cursos, vá até Packet Tracer (vide Figura 1).

Figura 1 – Acesso ao Packet Tracer

![Fonte: Autoria própria, 2022.](https://paperx-dex-assets.s3.sa-east-1.amazonaws.com/images/1674140170252-1ukOZ9xO95.png "Fonte: Autoria própria, 2022.")

Fonte: Autoria própria, 2022.

Na janela que irá se abrir, encontre o curso “Getting Started with Cisco Packet Tracer” (vide Figura 2).

Figura 2 – Curso do Cisco Packet Tracer

![Fonte: Autoria própria, 2022.](https://paperx-dex-assets.s3.sa-east-1.amazonaws.com/images/1674140110988-qkzaAK8cxJ.png "Fonte: Autoria própria, 2022.")

Fonte: Autoria própria, 2022.

Na próxima janela, acesse usando sua conta do Google ou crie uma conta na plataforma da Cisco (vide Figura 3).

Figura 3 – Acesso à plataforma

![](https://paperx-dex-assets.s3.sa-east-1.amazonaws.com/images/1674140092297-uqixuFzGzc.png)

Na próxima janela, selecione o instalador compatível com seu sistema operacional (vide Figura 4).

Figura 4 – Cenário de aplicação do firewall

![Fonte: Autoria própria, 2022.](https://paperx-dex-assets.s3.sa-east-1.amazonaws.com/images/1674140076028-SP3oXbLIYF.png "Fonte: Autoria própria, 2022.")

Fonte: Autoria própria, 2022.

Realize a instalação e após abrir o programa, configure sua área de trabalho conforme a Figura 5 para facilitar a visualização.

Figura 5 – Configurações no menu de Preferências

![Fonte: Autoria própria, 2022.](https://paperx-dex-assets.s3.sa-east-1.amazonaws.com/images/1674140063868-poad4j1ia1.png "Fonte: Autoria própria, 2022.")

Fonte: Autoria própria, 2022.

No menu inicial do programa, é possível fazer seleções do tipo drag and drop para adicionar os componentes de rede (roteador 2620XM e switch 2950-24), além do equipamento cliente (PC-PT). Para conectar os componentes, utilize o ícone de estrela nas conexões possíveis. Clique duas vezes em cada componente para configurá-lo, de forma que o IP 192.168.1.1 esteja alocado para o roteador, e o endereço 192.168.1.2 esteja alocado para o computador (PC0). Vide Figura 8 para referência.

Sabendo que ping é um comando para verificar se um equipamento em um endereço IP específico está respondendo na rede, realize também o ping no endereço 192.168.1.1 (endereço do roteador) a partir do computador PC0. Os resultados podem ser observados na Figura 6.

Figura 6 – Exemplo de rede com um computador

![Fonte: Autoria própria, 2022.](https://paperx-dex-assets.s3.sa-east-1.amazonaws.com/images/1674140035814-5fMa4tnIxH.png "Fonte: Autoria própria, 2022.")

Fonte: Autoria própria, 2022.

Adicione mais um computador (PC-PT) na rede e a ele atribua o endereço 192.168.1.3 (clique duas vezes no componente para configurá-lo). Novamente, para conectar os componentes, utilize o ícone de estrela nas conexões possíveis. Clique duas vezes em cada componente para configurá-lo. Agora, realize o ping a partir de PC0 para o novo computador PC1 que está no endereço 192.168.1.3. Vide a Figura 7 para referência.

Adicione mais dois dispositivos clientes na rede: dois equipamentos Laptop-PT, e atribua os endereços 192.168.1.4 e 192.168.1.5 aos novos equipamentos (clique duas vezes em cada componente para configurá-lo). Realize o ping a partir de PC0 nos novos endereços para verificar se a comunicação ocorre conforme esperado. Vide Figura 8 para referência.

Figura 7 – Exemplo de rede com dois computadores

![Fonte: Autoria própria, 2022.](https://paperx-dex-assets.s3.sa-east-1.amazonaws.com/images/1674140006526-n389wZs5fI.png "Fonte: Autoria própria, 2022.")

Fonte: Autoria própria, 2022.

Figura 8 – Exemplo de rede com quatro computadores

![Fonte: Autoria própria, 2022.](https://paperx-dex-assets.s3.sa-east-1.amazonaws.com/images/1674139948966-uHnmzF20of.png "Fonte: Autoria própria, 2022.")

Fonte: Autoria própria, 2022.

**Como aplicar na prática o que aprendeu**

Observe redes no seu trabalho, em sua escola ou em sua casa e tente modelar sua topologia no Cisco Packet Tracer.

**Conteúdo bônus**

**Tópicos avançados**

Para aprofundar seus conhecimentos sobre Cisco Packet Tracer, consulte o tutorial mais complexo (DIAS; SILVA, 2022).

Observação: Este conteúdo não será cobrado nas avaliações e estará, obrigatoriamente, presente nas videoaulas. Fique tranquilo(a)!

Referência Bibliográfica

Dias, Kelvin Lopes; Silva, Diego dos Passos. **Tutorial sobre o Cisco Packet Tracer**. Disponível em: <[https://docente.ifrn.edu.br/jeffersonduarte/disciplinas/redes-de-computadores-e-aplicacoes/aulas/tutorial-sobre-o-cisco-packet-tracer/view](https://docente.ifrn.edu.br/jeffersonduarte/disciplinas/redes-de-computadores-e-aplicacoes/aulas/tutorial-sobre-o-cisco-packet-tracer/view)> Acesso em 15/12/2022.