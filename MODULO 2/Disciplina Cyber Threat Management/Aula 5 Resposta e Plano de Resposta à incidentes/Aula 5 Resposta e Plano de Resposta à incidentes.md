[[Cyber Threat Management]]
## Resposta e Plano de Resposta à incidentes

**Introdução**

Uma das grandes preocupações de uma organização é, sem dúvidas, o tempo de resposta, recuperação e resiliência a um incidente, seja ele de qualquer natureza. Para que essa resposta seja satisfatória, alguns procedimentos e planos devem ser criteriosamente estabelecidos, testados e de conhecimento de todos. Quando se trata de cibersegurança, os riscos são ainda maiores e, portanto, o processo deve ser elaborado e o documento direcionado a uma ação coordenada para que a mitigação dos riscos ocorra da melhor forma.

**Objetivos da aula**

- Definir o que é incidente e quais os tipos principais.

- O que é um plano de resposta a incidentes e quais as etapas principais deste processo.

- Quais os padrões e orientações para cibersegurança propostos pelo NIST.

**Resumo**

**O que é um incidente de segurança?**

Um incidente de segurança é um evento que pode indicar que os sistemas ou dados de uma organização foram comprometidos ou que as medidas implementadas para os proteger falharam.

Em TI, um evento é qualquer coisa que tenha importância para o hardware ou software do sistema. Já um incidente é um evento que interrompe as operações normais. Os eventos de segurança geralmente são diferenciados pelo grau de gravidade e pelo risco potencial associado à organização.

Se um único usuário tiver acesso negado a um serviço solicitado, por exemplo, isso pode ser considerado um evento de segurança, porque pode indicar um sistema comprometido, mas a falha de acesso também pode ser causada por muitas outras coisas. O fator comum para a maioria dos eventos de segurança, não importa o que os causou, é que eles normalmente não têm um impacto severo na organização. No entanto, se muitos usuários tiverem acesso negado, isso provavelmente indica um problema mais sério, como um ataque distribuído de negação de serviço (DDoS). De modo que esse evento pode ser classificado como um incidente de segurança devido ao seu impacto prejudicial nas operações.

Um incidente também pode ser definido como violação ou ameaça de violação das políticas de segurança de informática, políticas de uso aceitável, ou práticas de segurança padrão.

**Como prevenir um incidente de segurança**

Métodos e ferramentas comuns usados ​​para prevenir incidentes de segurança incluem o seguinte:

- Treine regularmente os funcionários para garantir que eles estejam familiarizados com os padrões e práticas de segurança corporativa.
- Use auditores de TI internos e externos, revise regularmente as políticas e práticas de segurança de TI para garantir que estejam atualizadas, incluindo testes de penetração e vulnerabilidade de redes e sistemas.
- Certifique-se de que os patches de segurança para hardware e software sejam implementados e atualizados constantemente.
- Monitore instalações físicas, incluindo acesso seguro a centros de dados e armários, armários de arquivos e outras áreas de armazenamento que possam conter documentos impressos confidenciais.
- Monitore e registre atividades de usuários e dados em redes, estações de trabalho do sistema e dispositivos IoT. Use alertas automatizados em tempo real para detectar possíveis violações de segurança.
- Criptografe laptops e dispositivos móveis, bloqueie qualquer equipamento perdido ou roubado em campo.

**Como responder a um incidente de segurança**

Como as violações de segurança são, na verdade, um subconjunto de incidentes de segurança, as ferramentas e técnicas usadas para resolvê-las são semelhantes. Em todos os casos, o objetivo é subjugar ou resolver o incidente o mais rápido possível.

A seguir, estão algumas técnicas comuns que as organizações podem usar para responder a incidentes de segurança:

**Reúna a equipe -** coordenar a equipe de especialistas em segurança que irá avaliar a gravidade do incidente, comunicar a gestão e realizar a mitigação.

**Identificar, avaliar e conter o incidente -** identifique o que foi comprometido. Se uma rede específica estiver infectada, mas outras redes não, isole imediatamente a rede afetada para evitar que a infecção se espalhe. Ao mesmo tempo, preserve todos os dados da rede infectada para análise posterior.

**Recupere e restaure -** se os sistemas ou redes forem afetados tão gravemente que não possam ser operados com confiança, execute uma recuperação de desastre completa e failover. _(Failover é um modo operacional de backup no qual as funções de um componente do sistema são assumidas por um componente secundário quando o componente principal fica indisponível)_

**Notifique as pessoas afetadas pelo incidente -** se os dados de clientes foram comprometidos durante o incidente, notifique as pessoas afetadas.

**Resolver problemas internos -** se um ato malicioso foi perpetrado por um funcionário da empresa, notifique os recursos humanos para que as ações apropriadas sejam tomadas.

**Execute um incidente de segurança post-mortem** - depois que o incidente de segurança for resolvido, analise o que aconteceu, como aconteceu e como as medidas podem ser tomadas para evitar incidentes semelhantes no futuro. Revise as políticas e práticas para refletir quaisquer mudanças.

Avalie o desempenho da sua equipe - quanto tempo demorou para detectar o incidente? Quanto tempo demorou para resolver? Há algo que você poderia ter feito melhor?

**Tipos de incidentes**

Quando a questão é um tipo de incidente, tem relação direta com algum tipo de ataque, que constantemente pode ter diferentes origens e diferentes estratégias de respostas. Os ataques cibernéticos não apenas se tornaram mais comuns, como também se tornaram mais fáceis de realizar.

De acordo com um relatório da NETSCOUT Threat Intelligence, houve 4,83 milhões de ataques cibernéticos apenas no primeiro semestre deste ano.

A seguir, estão alguns tipos de ataques que podem se tornar incidentes de segurança:

- **Ataques baseados em malware** (ransomware, spyware, vírus, trojans etc.): Malware refere-se a "software malicioso” projetado para interromper ou roubar dados de um computador, rede ou servidor. O malware é um dos ataques cibernéticos mais comumente usados. E existem várias variações das quais você deve estar ciente. O malware mais utilizado e temido nas organizações nos últimos anos é o Ransomware. Esse tipo de malware criptografa arquivos em seu sistema para que você não possa acessá-los até pagar um “resgate” (geralmente em criptomoeda). Houve um aumento de 1.885% nos ataques de ransomware em todo o mundo a partir de 2021.

- **Ataques de phishing**: um ataque de phishing ocorre quando um cibercriminoso envia a você um e-mail fraudulento, mensagem, texto (chamado “smishing”) ou telefonema (chamado “vishing”). As mensagens de phishing e smishing podem instruí-lo a clicar em um link ou abrir um anexo de e-mail que fará o download de malware em seu dispositivo ou o enviará a um site falso projetado para roubar suas informações. Em muitos casos, os ataques de phishing lançam uma rede ampla e não têm como alvo indivíduos específicos (o que os torna mais fáceis de identificar). No entanto, existem alguns novos ataques cibernéticos de phishing que são mais direcionados e difíceis de detectar.

**Man-in-the-middle:** Um ataque man-in-the-middle (MitM) ocorre quando invasores interceptam dados ou comprometem sua rede para “escutar” você. Esses ataques são especialmente comuns ao usar redes Wi-Fi públicas, que podem ser facilmente invadidas por não terem uma criptografia forte no momento da conexão. Por exemplo, digamos que você esteja usando o Wi-Fi aberto e precise verificar o saldo de sua conta bancária. Quando você faz login, um hacker pode interceptar seus dados e capturar seu nome de usuário e senha.

**Negação de Serviço (DOS) e Negação de Serviço Distribuída (DDoS):** Muitos ataques cibernéticos visam sobrecarregar os servidores, forçando o desligamento dos serviços. Um ataque de negação de serviço (DOS) ocorre quando os hackers usam solicitações e tráfego falsos para sobrecarregar um sistema e desligá-lo. Um ataque distribuído de negação de serviço (DDoS) é o mesmo tipo de ataque, exceto que o hacker usa vários dispositivos violados ao mesmo tempo. O objetivo deste ataque é interromper os serviços.

**Ataques de injeção de SQL:** A maioria dos sites usa bancos de dados SQL para armazenar informações confidenciais, como logins, senhas e informações de contas. Os hackers usam um ataque de injeção de SQL para “enganar” o banco de dados para que forneça essas informações. Esses comandos podem ler dados confidenciais, modificar dados do banco de dados ou até mesmo adicionar novas funções fraudulentas. É um dos ataques mais comuns e também possui muitas formas de evitá-lo.

**Explorações e ataques de dia zero:** Explorações de dia zero são vulnerabilidades de segurança cibernética que existem em um software ou rede sem o conhecimento do fabricante. Por exemplo, a Apple pode lançar uma nova versão do iOS que contém acidentalmente uma maneira de hackers roubarem suas informações do iCloud. Ao descobrir a falha, a empresa atacada tem “zero dias” para consertá-la, pois já está vulnerável.  

**Ataque de IoT:** Dispositivos da Internet das Coisas como alto-falantes inteligentes, TVs e brinquedos, também podem ser alvos de ataques cibernéticos. Um ataque de IoT ocorre quando hackers roubam dados de um dispositivo — ou agrupam vários dispositivos de IoT em uma botnet — que podem ser usados ​​para ataques DDoS. Os dispositivos IoT geralmente não possuem software antivírus instalado, tornando-os alvos fáceis para hackers. Pode parecer improvável, mas até mesmo sua “geladeira inteligente” pode ser um soldado involuntário em um ataque cibernético.

**Ameaças internas:** Os ataques cibernéticos geralmente vêm de uma ameaça externa, como um grupo de hackers. Porém, também há a possibilidade de ameaças internas. As ameaças internas ocorrem quando alguém que trabalha para uma empresa rouba dados de propósito, dá acesso não autorizado a alguém ou vaza senhas. 

**Plano de resposta a incidentes**

**Um plano de resposta a incidentes** é um documento que descreve os procedimentos, etapas e responsabilidades de uma organização de seu programa de resposta a incidentes. O objetivo é prevenir ataques cibernéticos antes que eles aconteçam e minimizar o custo e a interrupção dos negócios resultantes de quaisquer ataques cibernéticos que ocorram.

Idealmente, uma organização define processos e tecnologias de resposta a incidentes em um plano formal de resposta a incidentes (IRP) que especifica exatamente como diferentes tipos de ataques cibernéticos devem ser identificados, contidos e resolvidos.

  
**O planejamento de resposta a incidentes geralmente inclui as seguintes etapas:**

**Preparação ou Planejamento**: Esta primeira fase de resposta é contínua, para garantir que o CSIRT sempre tenha os melhores procedimentos e ferramentas possíveis para responder, identificar, conter e recuperar de um incidente o mais rápido possível e com o mínimo de interrupção dos negócios. Por meio de avaliações regulares de riscos, o CSIRT identifica vulnerabilidades de rede, define os vários tipos de incidentes de segurança que representam um risco para a rede e prioriza cada tipo de acordo com seu impacto potencial na organização.

**Identificação, detecção e análise**: A segunda fase do IR é determinar se um incidente ocorreu, sua gravidade e seu tipo. Se no planejamento são definidas as formas de monitoramento, aqui, na identificação, é usado o monitoramento de ativos de TI para detectar qualquer padrão de comportamento anormal de um endpoint, seja um recurso em rede ou em cloud, e-mail, dispositivos, servidores, softwares ou rede interna. Tudo pode ser utilizado como indicador, correlacionando dados para se ter uma identificação rápida e precisa de eventos que podem levar a um incidente de TI.

**Contenção**: O objetivo da fase de contenção é interromper os efeitos de um incidente antes que ele possa causar mais danos. Na contenção, temos então a mitigação do ataque para reduzir os possíveis danos do ataque ou incidente de TI. Aqui, ainda, é evitado ao máximo perder provas ou evidências do incidente, auxiliando assim na identificação de futuros padrões de ataques baseado em comportamento e padrões.

**Erradicação**: Depois que a ameaça é contida, a equipe passa para a correção total e a remoção completa da ameaça do sistema. Isso envolve erradicar ativamente a própria ameaça — por exemplo, destruir malware, inicializar um usuário não autorizado ou desonesto da rede — e revisar os sistemas afetados e não afetados para garantir que nenhum vestígio da violação seja deixado para trás.

**Recuperação**: Uma reunião de lições aprendidas envolvendo todas as partes relevantes deve ser obrigatória após um incidente grave e desejável após incidentes menos graves com o objetivo de melhorar a segurança como um todo e o tratamento de incidentes em particular. Quando a equipe de resposta a incidentes está confiante de que a ameaça foi totalmente erradicada, ela restaura os sistemas afetados para operações normais. Isso pode envolver a implantação de patches, a reconstrução de sistemas a partir de backups e a colocação online de sistemas e dispositivos corrigidos.

**Revisões e documentação**: Ao longo de cada fase do processo de resposta a incidentes, é feita a coleta de evidências da violação e documentada as etapas necessárias para conter e erradicar a ameaça. Essas informações são de extrema importância para evitar e corrigir rapidamente novos incidentes.

**NIST Cybersecurity Framework**

O NIST Cybersecurity Framework, lançado em 2014, fornece um modelo para reduzir os riscos à infraestrutura crítica. Ele foi projetado para ajudar as organizações a entender, gerenciar e reduzir melhor seus riscos de segurança cibernética.

O NIST lista seus padrões em seu site oficial. Os padrões e recursos disponibilizados são baseados nas melhores práticas internacionais, são tecnologicamente neutros e podem ser implementados por organizações de todos os tamanhos e instituições federais.

O NIST Cybersecurity Framework inclui cinco conceitos principais em torno do ciclo de vida do risco de segurança cibernética.

![Fonte: https://nist.gov (acesso em 13/01/2023)](https://paperx-dex-assets.s3.sa-east-1.amazonaws.com/images/1676583920109-hQcN1kJyMu.png "Fonte: https://nist.gov (acesso em 13/01/2023)")

Fonte: [https://nist.gov](https://nist.gov) (acesso em 13/01/2023)

**Identificar**: determina como o risco de segurança cibernética é gerenciado, juntamente com quais sistemas, dados e recursos que são necessários.

**Proteger**: fornece proteções para conter incidentes de segurança de dados para que uma organização possa continuar fornecendo serviços críticos quando necessário.

**Detectar**: determina os protocolos em vigor que identificam eventos de segurança.

**Responder**: descreve as ações a serem tomadas durante um incidente de segurança cibernética.

**Recuperar**: Esta etapa identifica o que fazer após um ataque de segurança cibernética para manter a continuidade dos negócios e iniciar a recuperação de desastres.

**Como aplicar na prática o que aprendeu**

Em nossa aula, conhecemos o NIST Cybersecurity Framework, que é considerado um padrão para segurança tecnológica, além de possuir um plano e etapas para resposta a incidentes.

Outro padrão mais recente e muito aceito pelas organizações é o SANS - SysAdmin, Audit, Network and Security. O SANS tem como foco principal a segurança de TI, além de manter o maior repositório de informações de segurança do mundo. Com base nessas informações, faça uma busca na internet e liste quais as etapas para resposta a incidente são aplicadas pela SANS. Com isso, é possível verificar as similaridades com o NIST e adotar no momento oportuno aquela que se encaixa melhor nas necessidades da empresa.

**Conteúdo bônus**

**Tópicos avançados**

Umas das tecnologias utilizadas para a detecção de possíveis incidentes é a UEBA - Análise de Comportamento de Usuários e Entidades. A UEBA é uma solução de segurança cibernética que usa algoritmos e aprendizado de máquina para detectar anomalias no comportamento, não apenas dos usuários em uma rede corporativa, mas também dos roteadores, servidores e endpoints nessa rede.

A UEBA procura reconhecer qualquer comportamento peculiar ou suspeito – casos em que há irregularidades de padrões ou uso cotidianos normais. Por exemplo, se um usuário específico na rede baixa regularmente arquivos de 20 MB todos os dias, mas começa a baixar 4 GB de arquivos, o sistema UEBA consideraria isso uma anomalia e alertaria um administrador de TI ou, se as automações estiverem em vigor, desconectaria automaticamente esse usuário da rede.

Assim como o SIEM e o UEBA, outras ferramentas como EDR (endpoint detection and response), SOAR (security orchestration, automation and response) e o XDR (extended detection and response) podem auxiliar as organizações na prevenção e detecção de incidentes cibernéticos.

Referência Bibliográfica

LUTTGENS, J. T.; PEPE, M.; MANDIA, K. **Incident response & computer forensics**. 3. ed. New York, NY: McGraw-Hill Professional, 2014.

MAHN, A. et al. **Getting started with the NIST cybersecurity framework: A quick start guide** (Portuguese translation). [s.l.] National Institute of Standards and Technology, 2022.

SHACKLETT, M. E.; WIGMORE, I. **Security incident**. Disponível em: <[https://www.techtarget.com/whatis/definition/security-incident](https://www.techtarget.com/whatis/definition/security-incident)>. Acesso em 13 de janeiro de 2023.