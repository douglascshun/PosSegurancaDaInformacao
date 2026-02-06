[[Cybersecurity Essentials]]

## Ameaças, Ataques e Vulnerabilidades

**Introdução**

Tão importante quanto entender as necessidades de segurança cibernética de um sistema da informação é entender quais fatores internos e externos tornam estes requisitos relevantes. Nesta aula, iremos abordar as definições de ameaças, ataques e vulnerabilidades para entender quais os pontos fracos dos sistemas que desenvolvemos, quais ameaças externas tornam mais difícil garantir o cumprimento aos requisitos de segurança cibernética e entender um ataque cibernético considerando seu vetor de ataques e uma modelagem do atacante.

**Objetivos da aula**

- Representar o funcionamento de um sistema em uma arquitetura da solução;
- Identificar vulnerabilidades em uma arquitetura de um sistema;
- Identificar ameaças aos sistemas de informação;
- Representar um vetor de ataque associado a um ataque cibernético;
- Representar o entendimento sobre o atacante em um modelo.

**Resumo**

Por que ataques acontecem? Um primeiro motivo que podemos citar é por conta dos pontos fracos dos sistemas de informação. Ou seja, os sistemas que desenvolvemos podem estar tão frágeis que motivam ataques por sua facilidade de execução. Se este é um motivo relevante, convém então entender quais seriam estes pontos fracos.

Um primeiro passo para identificar os pontos fracos de um sistema é representar seu funcionamento em uma arquitetura. Por sua vez, a arquitetura são blocos e setas que ligam estes blocos? Representa a infraestrutura onde o sistema executa? Evidencia decisões de projeto? É um modelo do sistema? A resposta para todas estas questões é sim, a arquitetura nos permite descrever componentes de um sistema e suas integrações. Também pode descrever qual infraestrutura um sistema utiliza. Mas a definição mais relevante está relacionada à sua capacidade de evidenciar decisões de projeto e permitir nossa representação de um modelo do sistema.

A verdade é que um sistema não é algo estático, e sim que está em constante desenvolvimento. Mesmo sistemas mais estáveis podem precisar de novas versões devido a ajustes na infraestrutura que utilizam, como novas versões de sistemas operacionais ou de plataformas. Neste constante processo de desenvolvimento, a evolução do sistema ocorre por meio de diversas decisões de projeto, tomadas pela equipe de gestão e/ou de implementação do sistema específico. Se o sistema necessitou de mais segurança e estes mecanismos foram implementados, então a arquitetura deve refletir este novo estado do sistema. Por outro lado, a arquitetura nos permite representar nosso entendimento sobre o funcionamento do sistema, e que estará limitado aos aspectos que temos conhecimento sobre este sistema específico. Desta forma, podemos realizar a analogia que uma descrição arquitetural é similar a uma foto do sistema, e estas diversas fotos podem ser tiradas em diversos momentos do ciclo de vida do sistema. Outra analogia válida é que uma representação do funcionamento do sistema equivale a uma foto tirada de um modelo tridimensional, ou seja, limitada e parcial por natureza. Diversas fotos de diferentes perspectivas seriam necessárias para o completo entendimento do sistema.

Vamos relembrar o exemplo com nossos personagens Alice, Bob e Carlos. Alice deseja enviar uma mensagem secreta para Bob, e Carlos é um hacker que deseja atacar o sistema. Podemos detalhar este cenário ao descrever a arquitetura do sistema utilizado por Alice e Bob. Conforme representado na Figura 1, Alice envia a mensagem para um sistema de e-mail implantando em um servidor na nuvem utilizando seu dispositivo móvel, e Bob recebe a mensagem por meio de seu computador que possui acesso a esta plataforma de e-mail em nuvem. A nuvem computacional citada pode ser um servidor que está nos Estados Unidos, por exemplo.

Figura 1 – Arquitetura do cenário hipotético com Alice, Bob e Carlos

![Fonte: Autoria própria, 2022.](https://paperx-dex-assets.s3.sa-east-1.amazonaws.com/images/1674065356021-njzhD0n40P.png "Fonte: Autoria própria, 2022.")

Fonte: Autoria própria, 2022.

Com o modelo do sistema em mãos, é possível iniciar a análise de vulnerabilidades. As vulnerabilidades são os pontos fracos do sistema, pontos que se estiverem muito frágeis motivam ataques cibernéticos. No exemplo, Carlos pode identificar que o servidor em nuvem que possui todas as mensagens de e-mail não só da Alice e Bob, mas sim de muitos outros usuários, pode estar fracamente protegido. Por exemplo, credenciais administrativas podem estar com padrões muito simples de senhas, o que facilita um ataque de força bruta (tentar combinações de senhas de forma exaustiva).

Outro ponto fraco pode estar no canal de comunicação: se não for utilizado mecanismos de prevenção e recuperação de ataques, pode ser muito fácil obter as mensagens de e-mail enviadas (no caso, pela Alice) e recebidas (no caso, pelo Bob). Os próprios dispositivos clientes (celular da Alice e computador do Bob) podem estar com proteção fraca (senha simples e reutilizada por exemplo). Outro ponto fraco são os próprios usuários que podem não seguir as melhores práticas para gestão de senhas (anotações em _post-its_), o que facilita a personificação de Alice ou Bob pelo Carlos. Isto é, Carlos pode tentar se passar pela Alice para enviar mensagens para Bob, ou se passar pelo Bob para ter acesso às mensagens com informações sigilosas enviadas de Alice para Bob.

Além de entender os pontos fracos dos sistemas, também é relevante entender melhor as ameaças e ataques externos a estes sistemas. Afinal de contas, um ataque só ocorre se uma vulnerabilidade for explorada e se alguém estiver disposto a realizar o ataque.

Neste sentido, podemos lembrar dos conceitos de segurança cibernética. Informações que trafegam em um sistema devem ser confidenciais e íntegras, de forma que um terceiro mal-intencionado não possa ter acesso a informações sigilosas nem modificar o conteúdo de mensagens importantes. Devemos garantir a disponibilidade dos sistemas, verificar a identidade dos usuários e permitir que um terceiro possa verificar as ações realizadas por determinadas entidades no sistema. De forma simplificada, podemos definir ameaças como fatores ou ações capazes de impactar estes aspectos.

Por outro lado, descrever o vetor de um ataque cibernético nos permite entender como uma determinada vulnerabilidade está sendo explorada. Os pontos fracos do sistema existem de forma independente dos atacantes, mas ataques só ocorrem se uma ou mais vulnerabilidades forem exploradas. Para um determinado ataque, basta ter a representação da arquitetura do sistema, e as vulnerabilidades identificadas para levantar quais vulnerabilidades foram exploradas no ataque específico.

Por fim, podemos tentar entrar na mente do criminoso para levantar possíveis motivações dos ataques. Atacantes podem ser motivados por questões de ativismo, por questões monetárias ou até pelo simples prazer em causar confusão, por exemplo. É claro que se a modelagem do sistema é algo incompleto, a modelagem do atacante também será. Pode ser difícil ou até impossível saber toda a motivação do atacante, mas representar nosso entendimento sobre o criminoso pode nos auxiliar a avaliar a eficácia de contramedidas e identificar o que está dentro do radar e o que está fora. Se o criminoso tiver somente motivação de causar confusão, aplicar proteções que aumentam o custo do ataque pode ser o suficiente para evitar ataques futuros. Contudo, se o atacante também tiver motivação monetária, e quem estiver financiando o ataque fornecer ainda mais recursos, podemos ainda ter ataques futuros, em um cenário hipotético.

Nesta aula, apresentamos como representar o funcionamento de um sistema em uma arquitetura, de forma a identificar seus pontos fracos (vulnerabilidades). Houve a definição de ameaça aos sistemas de informação e como este conceito está relacionado com os requisitos de segurança, além da apresentação da definição de vetor de ataque cibernético e modelagem do atacante.

**Como aplicar na prática o que aprendeu**

Obtenha ataques veiculados na mídia e tente identificar a vulnerabilidade explorada e as possíveis motivações dos atacantes.

**Conteúdo bônus**

**Tópicos avançados**

Entenda os ataques descritos em [Kaspersky - As sete principais ameaças virtuais que merecem atenção](https://www.kaspersky.com.br/resource-center/threats/top-7-cyberthreats), que possui exemplos de violações de dados de lojas, vulnerabilidades em dispositivos móveis, roubo de identidades, violações de dados da área da saúde, dentre outros para aprofundar seus conhecimentos.

Observação: Este conteúdo não será cobrado nas avaliações e estará, obrigatoriamente, presente nas videoaulas. Fique tranquilo(a)!

Referência Bibliográfica

Kaspersky. **As sete principais ameaças virtuais que merecem atenção**. Disponível em: < [https://www.kaspersky.com.br/resource-center/threats/top-7-cyberthreats](https://www.kaspersky.com.br/resource-center/threats/top-7-cyberthreats)>. Acesso em 15/12/2022.