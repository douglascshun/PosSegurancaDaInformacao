[[CyberOps]]

**Introdução**

O módulo em questão apresenta conhecimentos variados e determinantes para boas práticas em segurança da informação e cyberops. Os tópicos seguiram uma organização didática de seis momentos. O primeiro tópico abordou o conceito de incidente e resposta a incidente. Logo após, foram discutidos metodologias e processos de respostas a incidentes. Em um terceiro momento, foi apresentada a importância de um CSIRT. O quarto tópico trouxe à baila as importantes ferramentas de segurança computacional conhecidas como Honeypot e Honeytokens. Elas representam um avanço tecnológico significativo, pois simulam um ambiente comprometido ao invasor, contudo concentram-se em capturar o máximo de informações sobre o atacante. O quinto momento versou sobre como proceder diante de incidentes de segurança e como formalizar uma resposta, bem como quais os órgãos responsáveis em acolher esses registros. Por fim, foi revelada a importância e infraestrutura de uma sala de guerra com aplicação ao universo de segurança da informação.

**Objetivos da aula**

Compreender como se dá o processo de notificação a um incidente de segurança;

Apresentar a metodologia e os procedimentos de resposta a um incidente;

Reconhecer a importância de um CSIRT;

Conhecer ferramentas de HoneyPot e Honeytokens;

Apresentar a infraestrutura e aplicação de uma sala de guerra direcionada a cyberops.

**Resumo**

Esse módulo apresenta seus conteúdos direcionados a atividades de prática operacional em segurança da informação, privilegiando ações diretamente relacionadas aos procedimentos que devem ser adotados para a notificação de um incidente de segurança. Em consonância com essas práticas também foram discutidos os procedimentos de análise e metodologias que norteiam a dinâmica de resposta a um incidente.

Inicialmente, foram estudados os elementos conceituais que atendem as demandas por respostas a um incidente de segurança. É importante compreender a simplicidade do processo de notificação e que o Centro de Estudos, Resposta e Tratamento de Incidentes de Segurança no Brasil – CERT, que é um braço do CGI – Comitê Gestor da Internet no Brasil, é o órgão responsável por receber uma notificação de incidente, bem como desenvolver o tratamento dessa informação em diferentes níveis de aplicação.

Um ponto marcante desse estudo é observar na definição do próprio CERT o conceito de incidente. Segundo o CERT (2022),

"Um incidente de segurança pode ser definido como qualquer evento adverso, confirmado ou sob suspeita, relacionado à segurança de sistemas de computação ou de redes de computadores.”

Disponível em: <[https://www.cert.br/docs/certbr-faq.html](https://www.cert.br/docs/certbr-faq.html)>. **(Acesso em 17/02/2023)**

Isso é um importante marco para ajudar na disseminação desse relevante conhecimento. Uma iniciativa interessante foi a apresentação de uma lista de exemplos de situações que configuram um incidente de segurança, como:

- tentativas de ganhar acesso não autorizado a sistemas ou dados;
- ataques de negação de serviço;
- uso ou acesso não autorizado a um sistema;
- modificações em um sistema, sem o conhecimento, instruções ou consentimento prévio do dono do sistema;
- desrespeito à política de segurança ou à política de uso aceitável de uma empresa ou provedor de acesso.

Passando para a dimensão que lida com metodologias e procedimentos de resposta a incidentes de segurança, a primeira necessidade é ter um plano de resposta a incidentes em vigor que abarque processos internos e externos de uma organização.

Durante um ataque ou após um incidente é muito importante:

- Manter a calma;
- Mantenha as evidências;
- Envolver o departamento jurídico;
- Cuidado ao compartilhar informações sobre o incidente publicamente.

Nos temas estudados foi possível perceber o destaque para o CSIRT (Computer Security Incident Response Team) que, em tradução livre, significa Equipe de Resposta a Incidentes de Segurança de Computadores. Esse tema demonstrou a importância desse time em uma organização, perante aos desafios impostos frente às ações de resposta a incidentes de segurança da informação.

Um CSIRT provê serviços de suporte para prevenção, tratamento e resposta a incidentes de segurança em computadores. Visando clarear as áreas de atuação do CSIRT, podemos citar:

- A redução do impacto do incidente;
- Confiabilidade;
- Ajuda ao departamento jurídico;
- Retornar o ambiente ao estado de produção.

Um Honeypot é um recurso computacional de segurança dedicado a ser sondado, atacado ou comprometido. Um Honeynet nada mais é do que um tipo de honeypot. Especificamente, é um honeypot de alta interatividade, projetado para pesquisa e obtenção de informações dos invasores. É conhecido também como "honeypot de pesquisa". Vale destacar algumas aplicabilidades:

- Detectar ataques internos;
- Coletas assinaturas de ataques;
- Identificar varreduras e ataques automatizados;
- Detectar máquinas comprometidas;
- Identificar padrões;
- Coletar Código malicioso (malware);
- Manter atacantes afastados de sistemas importante;
- Detectar máquinas com problemas de configuração.

O penúltimo tema revelou diversos modelos de notificação para facilitar a integração com sistemas de acompanhamento e notificação de incidentes. Os modelos também estão disponíveis para download na internet em arquivos .txt nos idiomas português (pt-br) e inglês (en-us), compactados em arquivos .zip, conforme o idioma:

Modelos em Português: **certbr-templates-pt-br.zip**

Modelos em Inglês: **certbr-templates-en-us.zip**

**Como aplicar na prática o que aprendeu**

A Lei Geral de Proteção de Dados (LGPD) determina aos agentes de tratamento de dados pessoais (controladores e operadores) a adoção de medidas para prevenir a ocorrência de danos aos titulares em virtude de suas atividades. 

Na eventualidade de um incidente de segurança, uma importante medida de mitigação de danos é a comunicação da ocorrência aos titulares dos dados pessoais violados. Dessa forma, eles poderão tomar conhecimento do ocorrido e adotar medidas de precaução para mitigar os riscos a que foram expostos em razão do incidente.

A LGPD impõe aos controladores, em seu art. 48, o dever de comunicar aos titulares e à ANPD a ocorrência de incidentes que possam causar riscos ou danos relevantes aos titulares. O cumprimento dessa obrigação junto à ANPD e aos titulares afetados, se dá no processo de Comunicação de Incidente de Segurança (CIS).

Leia o artigo no site da Autoridade Nacional de Proteção de Dados e esteja preparado para aplicar esse conhecimento quando necessário.

Disponível em; <[https://www.gov.br/anpd/pt-br/canais_atendimento/agente-de-tratamento/comunicado-de-incidente-de-seguranca-cis](https://www.gov.br/anpd/pt-br/canais_atendimento/agente-de-tratamento/comunicado-de-incidente-de-seguranca-cis)>. **(Acesso em 17/02/2023)**

**Conteúdo bônus**

**Tópicos avançados**

O honeypot é um sistema conectado à rede e configurado como chamariz para atrair os ataques cibernéticos detectando, desviando e estudando as tentativas dos hackers em obter acesso não autorizado aos sistemas de informação.

A função de um honeypot é se apresentar na internet como um alvo potencial para invasores — geralmente, um servidor ou outra fonte de alto valor — e coletar informações, notificando os defensores — white hats — sobre quaisquer tentativas de acesso à isca por usuários não autorizados.

Entre no site Distributed Honeypots Project e interaja com os diversos honeypost disponíveis no link: CERT.br - Distributed Honeypots Project

**Referência Bibliográfica**

**Bibliografia Básica**

RICCI, Bruno. **Rede Segura**: VPN Linux, Editora Ciência Moderna, 2007.

TANENBAUM, A. S., **Redes de Computadores**. Rio de Janeiro, Campus, 2003.

COSTA, Daniel Gouveia. **Administração de Redes com Scripts**, 2ª Edição, Editora Brasport, 2010.

**Bibliografia Complementar**

SMITH, Rodercik W**. Linux**: Ferramentas Poderosas, 1ª Edição, 2004, Editora Ciência Moderna.

NAKAMURA, E. T., e GEUS, P. L., **Segurança de Redes em Ambientes Cooperativos**,2 ed. Ed. Berkley, São Paulo, 2007.

MORAES, Alexandre F. **Redes de Computadores**. 7ª Edição, Editora Érica, 2008.

MENDES, Douglas Rocha, **Redes de Computadores**, Ed. Novatec, 1ª Edição, 2007

STARLIN, Gorki, **Conceitos, Protocolos e Uso Tcp/Ip**: Redes de Computadores. 1ª Edição, Alta Books, 2004.