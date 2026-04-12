[[Computer Security Incident Response Teams]]

**Introdução**

Nessa aula, vamos conhecer as principais técnicas e estratégias contra vazamentos de dados, prevenindo perda de dados e exfiltração de dados (DLP). Além disso, conheceremos as Ameaças Avançadas Persistentes (APTs) e aprenderemos a revisar as técnicas e categorias de análise de malware e de artefatos. Por fim, teremos uma visão geral sobre o sistema DNS e seus desafios.

**Objetivos da aula**

- Conhecer as técnicas e estratégias contra vazamento de dados.
- Entender sobre as APTs.
- Conhecer a revisão das técnicas e categorias de análise de malware e de artefatos.
- Aprender sobre o sistema DNS.

**Resumo**

**Técnicas para prevenir perda e exfiltração de dados**

A prevenção da perda de dados é fundamental para a proteção de informações sensíveis de organizações e indivíduos. A perda de dados pode levar a grandes prejuízos financeiros, além de danificar a reputação das empresas e permitir o roubo de identidades.

A falta de conscientização e disciplina entre os funcionários é a causa mais comum de violação de dados. As formas mais comuns de violação negligente de dados incluem a remoção inadequada de informações, o uso de tecnologias inadequadas para um propósito específico e o roubo de dispositivos de armazenamento.

A comunicação e o treinamento com os funcionários são fundamentais para a prevenção da perda de dados e a conscientização sobre segurança deve ser parte do trabalho dos funcionários.

É importante que as empresas estejam atentas às novas tecnologias de consumo e que incluam controles técnicos de segurança para detectar e impedir ações que possam colocar em risco as informações confidenciais.

A prevenção da perda de dados (DLP) é fundamental para impedir que terceiros não autorizados obtenham acesso a dados sensíveis, concentrando a atenção, os esforços e os recursos nas informações verdadeiramente importantes.

É importante compreender os fluxos de dados para implementar a proteção de dados. Colocar sensores DLP apenas no perímetro das redes não é suficiente, já que muitos vazamentos não são detectados ou interrompidos. Uma abordagem melhor é usar uma variedade de sensores ajustados para fluxos de dados específicos. É necessário uma estratégia de proteção de dados abrangente e baseada em riscos, incorporando a perda de dados. Algumas áreas-chave a serem consideradas ao desenvolver estratégias de proteção de dados são backup e recuperação, ciclo de vida dos dados, segurança física, cultura de segurança e privacidade.

Há de se destacar que a maioria dos dados se moverá de acordo com processos de negócios específicos por meio de caminhos de rede específicos e que entender os fluxos de dados é fundamental para a implementação do DLP. A colocação de sensores DLP no perímetro das redes não é suficiente, já que muitos vazamentos não são detectados ou interrompidos. É necessário usar uma variedade de sensores ajustados para fluxos de dados específicos.

É preciso uma estratégia de proteção de dados abrangente e baseada em riscos, que incorpore a perda de dados. A avaliação do risco é crucial para a mitigação das rotas de exfiltração de dados. No entanto, o aumento do escrutínio de um conjunto crescente de itens de dados pode resultar em custos desproporcionais. Também é necessário incorporar a perda de dados ao processo de avaliação de risco.

Existem algumas áreas-chave a serem consideradas ao desenvolver estratégias de proteção de dados, como backup e recuperação, ciclo de vida dos dados, segurança física, cultura de segurança e privacidade. É importante considerar a perda de dados devido a falhas eletromecânicas ou humanas e que é necessário proteger os dados durante a transição de um estágio para outro. Além disso, a cultura de segurança pode ser um tremendo controle se devidamente educada e incentivada. É importante equilibrar a necessidade de monitorar dados com a necessidade de proteger a privacidade de indivíduos. Toda política de proteção de dados deve equilibrar cuidadosamente essas necessidades.

**Ameaças avançadas persistentes (APTs)**

As Ameaças Persistente Avançada (APT) são consideradas as ameaças mais sofisticadas e perigosas para as organizações, devido ao seu alto nível de conhecimento e recursos necessários, além de combinar vários vetores de ataque. As APTs são características por sua multi-etapa de ataque, furtividade, adaptação aos esforços de defensores, e um conjunto agrupado de comportamentos adversários e recursos. O objetivo das APTs é obter acesso persistente aos sistemas de destino sem ser detectado. Essas ameaças costumam ser coordenadas por organizações governamentais e militares, tendo em vista seus objetivos políticos.

As APTs podem ser extremamente benéficas para os agentes de ameaças devido à sua sofisticação e natureza direcionada. Os APTs podem ter objetivos políticos extremos, como atingir órgãos militares, de defesa e outros órgãos governamentais sensíveis. Em menor escala, os APTs podem ser significativos para resultados competitivos. Por isso, é importante que as organizações adotem medidas de segurança apropriadas para evitar e exfiltrar continuamente as informações, de forma a prevenir ataques persistentes.

Os operadores por trás dessas campanhas APT estão bem equipados e usam técnicas que indicam treinamento formal e financiamento significativo. Além disso, suas ameaças são geralmente apoiadas por um amplo espectro de suporte de inteligência, desde métodos de vigilância digital até técnicas tradicionais focadas em alvos humanos. Dada a complexidade das APTs, pode ser difícil lidar com elas sozinho, o que levou a um desenvolvimento recente na comunidade de segurança, o compartilhamento automático de inteligência contra ameaças.

Existem diferentes tipos de invasores e suas táticas, como as ameaças persistentes avançadas (APTs), que usam uma variedade de táticas, técnicas e procedimentos (TTPs) para obter acesso a um ambiente de negócios e permanecer nele o máximo possível, o que pode levar anos. Esses invasores passam por diferentes etapas, como reconhecimento, desenvolvimento de recursos, acesso inicial, execução, persistência, escalonamento de privilégios e evasão de defesa, para alcançar seus objetivos.

Na etapa de reconhecimento, o invasor coleta informações sobre o alvo, enquanto na etapa de desenvolvimento de recursos, ele cria a infraestrutura a partir da qual lançará ataques. Na etapa de acesso inicial, o invasor compromete os primeiros sistemas, enquanto na etapa de execução, ele usa várias técnicas para executar o código. A etapa de persistência é onde o invasor tenta manter um acesso consistente ao sistema comprometido, e na etapa de escalonamento de privilégios, ele tenta obter o nível mais alto de privilégios possível. Na última etapa, a evasão de defesa, o invasor precisa passar por várias defesas para realizar seus objetivos.

**Revisão das técnicas e categorias de análise de malware**

A análise de malware consiste em examinar o software para identificar se ele é malicioso e, em caso afirmativo, compreender como ele funciona. A análise pode ser estática ou dinâmica. A análise estática é quando a amostra do malware é examinada sem executá-la. Nessa abordagem, é necessário entender a linguagem _assembly_, já que o analista está olhando para a desmontagem do programa. Também é importante mencionar a existência de empacotadores e criptografadores, que são usados para entregar o malware e evitar a detecção por antivírus.

Para a análise estática, existem ferramentas disponíveis, como BinText, que extrai texto de arquivos de qualquer tipo, permitindo encontrar informações úteis. Outra ferramenta popular é o IDA, que permite descompilar um arquivo e ver seu código-fonte. A análise dinâmica, por sua vez, envolve executar o código do malware para compreender como ele interage com o sistema host e o impacto da infecção. Essa abordagem deve ser feita em uma máquina isolada.

A desmontagem é um processo de conversão dos códigos de operação do código executável em linguagem _assembly_. Essa abordagem é útil para compreender o que o programa fará, além de executá-lo, e é uma forma de ver o código, embora não seja tão legível quanto o código-fonte. Outro fator de grande importância é a análise do malware, especialmente no que diz respeito a empacotadores e criptografadores, que podem ajudar o malware a passar pelos programas antivírus.

**Visão geral do sistema DNS e seus desafios**

Nessa parte, abordaremos dois temas: Bancos de Dados e Abuso/uso indevido de DNS.

No primeiro, é destacada a importância da proteção das informações de contato, que estão armazenadas nos bancos de dados internos, e das informações públicas, como DNS e Whois. As informações armazenadas nesses bancos de dados devem ser consideradas "não confiáveis" e questionadas quanto à autenticidade e integridade dos dados. Em relação ao abuso de DNS, existem vários tipos de ataques e que é difícil para os usuários detectar se o caminho de resolução está sendo manipulado ou se o domínio é malicioso. Nesse sentido, a responsabilidade de fazer algo a respeito é dos operadores de DNS, CERTs, provedores de hospedagem, ISPs e todos os outros, que devem adotar melhores práticas e higiene cibernética.

No que se refere aos Bancos de Dados, eles são uma parte integrante e importante do processo de interação e da infraestrutura de comunicação do CSIRT. Portanto, devem ser protegidos com muito cuidado, pois, se um invasor conseguir manipular o banco de dados, poderá comprometer os dados e inserir informações aparentemente autenticadas, nas quais os membros da equipe confiarão. O mesmo problema existe ao usar fontes de informação públicas, como DNS e Whois, que são frequentemente usados para entrar em contato com sites de vítimas. No entanto, as informações nesses bancos de dados devem ser consideradas "não confiáveis", pois podem ser manipuladas e conter erros, o que pode levar à transmissão de informações para a pessoa errada.

Já em relação ao Abuso/uso indevido de DNS, vários tipos de ataques podem ser realizados, incluindo falsificação de DNS, envenenamento de DNS, sequestro de domínio, captura de domínio e cybersquatting. A responsabilidade de fazer algo a respeito é dos operadores de DNS, CERTs, provedores de hospedagem, ISPs e todos os outros, que devem adotar melhores práticas e higiene cibernética. Para ajudar a identificar os responsáveis pelos endereços IP, existem vários sites que podem ser usados para pesquisar Whois e geolocalização de endereços IP.

**Como aplicar na prática o que aprendeu**

O tratamento avançado de incidentes em um CSIRT envolve a aplicação de técnicas e ferramentas especializadas para lidar com incidentes complexos de segurança cibernética. Algumas práticas que podem ser aplicadas na prática incluem:

- Investigação detalhada: A equipe de resposta a incidentes deve realizar uma investigação detalhada do incidente, coletando informações sobre o comportamento do invasor, as vulnerabilidades exploradas e as atividades realizadas no sistema comprometido.
- Análise de malware: É importante realizar análises de malware para identificar as funcionalidades e objetivos do código malicioso que possa estar presente nos sistemas comprometidos. Isso permitirá que a equipe identifique a natureza da ameaça e possa implementar medidas para removê-la.
- Análise de tráfego de rede: A análise de tráfego de rede é uma técnica importante para identificar as comunicações entre o invasor e os sistemas comprometidos. Essa análise pode ajudar a equipe de resposta a entender como o invasor entrou na rede, como se movimentou na rede e que tipo de informações foram exfiltradas.
- Análise forense de disco: A análise forense de disco pode ajudar a equipe de resposta a incidentes a identificar a origem do incidente, os dados que foram acessados e as atividades que foram realizadas pelos invasores. A equipe pode usar ferramentas especializadas para coletar dados e informações forenses, como histórico de navegação, logins, arquivos deletados e comunicações realizadas.
- Mitigação e remediação: Com base na análise das informações coletadas, a equipe de resposta a incidentes deve implementar medidas para mitigar e remover as ameaças identificadas. Isso pode incluir a aplicação de patches de segurança, a configuração de regras de firewall, a remoção de contas de usuário comprometidas e a implementação de controles de segurança adicionais.
- Monitoramento e prevenção: Após a resolução do incidente, a equipe de resposta a incidentes deve monitorar a rede para garantir que as ameaças tenham sido completamente removidas e que nenhuma nova atividade maliciosa esteja ocorrendo. Além disso, a equipe deve implementar medidas para prevenir futuros incidentes, incluindo o treinamento de usuários, a atualização de políticas de segurança e a implementação de controles de segurança adicionais.
- Comunicação e documentação: Durante todo o processo de tratamento de incidentes, é importante manter um registro detalhado de todas as atividades realizadas pela equipe. Isso inclui documentos de comunicação com as partes envolvidas, detalhes dos sistemas afetados, descrição das ameaças e atividades realizadas pela equipe. Esses registros podem ser usados para avaliar o desempenho da equipe e identificar áreas de melhoria para futuros incidentes.

**Conteúdo bônus**

**Tópicos avançados**

Observação: Este conteúdo não será cobrado nas avaliações e estará, obrigatoriamente, presente nas videoaulas. Fique tranquilo(a)!

- Análise de dados em tempo real: A capacidade de analisar grandes quantidades de dados em tempo real é fundamental para identificar rapidamente ameaças e ataques em andamento. Os CSIRTs podem usar ferramentas de análise de segurança, como SIEMs (Security Information and Event Management) e SOAR (Security Orchestration, Automation, and Response), para coletar e correlacionar dados de diferentes fontes e identificar possíveis ataques.
- Resposta a incidentes em nuvem: À medida que as organizações migram seus sistemas para a nuvem, os CSIRTs precisam se adaptar para lidar com incidentes em ambientes de nuvem. Isso inclui o uso de ferramentas e técnicas especializadas para monitorar e responder a incidentes em nuvem, como o uso de serviços de monitoramento de segurança de nuvem e a aplicação de controles de segurança na nuvem.
- Análise de ameaças persistentes avançadas (APTs): As APTs são ameaças sofisticadas e persistentes que podem evadir as defesas tradicionais de segurança. O tratamento avançado de incidentes envolve a aplicação de técnicas e ferramentas especializadas para detectar e responder a essas ameaças, incluindo o uso de análise comportamental, análise de tráfego de rede e análise forense.
- Compartilhamento de informações sobre ameaças: O compartilhamento de informações sobre ameaças entre CSIRTs e outras organizações pode ajudar a prevenir futuros incidentes. Os CSIRTs podem participar de comunidades de compartilhamento de informações de segurança cibernética e usar ferramentas de inteligência de ameaças para obter informações sobre ameaças em tempo real.
- Treinamento e conscientização de usuários: Os usuários finais são frequentemente o elo mais fraco na cadeia de segurança cibernética, e o treinamento e a conscientização dos usuários finais são fundamentais para prevenir incidentes. Os CSIRTs podem aplicar técnicas avançadas de treinamento, como simulações de phishing e jogos de segurança cibernética, para ajudar a melhorar a conscientização e a segurança dos usuários finais.
- Análise de dados de inteligência de ameaças: A análise de dados de inteligência de ameaças pode ajudar os CSIRTs a identificar tendências e padrões em ataques cibernéticos e desenvolver respostas mais eficazes. Os CSIRTs podem usar ferramentas de inteligência de ameaças para coletar e analisar informações sobre ameaças em tempo real e usar essas informações para melhorar as defesas de segurança.
- Preparação para incidentes de cibersegurança em larga escala: Os CSIRTs devem estar preparados para lidar com incidentes de segurança cibernética em larga escala, como ataques coordenados em várias organizações ou setores. Isso inclui a implementação de planos de resposta a incidentes em larga escala, a coordenação com outras organizações e setores.

Referência Bibliográfica

KRAUS, Adam; DEANE, Andrew James. **The Official (ISC) 2 CISSP CBK Reference**. 6. ed. EUA: Wiley, 2021.

CHAPMAN, Brent. **Comptia Cysa+ Cybersecurity Analyst Certification All-In-One Exam Guide**. Second Edition. 2. ed. EUA: McGraw-Hill Companies, 2020.

MESSIER, Ric. **CEH v11 Certified Ethical Hacker Study Guide**. EUA: Sybex, 2021.

EASTTOM, William Chuck. **Certified Ethical Hacker (CEH)**. 3. ed. EUA: Pearson, 2021.

**HANDBOOK for Computer Security Incident Response Teams (CSIRTs)**. 3. ed. Technical Report, TF-CSIRT, 2012.

CERT.BR. **Neutralidade da rede e gerenciamento de tráfego**: reflexões e desafios. In: Internet Governance Forum (IGF), 2019. Disponível em: [https://www.cert.br/docs/palestras/certbr-igf2019.pdf](https://www.cert.br/docs/palestras/certbr-igf2019.pdf). Acesso em 15 fev. 2023.

CERT.BR. **DNS**: segurança, monitoramento e serviços. In: Roadsec São Paulo, 2017. Disponível em: [https://www.youtube.com/watch?v=oTJIvUPun_8](https://www.youtube.com/watch?v=oTJIvUPun_8). Acesso em 15 fev. 2023.

CERT.BR. **Compromised CPEs and Rogue DNS servers**: attacks and response challenges. In: 8th LAC-CSIRTs - Latin American and Caribbean Meeting of CSIRTs, Lima, Peru, 2015. Disponível em: [https://www.cert.br/docs/palestras/certbr-lac-csirts-lima2015-2.pdf](https://www.cert.br/docs/palestras/certbr-lac-csirts-lima2015-2.pdf). Acesso em 15 fev. 2023.

CERT.BR. **Boas práticas para a construção de um CSIRT efetivo**. In: 4º ENISE - Encontro de Segurança da Informação do SENAC, Medellín, Colômbia, 2013. Disponível em: [https://www.cert.br/docs/palestras/certbr-lac-csirts-medellin2013-2.pdf](https://www.cert.br/docs/palestras/certbr-lac-csirts-medellin2013-2.pdf). Acesso em 15 fev. 2023.

CERT.BR. **O papel dos CSIRTs na internet brasileira**. In: 40ª Reunião do ICANN, São Paulo, Brasil, 2010. Disponível em: [https://www.cert.br/docs/palestras/certbr-icann2010.pdf](https://www.cert.br/docs/palestras/certbr-icann2010.pdf). Acesso em 15 fev. 2023.