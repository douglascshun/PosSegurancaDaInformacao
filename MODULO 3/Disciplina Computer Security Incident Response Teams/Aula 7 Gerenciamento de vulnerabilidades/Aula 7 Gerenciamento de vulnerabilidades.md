[[Computer Security Incident Response Teams]]
## Gerenciamento de vulnerabilidades

**Introdução**

Nesse módulo, você compreenderá as causas fundamentais das vulnerabilidades, através de um entendimento das noções básicas sobre as mesmas. Em seguida, adentraremos no processo de tratamento de vulnerabilidade, dividido em fases.

Além disso, você também adquirirá uma compreensão ampla sobre as principais funções de análise, coordenação e resposta às vulnerabilidades. Por fim, veremos como publicar e comunicar vulnerabilidades, através do desenvolvimento de publicações e comunicações eficazes.

**Objetivos da aula**

- Compreender as noções básicas e causas fundamentais das vulnerabilidades.
- Compreender as fases do processo de tratamento de vulnerabilidades.
- Conhecer as funções de análise, coordenação e resposta a vulnerabilidades.
- Aprender a desenvolver publicações e comunicação eficazes sobre vulnerabilidades.

**Resumo**

**Causas fundamentais das vulnerabilidades**

Componentes de Software: São os elementos que compõem programas de software maiores, incluindo bibliotecas compartilhadas, controles ActiveX, etc. Não são executados diretamente pelo usuário e não têm vulnerabilidades fora do contexto de um programa maior.

Versões do Programa: São imagens executáveis que podem ser instaladas e executadas, enquanto produtos são uma abstração de marketing. As versões do programa podem ter vulnerabilidades, enquanto os produtos não.

Mitigações: São soluções para vulnerabilidades de software, podem ser simples como substituir uma operação de cópia de _string_, ou envolver ajustes no sistema/rede para impedir a exploração da vulnerabilidade. Identificar as mitigações é importante para determinar quais vulnerabilidades podem ser resolvidas.

Falhas de Segurança: São defeitos no código-fonte ou componentes de software que podem levar a vulnerabilidades de software. É importante entender e analisar as falhas de segurança para determinar a possibilidade de vulnerabilidades em programas.

Propriedades de Vulnerabilidade: São as propriedades interessantes das vulnerabilidades que são relevantes para analistas de vulnerabilidade, manipuladores, administradores de sistema e rede.

Propriedades de Exploração: _Exploits_ executam código através de injeção na memória. O local de injeção e a consequência do _exploit_ variam. _Exploits_ podem ser usados para travar programas, ler/gravar memória, ou executar código arbitrário.

**Tratamento de vulnerabilidades**

O processo de tratamento de vulnerabilidades consiste em quatro fases: Preparação, Recebimento, Verificação e Resolução.

A Preparação envolve o desenvolvimento de políticas, processos e recursos antes de iniciar o programa.

Na fase de Recebimento, o processo é iniciado ao receber um relatório de vulnerabilidade, que pode ter sido encontrado interna ou externamente ao fornecedor.

Na verificação, o fornecedor tenta confirmar a vulnerabilidade e determinar a gravidade.

A fase de Resolução envolve a correção da vulnerabilidade. Se a vulnerabilidade não puder ser verificada, o fornecedor pode sair do processo sem correção. Todos os relatórios de vulnerabilidades devem ser registrados.

**Análise, coordenação e resposta**

A Área de Serviços de Gerenciamento de Vulnerabilidades inclui serviços relacionados à descoberta, análise e tratamento de novas e conhecidas vulnerabilidades de segurança em sistemas de informação.

Cada CSIRT pode fornecer apenas alguns desses serviços, dependendo de suas responsabilidades. Por exemplo, um CSIRT pode limitar seus serviços ao conhecimento de novas vulnerabilidades através de fontes públicas e emissão de alertas de segurança, sem necessariamente participar na correção da vulnerabilidade.

Análise de Vulnerabilidade: Este serviço tem como objetivo compreender e identificar uma vulnerabilidade confirmada. É destinado a entender a vulnerabilidade e seu impacto potencial, bem como identificar uma ou mais estratégias para prevenir ou minimizar sua exploração.

Triagem de vulnerabilidade: A triagem é a primeira função do serviço de Análise de Vulnerabilidades. Consiste em categorizar, priorizar e avaliar uma vulnerabilidade para determinar se é relevante e tem impacto nos sistemas envolvidos.

Análise da causa raiz da vulnerabilidade: Esta função tem como objetivo identificar a falha que está causando a vulnerabilidade. O objetivo é compreender as circunstâncias que permitem a existência da vulnerabilidade e em que circunstâncias ela pode ser explorada.

Registro de informações: A triagem resulta no registro de informações categorizadas, priorizadas e atualizadas sobre uma vulnerabilidade.

Serviço de Coordenação de Vulnerabilidade: O objetivo deste serviço é trocar informações e coordenar atividades relacionadas a processos de divulgação coordenada de vulnerabilidades (CVD). Ele envolve a coordenação da troca de informações entre as várias partes interessadas, incluindo localizadores/relatores de vulnerabilidades, fornecedores afetados, desenvolvedores, PSIRTs, pesquisadores, CSIRTs, e coordenadores de vulnerabilidades.

Função de Notificação/Relatório de Vulnerabilidade: Este serviço visa compartilhar ou relatar novas informações de vulnerabilidade com outras partes envolvidas no processo de CVD. Isso envolve notificar e trabalhar com várias partes, incluindo fornecedores afetados, desenvolvedores, PSIRTs, e especialistas confiáveis.

Função de Coordenação das Partes Interessadas em Vulnerabilidade: Esta função é responsável por conduzir a coordenação de acompanhamento e compartilhamento de informações entre as várias partes interessadas e participantes envolvidos no processo de CVD. Isso inclui a coordenação da troca de informações e o acordo sobre o momento e sincronização da divulgação.

Resultados do Serviço de Coordenação de Vulnerabilidade: O resultado desejado é o compartilhamento de informações sobre vulnerabilidades de forma eficaz, oportuna e responsável entre os participantes, permitindo o desenvolvimento e anúncio de soluções de remediação/mitigação.

Desenvolvimento de Publicação de Vulnerabilidade: Este é considerado uma subfunção da Função de Coordenação das Partes Interessadas em Vulnerabilidade e envolve o planejamento e preparação para a divulgação da vulnerabilidade.

Importância do Serviço de Coordenação de Vulnerabilidade: O Serviço de Coordenação de Vulnerabilidade é fundamental para garantir a eficácia e oportunidade na abordagem de vulnerabilidades, bem como para promover a responsabilidade e transparência na comunicação entre as várias partes interessadas.

O objetivo do Serviço de Resposta de Vulnerabilidade é obter informações sobre vulnerabilidades conhecidas e agir para prevenir, detectar e remediar/mitigar tais vulnerabilidades. Este serviço pode incluir a detecção de vulnerabilidades divulgadas, a correção ou mitigação dessas vulnerabilidades e a prevenção de sua exploração.

A finalidade da correção de vulnerabilidade é corrigir ou mitigar vulnerabilidades para evitar sua exploração.

Quem executa o Serviço de Resposta de Vulnerabilidade: Este serviço e suas funções relacionadas são geralmente executadas por outros grupos especializados dentro de uma organização, normalmente não o CSIRT. É improvável que este serviço seja fornecido pelo Coordenador de CSIRT.

**Desenvolvimento de publicações e comunicações eficazes**

Divulgação de vulnerabilidade: divulgar informações sobre vulnerabilidades é um tópico polêmico na comunidade de resposta a incidentes e segurança de computadores. Diferentes opiniões estão sendo debatidas para chegar a um padrão ou processo comum.

4 fases da DCV: o processo de divulgação de vulnerabilidades pode ter fases ligeiramente diferentes. A seguir, apresentamos uma versão do processo ISO/IEC 30111 com mais fases para descrever o que é visto no CERT/CC: descoberta, relatório, validação e triagem, correção, conscientização pública e implantação.

Escolhendo uma política de divulgação: definir uma política de divulgação é importante para os responsáveis pelo processo. Uma política clara estabelece as expectativas de todas as partes envolvidas e garante boas relações entre descobridores, relatores, fornecedores, coordenadores e outras partes interessadas.

Conteúdo da política de divulgação: uma política de divulgação geralmente descreve o que as partes interessadas em CVD (descobridores, relatores, fornecedores, coordenadores) podem esperar em termos de escopo, exceções, proteção contra retribuições legais, requisitos de qualidade do relatório, idiomas de comunicação e outros detalhes relevantes.

Considerações éticas na divulgação de vulnerabilidades: a divulgação de vulnerabilidades é uma questão ética complexa, pois pode levar a consequências negativas para usuários, empresas e a sociedade como um todo. Por isso, é importante ter cuidado e considerar a privacidade, a segurança e os direitos dos usuários, bem como as implicações para a infraestrutura de segurança.

Padrões internacionais na divulgação de vulnerabilidades: existem alguns padrões internacionais para ajudar na divulgação de vulnerabilidades, como o ISO/IEC 30111 e o CERT/CC. Esses padrões fornecem orientações sobre o processo de descoberta, relatório, validação, correção, conscientização pública e implantação, e são amplamente aceitos na comunidade de segurança de computadores.

**Como aplicar na prática o que aprendeu**

- Identificação de vulnerabilidades: O primeiro passo no gerenciamento de vulnerabilidades é identificar quais sistemas e aplicativos estão em uso na organização e quais vulnerabilidades podem afetá-los. Isso pode ser feito usando ferramentas de digitalização de vulnerabilidades ou serviços gerenciados de segurança.
- Avaliação de risco: Depois que as vulnerabilidades são identificadas, é importante avaliar o risco de cada vulnerabilidade para priorizar quais devem ser corrigidas primeiro. Isso pode ser feito usando uma combinação de fatores, como a gravidade da vulnerabilidade, o impacto potencial na organização e a probabilidade de um ataque bem-sucedido.
- Correção de vulnerabilidades: Depois que as vulnerabilidades são avaliadas, o próximo passo é corrigi-las. Isso pode envolver a aplicação de patches de segurança, atualizações de software ou configurações de segurança mais rígidas. É importante ter um processo claro e bem definido para corrigir as vulnerabilidades, incluindo a definição de responsabilidades e prazos claros para as correções.
- Monitoramento contínuo: O gerenciamento de vulnerabilidades não é uma atividade única - é um processo contínuo. É importante monitorar continuamente os sistemas e aplicativos em busca de novas vulnerabilidades e aplicar correções conforme necessário. Isso pode ser feito usando ferramentas de detecção de vulnerabilidades ou serviços gerenciados de segurança.
- Teste de penetração: O teste de penetração é uma técnica de segurança que pode ser usada para avaliar a eficácia do gerenciamento de vulnerabilidades. Isso envolve simular um ataque em um sistema ou aplicativo para identificar possíveis vulnerabilidades que possam ter sido perdidas. Os testes de penetração podem ser conduzidos internamente ou por terceiros.
- Comunicação e documentação: É importante documentar todas as atividades relacionadas ao gerenciamento de vulnerabilidades, incluindo a identificação de vulnerabilidades, avaliação de riscos, correção e monitoramento. Além disso, é importante manter uma comunicação clara com outras partes interessadas, como a equipe de TI, para garantir que todas as vulnerabilidades sejam tratadas de forma adequada e transparente.
- Automação: Automatizar o gerenciamento de vulnerabilidades pode ajudar a acelerar o processo e reduzir a carga de trabalho manual. Ferramentas de gerenciamento de vulnerabilidades podem automatizar a detecção de vulnerabilidades, avaliação de riscos, aplicação de correções e monitoramento contínuo.

**Conteúdo bônus**

**Tópicos avançados**

Observação: Este conteúdo não será cobrado nas avaliações e estará, obrigatoriamente, presente nas videoaulas. Fique tranquilo(a)!

- Automação avançada: Além de automatizar a detecção de vulnerabilidades e a aplicação de correções, as ferramentas de gerenciamento de vulnerabilidades podem incluir recursos avançados, como aprendizado de máquina e análise de comportamento, para identificar padrões de atividade suspeita e prever vulnerabilidades antes que elas possam ser exploradas.
- Gestão de patches: A gestão de patches é uma parte importante do gerenciamento de vulnerabilidades. No entanto, gerenciar patches em uma grande organização pode ser um desafio. Ferramentas de gerenciamento de patches avançadas podem ajudar a automatizar a aplicação de patches em sistemas e aplicativos em toda a organização, além de monitorar e relatar o status do patch em tempo real.
- Vulnerabilidade de software personalizado: O software personalizado é usado em muitas organizações e pode apresentar vulnerabilidades únicas que podem ser difíceis de detectar e corrigir. O gerenciamento de vulnerabilidades para software personalizado pode envolver a análise do código-fonte, testes de penetração personalizados e avaliação de riscos mais avançada para determinar as vulnerabilidades mais críticas.
- Análise de impacto: Ao avaliar o risco de vulnerabilidades, é importante considerar o impacto que uma vulnerabilidade pode ter em toda a organização. A análise de impacto avançada pode ajudar a identificar quais sistemas e aplicativos são mais críticos e quais vulnerabilidades apresentam o maior risco para a organização.
- Integração com outras ferramentas de segurança: O gerenciamento de vulnerabilidades é uma parte importante de um programa de segurança mais amplo. Integrar as ferramentas de gerenciamento de vulnerabilidades com outras ferramentas de segurança, como sistemas de detecção de intrusão e SIEM, pode fornecer uma visão mais abrangente do ambiente de segurança e ajudar a identificar possíveis ameaças.
- Gerenciamento de vulnerabilidades em ambientes em nuvem: O gerenciamento de vulnerabilidades em ambientes em nuvem pode apresentar desafios únicos, como a necessidade de monitorar recursos em nuvem em tempo real e a aplicação de patches em um ambiente altamente distribuído. Ferramentas de gerenciamento de vulnerabilidades avançadas para ambientes em nuvem podem ajudar a mitigar esses desafios.

Referência Bibliográfica

SOFTWARE ENGINEERING INSTITUTE | CARNEGIE MELLON UNIVERSITY. **What Skills Are Needed When Staffing Your CSIRT?** EUA, 2017.

ISO/IEC. **ISO/IEC 30111:2019 Information technology** — Security techniques — Vulnerability handling processes. Geneva, Switzerland. Data de publicação: 2019.

Chase, M., Nichols, D., & Maimon, G. (2017). **The CERT® Guide to Coordinated Vulnerability Disclosure**. Addison-Wesley Professional.