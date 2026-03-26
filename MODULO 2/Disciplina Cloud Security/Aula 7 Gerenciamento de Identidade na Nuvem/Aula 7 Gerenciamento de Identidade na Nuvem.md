[[Cloud Security]]

**Introdução**

Além de prover recursos a nuvem, oferece a gestão destes recursos em sistemas como o IAM da AWS que permite alocar a cada usuário apenas os sistemas e privilégios que ele necessita, sendo assim, o provisionamento de identidade é o processo de orquestrar a criação de contas de usuário e permissões de email na forma de regras e funções.

Desta forma, sobre o provisionamento, podemos afirmar que também inclui outras tarefas, como o fornecimento de recursos físicos em conexão com a ativação de novos usuários.

**Objetivos da aula**

- Compreender como a segurança é feita através do correto provisionamento de identidade;
- Conhecer os conceitos e processos da Autenticação de usuários;
- Compreender a importância da Federação na gestão de usuários;
- Conhecer os principais benefícios da gestão de perfis do usuário.

**Resumo**

**Provisionamento de identidade**

Ao se inscrever em uma conta da AWS a empresa tem a sua disposição todos os recursos existentes no provedor, o que significa que existe um grande poder e responsabilidade, algo que deve ser gerenciado com extrema cautela.

Portanto, é preciso compreender que será necessário adicionar componentes de fluxo de trabalho além dos padrões e protocolos do setor para gerenciamento de identidade e sistemas de provisionamento. Esse fluxo permite que os administradores especifiquem um conjunto de eventos para adicionar usuários com base em sua função e aprovação pelo pessoal responsável dentro da organização. A automatização desse processo garante a consistência e permite uma auditoria detalhada de cada etapa.

Os recursos são acessados ​​por meio do provisionamento de identidade, que é usado para gerenciar o controle de acesso e seus repositórios. Em sua forma mais simples, o ID corresponde a um ID (ID) de Sequência de Eventos para adicionar usuários com base nas funções e aprovações das partes responsáveis ​​dentro de uma organização. A automatização desse processo garante a consistência e permite uma auditoria detalhada de cada etapa. Para Lima (2018), “Uma identidade está associada a usuários ou serviços, que têm diversos IDs em uma variedade de sistemas. Por exemplo, um usuário pode ter IDs em:”

- Um sistema de arquivos de rede nos diretórios compartilhados;
- Vários aplicativos de mainframe;
- um módulo de gestão de relacionamento com o cliente (CRM);
- Sistemas de estoque, vendas, financeiros, etc.;
- Aplicações ligadas aos parceiros da cadeia de suprimentos. (LIMA 2018, p.134).

Identidades no ambiente de TI não são apenas funcionários, parceiros e clientes. Em relação às leis e regulamentos, existe a lei nº 25.276/16 (Brasil, 2016). E para proteção de dados pessoais e regulamentos de outros países, existe a Lei Gramm-Leach-Bliley (GLB). Os bancos devem controlar e relatar por meio de auditorias as atividades de seus funcionários em relação às suas transações com clientes, bem como as de seus parceiros de negócios e clientes que tenham acesso a dados protegidos.

O custo de conformidade com as leis GLB em um ambiente com muitas contas de usuários internos pode ser proibitivo em um mercado competitivo se o processo for ineficiente. Portanto, gerenciar os usuários e as contas de serviço que têm acesso aos servidores de TI é uma tarefa fundamental da administração de segurança.

**Autenticação**

Autenticação é o processo de validação das credenciais de um usuário ao tentar acessar um recurso protegido. A autenticação de ID de usuário (identificador) baseada em senha é a solução predominantemente implementada. Por outro lado, serve como um mecanismo adequado para a maioria das necessidades de negócios e é vulnerável a muitas ameaças conhecidas.

A autenticação é importante para proteger os recursos da nuvem. Valide a identidade de uma entidade (usuário ou máquina) que deseja acessar os recursos da nuvem. Isso deve ser feito de forma segura, confiável e gerenciável (CSA 2012; NOVAIS FERRAZ 2019). A autenticação é o processo de validação das credenciais de uma entidade que tenta acessar um recurso protegido. A autenticação deve ser feita de forma segura, confiável e transparente.

As contas que exigem um nível mais alto de segurança podem exigir autenticação multifator. O sistema de autenticação deve ser capaz de fornecer autenticação adaptável com base no nível de risco da transação, usando a definição de risco de transação de negócios como guia.

Para Gaehtgens, Allan e Care (2019 _apud_ Novais Ferraz 2019, p.42), a autenticação visa estabelecer confiança nas identidades de entidades e serviços em todas as interações. As tecnologias de autenticação baseadas em análises, incluindo biometria comportamental contínua, são adequadas para verificação de identidade e prevenção de fraudes e permitem abordagens adaptativas.

Segundo Stallings (2015 e Novais Ferraz 2019, p.42). Autenticação é o processo de validação de uma identidade reivindicada por ou em nome de uma entidade do sistema, e desta forma temos que um processo de autenticação consiste em duas etapas:

- Etapa de identificação que consiste em apresentar um identificador ao sistema de segurança, essas identidades autenticadas são base para o controle de acesso;
- Etapa de verificação que consiste em apresentar ou gerar informações de identificação que corroboram o vínculo entre a entidade e o identificador.

Existem quatro meios gerais de autenticação da identidade de um usuário, que podem ser usados isoladamente ou em combinação:

1. Algo que o indivíduo sabe: alguns exemplos são uma senha, um número de identificação pessoal (PIN, do acrônimo em inglês para personal identification number) ou respostas a um conjunto de perguntas pré-estipuladas;
2. Algo que o indivíduo possui: alguns exemplos são chaves criptográficas, cartões de senha eletrônica, smart cards e chaves físicas. Esse tipo de autenticador e conhecido como um token;
3. Algo que o indivíduo é (biometria estática): alguns exemplos são reconhecimento por impressão digital, retina e face;
4. Algo que o indivíduo faz (biometria dinâmica): alguns exemplos são reconhecimento pelo padrão de voz, características de escrita manual e ritmo de digitação. (NOVAIS FERRAZ 2019, p.43).

**Federação**

Um importante recurso de segurança para o processo de gestão das identidades é o uso das Federações. Os serviços de identidade federada permitem que as organizações gerenciem as identidades de seus usuários e acessem recursos de organizações parceiras que fornecem serviços autorizados para usuários específicos. Os processos de gerenciamento de identidade federada ajudam a gerenciar o ciclo de vida das identidades e contas de usuários em sistemas parceiros, enquanto o logon único federado ajuda a autenticar os usuários internamente e a comunicar suas identidades aos ISPs.

De acordo com Novais Ferraz (2019), os serviços de nuvem, como tokens, são confiáveis. Isso permite que as organizações gerenciem o processo de certificação. Identidade federada significa que indivíduos (indivíduos ou organizações) podem usar credenciais (IDs locais, senhas biométricas, etc.) para acessar redes de várias entidades (governos, empresas, etc.).

A federação de identidades dá aos usuários acesso transparente aos serviços oferecidos por membros e parceiros. Essa federação é suportada por padrões de comunicação e mensagens, como SAML (_Security Assertion Markup Language_). A federação de identidades permite transparência e robustez em um único acesso, pois o usuário possui apenas uma credencial criada na autoridade de origem.

O gerenciamento de identidade federada fornece políticas, processos e mecanismos para gerenciar o acesso confiável a identidades e sistemas em uma organização. E de acordo com Novais Ferraz (2019), isso permite a reutilização de identidades de usuários em todos os limites organizacionais, garantindo gerenciamento eficiente do ciclo de vida do usuário, conformidade e correspondência de informações relevantes do usuário entre duas organizações parceiras. Não há necessidade de sobrecarga administrativa excessiva.

O objetivo principal do gerenciamento de identidade federada é permitir que os usuários em um domínio de segurança acessem os sistemas de outro domínio. Isso permite o logon único federado. Os sistemas de gerenciamento de identidade e acesso devem oferecer suporte à colaboração interorganizacional, especialmente para fornecer recursos como SSO. As identidades utilizadas nesse contexto são chamadas de identidades federadas, tal como defende Chadwick (2009; NOVAIS FERRAZ 2019, p.51).

Neste escopo temos o Federated Identity Management (FIM), recurso que visa facilitar o gerenciamento de identidades, processos e políticas entre entidades cooperantes usando controles distribuídos. A estrutura FIM consiste em processos e todas as tecnologias subjacentes para criar, gerenciar e usar identidades digitais comuns em várias organizações.

Para CSA (2012, _apud_  NOVAIS FERRAZ 2019, p. 52), temos que o logon único (SSO) federado permite que você confie na autenticação de usuários em um domínio em diferentes domínios (como diferentes provedores de serviços). Isso oferece aos usuários conveniência e melhor segurança se o domínio de autenticação mantiver uma forte postura de segurança. O logon único federado é necessário como um recurso padrão que aproveita o gerenciamento de identidade federada para facilitar o acesso de domínio entre organizações e segurança cruzada aos recursos.

Figura 1: Processo de autenticação federado.

![Fonte: Novais Ferraz (2019, p.53).](https://paperx-dex-assets.s3.sa-east-1.amazonaws.com/images/1678490826586-eeyTnoGemV.png "Fonte: Novais Ferraz (2019, p.53).")

Fonte: Novais Ferraz (2019, p.53).

Em ambientes de nuvem, geralmente há vários aplicativos e serviços da Web projetados para oferecer suporte aos usuários, exigindo autenticação. Em alguns casos, pode ser prático e seguro usar uma infraestrutura SSO centralizada conectada a uma autoridade central. O Web SSO fornece uma infraestrutura de SSO para aplicativos da web. No entanto, o Web SSO provou ser um mecanismo de controle de acesso muito fraco.

O Web SSO pode ser usado para autenticação de usuários para sistemas de uso geral, mas o SSO federado é altamente recomendado para aplicativos de negócios (CSA 2012; NOVAIS FERRAZ 2019). Novamente o autor nos mostra que o SSO é um sistema de acesso único. Nesse sistema, os usuários autenticam apenas uma vez para acessar vários aplicativos em um único domínio ou em vários domínios que confiam uns nos outros.

A federação fornece acesso confiável a domínios associados e o gerenciamento de identidade federada define políticas e processos para gerenciar identidade e acesso em federações. Nesse contexto, o SSO federado em um ambiente federado fornece acesso a aplicativos em diferentes domínios confiáveis ​​por meio de protocolos específicos (NOVAIS FERRAZ 2019).  

**Gestão de perfis do usuário**

A identidade é um conceito fundamental para gerirmos o processo de concessão de acesso a usuários, aplicações e serviços. A identidade deve existir antes que um usuário possa fazer, por exemplo, qualquer trabalho produtivo em um projeto tecnológico. Ao mesmo tempo que identidades são usadas para controlar o acesso aos dados, estes devem ser protegidos com o intuito de garantir sua integridade e a privacidade de informações confidenciais.

Entretanto, a necessidade de acesso levou à criação de processos de gestão de identidade e concessão que podem ser caros e de difícil gestão. É de fundamental importância gerenciar os riscos, tais como roubos de informações, violações e ataques cibernéticos (LIMA 2018, p.146).

Figura 4 - Um papel - múltiplas identidade

![Fonte: Sullivan. (2016, p. 99 apud Lima 2018, p.147).](https://paperx-dex-assets.s3.sa-east-1.amazonaws.com/images/1678490884504-3vZTa3xEsJ.png "Fonte: Sullivan. (2016, p. 99 apud Lima 2018, p.147).")

Fonte: Sullivan. (2016, p. 99 apud Lima 2018, p.147).

As exigências de conformidade a leis e regulamentos se estendem ao gerenciamento de identidade, ao controle de acesso e à necessidade de geração de logs para evidências de auditoria, ou seja, controles que podem ser complexos em ambientes de computação em nuvem.  Em suma, o gerenciamento de identidade é uma prática comum nas organizações, destinada a:

- Reduzir custos e melhorar a eficiência operacional;
- Cumprir leis e regulamentos aplicáveis;
- Permitir operações de negócio mais ágeis e seguras. (LIMA 2018, p.146).

Eliminar os riscos do processo de gerenciamento de identidade sempre foi uma parte importante da operação segura dos processos de TI e, como vimos, é fundamental para a computação em nuvem, pois os dados são armazenados fora da organização.

**Como aplicar na prática o que aprendeu**

**Gerir identidades é importante, mas é preciso proteger este processo!**

Existem pessoas capazes de escrever a senha de suas contas bancárias em seus cartões, algo que revela ser uma gigantesca vulnerabilidade, facilitando o desvio de recursos financeiros.

Na computação, no desenvolvimento de aplicações, estes dados de segurança podem ser manipulados de forma que dificilmente sejam subtraídos por hackers mal intencionados. Recomendo buscar por artigos que demonstrem formas de se proteger os dados de identidade de usuários.

**Conteúdo bônus**

**Tópicos avançados**

**Privacidade e Gerenciamento de Identidades**

Devido ao crescimento na preocupação com a privacidade dos dados pessoais, o tema da lei LGPD vem aumentando as discussões sobre os vários aspectos da segurança nas empresas, desta forma, podemos compreender que a computação em nuvem oferece vantagens em termos de dinamismo, elasticidade, disponibilidade e custo, mas dificulta o gerenciamento da segurança da informação.

Especialmente de uma perspectiva de gerenciamento de identidade, os ambientes de nuvem apresentam desafios significativos com várias regras de acesso para aplicativos, diferentes dados do usuário e diferentes tecnologias.

Questões de segurança, incluindo proteção de privacidade, são uma preocupação constante e um importante tópico de pesquisa em ambientes de computação em nuvem.

Assegurar a privacidade, minimizar a divulgação de dados necessários, ter em conta as preferências dos utilizadores e assegurar o cumprimento de compromissos ou acordos estabelecidos entre prestadores de serviços e consumidores.

Pesquise mais sobre o tema e artigos que abordam a questão da segurança no gerenciamento das identidades e acesso aos sistemas na nuvem.

Observação: Este conteúdo não será cobrado nas avaliações e estará, obrigatoriamente, presente nas videoaulas. Fique tranquilo(a)!

Referência Bibliográfica

NOVAIS FERRAZ, Claudio Augusto. **Gestão de Riscos em Computação em Nuvem para a Gestão de Identidade e Acessos aplicada ao Sistema Decom Digital do Ministério da Economia.** -- Brasília, 2019. Disponível em: <[https://repositorio.unb.br/bitstream/10482/37502/1/2019_ClaudioAugustoNovaisFerraz.pdf](https://repositorio.unb.br/bitstream/10482/37502/1/2019_ClaudioAugustoNovaisFerraz.pdf)> Acesso em: 30/12/2022.