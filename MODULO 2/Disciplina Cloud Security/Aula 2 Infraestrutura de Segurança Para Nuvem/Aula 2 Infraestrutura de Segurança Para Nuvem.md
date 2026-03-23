[[Cloud Security]]

**Introdução**

Estudante, embora a nuvem seja cada vez mais segura, ela abriga a cada dia mais dados, mais ativos digitais e recursos computacionais, e tudo isso é extremamente valioso, o que faz com que ela seja alvo de constantes ataques de hackers.

Nesta aula vamos compreender melhor o que é a segurança para a nuvem e quais são os principais recursos que são elencados para que seja possível tornar cada vez mais segura a vida digital das pessoas e os ativos digitais das empresas. Dentre os principais recursos de segurança da nuvem existe um tema que desejo que você, estudante, complemente seus conhecimentos (isso vai te destacar como profissional), que é a Alta Disponibilidade.

**Objetivos da aula**

- Definir os principais aspectos dos datacenters;
- Compreender o conceito de Alta Disponibilidade e de recuperação de desastres na computação em nuvem;
- Compreender a importância dos processos de gerenciamento da infraestrutura de computação em nuvem;
- Conhecer as novas tendências em infraestrutura na nuvem.

**Resumo**

**Principais aspectos dos datacenters**

Um data center, também conhecido como centro de processamento de dados (DPC), é um ambiente especialmente projetado para hospedar componentes eletrônicos computacionais de alto desempenho, como servidores, roteadores e redes de armazenamento, e desta forma, sua principal função é fornecer processamento e armazenamento de dados altamente controlados.

De acordo com Mariano et al. (2020, p.92), temos que um data center, também conhecido como centro de processamento de dados (DPC), é um ambiente especialmente projetado para hospedar componentes eletrônicos de alto desempenho, como servidores, roteadores e redes de armazenamento. Sua principal função é fornecer processamento e armazenamento de dados altamente controlados.

Agora para Veras (2009, _apud_ MILLER, 2012, documento online), estima-se que a maioria das grandes e médias empresas norte-americanas possuam seus próprios data centers. Por exemplo, a Alphabet Inc., empresa que controla o Google, investiu quase US$ 1 bilhão em 2011 para expandir sua rede global de data centers.

Devemos compreender que, em geral, a infraestrutura do data center inclui conectividade com o backbone da Internet, sistemas de controle HVAC, backup físico para acesso a componentes armazenados, redundância para supressão de incêndio, recuperação de dados e sistemas de energia redundantes. Para garantir alta disponibilidade operacional, a construção do data center requer um projeto de infraestrutura sofisticado que pode ser custoso.

Devido a sua criticidade, todo cuidado com o local de instalação deve ser tomado, e desta forma, os data centers devem ser construídos em locais de baixo risco de desastres com estradas de fácil acesso, próximos a concessionárias de energia e provedores de conectividade de backbone de Internet. Ao escolher uma localização geográfica para o seu data center, considere a proximidade das pistas do aeroporto (devido ao risco de queda de aeronaves), a proximidade de rios e oceanos (risco de incêndios, terremotos e tornados, além de deslizamentos de terra).

No que diz respeito ao armazenamento do centro de dados, os data centers exigem componentes de armazenamento mais robustos que garantam a segurança e a integridade dos dados. Podemos exemplificar como sendo um de seus importantes recursos de segurança a serem implementados nos datacenters, os métodos de backup armazenados remotamente para que uma cópia dos dados possa ser armazenada com segurança em um local remoto no caso de um desastre de grande escala.

A infraestrutura do data center é baseada em várias tecnologias de armazenamento, como SAN e NAS. Uma SAN (rede de área de armazenamento) é uma rede privada que conecta vários dispositivos de armazenamento a servidores, fornecendo flexibilidade, disponibilidade e escalabilidade. Uma rede de área de armazenamento pode usar discos rígidos (HD), unidades de armazenamento sólido (SSD), armazenamento em fita, servidores de banco de dados e muito mais.

Conforme apresenta Mariano et al. (2020), o NAS (_Network Attached Storage_) é um dispositivo de rede para armazenamento de dados com sistema próprio que permite a interoperabilidade de acesso. Isso significa que ele pode ser acessado de qualquer sistema operacional. Esses dispositivos devem usar tecnologia que permita privacidade. Os servidores normalmente usam a tecnologia RAID (_Redundant Array of Independent Disks_). Utiliza recursos de componentes de hardware controlados por software para facilitar a redundância das informações registradas.

**Serviços de alta disponibilidade e de recuperação de desastres**

Nas últimas duas décadas, a quantidade e o valor da informação aumentaram exponencialmente, especialmente com o vertiginoso crescimento do comércio eletrônico. Somado a este fato, usuários e instituições têm investido somas significativas de dinheiro para garantir que essas informações sejam acessadas de forma rápida e dinâmica. Acessar essas informações quando você precisa não é tão fácil quanto você imagina. Principalmente em instituições onde o valor da informação é alto, como instituições financeiras e órgãos governamentais. Nessas instituições, a perda de informações pode ter consequências imprevisíveis, afetando as finanças, a política e até a reputação.

Vamos aproveitar o momento e realizar uma breve conceitualização sobre a importante Alta Disponibilidade, onde DEVMEDIA (2012), apresenta que um serviço ou aplicativo altamente disponível é aquele que está disponível 99,999% do tempo (cinco noves de disponibilidade). Ao longo de um ano, para uma previsão de 7 dias por semana, 24 horas por dia, 99,999% significa que o sistema está desligado por cerca de 5 minutos e 35 segundos. Esse nível de alta disponibilidade é difícil de ser alcançado, mas outros valores (4 noves ou 3 noves) são aceitáveis. A Tabela 1 resume esses níveis.

Quadro 1: Os níveis de disponibilidade.

![Fonte: DEVMEDIA (2012, ONLINE).](https://paperx-dex-assets.s3.sa-east-1.amazonaws.com/images/1678372554155-LFlT51QQbH.png "Fonte: DEVMEDIA (2012, ONLINE).")

Fonte: DEVMEDIA (2012, ONLINE).

Para garantir alta disponibilidade, o sistema não deve ter nenhum ponto único de falha (Single Point Of Failure), desta forma, Software, dados e equipamentos redundantes suficientes são agrupados, provisionados, para permitir a migração transparente (_failover_) do sistema, se necessário. Mas também é preciso de ferramentas, processos e habilidades para tornar a transição transparente. A propósito, quanto mais padronizado for o processo, mais fácil será automatizá-lo.

Para DEVMEDIA (2012), os requisitos para implementar alta disponibilidade incluem a replicação de data centers geograficamente dispersos (DPCs), espelhamento ou replicação de dados entre diferentes DPCs, sistemas de armazenamento à prova de acidentes e dados em CPDs. inclui um alto nível de segurança lógica e física.

Desta forma, fica a dica para se tomar grande atenção, pois esses requisitos implicam em outras características importantes do sistema que não devem ser negligenciadas, como a Escalabilidade, a flexibilidade, a adaptabilidade e resiliência.

A replicação e a redundância necessárias para alta disponibilidade reduzem a escalabilidade e a flexibilidade do sistema. Em outras palavras, solicitações de mais capacidade de armazenamento ou processamento, ou mudanças nos requisitos de software significa dobrar ou triplicar os investimentos em equipamentos e sistemas. Portanto, projetos cuidadosos e bem pensados ​​são necessários para evitar mudanças excessivamente dramáticas ou frequentes.

Sobre a recuperação de desastres, o conceito envolve garantir a consistência das infraestruturas de armazenamento de dados distribuídas em diferentes locais. Se vários componentes falharem em um site, um DPC em outro site pode assumir a transação de forma transparente.

Devemos compreender que, ao contrário do que determina a alta disponibilidade, uma pequena perda de dados transacionais é aceitável em uma situação de recuperação de desastres.. Essa perda de dados transacionais pode ser facilmente recuperada dos logs gerados pelo sistema de banco de dados. Essa propriedade permite considerar a replicação assíncrona de dados em um ambiente de recuperação de desastre adequado.

**Gerenciamento de infraestruturas**

Estudante, fica evidente que os provedores oferecem seus produtos e serviços na nuvem através da construção e integração e implementação de data centers para a nuvem. Desta forma são capazes de fornecer serviços relacionados, implementar os requisitos de enquadramento nas camadas superiores do padrão TIA-942 e considerar sua escalabilidade para atender aos requisitos atuais e futuros dos clientes.

Segundo Morris (2016 apud MARIANO ET AL. 2020, p.258), as rotinas de gerenciamento e manutenção da infraestrutura em nuvem podem (e devem) aproximar processualmente as técnicas utilizadas para construir software, e o autor chama isso de código da infraestrutura. Infraestrutura como código é uma abordagem para automatizar a infraestrutura baseada em práticas de desenvolvimento de software. Ele se baseia em rotinas consistentes e repetíveis para modificar e automatizar sistemas e suas configurações. Essa infraestrutura é, portanto, regida por definições escritas em arquivos de configuração que são implementados automaticamente no sistema.

A adoção desta abordagem justifica-se pela necessidade de dotar os responsáveis ​​pela gestão das infraestruturas de condições para acelerarem a mudança e a melhoria. Isso permite que as organizações (privadas ou públicas) atendam às suas necessidades em constante mudança. A premissa aqui é que ferramentas modernas podem lidar com infraestrutura como software e dados. Ele permite que os usuários apliquem ferramentas de desenvolvimento de software, como sistemas de controle de versão (VCS), bibliotecas de teste automatizadas e orquestração de implantação para gerenciar sua infraestrutura.

Além disso, possibilita o desenvolvimento orientado a testes (ou desenvolvimento guiado por testes, em português), integração contínua (CI), entrega contínua (CD), tal como defende Morris (2016, _apud_ MARIANO ET AL. 2020, p. 258), a infraestrutura como código é aplicada e os resultados são comprovados nos ambientes mais exigentes. Segundo Morris (2016 apud Mariano et al. 2020, p.258), as organizações que adotam essa abordagem desejam que sua infraestrutura de TI esteja pronta para mudanças e não se torne um obstáculo para o crescimento de seus equipamentos técnicos.

Além disso, você não deseja que o tempo e o pool de talentos de sua equipe de TI sejam dedicados a tarefas mundanas e repetitivas. A aplicação dessa abordagem também cria a expectativa de que a equipe será capaz de restaurar as estruturas rapidamente no caso de uma interrupção ou desastre. Uma maneira de minimizar a ocorrência desses fenômenos relacionados à infraestrutura é usar ferramentas para automatizar etapas como a criação de novos servidores ou a realização de determinadas alterações de configuração.

**Tendências em infraestrutura**

Em geral, as tendências na infraestrutura de nuvem andam de mãos dadas com os avanços nas tecnologias que compõem essa infraestrutura e a prevalência da nuvem como um meio seguro de armazenamento e processamento de dados. Os pontos a seguir ilustram essas tendências. Assim, a maior capacidade de armazenamento surge como uma das maiores preocupações das empresas desenvolvedoras de soluções de tecnologia na década de 2020 e anos seguintes, pois por exemplo, 1 TB de capacidade de armazenamento era impensável para discos rígidos no passado, mas hoje essa capacidade é comum até mesmo em discos rígidos pessoais.

Outro ponto de constante evolução da Infraestrutura computacional, está na difusão da computação em nuvem, pois à medida que o uso da computação em nuvem se torna mais prevalente, mais provedores poderão investir em novas tecnologias e serviços. Quanto mais dinheiro os clientes pagam pelos serviços, maior a probabilidade de esses serviços serem mais baratos, segundo defende Mariano et al. (2020).

Claro que cada aspecto da infraestrutura deve evoluir, para que não sejam criados gargalos produtivos, e desta forma, outra tendência tecnológica implica em uma melhor velocidade e qualidade de conexão. De acordo com Mariano et al. (2020), a conectividade aprimorada de dispositivos eletrônicos com a Internet alimentou ainda mais a adoção da computação em nuvem. Há alguns anos, conexões não confiáveis ​​poderiam atrasar a decisão de usar os serviços do provedor de nuvem, mas hoje o assunto não é primordial.

Como resultado do crescimento projetado no uso da computação em nuvem e do desenvolvimento antecipado de tecnologias relacionadas, surge um cenário altamente plausível: Adoção generalizada de computação sem servidor, a tecnologia _serverless_. Trata-se de um modelo computacional no qual os servidores são fornecidos e gerenciados por provedores de serviços em nuvem. Nesse caso, o cliente pode confiar não apenas os dados, mas também o aplicativo e a configuração geral ao provedor, reduzindo o custo de aquisição, configuração e manutenção de hardware e eliminando a necessidade de investir em licenças de software.

Que tal parar aqui e desmistificar o termo _serverless?_ Neste importante serviço da computação em nuvem, o servidor realmente existe, mas está localizado junto a um provedor de serviços que gerencia e entrega sua capacidade de acordo com a carga de trabalho, sendo abstraído para o usuário. A principal função das plataformas _serverless_ é simular um sistema de processamento de eventos, conforme mostra a figura a seguir:

Figura 2. Arquitetura de um serviço de serverless computing.

![Fonte: Adaptado de Baldini et al. (2017 apud Mariano et al. 2020, p.264).](https://paperx-dex-assets.s3.sa-east-1.amazonaws.com/images/1678372595535-ntUUWFpkdQ.png "Fonte: Adaptado de Baldini et al. (2017 apud Mariano et al. 2020, p.264).")

Fonte: Adaptado de Baldini et al. (2017 apud Mariano et al. 2020, p.264).

Para Mariano et al. (2020), esse serviço recebe eventos de usuários por HTTP, enfileira os eventos, determina a instância para a qual enviar os eventos e aguarda uma resposta. Em seguida, ele fornece uma resposta ao usuário e interrompe o processo quando não há mais eventos. Existem variações nessa plataforma e implementações com base em dimensões como custo, escalabilidade e tolerância a falhas. Portanto, os clientes devem estar atentos a essas características ao adquirir serviços.

Esse serviço recebe eventos de usuários por HTTP, enfileira os eventos, determina para quais instâncias enviar os eventos e aguarda respostas. Em seguida, ele fornece uma resposta ao usuário e interrompe o processo quando não há mais eventos. Existem variações nessa plataforma e implementações com base em dimensões como custo, escalabilidade e tolerância a falhas. Portanto, os clientes devem estar atentos a essas características ao adquirir serviços.

**Como aplicar na prática o que aprendeu**

**Seja destaque na segurança para a nuvem, conheça as skills mais requisitadas!**

Para o programador conquistar bons contratos é preciso compreender que nunca se deve deixar de lado a capacitação, o constante aprendizado. Pois novos sistemas, frameworks e SDKs surgem o tempo todo e com a Inteligência Artificial cada vez mais popular, novas habilidades passam a ser demandadas pelas empresas.

Conheça o que as empresas buscam em seus profissionais, em termos de skills, consultando mais detalhes pesquisando sobre o tema “As 10 habilidades principais para uma estratégia de nuvem bem-sucedida”.

**Conteúdo bônus**

**Tópicos avançados**

**Diferenciando a segurança de TI da segurança na nuvem**

Muita coisa mudou na computação, na informática com a computação em nuvem, e a segurança também. O que antes era acessado apenas de forma local, restrita e mais segura, agora está em domínio público e vulnerável a ataques de diversas fontes.

Se você já conhece bem a segurança na computação, compare seus conhecimentos neste artigo sobre as especificidades de segurança na nuvem oferecido pela Red Hat sob o título “O que há de diferente na segurança em nuvem?”, e temas relacionados.

Observação: Este conteúdo não será cobrado nas avaliações e estará, obrigatoriamente, presente nas videoaulas. Fique tranquilo(a)!

Referência Bibliográfica

DEVMEDIA. **Alta Disponibilidade e Recuperação de Desastres**: Revista Infra Magazine 4. Disponível em: <[https://www.devmedia.com.br/alta-disponibilidade-e-recuperacao-de-desastres-revista-infra-magazine-4/23443](https://www.devmedia.com.br/alta-disponibilidade-e-recuperacao-de-desastres-revista-infra-magazine-4/23443)>. Acesso em: 27 de dezembro de 2022.

MARIANO. Diego César Batista... [et al.]. **Infraestrutura de TI**. – Porto Alegre: SAGAH, 2020.