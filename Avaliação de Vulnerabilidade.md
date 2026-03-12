[[CyberOps]]

**Introdução**

Nesse módulo, os estudos iniciaram apresentando os tipos de proteção de endpoint, buscando alertar sobre esses dispositivos e despertar a atenção para práticas simples, contudo, representam resultados significativos no que concerne à gestão de ativos em uma rede. Em um segundo momento, foram discutidas as técnicas de criação de perfil de rede e servidores. A especificação do domínio e a identificação dos objetivos de análise constitui o processo de criação de perfil. O CVSS busca construir pontuações de gravidade de cada uma vulnerabilidade mapeada, assim é possível estabelecer prioridades a respostas de incidentes. A análise de risco e vulnerabilidades se debruça em estabelecer um processo de avaliação e identificação de falhas e potenciais ameaças à segurança de uma infraestrutura tecnológica. O sistema de gerenciamento de segurança da informação inclui uma série de abordagens organizacionais que visam articular a proteção da informação empresarial e consolidar o conceito de sistema seguro por meio das variáveis de confidencialidade, integridade e disponibilidade.

**Objetivos da aula**

- Conhecer os principais tipos de proteção de endpoint;
- Apresentar as técnicas relevantes definição de perfil de rede e servidor;
- Compreender o conceito e as definições de CVSS;
- Analisar os aspectos tecnológicos por meio de análise de risco e vulnerabilidades;
- Reconhecer os elementos de gestão em um sistema de gerenciamento de segurança da informação.

**Resumo**

O módulo iniciou apresentando as principais ações de proteção de endpoint, assim é importante destacar alguns tipos de endpoint: hardware de rede, infraestrutura de nuvem, dispositivos móveis e dispositivos de internet das coisas. Como destaque de componentes de segurança de endpoint, o Anti-Bot identifica e bloqueia o tráfego de comando remoto de botnet. O Anti-Malware, identifica e corrige atuação de malware rastreando assinaturas e detecção de anomalias. O Anti-Ransomware promove análise comportamental e detecção de operações.

Para a construção de perfil de rede e servidores são sugeridos, inicialmente, como fundamento preliminar a especificação do domínio do problema. Em seguida, a identificação dos objetivos. Em continuidade ao processo, a criação de um banco de dados formado por perfis já constituídos contribui para análise e inclusão de novos dados relevantes naquele domínio. A preparação de dados visa remover ruídos e a complexidade diante de atributos irrelevantes. A mineração de dados é uma técnica que utiliza algoritmo ou heurística com o objetivo de atender ao modelo e objetivos pré-definidos.

Ainda na dimensão de criação de perfil, a Interpretação baseia-se nos outputs na mineração de dados e auxilia no processo de tomada de decisão. A etapa de Aplicação submete os perfis construídos aos algoritmos que testam e validam as regras estabelecidas. Por fim, a Decisão cabe à organização direcionar ações ou políticas que devem ser aplicadas a grupos ou indivíduos submetidos a um determinado domínio.

O Common Vulnerability Scoring System (CVSS) é um padrão da indústria gratuito e aberto para avaliar a gravidade das vulnerabilidades de segurança do sistema de computador. As pontuações são calculadas com base em uma fórmula que depende de várias métricas que aproximam a facilidade e o impacto de um exploit. Podemos apontar as métricas básicas para um CVSS:

- Vetor de acesso: mostra como a vulnerabilidade pode ser explorada;
- Complexidade de acesso: revela o nível de complexidade de exploração da vulnerabilidade;
- Autenticação: mostra o número de acessos ou tentativa de acesso de um invasor;
- Confidencialidade: descreve o impacto de vazamento dos dados;
- Integridade: descreve o comprometimento dos dados;
- Disponibilidade: descreve o comprometimento da infraestrutura, serviços e recursos.

A análise de vulnerabilidades deve ser compreendida como o processo de avaliação e identificação de falhas e potenciais ameaças à segurança de uma infraestrutura tecnológica, isto é, as brechas na segurança que podem facilitar o ataque de criminosos virtuais.

Os principais objetivos da análise de vulnerabilidades são: redução de prejuízos financeiros, maior proteção dos ativos, aumento de disponibilidades e otimização de investimentos em infraestrutura. Podemos realizar a análise de vulnerabilidades partindo da avaliação de risco, depois avaliação de vulnerabilidades e, por último, realizar o tratamento de risco. Dando destaque a avaliação de vulnerabilidades a metodologia STRIDE representa um acrônimo:

- S (Spoofing of identity): roubo de identidade ou falsificação;
- T (Tampering with data): violação ou adulteração de dados;
- R (Repudiation of transaction): repúdio de transação;
- I (Information disclosure): divulgação não autorizada de informação;
- D (Denial of service): ataques de negação de serviço;
- E (Elevation of privilege): elevação de privilégio.

O último tema estudado neste módulo versa sobre sistema de gerenciamento de segurança da informação, que em termos conceituais é um sistema de gestão voltado para a Segurança da Informação, que inclui toda a abordagem organizacional usada para proteger a informação empresarial e seus critérios de Confidencialidade, Integridade e Disponibilidade.

Em sua estrutura, um SGSI deve contemplar ações e mecanismos de gestão que suportem e viabilizem:

- estratégias, planos, políticas de segurança;
- medidas, controles, e diversos instrumentos;
- estabelecer, implementar, operar, monitorar;
- uso para analisar criticamente, manter e melhorar a segurança da informação.

A ideia desse módulo foi apresentar conceitos de atuação em nível estratégico e operacional em qualquer infraestrutura de segurança da informação.

**Como aplicar na prática o que aprendeu**

Na intenção de ampliar os conhecimentos apresentados no módulo, realize um mapeamento de sistemas de gerenciamento de segurança da informação, produzindo uma base de consulta relevante para conhecimento do cenário envolvendo sistemas de informação desse contexto.

**Conteúdo bônus**

**Tópicos avançados**

Saiba como implantar o Microsoft Defender for Endpoint para que sua empresa possa aproveitar a proteção preventiva, detecção pós-violação, investigação automatizada e resposta. Este guia ajuda você a trabalhar com as partes interessadas para preparar seu ambiente e, em seguida, integrar os dispositivos de maneira metódica, passando da avaliação para um piloto significativo e para a implantação completa. Disponível em: <[https://learn.microsoft.com/en-us/microsoft-365/security/defender-endpoint/deployment-phases?view=o365-worldwide](https://learn.microsoft.com/en-us/microsoft-365/security/defender-endpoint/deployment-phases?view=o365-worldwide)>. **(Acesso em 16/02/2023)**

Referência Bibliográfica

**Bibliografia Básica**

RICCI, Bruno. **Rede Segura:** VPN Linux, Editora Ciência Moderna, 2007.

TANENBAUM, A. S., **Redes de Computadores**. Rio de Janeiro, Campus, 2003.

COSTA, Daniel Gouveia. **Administração de Redes com Scripts**, 2ª Edição, Editora Brasport, 2010.

**Bibliografia Complementar**

SMITH, Roderick W**. Linux**: Ferramentas Poderosas, 1ª Edição, 2004, Editora Ciência Moderna.

NAKAMURA, E. T., e GEUS, P. L., **Segurança de Redes em Ambientes Cooperativos**,2 ed. Ed. Berkley, São Paulo, 2007.

MORAES, Alexandre F. **Redes de Computadores**. 7ª Edição, Editora Érica, 2008.

MENDES, Douglas Rocha, **Redes de Computadores**, Ed. Novatec, 1ª Edição, 2007

STARLIN, Gorki, **Conceitos, Protocolos e Uso Tcp/Ip**: Redes de Computadores. 1ª Edição, Alta Books, 2004.