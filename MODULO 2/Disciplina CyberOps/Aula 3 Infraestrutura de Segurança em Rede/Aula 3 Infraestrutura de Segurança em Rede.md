[[CyberOps]]

**Introdução**

No módulo de infraestrutura de segurança em rede, foram estudados em quatro momentos, tópicos de redes de computadores que estão relacionados a vulnerabilidades atreladas desde a gênese do desenvolvimento das redes de computadores na década de 1950 até a atualidade. Na abordagem sobre as ameaças e ataques de rede, buscou-se a compreensão da forma em que se estabelecem as ameaças, considerando os aspectos tecnológicos e o fator humano, tangenciando as estratégias de segurança e, às vezes, configurando o elo fraco na arquitetura concebida. Em um terceiro momento do módulo, o protocolo TCP/IP recebeu um destaque e entraram em evidência as vulnerabilidades da pilha TCP/IP, que, para qualquer profissional de segurança da informação, precisa ser conhecida e contemplada em suas ações. Por fim, atendendo a um dos pilares da infraestrutura de segurança em rede, que é o monitoramento, foram apresentadas uma variedade de ferramentas que com esse propósito.

**Objetivos da aula**

- Apresentação de equipamentos e conceitos de topologia de rede, bem como seus equipamentos e boas práticas de segurança;
- Estabelecer compreensão de ameaças e ataques em rede de computadores;
- Identificar as particularidades no protocolo TCP/IP que geram vulnerabilidades em uma rede de computadores; e
- Revelar ferramentas de monitoramento e controle de rede.

**Resumo**

Inicialmente, o módulo de infraestrutura de segurança em rede abordou os elementos de topologia de rede, apresentando as diversas possibilidades de estruturação e concepção de equipamentos e cabeamento. Ainda no contexto dos equipamentos de rede, foram listados os mais significativos para relembrar aos já ambientados com esses materiais e, não obstante, permitir aos iniciados um direcionamento no assunto.

Na sequência dos temas propostos, houve uma abordagem holística das ameaças e ataques de rede de computadores, destacando os espectros físicos e lógicos. Em uma abordagem física, consideramos uma série de precauções que passam pelo fornecimento ininterrupto de energia elétrica, condicionamento de ar adequado e até mesmo o acesso físico à sala que concentra os equipamentos. Também foram revelados os tipos de ataque mais comuns, com intenção de massificar esse conhecimento, para obtenção de melhores estratégias de proteção e segurança.

No terceiro momento dos conteúdos, demos destaque às vulnerabilidades da pilha de execução do protocolo TCP/IP, pois é preciso considerar esse protocolo como um dos mais relevantes na comunicação entre computadores e dispositivos digitais, bem como o funcionamento da internet, sua conectividade e arquitetura, estão atrelados às peculiaridades encontradas nos aspectos técnicos que suas implementações.

Foram apresentados os conceitos e arquitetura de ataques mais comuns que exploram algumas vulnerabilidades nativas no protocolo IP como: IP address spoofing, ARP Spoofing. No protocolo TCP foram listados: ICMP Attacks, Packet reassembly and sequence prediction, MitM attacks. Dentre os ataques relacionados merece destaque o DoS (Denied of Servise) e o DDoS (Distribuid Denied of Service), pois são ataques que exploram fatores estruturantes na arquitetura desses protocolos e representam uma grande ameaça.

A abordagem sobre ferramentas de monitoramento de rede buscou conscientizar todos que atualmente estão na condição de discentes, que serão futuros profissionais de tecnologia da informação, envolvidos com segurança da informação, que o monitoramento é imprescindível e necessário para uma gestão de rede eficiente. Entendendo que as demandas são específicas, foram apresentadas uma série de ferramentas com funcionalidades para diferentes necessidades.

Relembrando as topologias de uma rede, vale destacar a topologia em estrela, pois é a mais comumente adotada por sua alta disponibilidade de escalabilidade, bem como sua aceitação por diversos equipamentos de fabricantes diferentes. A versatilidade da topologia em estrela é amplamente reconhecida, uma percepção prática revela que isso também explica porque é utilizada até em pequenas redes domésticas.

Com o aumento de incidentes de segurança da informação em diversos níveis de atuação e comprometimento de ativos, para alguns autores e pesquisadores da área, a melhor defesa é o ataque. Assim, torna-se imperativo conhecer as etapas de um ataque para que, estrategicamente, você possa definir suas ações de defesa. Resumidamente as etapas de um ataque são:

- Footprinting: levantamento de informação do alvo.
- Scanning: rastreamento de portas e serviços do alvo.
- Enumeration: extrai informações mais detalhadas do alvo.
- System hacking: planejamento e execução do ataque baseado nas informações do alvo.
- Escalation of privilegie: obtenção de mais privilégios e elevação de acesso administrativo
- Covering tracks: remoção de evidências e rastros do ataque.
- Planting of backdoors: malware que permite ao invasor retornar de forma simplificada.

Uma série de ataques foram descritos textualmente e apresentados graficamente, com o objetivo de revelar o “_modus operandi_” desses ataques, contudo merece destaque o ataque Denial of Service (DoS), que é o temido ataque de negação de serviço, pois explora uma vulnerabilidade do protocolo TCP/IP, sobrecarregando o servidor alvo de requisições até que ele simplesmente congela diante de uma demanda que não consegue atender, tornado o serviço ou sistema indisponível. 

**Como aplicar na prática o que aprendeu**

No livro “Introdução ao Pentest”, o autor Daniel Moreno oferta um procedimento que consolida na prática alguns dos conceitos estudados até aqui. Em sua versão eletrônica, disponível no link: <[https://books.google.com.br/books?hl=en&lr=&id=FD-4DwAAQBAJ&oi=fnd&pg=PA18&dq=Como+Estudar+e+Pentest+&ots=cC1z79L5Xy&sig=fNlEUNy2_QFe8KS1zJiEVRZfhfk&redir_esc=y#](https://books.google.com.br/books?hl=en&lr=&id=FD-4DwAAQBAJ&oi=fnd&pg=PA18&dq=Como+Estudar+e+Pentest+&ots=cC1z79L5Xy&sig=fNlEUNy2_QFe8KS1zJiEVRZfhfk&redir_esc=y#v=onepage&q&f=false)[v=onepage&q&f=false](https://books.google.com.br/books?hl=en&lr=&id=FD-4DwAAQBAJ&oi=fnd&pg=PA18&dq=Como+Estudar+e+Pentest+&ots=cC1z79L5Xy&sig=fNlEUNy2_QFe8KS1zJiEVRZfhfk&redir_esc=y#v=onepage&q&f=false)> **(Acesso em 16/02/2023)**, é permitido acessar algumas partes dos capítulos que compõem o livro. Indico a execução da técnica de Footprinting que está detalhada no capítulo 5.

**Conteúdo bônus**

**Tópicos avançados**

A segurança da informação é uma das modalidades mais exigidas na proteção de dados, sistemas, aplicações e máquinas em um ambiente corporativo. Configurações ruins, ausência de métodos de proteção, programas desenvolvidos sem uma política de segurança, sem tratativa sobre aplicações e dados propiciam brechas que facilitam ataques cibernéticos comprometendo empresas e gerando perdas monetárias. O trabalho de conclusão de curso indicado no link abaixo, visa desenvolver um laboratório virtual para aplicar o pentest, uma metodologia de trabalho que simula ataques de invasão para identificar e mitigar vulnerabilidades eticamente, em diversos cenários simulados em que uma organização pode se deparar. Aproveite o trabalho para ter contato com a legislação atual pertinente aos crimes digitais e sua influência sobre o escopo de trabalho realizado pelo analista e auditor do pentest e execute um laboratório virtual seguindo o modelo apresentado no trabalho. Disponível em: <[https://repositorio.uniceub.br/jspui/handle/235/12374](https://repositorio.uniceub.br/jspui/handle/235/12374)>. **(Acesso em 16/02/2023).**

Referência Bibliográfica

**Bibliografia Básica**

RICCI, Bruno. **Rede Segura:** VPN Linux, Editora Ciência Moderna, 2007.

TANENBAUM, A. S., **Redes de Computadores**. Rio de Janeiro, Campus, 2003.

COSTA, Daniel Gouveia. **Administração de Redes com Scripts**, 2ª Edição, Editora Brasport, 2010.

**Bibliografia Complementar**

SMITH, Rodercik W**. Linux: Ferramentas Poderosas**, 1ª Edição, 2004, Editora Ciência Moderna.

NAKAMURA, E. T., e GEUS, P. L., **Segurança de Redes em Ambientes Cooperativos**,2 ed. Ed. Berkley, São Paulo, 2007.

MORAES, Alexandre F. **Redes de Computadores**. 7ª Edição, Editora Érica, 2008.

MENDES, Douglas Rocha, **Redes de Computadores**, Ed. Novatec, 1ª Edição, 2007

STARLIN, Gorki, **Conceitos, Protocolos e Uso Tcp/Ip:** Redes de Computadores. 1ª Edição, Alta Books, 2004.