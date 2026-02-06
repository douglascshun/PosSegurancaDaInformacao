[[Cybersecurity Essentials]]
## Conceitos de Segurança Cibernética

**Introdução**

Nesta aula, os principais conceitos de segurança cibernética serão abordados. Estes conceitos são relevantes para o desenvolvimento seguro de sistemas de informação pois descrevem requisitos que estes sistemas devem cumprir. Estes requisitos são: confidencialidade e integridade das informações, disponibilidade, autenticidade e irretratabilidade.

**Objetivos da aula**

- Identificar quais informações são confidenciais em um sistema da informação;
- Identificar quais informações o sistema deve garantir que estejam íntegras;
- Relacionar o requisito de disponibilidade com o nível de operação necessário do sistema;
- Identificar quais entidades devem ter sua identidade verificada em um sistema de informação;
- Identificar se a irretratabilidade é necessária em um sistema da informação.

**Resumo**

Sempre que vamos desenvolver um sistema, devemos pensar em que requisitos ele deve atender. Isto é, quais as necessidades dos usuários do sistema de informação, como e quando ele será usado. Para desenvolver um sistema de forma segura, ou seja, pensando na segurança desde a sua concepção, devemos nos atentar aos requisitos de segurança da informação que o sistema deve atender.

Por exemplo, ao criar um sistema é comum pensar em funcionalidades, em casos de uso e jornadas de usuário que o sistema deve atender. Porém, como podemos pensar nas necessidades de segurança cibernética que o sistema deve apresentar?

Ao pensar nestes requisitos de segurança no processo de desenvolvimento do sistema, podemos evitar uma série de possíveis impactos negativos relacionados a decisões ruins de projeto em relação à segurança da informação. Quando deixamos de considerar os requisitos de segurança, o que ocorre é que as decisões de projeto acabam por não levar em consideração as necessidades de proteção de dados sensíveis deste sistema. Dentre as consequências de ignorar a segurança da informação no desenvolvimento de um sistema, estão os impactos monetários e a reputação da empresa que está desenvolvendo o sistema da informação.

Por diversas vezes, devido à pressão do mercado, a gestão do desenvolvimento de um novo sistema pode priorizar funcionalidades e negligenciar a segurança cibernética. Porém, esta conta pode ficar cada vez mais cara se o sistema se tornar vulnerável a ataques de _hackers_ que irão afetar os requisitos de segurança cibernética e levar aos impactos nocivos à reputação da empresa e ao próprio sistema de informação em si.

Neste ponto, espero que a relevância dos requisitos de segurança de informação esteja clara e justificada. Não há como pensar somente em funcionalidades, devemos pensar que o sistema também deve cumprir alguns aspectos de segurança da informação para que o sistema em desenvolvimento seja, além de útil para o negócio, também seguro, de forma que seus usuários consigam ter a confiança que o sistema consegue proteger os dados sensíveis fornecidos de forma satisfatória.

A primeira definição importante é a confidencialidade. Para entender este conceito, podemos pensar em um cenário hipotético (representado na Figura 1) em que uma pessoa A (que chamaremos de Alice) manda uma mensagem para uma pessoa B (Bob). Esta mensagem pode ser uma saudação entre amigos e até conter alguma informação sigilosa. O que ocorre se uma pessoa C (Carlos) tiver acesso a esta informação? Carlos é um terceiro, não autorizado a ter acesso à mensagem enviada de Alice para Bob, e a confidencialidade da informação contida na mensagem seria perdida se Carlos tivesse acesso à mensagem. A informação, que antes era conhecida apenas pela Alice, e deveria, após o envio da mensagem, ser conhecida por Bob, pode passar a ser conhecida também pelo Carlos. Se a informação for relacionada a algo íntimo entre Alice e Bob, podemos, inclusive, ter uma violação de privacidade.

Figura 1 – Cenário hipotético com Alice, Bob e Carlos

![[exemplo de Confidencialidade.png]]

Fonte: Autoria própria, 2022.

O segundo conceito importante é a integridade das informações manipuladas por um sistema da informação. Veja que a confidencialidade possui relação com o grau em que uma informação é confidencial e contínua; desta forma, uma perda de confidencialidade não implica necessariamente na modificação da mensagem. No exemplo fornecido, Carlos pode ter acesso indevido e saber mais do que deveria, mas o requisito de confidencialidade não significa que Carlos modificou a mensagem. Já o conceito de integridade foca exatamente na verificação de que a mensagem não teve qualquer modificação indevida. Retomando o exemplo, isso quer dizer que se Alice envia uma mensagem para Bob, mas Carlos obtém a mensagem e a modifica, para então encaminhar a mensagem para Bob, então teremos uma violação de integridade da mensagem. Isto é, a mensagem não está mais íntegra, e a informação contida nesta mensagem pode estar errada. Uma saudação entre amigos poderia se tornar uma troca de críticas fortes, por exemplo.

No cenário hipotético entre Alice, Bob e Carlos, há uma premissa forte que há um canal de comunicação funcional entre Alice e Bob. Ou seja, Alice consegue se comunicar com Bob por meio de algum canal de comunicação. Um outro ataque possível que Carlos pode fazer está relacionado à disponibilidade deste canal de comunicação. O que ocorre se, para começo de conversa, Alice nem conseguir enviar uma mensagem para Bob pois o sistema ou ferramenta que Alice iria usar para enviar a mensagem está indisponível? Como uma consequência relevante de ataques cibernéticos é a indisponibilidade de sistemas de informação, convém, também, considerar a disponibilidade como um requisito importante relacionado à segurança cibernética.

Outra premissa forte no cenário levantado é que Alice é realmente a Alice e Bob é realmente o Bob. Porém, o que ocorre se Carlos tentar se passar pela Alice para enviar uma mensagem para Bob? Neste caso, temos uma personificação que, se bem-sucedida, pode levar Bob a receber mensagens que a Alice verdadeira nunca gostaria de enviar. Por outro lado, se Carlos personificar Bob, ele pode receber mensagens com informações que ele nunca deveria ter acesso. Neste contexto, a autenticidade está relacionada à verificação de identidade de Alice e Bob, as entidades legítimas do sistema. Para fazer esta verificação de identidade, podemos usar algo que somente a Alice saiba (uma senha), algo que somente ela possua (um cartão), ou algo que somente ela seja (utilizando biometria facial por exemplo).

Por fim, a irretratabilidade é um requisito de segurança da informação que está relacionado à rastreabilidade das informações. No exemplo hipotético, vamos pensar no cenário em que Alice enviou uma mensagem com uma linguagem inapropriada para Bob. Bob pode estranhar e tentar verificar com alguma outra pessoa se a Alice realmente enviou aquela mensagem. Alice poderia alegar que Carlos é quem enviou, e não ela. A irretratabilidade está ligada ao fato de a Alice não conseguir negar algo que fez, no exemplo seria o envio da mensagem. Se a mensagem estiver assinada pela Alice (e for comprovada sua legitimidade), Bob pode ter certeza de que a Alice realmente é quem enviou a mensagem, principalmente se houver outra pessoa, um terceiro confiável, que também consiga verificar a legitimidade da assinatura da Alice.

Nesta aula, os principais conceitos de segurança da informação foram abordados. Pensar na confidencialidade e integridade das informações, na disponibilidade do sistema, na autenticidade dos usuários e no aspecto de irretratabilidade (não negar o que fez) são um primeiro passo importante para o desenvolvimento de aplicações e sistemas de forma segura.

**Como aplicar na prática o que aprendeu**

Pense em sistemas de informação que você utiliza no dia a dia e tente relacionar os conceitos vistos com as necessidades destes sistemas. Quais informações são mais críticas e, portanto, devem ser confidenciais e ter sua integridade garantida? Uma indisponibilidade do sistema causa quais impactos? Como o sistema verifica a identidade de seus usuários? A irretratabilidade é útil para este sistema?

**Conteúdo bônus**

**Tópicos avançados**

A segurança da informação, sob uma perspectiva empresarial, está presente na primeira leitura recomendada, que também lista alguns impactos de ataques cibernéticos e dicas para melhorar a segurança de uma empresa (SEBRAE, 2022).

Observação: Este conteúdo não será cobrado nas avaliações e estará, obrigatoriamente, presente nas videoaulas. Fique tranquilo(a)!

Referência Bibliográfica

Sebrae. **Os 5 pilares da segurança da informação e como gerenciá-los**. Disponível em: <[https://respostas.sebrae.com.br/os-5-pilares-da-seguranca-da-informacao-e-como-gerencia-los](https://respostas.sebrae.com.br/os-5-pilares-da-seguranca-da-informacao-e-como-gerencia-los). Acesso em 15/12/2022.