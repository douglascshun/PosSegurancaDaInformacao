[[Network Defense]]

**Introdução**

Agora, vamos entender a importância da segurança nos serviços em nuvem, entendendo suas categorias, tipos e desafios.

  
**Objetivos da aula**

- O que é um Sistema em Nuvem?
- Importância da segurança nos Sistemas em Nuvem e suas Categorias
- Arquiteturas/Modelos de segurança
- Tipos de Estruturas de Segurança em Nuvem
- Zero Trust e desafios da Segurança em Nuvem

  
**Resumo**

**Importância da segurança nos Sistemas em Nuvem**

Quando um atacante quer acessar ou invadir um sistema, o primeiro obstáculo é a camada 1, ou seja, ele precisa entrar no prédio, passando pela portaria, para chegar fisicamente até o equipamento e iniciar sua ação. Contudo, nos sistema em nuvem, não temos nenhuma obstrução, ou controle de acesso para chegar até a sala ou ambiente onde se encontram os dispositivos, também não temos como implementar segurança de camada 2, pois o atacante pode chegar ao sistema sem precisar se conectar a algum switch sobre nossa gerência. Isso faz com que toda a segurança de sistemas em nuvem comece na camada 3 (camada de internet). As estratégias de camada 1 e 2 não estão disponíveis.

  
**Aspectos da Segurança em Nuvem.**

A **segurança de dados** é um aspecto que envolve o objetivo técnico de prevenir as ameaças. As ferramentas e tecnologias permitem que provedores e clientes instalem barreiras para o acesso e controlem a visibilidade de dados confidenciais. Entre eles, a criptografia é com certeza uma das ferramentas disponíveis mais eficientes, pois ela codifica seus dados para que apenas alguém que possua a chave de cifra possa lê-los. Se os seus dados forem roubados ou perdidos, ficarão totalmente ilegíveis e não farão sentido. As proteções de dados em trânsito, como VPNs (redes privadas virtuais), também se destacam nas redes em nuvem.

O **gerenciamento de identidade e acesso** (IAM) é um item que se relaciona aos privilégios de acesso concedidos à conta de um usuário. O gerenciamento desta autenticação e/ou autorização de contas dos usuários aqui também é válido. São essenciais estes controles de acesso para impedir que usuários, legítimos ou mal-intencionados, consigam acessar, comprometer dados e sistemas confidenciais. Administração de senha, autenticação multifator e outros métodos estão ao alcance do IAM.

A **governança** está concentrada em políticas para detectar, prevenir e mitigar ameaças. Está focada principalmente em empresas, mas mesmo os clientes individuais da nuvem podem se beneficiar considerando adequadamente as políticas e o treinamento de comportamento seguro do usuário. São utilizados principalmente em ambientes organizacionais, mas as regras de uso seguro e resposta às ameaças podem ser úteis para qualquer cenário.

**A** **retenção de dados (DR-Data Retencion) e o planejamento de continuidade de negócios (BC-Business Continuity)** implicam em medidas técnicas para a recuperação de desastres nos casos de perda de dados. Métodos que forneçam redundância para os dados, como cópias de segurança, são essenciais para qualquer plano que envolva DR e BC. Além disso, pode ser útil contar com sistemas técnicos que possam garantir operações ininterruptas. Estruturas para comprovar a validade das cópias de segurança e instruções detalhadas de recuperação para os funcionários são de igual importância para um plano BC completo.

**A conformidade legal** está relacionada à proteção da privacidade dos dados do usuário, conforme foi definido legalmente. Os governos e as empresas são responsáveis pela proteção das informações privadas dos usuários contra exploração principalmente para fins lucrativos. Como tal, as organizações devem seguir os regulamentos para cumprir com estas políticas. Uma possível abordagem é o mascaramento de dados, que oculta a identidade deles por meio de métodos de criptografia.

**Arquiteturas/Modelos de segurança**

![Fonte: Autoria própria, 2023.](https://paperx-dex-assets.s3.sa-east-1.amazonaws.com/images/1678143422387-OKwTkfYoiN.png "Fonte: Autoria própria, 2023.")

Fonte: Autoria própria, 2023.

O primeiro item que se deve levar em consideração ao montar uma arquitetura ou modelo de segurança é o negócio do cliente, pois de nada adianta um sistema ultra seguro que não atende ao objetivo da empresa. Muitos dos técnicos se ligam apenas aos aspectos técnicos e esquecem que são uma ferramenta, com o objetivo de que a empresa ganhe dinheiro.

![Fonte: Autoria própria, 2023.](https://paperx-dex-assets.s3.sa-east-1.amazonaws.com/images/1678143439501-NzpeuE7WL8.png "Fonte: Autoria própria, 2023.")

Fonte: Autoria própria, 2023.

O segundo item que deve ser observado é o dado. Como vamos proteger os dados que vão trafegar na nuvem, que é um ambiente público e inseguro, devemos criptografar todos os dados, definir como se fará esta ação, quais os protocolos de criptografia serão utilizados, se são compatíveis com os dispositivos que a empresa opera, qual o custo computacional desta ação e que tipos de chaves utilizar. Por exemplo, não adianta utilizar uma chave criptográfica extremamente alta com um algoritmo super forte que torna a operação extremamente lenta, devemos dosar a segurança com a usabilidade.

![Fonte: Autoria própria, 2023.](https://paperx-dex-assets.s3.sa-east-1.amazonaws.com/images/1678143461251-3VMQT4Hv4o.png "Fonte: Autoria própria, 2023.")

Fonte: Autoria própria, 2023.

O terceiro ponto a ser observado é a aplicação. Ela também deve ser protegida, pois estará rodando na nuvem e qualquer um terá acesso a mesma. O mais comum seria uma proteção de login e senha, mas isso é muito pouco hoje, a autenticação por dois mecanismos diferentes deve ser sempre cogitado, além de sistemas de monitoramento contra ataques de força bruta.

![Fonte: Autoria própria, 2023.](https://paperx-dex-assets.s3.sa-east-1.amazonaws.com/images/1678143482558-GcTrk0EZPN.png "Fonte: Autoria própria, 2023.")

Fonte: Autoria própria, 2023.

O quarto fator que se deve abordar é a tecnologia, pois nossa arquitetura/modelo deve ser adequada a mesma. Se temos um servidor virtual, é um cenário. Se temos um container, é outro completamente diferente. Por isso, deve ser levado em consideração.

**Estruturas de Segurança na Nuvem.**

Todo profissional que trabalha com TI em qualquer parte do mundo deve considerar no mínimo três estruturas de segurança na nuvem:

- **Organização Internacional para Padronização (ISO):** Esta instituição é a mais famosa mundialmente, tem a finalidade de criar padrões internacionais. Ela tem duas ISOs 27017 e 27018, que tratam da segurança na nuvem.
- **Instituto Nacional de Padrões e Tecnologia (NIST):** Este é um outro órgão de normas internacionais que tem sede nos EUA e fornece listas de verificação de estrutura para se estabelecer um sistema novo. Além disso, tem vários artigos sobre problemas específicos associados à segurança em nuvem.
- **Cloud Security Alliance (CSA):** É uma Organização que possui um conjunto de normas que fornecem questionários e formulários de avaliação muito detalhados, servindo para ajudar na auditoria de fornecedores terceirizados e de seus próprios sistemas a nível técnico.

![Fonte: Autoria própria, 2023.](https://paperx-dex-assets.s3.sa-east-1.amazonaws.com/images/1678143521393-i1RSiwFyTB.png "Fonte: Autoria própria, 2023.")

Fonte: Autoria própria, 2023.

Zero Trust significa confiança zero, ou sem perímetro, seu conceito é “nunca confie, verifique sempre”.

**Usuários:** Verifique a identidade e monitore continuamente todos os usuários, pois nenhum acesso pode ser executado a nenhum sistema ou dispositivo sem que o usuário seja autenticado e verificado.

**Dispositivos:** Não devemos confiar nem mesmo nos dispositivos. Uma simples impressora deve ser também verificada e monitorada, é comum pensarmos em dispositivos como sendo seguros e confiáveis. O IP da impressora pode estar habilitado e liberado no firewall e se um invasor clonar este IP, terá acesso ao sistema, mesmo dispositivos aparentemente inofensivos podem ser uma fonte de falha.

**Redes:** Normalmente, confiamos na rede interna da empresa e pensamos que toda informação que trafega nela é segura, mas pelo princípio Zero Trust não devemos confiar nisso, mesmo na rede que é considerada segura como a interna ou a de uma VPN, devemos verificar a autenticidade dos dados e das entidades envolvidas.

**Aplicações:** Quando se trata de acesso aos aplicativos, as organizações devem presumir que todos os que acessam seu site são mal-intencionados. As violações relacionadas ao acesso continuam a aumentar e não mostram sinais de diminuição.

**Dados:** Classifique informações confidenciais em seus dados para orientar políticas e controles sobre o que precisa ser protegido. Os dados devem ser criptografados e assinados digitalmente para garantir a confiabilidade, autenticidade e integridade.

**Desafios da segurança em Nuvem:**

- Contenção de riscos escondidos e dispositivos invasores;
- Resposta lenta aos ataques;
- Proteção para nuvem híbrida;
- Coordenação da segurança em múltiplas nuvens;
- Ampliação de segurança para uma nuvem futura: contêineres, DevOps e ferramentas.

**Conteúdo bônus**

**Tópicos avançados**

Temos vários serviços em nuvem que podem ser implementados e usados gratuitamente por um período. A Amazon, Google e Microsoft, por exemplo, permitem que se faça uma conta gratuita e utilize por um período de testes para aprender e verificar as funcionalidades. Seguem os links:

[www.aws.amazon.com](http://www.aws.amazon.com/) 

[www.azure.microsoft.com](http://www.azure.microsoft.com/) 

[cloud.google.com](http://www.cloud.google.com/) 

Referência Bibliográfica

ABNT NBR ISO/IEC 27001:2006 - **Sistemas de gestão de segurança da informação.**

ABNT NBR ISO/IEC 27002:2005 - **Código de prática para a gestão da segurança da informação.**

ABNT NBR ISO/IEC 27003:2011 – **Diretrizes para implantação de um sistema de gestão da segurança da informação.**

ABNT NBR ISO/IEC 27007:2012 - **Diretrizes para auditoria de sistemas de gestão da segurança da informação.**

BEAL, Adriana. **Segurança da informação: princípios e melhores práticas para proteção dos ativos de informação nas organizações.** São Paulo: Atlas, 2005.

BENANTAR, Messaoud. **Introduction to the public key infrastructure for the Internet.** Upper Saddle River, N.J.: Prentice-Hall : PTR, 2002.

COULOURIS, G. F. **Distributed systems: concepts and design.** 5nd. ed. London: Addison-Wesley, 2011.

DIAS, Cláudia. **Segurança e auditoria da tecnologia da informação.** Rio de janeiro: Axcel Books do Brasil, 2000.

FERREIRA, Fernando Nicolau Freitas. **Segurança da informação.** Rio de Janeiro: Ciência Moderna, 2008.

FONTES, Edison. **Vivendo a segurança da informação – Orientações práticas para pessoas e organizações.** São Paulo: Sicurezza, 2000.

KIZZA, Joseph Migga. **Computer network security and cyber ethics.** 2nd ed. Jefferson: McFarland & Company, 2006.

KUROSE, James F.; ROSS, Keith W. "Computer Networking", **Pearson Education**, 2012.

MENEZES, Josué das Chagas. **Gestão da segurança da informação.** Leme: J. H. Mizuno, 2006.

STALLINGS, William. **Criptografia e segurança de redes: princípios e práticas.** São Paulo: Pearson Education do Brasil, 2010.

STALLINGS, William. **Criptografia e segurança de redes: princípios e práticas.** São Paulo: Pearson Education do Brasil, 2010.

SCHNEIER, Bruce. **Segurança.com: segredos e mentiras sobre a proteção na vida digital.** Rio de Janeiro: Campus, 2001.

TANENBAUM, Andrew S.; FEAMSTER, Nick; WETHERALL, David J.; **Computer Network**. Rio de Janeiro: Pearson, 2020.