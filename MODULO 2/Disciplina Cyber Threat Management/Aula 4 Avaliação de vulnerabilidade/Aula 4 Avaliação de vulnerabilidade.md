[[Cyber Threat Management]]

**Introdução**

Hoje em dia, as vulnerabilidades em cibersegurança se tornaram problemas graves, enfrentados não só por organizações, mas por todos que utilizam qualquer dispositivo digital. Envolve muito mais que simples questões de usabilidade. As vulnerabilidades podem estar no hardware, software, aplicativos e em muitos outros meios que fogem da visão singular de organizações e usuários que não estejam atentos e preparados para este problema.

**Objetivos da aula**

- Definir o que é vulnerabilidade e quais os tipos principais.

- Quais as ferramentas e etapas necessárias para avaliar as vulnerabilidades.

- Quais os principais pontos e as etapas para identificar uma vulnerabilidade.

- Como o SIEM pode auxiliar no gerenciamento de cibersegurança.

**Resumo**

**O que é Vulnerabilidade?**

Uma vulnerabilidade é uma fraqueza que pode ser explorada por ciber criminosos para obter acesso não autorizado a um sistema de computador, redes, sites ou qualquer dispositivo digital. Depois de explorar uma vulnerabilidade, um ataque cibernético pode executar código malicioso, instalar malware e até mesmo roubar dados confidenciais.

As vulnerabilidades podem ser exploradas por uma variedade de métodos, incluindo injeção de SQL, estouros de buffer, cross-site scripting (XSS) e kits de exploração de código aberto que procuram vulnerabilidades conhecidas e pontos fracos de segurança em aplicativos da web.

Muitas vulnerabilidades afetam os softwares populares como sistemas operacionais ou navegadores, colocando os muitos clientes que usam o software em um risco elevado de violação de dados ou ataques. Essas explorações de dia zero são registradas pelo MITRE como Common Vulnerability Exposure (CVE).

_“Zero-day exploit” (Explorações de dia zero) refere-se ao método que os hackers usam para atacar software. “Zero-day vulnerability” (Vulnerabilidades de dia zero) refere-se à falha não descoberta em seu sistema”_

**Causas de Vulnerabilidade**

As vulnerabilidades podem ter diversas origens, desde fatores como software ou fatores humanos, o responsável pela cibersegurança da organização deve buscar ter o máximo controle sobre situações que possam ser vulneráveis, segue alguns exemplos:

- Sistemas complexos – ‍Sistemas complexos aumentam a probabilidade de configurações incorretas, falhas ou acesso não intencional.
- Familiaridade – Os invasores podem estar familiarizados com códigos comuns, sistemas operacionais, hardware e software que levam a vulnerabilidades conhecidas.
- Conectividade – ‍Dispositivos conectados são mais propensos a ter vulnerabilidades.
- Gerenciamento inadequado de senhas – Senhas fracas e reutilizadas podem levar de uma violação de dados a várias.
- Falhas do SO – ‍Os sistemas operacionais também podem ter falhas. Sistemas operacionais não seguros por padrão podem dar aos usuários acesso total e se tornar um alvo para vírus e malware.‍
- Internet – ‍A internet está cheia de spyware e adware que podem ser instalados automaticamente nos computadores.
- Bugs de software – Às vezes, os programadores podem acidentalmente deixar um bug explorável no software.
- Entrada de usuário não verificada – ‍Se o software ou um site presumir que todas as entradas são seguras, ele pode executar injeção de SQL não intencional.
- Pessoas – A engenharia social é a maior ameaça para a maioria das organizações. Assim, os humanos podem ser uma das maiores causas de vulnerabilidade.

**Tipos de Vulnerabilidades**

Ao revisar a postura e a abordagem de segurança cibernética de sua empresa, é importante perceber que as vulnerabilidades de segurança cibernética estão sob o controle da organização — não do cibercriminoso. Esse é um aspecto do cenário de segurança cibernética que as empresas podem abordar e gerenciar proativamente, tomando as medidas apropriadas e empregando as ferramentas, processos e procedimentos adequados.

Segue abaixo os tipos mais comuns de vulnerabilidade.

- Erros de configuração do sistema - os ativos de rede que possuem controles de segurança díspares ou configurações vulneráveis ​​podem resultar em configurações incorretas do sistema. Os cibercriminosos geralmente investigam as redes em busca de configurações incorretas do sistema e lacunas que parecem exploráveis.
- Software desatualizado - semelhante às configurações incorretas do sistema, os hackers tendem a sondar as redes em busca de sistemas não corrigidos, que são alvos fáceis. Essas vulnerabilidades não corrigidas podem ser exploradas por invasores, para roubar informações confidenciais. Para minimizar esses tipos de riscos, é essencial estabelecer um cronograma de gerenciamento de patches, para que todos os patches de sistema mais recentes sejam implementados assim que forem lançados.
- Credenciais de autorização ausentes ou fracas - uma tática comum que os invasores usam é obter acesso a sistemas e redes por meio de força bruta, como adivinhar as credenciais dos funcionários. É por isso que é crucial que os funcionários sejam instruídos sobre as melhores práticas de segurança cibernética, para que suas credenciais de login não sejam facilmente exploradas.
- Ameaças internas maliciosas - Seja com intenção maliciosa ou não intencional, os funcionários com acesso a sistemas críticos às vezes acabam compartilhando informações que ajudam os criminosos cibernéticos a violar a rede. As ameaças internas podem ser realmente difíceis de rastrear, pois todas as ações parecerão legítimas. Para ajudar a combater esses tipos de ameaças, deve-se investir em soluções de controle de acesso à rede e segmentar a rede de acordo com a experiência e experiência do funcionário.
- Criptografia de dados ausente ou ruim - é mais fácil para os invasores interceptar a comunicação entre os sistemas e violar uma rede, se ela tiver criptografia ruim ou ausente. Quando há informações ruins ou não criptografadas, os adversários cibernéticos podem extrair informações críticas e injetar informações falsas em um servidor.
- APIs não seguras - outra vulnerabilidade de segurança comum são as interfaces de programação de aplicativos (APIs) não seguras. As APIs fornecem uma interface digital que permite que aplicativos ou componentes de aplicativos se comuniquem entre si pela Internet ou por meio de uma rede privada. As APIs são alguns dos poucos ativos organizacionais com um endereço IP público. Se não forem devidamente protegidos, eles podem se tornar um alvo fácil para os invasores violarem.
- Controle de acesso ou acesso não autorizado - as empresas geralmente concedem aos funcionários mais acesso e permissões do que o necessário para desempenhar suas funções de trabalho. Isso aumenta as ameaças baseadas em identidade e expande o acesso a adversários, em caso de violação de dados. Para resolver esse problema, as organizações devem implementar o princípio do privilégio mínimo (POLP), um conceito e prática de segurança de computador que dá aos usuários direitos de acesso limitados com base nas tarefas necessárias para seu trabalho.
- Não entendendo o “Modelo de Responsabilidade Compartilhada” (ou seja, Ameaças de Tempo de Execução) - as redes em nuvem aderem ao que é conhecido como “modelo de responsabilidade compartilhada”. Isso significa que grande parte da infraestrutura subjacente é protegida pelo provedor de serviços em nuvem. No entanto, a organização é responsável por todo o resto, incluindo o sistema operacional, aplicativos e dados.

**Avaliação de Vulnerabilidade**

O processo de encontrar vulnerabilidades e riscos em redes de computadores, sistemas, hardware, aplicativos e outros aspectos do ecossistema de TI é conhecido como avaliação de vulnerabilidade.

As avaliações de vulnerabilidade fornecem, às equipes de segurança e outras partes interessadas, os dados de que precisam para identificar e priorizar ameaças, para possível correção no tempo certo.

Existem vários tipos de avaliações de vulnerabilidade:

- **Avaliação baseada em rede:** esse tipo de avaliação é usado para identificar possíveis problemas na segurança da rede e detectar sistemas vulneráveis ​​em redes com e sem fio.
- **Avaliação baseada em host:** A avaliação baseada em host pode ajudar a localizar e identificar vulnerabilidades em servidores, estações de trabalho e outros hosts de rede. Ele geralmente avalia portas e serviços abertos e torna mais visíveis as definições de configuração e o gerenciamento de patches dos sistemas verificados.
- **Avaliação de rede sem fio:** envolve a varredura de redes Wi-Fi e vetores de ataque na infraestrutura de uma rede sem fio. Ela ajuda a validar se uma rede está configurada com segurança, para evitar acesso não autorizado, e também pode detectar pontos de acesso não autorizados.
- **Avaliação de aplicações:** É a identificação de vulnerabilidades de segurança em aplicações web e seu código-fonte. Isso é obtido implementando ferramentas automatizadas de varredura de vulnerabilidade no front-end, ou analisando o código-fonte de forma estática ou dinâmica.
- **Avaliação de banco de dados:** A avaliação de bancos de dados ou sistemas de big data, quanto à vulnerabilidades e configuração incorreta, identificando bancos de dados não autorizados ou ambientes de desenvolvimento/teste inseguros, e classificando dados confidenciais para melhorar a segurança dos dados.

**Gerenciamento de Vulnerabilidade**

Para estar sempre um passo à frente de ataques maliciosos, os profissionais de segurança precisam ter um processo para monitorar e gerenciar as vulnerabilidades conhecidas.

Com as redes se tornando cada vez mais complexas, tornou-se fundamental gerenciar ativamente as vulnerabilidades de segurança cibernética. Para isso, é essencial ter visibilidade dos ecossistemas de rede internos e de terceiros.

As principais etapas de um gerenciamento são:

- **Identificar vulnerabilidades:** analisando varreduras de rede, logs de firewall, resultados de testes de penetração e resultados de varreduras de vulnerabilidade, para encontrar anomalias que possam destacar vulnerabilidades propensas a ataques cibernéticos.
- **Verificar vulnerabilidades:** decida se uma vulnerabilidade identificada pode ser explorada e classifique sua gravidade para entender o nível de risco.
- **Mitigar vulnerabilidades:** crie contramedidas apropriadas e meça sua eficácia, se um patch não estiver disponível.
- **Corrigir as vulnerabilidades:** atualize ou troque o software ou hardware vulnerável sempre que possível. É hora de traçar um cronograma e um plano de trabalho para a correção.

**O que é gerenciamento de eventos e informações de segurança (SIEM)?**

É uma abordagem que combina funções de Gerenciamento de Informações de Segurança (SIM) e Gerenciamento de Eventos de Segurança (SEM), em um único sistema de gerenciamento de segurança.

Os princípios subjacentes de todo sistema SIEM são agregar dados relevantes de várias fontes, identificar desvios da norma e tomar as medidas apropriadas. Por exemplo, quando um possível problema é detectado, um sistema SIEM pode registrar informações adicionais, gerar um alerta e instruir outros controles de segurança a interromper o progresso de uma atividade.

No nível mais básico, um sistema SIEM pode ser baseado em regras ou empregar um mecanismo de correlação estatística para fazer conexões entre as entradas do log de eventos. Os sistemas SIEM avançados evoluíram para incluir análises de comportamento de usuários e entidades, bem como orquestração, automação e resposta de segurança.

As ferramentas SIEM reúnem dados de log e eventos criados por sistemas host em toda a infraestrutura de uma empresa e reúnem esses dados em uma plataforma centralizada. Os sistemas host incluem aplicativos, dispositivos de segurança, filtros antivírus e firewalls. As ferramentas SIEM identificam e classificam os dados em categorias, como logins bem-sucedidos e com falha, atividade de malware e outras atividades maliciosas prováveis.

O software SIEM gera alertas de segurança, quando identifica possíveis problemas de segurança. Usando um conjunto de regras predefinidas, as organizações podem definir esses alertas como de baixa ou alta prioridade.

O software permite que as organizações detectem incidentes que, de outra forma, poderiam passar despercebidos; também pode ajudar uma organização a atender aos requisitos de conformidade, gerando automaticamente relatórios que incluem todos os eventos de segurança registrados entre essas fontes.

**Como aplicar na prática o que aprendeu**

Com a chegada da pandemia, o trabalho remoto passou de tendência para realidade. Com isso, os chamados "endpoints" passaram a ter uma atenção redobrada, pois seria preciso acessar redes, sistemas e demais serviços de uma organização de fora da mesma. Há muitas formas seguras de se realizar este processo, mas nem todas as empresas estavam preparadas. Com isso cresceu uma tendência chamada Zero Trust, onde as estratégias de acesso passaram de "confiar, mas verificar" para "nunca confiar, sempre verificar". No modelo Zero Trust, nenhum acesso, dispositivo ou usuário é confiável para acessar um recurso, até que sua identidade e autorização sejam verificadas. Faça uma pesquisa e busque pelas principais funcionalidades e benefícios deste modelo.

**Conteúdo bônus**

**Tópicos avançados**

Há inúmeras ferramentas disponíveis para detecção e avaliação de vulnerabilidades. Essas ferramentas podem ser usadas em redes, sistemas operacionais, sites, sistemas web, entre outros.

Algumas ferramentas de avaliação de vulnerabilidade:

- Netsparker
- Acunetix
- Intruder
- SolarWinds Network Vulnerability Detection
- Apptrana
- Syxsense
- Breachlock
- Openvas

Selecione pelo menos duas ferramentas e faça uma pesquisa direcionada, para verificar como e onde é realizada a análise de vulnerabilidade.      

Referência Bibliográfica

Vulnerability Assessment In Cybersecurity: A Complete Guide. **Cybersecurity For Me**, 2023. Disponível em: <[https://cybersecurityforme.com/vulnerability-assessment/](https://cybersecurityforme.com/vulnerability-assessment/)>. Acesso em 13 de janeiro de 2023.

‌What is a vulnerability? Definition + examples. **Upguard**, 2022. Disponível em: <[https://www.upguard.com/blog/vulnerability](https://www.upguard.com/blog/vulnerability)>. Acesso em 13 de janeiro de 2023.

GILLIS, A. S.ROSECRANCE, L. What is SIEM? **TechTarget**, 2022. Disponível em: <[https://www.techtarget.com/searchsecurity/definition/security-information-and-event-management-SIEM](https://www.techtarget.com/searchsecurity/definition/security-information-and-event-management-SIEM)>. Acesso em 13 de janeiro de 2023.