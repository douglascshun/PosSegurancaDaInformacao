

**Introdução**

Neste módulo, foram discutidos conceitos sobre computação forense e o processo de investigação digital, bem como os procedimentos executados na construção de uma cadeia de custódia de evidências. Uma importante dimensão em matéria de investigação digital está no estudo de sistemas de arquivos. Por fim, os temas sobre análise de rede e logs, abordaram sobre duas atividades primordiais em processos de gestão e segurança da informação.

**Objetivos da aula**

- Apresentar os conceitos e definições de computação forense;
- Reconhecer os procedimentos para preservação de evidências;
- Aprofundar na arquitetura e particularidades dos sistemas de arquivos;
- Articular e executar análise de rede e logs de serviços.

**Resumo**

O módulo em questão versa sobre uma área de atuação profissional muito interessante e desafiadora, que é a área de computação forense. Entender inicialmente o que faz um perito forense e qual sua atuação perante um processo judicial, expande o mercado de trabalho para profissionais de tecnologia da informação.

O objetivo da computação forense é examinar a mídia digital de maneira forense, com o objetivo de: identificar, preservar, recuperar, analisar e apresentar fatos e opiniões sobre a informação digital.

É importante salientar que um laboratório de computação forense é uma zona segura e protegida onde os dados eletrônicos podem ser gerenciados, preservados e acessados ​​em um ambiente controlado. Lá, há um risco muito reduzido de dano ou modificação da prova. Os examinadores forenses de computador têm os recursos necessários para extrair dados significativos dos dispositivos que estão examinando.

O processo de análise forense segue a seguinte dinâmica:

- Criar registro para cada evidência
- Criar assinatura das evidências
    - MD5
    - SHA1
    - SHA256
- Evitar comprometer evidências
- Criar relatório detalhado da investigação
    - Comandos executados
    - Pessoas entrevistadas
    - Evidências coletadas

Ainda no universo da perícia forense, a cadeia de custódia de evidências é um registro detalhado de como as evidências foram tratadas durante a análise forense, desde a coleta até os resultados finais. Este registro deve conter informações sobre quem teve acesso às evidências ou às cópias utilizadas. Durante um processo judicial, este registro vai garantir que as provas não foram comprometidas. Cada evidência coletada deve ter um registro de custódia associado a ela.

Um registro de custódia deve conter pelo menos os seguintes itens:

- Data e hora de coleta da evidência;
- De quem a evidência foi apreendida;
- Informações sobre o hardware, como fabricante, modelo, números de série, etc;
- Nome da pessoa que coletou a evidência;
- Descrição detalhada da evidência;
- Nome e assinatura das pessoas envolvidas;
- Identificação do caso e identificação da evidência (tags);
- Assinaturas MD5/SHA1 das evidências, se possível;
- Informações técnicas pertinentes.

No campo da análise de sistema de arquivos, é primordial compreender que toda investigação deve ser realizada em imagem dos arquivos originais, pois uma cópia de um arquivo já traz modificações em sua estrutura e composição. MACtimes são informações cronológicas e atributos de tempo de um arquivo, onde:

- mtime (Modification time): mostra a última data e hora em que o arquivo foi modificado.
- atime (Access time): mostra a última data e hora em que um diretório ou arquivo foi acessado/lido.
- ctime (Creation time): mostra a data e hora em que arquivo foi criado.

Análise de logs representa uma forma a apresentar informações sobre um sistema de forma clara e compreensível, além de apontar a técnica para determinar a posteriori violações de segurança.

Já a análise de rede lida com dados voláteis que trafegam na execução dos processos e serviços de um modelo de negócio.

Existe um consenso que uma boa prática de gestão de segurança da informação contempla em algum nível de atuação, pois somente o monitoramento constante dessas variáveis pode contribuir de forma significativa no processo de tomada de decisão.

**Como aplicar na prática o que aprendeu**

SHA-1 produz um resumo de mensagem baseado em princípios semelhantes aos usados por Ronald L. Rivest do MIT no projeto dos algoritmos de resumo de mensagem MD2, MD4 e MD5, mas gera um valor de hash maior (160 bits versus 128 bits).

O SHA-1 foi desenvolvido como parte do projeto Capstone do governo dos Estados Unidos. A especificação original do algoritmo foi publicada em 1993 sob o título Secure Hash Standard, FIPS PUB 180, pela agência de padrões do governo dos EUA NIST (Instituto Nacional de Padrões e Tecnologia). Esta versão agora é chamada de SHA-0. Ele foi retirado pela NSA logo após a publicação e foi substituído pela versão revisada, publicada em 1995 no FIPS PUB 180-1 e comumente designada SHA-1. O SHA-1 difere do SHA-0 apenas por uma única rotação bit a bit no agendamento de mensagem de sua função de compactação. De acordo com a NSA, isso foi feito para corrigir uma falha no algoritmo original que reduzia sua segurança criptográfica, mas eles não forneceram nenhuma explicação adicional. As técnicas publicamente disponíveis demonstraram, de fato, um comprometimento do SHA-0, em 2004, antes do SHA-1 em 2017.

O artigo que está referenciado no link abaixo, ensina a identificar e descriptografar hashes de senhas (MD5 e SHA1). Após a leitura do artigo siga as atividades práticas que são propostas no corpo do texto. Disponível em: <[https://www.linkedin.com/pulse/descobrindo-senhas-md5-e-sha1-em-menos-de-15-minutos-rossetti/?originalSubdomain=pt](https://www.linkedin.com/pulse/descobrindo-senhas-md5-e-sha1-em-menos-de-15-minutos-rossetti/?originalSubdomain=pt)>. **(Acesso em 17/02/2023)**

**Conteúdo bônus**

**Tópicos avançados**

O SHA-1 faz parte de várias aplicações e protocolos de segurança amplamente utilizados, incluindo TLS e SSL, PGP, S/MIME e IPsec. Tais aplicações podem também usar MD5; Ambos MD5 e SHA-1 descendem de MD4. O hashing de SHA-1 também é utilizado em sistemas de controle de revisão distribuídos como Git, Mercurial e Monotone para identificar revisões, assim como detectar corrupção ou adulteração de dados. O algoritmo também foi utilizado no console de videogame Nintendo Wii para verificação de assinatura durante a inicialização do sistema, entretanto, uma falha significativa nas primeiras implementações do firmware permitiam que um atacante ignorasse o esquema de segurança do sistema. Pesquise sobre algoritmo SHA-1 e funções de Hashing no artigo indicado no link abaixo e amplifique seus conhecimentos sobre criptografia. Disponível em: <[https://csrc.nist.gov/csrc/media/publications/fips/180/4/final/documents/fips180-4-draft-aug2014.pdf](https://csrc.nist.gov/csrc/media/publications/fips/180/4/final/documents/fips180-4-draft-aug2014.pdf)>. **(Acesso em 23/02/2023)**

Referência Bibliográfica

**Bibliografia Básica**

RICCI, Bruno. **Rede Segura:VPN Linux**, Editora Ciência Moderna, 2007.

TANENBAUM, A. S., **Redes de Computadores**. Rio de Janeiro, Campus, 2003.

COSTA, Daniel Gouveia. **Administração de Redes com Scripts**, 2ª Edição, Editora Brasport, 2010.

**Bibliografia Complementar**

SMITH, Rodercik W**. Linux: Ferramentas Poderosas**, 1ª Edição, 2004, Editora Ciência Moderna.

NAKAMURA, E. T., e GEUS, P. L., **Segurança de Redes em Ambientes Cooperativos**,2 ed. Ed. Berkley, São Paulo, 2007.

MORAES, Alexandre F. **Redes de Computadores**. 7ª Edição, Editora Érica, 2008.

MENDES, Douglas Rocha, **Redes de Computadores**, Ed. Novatec, 1ª Edição, 2007

STARLIN, Gorki, **Conceitos, Protocolos e Uso Tcp/Ip: Redes de Computadores.** 1ª Edição, Alta Books, 2004.