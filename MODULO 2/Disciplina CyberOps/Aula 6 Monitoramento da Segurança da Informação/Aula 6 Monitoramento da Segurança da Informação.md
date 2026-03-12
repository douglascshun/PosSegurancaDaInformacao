**Introdução**

O módulo em questão foi dividido em cinco temas que abordam desde a natureza dos dados usados em monitoramento de segurança, passando por análise e alertas de logs, finalizando com o entendimento de como funciona um network security monitoring. Vale destacar que no tópico sobre alertas foram apresentados conceitos e práticas muito significativos no tocante a estruturação, configuração e classificação de alertas. Assim, todo conhecimento oferecido neste módulo tem aplicabilidade em muitas ações de cyberops e segurança da informação.

**Objetivos da aula**

- Verificar os diferentes tipos de dados envolvidos em monitoramento de segurança;
- Analisar logs e arquivos de logs;
- Compreender as dinâmicas de alertas em um sistema de segurança da informação;
- Avaliar e interpretar a correlação de alertas;
- Entender como funciona um network security monitoring.

**Resumo**

O primeiro tema estudado neste módulo versou sobre tipos de dados usados no monitoramento de segurança. Contudo é imperativo apresentar as três categorias de atuação básica de monitoramento, que são: monitoramento técnico, funcional e de processos de negócios.

Ainda na temática sobre monitoramento de segurança, cabe destacar os tipos aplicativos ou software/dados de monitoramento:

**Tempo de atividade / monitoramento de disponibilidade:** analisa periodicamente o servidor para ver se ele está ligado

**Monitoramento de desempenho do site:** uma biblioteca JavaScript pode não aparecer, tornando a página semi-funcional

**Monitoramento de recursos:** monitorar todos os tipos de aspectos de desempenho das operações do servidor.

No monitoramento de erros, é possível instrumentalizar os servidores especificamente para rastrear e monitorar erros de aplicativos. Alguns erros são esperados, porém, o administrador deve se preocupar se esse número aumentar significativamente.

O monitoramento de log busca observar arquivos de log, principalmente porque os servidores geram todos os tipos de logs de aplicativos. Também é muito significativo o monitoramento entre dispositivos de rede como roteadores, firewall, switches e outros equipamentos.

Na atividade de análise de logs de dispositivos e segurança de redes, cada artefato e aplicativo gera logs, que podem conter dados cruciais de integridade e segurança dos processos e serviços. Por exemplo, os logs de eventos podem registrar alterações de configuração, movimentação de arquivos e diretórios, alterações de contas privilegiadas, etc.

Ainda sobre alertas, as categorias de alertas de segurança consistem em: alertas de reconhecimento, alertas de credenciais comprometidas, alertas de movimento lateral, alertas de predominância de domínio e alertas de exfiltração. A correlação de alertas em incidentes de segurança consiste em analisar diferentes sinais em todos os recursos, concatenando conhecimento de segurança e inteligência artificial para analisar alertas, descobrindo novos padrões de ataque, à medida que ocorrem.

No que se refere à avaliação e correlação de alertas, a análise de segurança no campo de inovações em tecnologias de big data e aprendizado de máquina são usadas para consolidar os eventos de avaliação em toda a atuação de nuvem, detectando ameaças que seriam impossíveis de identificar usando estratégias abordagens manuais, buscando a prever a evolução de ataques.

Um destaque da avaliação e correlação de alertas é a análise comportamental que representa uma técnica que analisa e compara dados em uma coleção de padrões conhecidos. Contudo, esses padrões não são assinaturas simples, são construídos através de algoritmos de aprendizado de máquina que são correlacionados a grandes conjuntos de dados.

Em contraponto à análise de comportamento, que depende de padrões conhecidos derivados de grandes bancos de dados, a detecção de anomalias é mais "personalizada" e se foca nas linhas de base que são específicas das suas implantações. A aprendizagem de máquina é aplicada para definir a atividade normal das implantações e, em seguida, as regras são construídas com intuito de definir condições de exceção que possam materializar um evento de segurança.

O monitoramento de segurança de rede representa com conjunto de ações de coleta de métricas de:

- Comunicação cliente-servidor;
- Carga útil de rede;
- Sessões de tráfego criptografadas;
- Detecção de padrões nos fluxos de tráfego.

Conceitualmente, o principal objetivo do monitoramento de segurança de rede é fornecer um serviço contínuo que verifica o ambiente de negócios em busca de atividades suspeitas e ameaças. As equipes de TI podem então investigar as atividades relatadas e tomar as medidas corretivas apropriadas.

**Como aplicar na prática o que aprendeu**

Nmap ("Network Mapper") é um utilitário gratuito e de código aberto para descoberta de rede e auditoria de segurança. Muitos sistemas e administradores de rede também o consideram útil para tarefas como inventário de rede, gerenciamento de agendamentos de atualização de serviço e monitoramento de host ou tempo de atividade de serviço. O Nmap usa pacotes IP brutos de novas maneiras para determinar quais hosts estão disponíveis na rede, quais serviços (nome e versão do aplicativo) esses hosts estão oferecendo, quais sistemas operacionais (e versões do sistema operacional) estão executando, que tipo de filtros/firewalls de pacotes estão em uso, e dezenas de outras características. Ele foi projetado para escanear rapidamente grandes redes, mas funciona bem em hosts únicos. O Nmap é executado em todos os principais sistemas operacionais de computador e os pacotes binários oficiais estão disponíveis para Linux, Windows e Mac OS X. Além do clássico executável Nmap de linha de comando, o pacote Nmap inclui uma GUI avançada e visualizador de resultados (Zenmap), uma ferramenta flexível de transferência de dados, redirecionamento e depuração (Ncat), um utilitário para comparar resultados de varredura (Ndiff) e uma ferramenta de geração de pacotes e análise de resposta (Nping). Utilizando o nmap desenvolva uma prática pessoal e busque vulnerabilidades em sua rede doméstica.

**Conteúdo bônus**

**Tópicos avançados**

Como um novato realizando reparos automotivos, posso lutar por horas tentando encaixar minhas ferramentas rudimentares (martelo, fita adesiva, chave inglesa, etc) na tarefa em questão. Quando eu falho miseravelmente e reboco meu calhambeque até um mecânico de verdade, ele invariavelmente vasculha em um enorme baú de ferramentas até retirar o aparelho perfeito que faz o trabalho parecer fácil. A arte da varredura de portas é semelhante. Os especialistas entendem as dezenas de técnicas de varredura e escolhem a (ou combinação) apropriada para uma determinada tarefa. Usuários inexperientes e script kiddies, por outro lado, tentam resolver todos os problemas com a verificação SYN padrão. Como o Nmap é gratuito, a única barreira para o domínio da varredura de portas é o conhecimento. Isso, certamente, supera o mundo automotivo, onde pode ser necessária muita habilidade para determinar que você precisa de um compressor de mola de suporte, mas ainda assim terá que pagar milhares de dólares por isso. Leia o artigo sobre “Port Scanning Techniques” indicado no link a seguir. Disponível em: <[https://nmap.org/book/man-port-scanning-techniques.html](https://nmap.org/book/man-port-scanning-techniques.html)>. **(Acesso em 16/02/2023)**

**Referência Bibliográfica**

**Bibliografia Básica**

RICCI, Bruno. **Rede Segura:** VPN Linux, Editora Ciência Moderna, 2007.

TANENBAUM, A. S., **Redes de Computadores**. Rio de Janeiro, Campus, 2003.

COSTA, Daniel Gouveia. **Administração de Redes com Scripts**, 2ª Edição, Editora Brasport, 2010.

**Bibliografia Complementar**

SMITH, Roderick W**. Linux**: Ferramentas Poderosas, 1ª Edição, 2004, Editora Ciência Moderna.

NAKAMURA, E. T., e GEUS, P. L., **Segurança de Redes em Ambientes Cooperativos**, 2 ed. Ed. Berkley, São Paulo, 2007.

MORAES, Alexandre F. **Redes de Computadores**. 7ª Edição, Editora Érica, 2008.

MENDES, Douglas Rocha, **Redes de Computadores**, Ed. Novatec, 1ª Edição, 2007

STARLIN, Gorki, **Conceitos, Protocolos e Uso Tcp/Ip**: Redes de Computadores. 1ª Edição, Alta Books, 2004.