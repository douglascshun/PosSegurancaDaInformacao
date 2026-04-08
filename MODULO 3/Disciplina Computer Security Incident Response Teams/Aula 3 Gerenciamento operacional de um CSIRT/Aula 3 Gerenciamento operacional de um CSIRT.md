[[Computer Security Incident Response Teams]]

**Introdução**

Nessa aula, você compreenderá o ambiente de ameaças atual, bem como os processos básicos de gerenciamento de incidentes. Passaremos pelo código de ética do CSIRT e as ferramentas de segurança utilizadas.

Além disso, vamos conhecer a revisão sobre _probes_, _scans_ e diferentes tipos de ataque, aprendendo a identificar informações críticas e a lidar com o _hotline_, ou triagem, de um CSIRT.

**Objetivos da aula**

- Entender o ambiente de ameaças atual e os processos básicos de gerenciamento de incidentes.
- Conhecer o código de ética.
- Conhecer as ferramentas de segurança utilizadas em um CSIRT.
- Conhecer a revisão sobre _Probes_, _scans_ e tipos de ataques, bem como identificar informações críticas.
- Familiarizar-se com o tratamento do _Hotline_ de um CSIRT.

**Resumo**

**O ambiente operacional do CSIRT**

As estatísticas da CERT/CC sobre vulnerabilidades relatadas entre 1995 e 2002 ilustram a relação entre resposta, tratamento e gerenciamento de incidentes. A resposta a incidentes é uma das funções realizadas no tratamento de incidentes, que é um dos serviços prestados como parte do gerenciamento de incidentes.

É importante destacar a necessidade de coordenação e compartilhamento de informações entre recursos empresariais, como jurídico, relações públicas e gerenciamento de incidentes.

O FIRST CSIRT Services Framework descreve os serviços e funções de equipes de resposta a incidentes para padronizar a comunidade e ajudar na seleção e estabelecimento do portfólio de serviços de uma equipe. O _framework_ é baseado em quatro elementos: áreas de serviço, serviços, funções e subfunções.

Relatórios e solicitações são recebidos por meio de vários canais, incluindo e-mail, chamadas telefônicas, alertas do sistema de detecção de intrusão (IDS) e formulários de relatório de incidentes baseados na _web_.

Enfatiza-se a necessidade de comunicação e colaboração entre o gerenciamento de incidentes e outras funções empresariais, bem como a importância de selecionar serviços com base na missão, constituintes, recursos e capacidades da equipe. Por fim, é importante entender o cenário atual de ameaças e os conceitos básicos dos processos de gerenciamento de incidentes.

**Código de ética**

Um código de ética é um conjunto de regras que orientam os comportamentos da equipe em uma organização, alinhando-se com a missão e caráter da organização. Ele deve ser aplicado a todos os funcionários em todos os níveis e serve como uma atitude sem classe. O código de conduta serve como uma política para orientação em situações específicas e estabelece as bases para interações dentro e fora da equipe. Ele não precisa ter mais do que uma página de texto, mas pode ser mais longo e explicado com exemplos.

O exemplo do Código de Conduta da CSIRT é simples e depende totalmente do tipo de organização. O Código de Ética e Profissional da FIRST é um exemplo interessante que inspira e orienta a conduta ética de todos os membros da equipe, incluindo profissionais atuais e potenciais, instrutores, alunos, influenciadores e qualquer pessoa que use a tecnologia de computação de maneira impactante. Esse código inclui princípios formulados como declarações de responsabilidade e cada princípio é complementado por diretrizes. Os deveres não devem ser vistos como requisitos absolutos, mas sim conforme declarado no IETF RFC2119 para a definição de “DEVE”. A confiança é a base de muitas relações entre as equipes e muitas vezes é necessária antes que uma troca significativa de informações possa ocorrer.

**Ferramentas de segurança utilizadas em um CSIRT**

As ferramentas são necessárias para:

- Armazenar;
- Analisar e rastrear dados CSIRT;
- Analisar logs, arquivos e artefatos;
- Identificar endereços e contatos;
- Fazer varreduras em seus sistemas;
- Monitorar conexões;
- Detecção de intrusão;
- Controle de acesso;
- Verificação de integridade de arquivos;
- Criptografia/descriptografia;
- Comunicações seguras;
- Verificação.

**Revisão sobre probes, scans e tipos de ataques**

_Probe_ é um componente do sistema que monitora e analisa a atividade da rede e também pode executar ações de prevenção. É um pequeno programa utilitário usado para investigar e testar o status de um sistema, rede ou site. As _probes_ são usadas principalmente para fins legais para determinar se um dispositivo está funcionando e, também podem ser utilizadas por _hackers_ para localizar pontos fracos no sistema.

A diferença entre as técnicas de _scan_ e _probe_ está em como elas retornam informações. A técnica de _scan_ geralmente usa ferramentas para retornar informações precisas sobre algo, enquanto a _probe_ é usada para testar algum tipo de entrada e espera fundamentar sua descoberta por meio de uma saída. Por exemplo, para identificar se um site está em Wordpress, um usuário pode usar a técnica de _scan_ com ferramentas, aplicativos ou escanear o gerenciador de arquivos do servidor para fazer um scan em busca de arquivos comumente associados ao Wordpress. Já a técnica de _probe_ é normalmente utilizada quando um usuário não tem privilégio de acesso para investigar um site, assim a forma seria testar para ver se o site tem uma página de login.

O _scan_/_probe_ é a principal técnica para coletar o máximo de informações possível sobre um aplicativo da _web_ e a infraestrutura. Um _scan_ de site padrão é composto de várias etapas. Primeiro, detecta-se o sistema operacional instalado no servidor. Depois, todo o aplicativo pode ser escaneado para fornecer um mapa de todo o site, como todas as páginas, _cookies_ e fluxo de transações, informações que podem ser utilizadas para identificar o processo de autenticação, a autorização, a toda lógica e mecanismos transacionais do aplicativo. As _probes_ e _scans_ são usadas em diferentes tipos de ataques, tais como roubo/violação de informações proprietárias ou confidenciais, acesso privilegiado não autorizado, fraude financeira, ataques de negação de serviço, entre outros.

**Identificação de informações críticas**

Coletar informações críticas é fundamental durante o tratamento de incidentes, assim como os detetives estão sempre buscando dados. É essencial identificar as informações relevantes que precisam ser coletadas para que o CSIRT possa tentar reuni-las. Essas informações incluem: quem está envolvido, informações de contato, o papel e a natureza do incidente, o escopo, o prazo do relatório, o que já foi feito e informações de suporte. Além disso, logs e artefatos de rede e sistema também podem fornecer informações importantes.

A maioria dos CSIRTs tem um mecanismo para receber relatórios, alertas ou solicitações. Isso pode incluir um alias de e-mail, uma linha direta, um formulário online ou em papel ou alertas automáticos por meio de IDS, programas de monitoramento de rede ou outros sensores de rede. A pesquisa organizacional CSIRT mostrou que a maioria dos participantes recebe relatórios por e-mail, seguido de denúncias por telefone e relatórios via IDS. A maioria dos CSIRTs bancários e financeiros e outros CSIRTs comerciais recebem denúncias por telefone, e-mail e IDS, enquanto os CSIRTs educacionais recebem principalmente denúncias por e-mail e IDS.

Rastrear e registrar informações de maneira lógica e metódica pode ser um desafio para equipes recém-formadas, e é importante saber o que precisa ser coletado e como essas informações precisam ser acessadas, usadas e arquivadas. Em 1991, Garfinkel e Spafford forneceram duas regras úteis para serem seguidas ao responder a incidentes: não entrar em pânico e documentar tudo. É fundamental seguir um processo lógico para coletar, registrar e rastrear informações e dados críticos durante o tratamento de incidentes.

**Tratamento do Hotline de um CSIRT**

_Hotline_ ou triagem é o processo de classificar, categorizar e priorizar relatórios de incidentes ou outras solicitações para uma equipe de resposta a incidentes de segurança cibernética (CSIRT). É um elemento crítico de qualquer CSIRT e serve como o veículo através do qual todas as informações fluem para o CSIRT. O processo de triagem fornece uma avaliação inicial de um relatório recebido e o coloca em fila para tratamento posterior. A função de triagem fornece uma visão instantânea do status atual de todas as atividades relatadas ao CSIRT, incluindo relatórios abertos e fechados, ações pendentes e o número de relatórios recebidos. Esse processo ajuda a identificar possíveis problemas de segurança e priorizar a carga de trabalho do CSIRT.

O processo de triagem é importante para fornecer uma compreensão do escopo da atividade de incidentes relatados. Dependendo de como a organização é fisicamente e geograficamente estruturada, a triagem pode ser fornecida de várias maneiras, incluindo triagem distribuída, onde cada área geográfica, divisão ou departamento fornece uma linha direta para receber solicitações e garantir que elas sejam encaminhadas para um banco de dados de rastreamento central.

Alternativamente, todos os relatórios de incidentes podem ser enviados diretamente para o CSIRT, que possui sua própria linha direta, alias de e-mail ou formulário da _web_. Outra abordagem é para o CSIRT trabalhar em estreita colaboração com uma _help desk_ separada em toda a empresa.

Para que o modelo de triagem funcione de maneira eficaz, o pessoal da _help desk_ de ajuda precisa entender os serviços fornecidos pelo CSIRT e saber quando procurar assistência dos membros do CSIRT. O CSIRT também precisa trabalhar em estreita colaboração com a equipe de _help desk_ para revisar ou reatribuir relatórios de problemas para os indivíduos apropriados no CSIRT para acompanhamento. O CSIRT também pode precisar de acesso ao banco de dados da _help desk_. Um mecanismo de comunicação seguro entre as duas entidades também será necessário.

**Como aplicar na prática o que aprendeu**

O Gerenciamento Operacional de um CSIRT (Computer Security Incident Response Team) envolve a definição, organização e coordenação de atividades de resposta a incidentes de segurança da informação em uma organização. Para aplicá-lo na prática, é necessário seguir algumas etapas:

- Identificar as funções e responsabilidades do CSIRT: Defina claramente as funções e responsabilidades do CSIRT, incluindo as atividades que serão realizadas, quem é responsável por cada atividade, quais são as prioridades de ação e como as informações serão comunicadas.
- Desenvolver um plano de resposta a incidentes: Elabore um plano de resposta a incidentes que inclua procedimentos detalhados para lidar com incidentes de segurança da informação, desde a identificação até a resolução. O plano deve ser atualizado regularmente para refletir as mudanças na infraestrutura de TI e nos riscos de segurança.
- Identificar e avaliar os riscos de segurança: Identifique as ameaças e vulnerabilidades à segurança da informação em sua organização e avalie o impacto potencial de incidentes de segurança da informação. Isso ajudará a priorizar as ações do CSIRT e garantir que os recursos sejam alocados adequadamente.
- Desenvolver procedimentos de comunicação e coordenação: Estabeleça procedimentos claros de comunicação e coordenação entre os membros do CSIRT e com outras partes interessadas, como equipes de TI, gestão executiva e outras organizações envolvidas na resposta a incidentes.
- Treinar os membros do CSIRT: Forneça treinamento regular aos membros do CSIRT para mantê-los atualizados sobre as melhores práticas de resposta a incidentes de segurança da informação. O treinamento deve incluir simulações de incidentes para ajudar os membros do CSIRT a praticar suas habilidades.
- Realizar testes de simulação: Realize testes regulares de simulação para verificar a eficácia do plano de resposta a incidentes e identificar áreas de melhoria.
- Gerenciar a documentação: Mantenha registros precisos de todos os incidentes de segurança da informação e das atividades do CSIRT, incluindo relatórios de incidentes, comunicações e ações tomadas. Isso ajudará a garantir que a organização possa aprender com os incidentes e melhorar a resposta a futuros incidentes.

**Conteúdo bônus**

**Tópicos avançados**

Observação: Este conteúdo não será cobrado nas avaliações e estará, obrigatoriamente, presente nas videoaulas. Fique tranquilo(a)!

O Gerenciamento Operacional de um CSIRT envolve várias áreas avançadas, como:

- Inteligência de ameaças: O CSIRT precisa coletar, analisar e compartilhar informações sobre ameaças de segurança da informação. Isso inclui a análise de malware, a identificação de vulnerabilidades, a análise de log e a correlação de eventos.
- Gerenciamento de incidentes complexos: Os incidentes de segurança da informação podem ser complexos e exigir uma resposta coordenada. O CSIRT precisa estar preparado para lidar com incidentes que envolvam várias organizações, múltiplos sistemas ou redes, e que possam ter impacto em larga escala.
- Resposta a incidentes em ambientes em nuvem: A computação em nuvem traz desafios adicionais para a resposta a incidentes de segurança da informação. O CSIRT precisa entender as nuances da computação em nuvem e desenvolver procedimentos de resposta a incidentes que sejam específicos para ambientes em nuvem.
- Análise forense digital: O CSIRT deve possuir habilidades avançadas de análise forense digital para identificar a causa raiz de um incidente e coletar evidências digitais que possam ser usadas em investigações criminais ou processos judiciais.
- Automação de processos: O Gerenciamento Operacional de um CSIRT pode se beneficiar de ferramentas de automação que possam agilizar o processo de resposta a incidentes. A automação pode ser usada para coletar e analisar logs, identificar malware e acelerar a investigação forense.
- Gestão de crises: O CSIRT precisa estar preparado para lidar com situações de crise que possam ter um impacto significativo na organização. Isso inclui a gestão da comunicação com as partes interessadas, a coordenação com outras equipes de emergência e a tomada de decisões rápidas e precisas sob pressão.
- Melhoria contínua: O Gerenciamento Operacional de um CSIRT deve ser baseado em uma abordagem de melhoria contínua. Isso envolve a análise de incidentes anteriores para identificar áreas de melhoria, a atualização constante dos procedimentos de resposta a incidentes e a implementação de treinamentos e simulações regulares.

Referência Bibliográfica

KILLCRECE, Georgia et al. **State of the Practice of Computer Security Incident Response Teams (CSIRTs)**. Carnegie Mellon University, EUA, 2003.

KILLCRECE, Georgia. **Steps for Creating National CSIRTs**. Carnegie Mellon University, EUA, 2004.

KILLCRECE, Georgia et al. **Organizational Models for Computer Security Incident Response Teams (CSIRTs)**. Carnegie Mellon University, EUA, 2003.

HOEPERS, Cristine. **Aspectos Técnicos e Regulatórios sobre Internet**. Curso TCU/NIC.br Evento Online, 09 de junho de 2022.

KILLCRECE, Georgia et al. **Creating and Managing Computer Security Incident Response Teams (CSIRTs)**. Software Engineering Institute, Carnegie Mellon University, EUA.