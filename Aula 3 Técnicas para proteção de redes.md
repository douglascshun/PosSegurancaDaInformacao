[[Network Defense]]

**Introdução**

O objetivo deste módulo é apresentar as técnicas mais comuns utilizadas em cada uma das camadas de rede.

**Objetivos da aula**

- Classificar os vários tipos de ataques às redes
- Técnicas de camada de Acesso
- Técnicas de camada de Rede e Internet
- Técnicas de camada de Transporte e Aplicação

**Resumo**

Podemos classificar os vários tipos de ataques e/ou ameaças de rede em:  
 

- Ativos - são aqueles que atuam sobre a informação que está sendo transmitida pela rede, interrompendo, modificando ou fabricando dados.
- Passivos - são aqueles que interceptam os dados que estão trafegando na rede, mas não atuam de nenhuma forma sobre eles, apenas fazendo a cópia dos mesmos.

**Tipos de Ataque ou Ameaças:**

**Interrupção**

![](https://paperx-dex-assets.s3.sa-east-1.amazonaws.com/images/1678135027367-tJgtO9lJBC.png)

A informação sai da origem e não consegue chegar ao destino, pois de alguma forma foi bloqueada.

**Interceptação**

![](https://paperx-dex-assets.s3.sa-east-1.amazonaws.com/images/1678135125469-UrkjZkZeyU.png)

A informação sai da origem, mas um atacante consegue interceptar e copiar antes de chegar ao destino.

**Modificação**

![](https://paperx-dex-assets.s3.sa-east-1.amazonaws.com/images/1678135163509-xn3xT8pOoa.png)

A informação sai da origem e é interceptada pelo atacante que modifica a mesma antes de encaminhá-la ao destino.

**Fabricação**

![](https://paperx-dex-assets.s3.sa-east-1.amazonaws.com/images/1678135204862-cVXoi5eO32.png)

A informação é fabricada pelo atacante, que falsifica o endereço de origem da informação para enganar o destino.  
 

Resumo:

![](https://paperx-dex-assets.s3.sa-east-1.amazonaws.com/images/1678135278590-SxEJGay9gJ.png)

Os mais importantes riscos para a segurança da informação são:

  
**Perda de confidencialidade:** quando a informação é revelada para as pessoas não autorizadas**;**

**Perda de integridade:** quando a informação perde a sua exatidão, se torna incompleta**;**

**Perda de disponibilidade:** quando a informação deixa de estar acessível e/ou utilizável pelo destinatário.

**Técnicas de camada de Acesso**

A proteção da rede não é apenas uma função lógica, ela começa no acesso físico. Uma das formas de um atacante roubar as suas informações é roubar fisicamente o servidor. Imagine: você criou um sistema de proteção dos dados de última geração, com dezenas de firewalls, sistemas de controle e o atacante simplesmente rouba o servidor, retira o HD e tem acesso a todos os seus arquivos. Por que você não se preocupou em defender ou proteger o acesso físico ao equipamento? A proteção de rede deve ser pensada em camadas, e a primeira delas é a camada de acesso, onde devemos iniciar nossos estudos e projetos, o acesso físico aos equipamentos deve ser protegido e isso passa por duas etapas:

1) **Segurança Física das Instalações:** A proteção da informação empresarial sensível tem sido um enorme desafio para as empresas, porque as diversas ameaças que existem têm potencial para trazer grandes prejuízos.

Por isso, é importante que haja uma integração entre TI (área responsável pela segurança lógica) e a área de Segurança Patrimonial (área responsável pela segurança física de instalações).

Diferente do que a maioria acredita, a segurança da informação não é uma atividade exclusiva do setor da Tecnologia da Informação. A segurança das informações é responsabilidade de todos na organização e, principalmente, das áreas de Tecnologia da Informação e de Segurança Patrimonial de acordo com suas expertises.

Logo, a segurança física da instalação é a primeira linha de defesa da rede, que é composta, basicamente, através de uma barreira perimetral (cerca, muro, etc.), um ou mais pontos de acessos (portarias), dotados de dispositivos mecânicos de controle (ex.: cancelas e portões) ou eletrônicos (ex.: fechaduras eletrônicas e catracas) e por políticas e procedimentos de segurança física, além de sistemas de alarme e câmeras de segurança. Essas são algumas das medidas de segurança adotadas explorando os meios físicos, tecnológicos e organizacionais, e utilizando-os como barreiras físicas de proteção para um perímetro de segurança que foi previamente delimitado, a fim de administrar e controlar o acesso ao referido perímetro. Se apresentam como alguns obstáculos à progressão física de indivíduos, e tratam-se de métodos para evitar o acesso de pessoas não autorizadas às áreas em que se encontram dados de informações que são críticas para a empresa. É a forma de proteger informações e equipamentos contra usuários que não estão autorizados a acessá-los.

A primeira linha de defesa é proteger fisicamente a instalação ou prédio onde a informação se encontra. Limitando e controlando as pessoas que podem entrar e sair do referido edifício.

**2) Segurança Física dos Equipamentos:** Uma vez que a Instalação está segura, devemos nos preocupar em proteger os equipamentos, não adianta nada o switch completamente exposto, para que qualquer um possa ligar um cabo numa porta livre. Todos os equipamentos ativos e passivos devem ser também protegidos do ponto de vista de acesso físico, todos os racks devem ser trancados com chave e cadeado, todos os armários de Telecom devem possuir chave, e o acesso deve ser rigidamente controlado. É muito comum encontrar racks que estão trancados, mas a tampa lateral se abre sem chave, dando acesso físico aos equipamentos. Isso é inadmissível, é desleixo completo com a segurança. Quando falamos em proteção de rede, o conceito vai do acesso físico a todos os equipamentos da rede até a mais moderna solução de software. Se um atacante tiver acesso a um switch da empresa, pronto, temos uma brecha de segurança para um ataque. A segurança do acesso físico aos equipamentos e cabeamentos é a primeira linha de defesa, os cabos de rede devem todos passar por estruturas fechadas, nenhum cabo pode estar exposto ou acessível, muito menos visível.

**Técnicas camada de rede**

Quando falamos de técnicas de proteção de camada de rede, estamos falando da camada 2 do modelo OSI em que o principal equipamento é o switch, que é a coluna onde se ergue e se baseia a rede local da empresa. Logo, falamos de técnicas que envolvem este dispositivo, esta camada e protocolos de rede. O mais importante protocolo de camada 2 é o Ethernet, logo, ele também é nosso alvo quando pensamos nesta camada.

Cada dispositivo de rede vem com um endereço MAC de fábrica, que é o endereço de camada 2. Ter o cadastro de cada dispositivo, em que porta está conectado, qual o seu MAC, é uma excelente medida de controle, porque podemos implementar filtros de MAC, que funcionam como firewalls de camada 2, onde só vamos aceitar quadros com aquele MAC de origem se vier da porta X do switch. Se vier de outra porta não aceitamos. Este tipo de filtro é muito poderoso, mas, infelizmente, muitos não o implementam.

**Técnicas camada de internet**  
 

Os principais protocolos que representam esta camada são o IPv4 e o IPv6. Todas as técnicas desta camada são baseadas na compreensão de como estes protocolos funcionam, e nos filtros que são implementados agora não mais com MAC de origem ou destino como no anterior, mas basicamente com IPv4 ou IPv6 de origem ou destino.

Como ambos os protocolos atuam simultaneamente, e são completamente independentes, todas as técnicas devem ser implementadas em pilha dupla, ou seja, devemos implementar para o IPv4 e para o IPv6.

O dispositivo físico que representa e atua nesta camada de rede é o roteador e nele podemos implementar e monitorar estes protocolos.

**Técnicas camada de transporte**  
 

Nesta camada temos, principalmente, os protocolos TCP e UDP. Da mesma forma, as técnicas implementadas são baseadas na compreensão destes protocolos, mas basicamente utilizam filtros baseados em porta de origem e destino, correlacionando com os anteriores que utilizavam MAC ou IP de origem e destino. Agora, se verifica a porta, ou algum outro parâmetro específico do protocolo.

  
**Técnicas camada de aplicação**  
 

Para esta camada temos diversas aplicações diferentes, e a compreensão delas é essencial para a implementação de uma defesa, por exemplo, a aplicação mais comum utiliza o protocolo HTTP e as técnicas são diferentes das utilizadas para o e-mail, por exemplo, que é outra aplicação muito comum. No e-mail, temos um problema que é o spam, problema que não afeta a aplicação HTTP. Outra aplicação é o DNS que também tem suas próprias peculiaridades. Em resumo, cada aplicação tem suas próprias técnicas, que são muito particulares e se aplicam especificamente a elas.

**Conteúdo bônus**

**Tópicos avançados**

O CERT.br publicou em julho de 2000 sua primeira cartilha de segurança para a Internet. Ela foi revisada várias vezes, pois a internet evoluiu, novos ataques surgiram, e novas aplicações também. Se quiser saber mais sobre o assunto, acesse o site cert.br para maiores informações.

Referência Bibliográfica

ABNT NBR ISO/IEC 27001:2006 - **Sistemas de gestão de segurança da informação**.

ABNT NBR ISO/IEC 27002:2005 - **Código de prática para a gestão da segurança da informação.**

ABNT NBR ISO/IEC 27003:2011 – **Diretrizes para implantação de um sistema de gestão da segurança da informação.**

ABNT NBR ISO/IEC 27007:2012 - **Diretrizes para auditoria de sistemas de gestão da segurança da informação.**

ABNT NBR 16167:2013 - **Diretrizes para classificação, rotulação e tratamento da informação.**

BEAL, Adriana. **Segurança da informação: princípios e melhores práticas para proteção dos ativos de informação nas organizações.** São Paulo: Atlas, 2005.

DIAS, Cláudia. **Segurança e auditoria da tecnologia da informação.** Rio de janeiro: Axcel Books do Brasil, 2000.

FERREIRA, Fernando Nicolau Freitas. **Segurança da informação.** Rio de Janeiro: Ciência Moderna, 2008.

FONTES, Edison. **Vivendo a segurança da informação – Orientações práticas para pessoas e organizações.** São Paulo: Sicurezza, 2000.

KIZZA, Joseph Migga. **Computer network security and cyber ethics**. 4th ed. Jefferson: McFarland & Company, 2014.

KIZZA, Joseph Migga. **Computer network security and cyber ethics**. 2nd ed. Jefferson: McFarland & Company, 2006.

KUROSE, James F.; ROSS, Keith W. **"Computer Networking"**. Pearson Education, 2012.

MENEZES, Josué das Chagas. **Gestão da segurança da informação**. Leme: J. H. Mizuno, 2006.

SCHNEIER, Bruce. **Segurança.com: segredos e mentiras sobre a proteção na vida digital.** Rio de Janeiro: Campus, 2001.

STALLINGS, W; **"Cryptography and Network Security"**; Prentice Hall, 4th Edition, 2005.

STALLINGS, William. **Criptografia e segurança de redes: princípios e práticas.** São Paulo: Pearson Education do Brasil, 2010.

STINSON, D.; **Cryptography Theory and Practice - CRC Press**, ISBN: 1-584- 88508-4, 2005;

TANENBAUM, Andrew S.; FEAMSTER, Nick; WETHERALL, David J.; **Computer Network**. Rio de Janeiro: Pearson, 2020.