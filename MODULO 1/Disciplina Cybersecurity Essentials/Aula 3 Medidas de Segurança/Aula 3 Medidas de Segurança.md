[[Cybersecurity Essentials]]
## Medidas de Segurança

**Introdução**

Após compreender os pontos fracos de um sistema, suas necessidades de segurança cibernética e quais ataques são possíveis, falta entender quais ataques devem ser priorizados para a proposição de contramedidas eficazes. Para isso, iremos apresentar a definição de risco, e como utilizar este conceito em uma análise de risco.

**Objetivos da aula**

- Identificar a probabilidade associada a cada ataque cibernético;
- Identificar o impacto associado a cada ataque cibernético;
- Realizar uma análise de risco de um sistema da informação.

**Resumo**

Antes de utilizar uma avaliação de risco para priorizar quais ataques são mais relevantes para um sistema da informação específico, convém definir o que é risco. Quando dizemos “isso é arriscado”, temos os conceitos de incerteza e probabilidade associados. Já quando dizemos “isso é perigoso”, estamos pensando em outros conceitos como consequência e impacto. Ambas as frases são importantes quando definimos risco, pois risco está associado a probabilidades dos ataques e suas consequências. Ou seja, um ataque terá risco maior se sua probabilidade de ocorrer for maior que outros ataques viáveis, e seu impacto for também maior. Podemos ter riscos moderados em casos intermediários, em que a probabilidade pode ser menor, porém o impacto maior, ou então se a probabilidade for maior, porém o impacto menor.

Podemos utilizar novamente o cenário hipotético com nossos personagens Alice, Bob e Carlos (vide Figura 1). Alice deseja enviar um e-mail com informações sigilosas para Bob utilizando seu dispositivo móvel corporativo. Bob por sua vez utiliza seu computador pessoal para acessar o aplicativo de e-mail e assim receber a mensagem de Alice.

Figura 1 – Arquitetura do cenário hipotético com Alice, Bob e Carlos

![Fonte: Autoria própria, 2022.](https://paperx-dex-assets.s3.sa-east-1.amazonaws.com/images/1674066106508-04rDwux1aF.png "Fonte: Autoria própria, 2022.")

Fonte: Autoria própria, 2022.

Podemos identificar as probabilidades de ataques em cada ponto da arquitetura. No servidor em nuvem, podemos considerar que por exemplo o fornecedor da solução (quem possui o servidor) implementou diversos mecanismos de segurança como um controle de acesso efetivo. Desta forma, podemos entender que a probabilidade de um ataque no servidor de e-mail implantado na nuvem (pode estar nos Estados Unidos, por exemplo) terá probabilidade baixa.

Prosseguindo para a Alice, podemos observar que ela utiliza um aparelho corporativo que já possui mais limitações realizadas pela empresa para evitar o vazamento de informações confidenciais. Além disso, a Alice também segue algumas recomendações de segurança, como uma senha com números, letras e algarismos especiais. Por estas razões, podemos definir que um ataque pela Alice possui probabilidade média.

Por outro lado, o Bob utiliza um aparelho pessoal para acessar o e-mail, que possui menos mecanismos de segurança para facilitar seu uso. Bob também pode não seguir recomendações de segurança e utilizar _post-its_ para anotar senhas em lugares compartilhados. Por estas razões, um ataque pelo Bob tem probabilidade alta.

Além das probabilidades, é relevante entender os impactos dos ataques para realizar uma avaliação de risco. A pergunta a ser respondida é: “considerando que um ataque ocorreu, qual seu impacto?”. De forma similar à identificação de probabilidades, podemos realizar esta análise por partes. O servidor em nuvem, se comprometido, pode ter um impacto enorme nos negócios da empresa em que Alice e Bob trabalham, pois, este servidor possui todas as mensagens de todos seus usuários, não somente de Alice ou Bob. Desta forma, o impacto de um ataque na nuvem é alto.

O impacto de um ataque no celular da Alice pode ser considerado baixo levando em conta que Alice pode não ter tantas informações sigilosas da empresa. Já o impacto de um ataque no computador do Bob pode ser maior pois além do e-mail ele possui outras informações sigilosas em programas específicos presentes no seu computador pessoal, que ele também utiliza para atividades profissionais.

A análise de risco resultante pode ser realizada ao combinar as análises anteriores de probabilidade e impacto. O servidor de e-mail na nuvem possui probabilidade baixa e impacto alto, resultando em um risco médio. O lado da Alice possui probabilidade média e impacto baixo, resultando em um risco entre baixo e médio. Por fim, o Bob possui probabilidade alta e impacto médio, resultando em risco entre médio e alto. Desta forma, fica evidente que uma atenção maior deve ser dada para o lado do Bob em termos de segurança cibernética.

Podemos também avaliar o risco em outro cenário como o representado na Figura 2.

Figura 2 – Arquitetura de um exemplo em Internet das Coisas

![Fonte: Autoria própria, 2022.](https://paperx-dex-assets.s3.sa-east-1.amazonaws.com/images/1674066154679-kCxJiVRgbJ.png "Fonte: Autoria própria, 2022.")

Fonte: Autoria própria, 2022.

Neste segundo exemplo, temos uma casa inteligente da Alice com controle e monitoramento pelo celular de um chuveiro inteligente e uma lâmpada inteligente.

O celular da Alice desta vez pode ser o pessoal, com menos travas de segurança e por isso com probabilidade média de sofrer um ataque. Por outro lado, o impacto de um ataque, se ele ocorrer, é alto pois o celular possui controle de todos os equipamentos conectados.

O servidor em nuvem pode continuar com probabilidade baixa e impacto alto, pois possui controle de todos os equipamentos, mas o fornecedor da solução de computação em nuvem pode implementar mais mecanismos preventivos de segurança.

Os dispositivos de Internet das Coisas podem ter probabilidade alta de serem atacados devido a poucos mecanismos de segurança nestes equipamentos. No caso da lâmpada, podemos ter um impacto médio devido a um mal funcionamento da lâmpada ocasionado por um ataque. Porém o chuveiro, além de ter probabilidade alta, pode ter também um impacto alto, devido a queimaduras que um morador pode sofrer em caso de ataque cibernético.

Realizando a avaliação de risco, o lado da Alice possui risco médio, assim como o servidor em nuvem. A lâmpada possui um risco entre médio e alto, e o chuveiro possui risco alto.

**Como aplicar na prática o que aprendeu**

Obtenha outros exemplos comerciais de aparelhos de Internet das Coisas em soluções de casa inteligente e realize uma avaliação de risco similar à apresentada.

**Conteúdo bônus**

**Tópicos avançados**

Uma perspectiva empresarial sobre a análise de risco está presente em (SILVA, 2022) para um aprofundamento dos conhecimentos.

Observação: Este conteúdo não será cobrado nas avaliações e estará, obrigatoriamente, presente nas videoaulas. Fique tranquilo(a)!

Referência Bibliográfica

Silva, Camila. **Análise de risco na segurança da informação: o que é e como fazer**. Disponível em: < [https://unico.io/unicocheck/blog/analise-risco-seguranca-informacao/#](https://unico.io/unicocheck/blog/analise-risco-seguranca-informacao/#:~:text=A%20an%C3%A1lise%20de%20riscos%20na,podem%20causar%20falhas%20futuras%2C%20etc)[:~:text=A%20an%C3%A1lise%20de%20riscos%20na,podem%20causar%20falhas%20futuras%2C%20etc](https://unico.io/unicocheck/blog/analise-risco-seguranca-informacao/#:~:text=A%20an%C3%A1lise%20de%20riscos%20na,podem%20causar%20falhas%20futuras%2C%20etc).> Acesso em 15/12/2022.