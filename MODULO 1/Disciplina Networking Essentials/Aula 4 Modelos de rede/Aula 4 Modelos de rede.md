[[Networking Essentials]]
## Modelos de rede

**Introdução**

As redes de computadores apresentam seus modelos conceituais para a construção que permite criar redes universais, compatíveis, mesmo quando seus componentes são desenvolvidos por empresas e linguagens diferentes.

Desta forma o modelo OSI de Open System Interconnection é uma estrutura hierárquica criada para dar suporte ao projeto de rede. Pretende-se facilitar a comunicação entre sistemas informáticos através de um conjunto de protocolos que permitem a comunicação entre diferentes sistemas.

**Objetivos da aula**

- Conhecer as camadas e aplicações do Modelo OSI;
- Conhecer as camadas e aplicações do Modelo TCP/IP;
- Compreender as funcionalidades de cada camada em ambos os modelos;
- Comparar as camadas dos modelos OSI x TCP/IP.

**Resumo**

**Modelo OSI**

Este modelo permite que dois sistemas se comuniquem sem alterar a lógica subjacente de hardware e software. O modelo OSI deve ser visto não como um protocolo, mas como um arquétipo usado para incorporar e descrever arquiteturas de rede flexíveis que funcionam juntas. O modelo OSI apresenta 7 camadas:

Figura 1: Camadas do modelo OSI.

![Fonte: Comer (2016, p. 14 apud p.84).](https://paperx-dex-assets.s3.sa-east-1.amazonaws.com/images/1677702470150-C4OefXB1rq.png "Fonte: Comer (2016, p. 14 apud p.84).")

Fonte: Comer (2016, p. 14 apud p.84).

Para o desenvolvimento do modelo, os projetistas verificaram o manuseio da transmissão de dados nos elementos mais básicos. Uma camada, portanto, define um grupo específico de funções que servem umas às outras. Desta forma, o modelo OSI forma uma arquitetura mais flexível e abrangente. (BARRETO; ZANIN; SARAIVA, 2018, p.85).

Por ser baseado em camadas, enfatiza que a grande importância desse modelo é definir como as camadas trabalham juntas por meio de interdependências, tornando o modelo mais completo e organizado. As camadas fornecem maior funcionalidade nos serviços de comunicação. Cada um tem critérios operacionais específicos definidos e é regido por protocolos padronizados para cada função.

Através do modelo OSI é possível desenvolver redes de computadores independentes da tecnologia utilizada, pois permitem realizar a comunicação de diferentes máquinas e definir as diretrizes gerais. De acordo com Fourozan e Fergan (2008 apud (Barreto, Zanin e Saraiva 2018, p.85), temos que o modelo OSI apresenta diversas vantagens, sendo a mais importante uma forma de padronização. Vale ressaltar, portanto, que o modelo decompõe a comunicação em rede em pedaços menores, facilitando o processo de aprendizagem e compreensão.

Outra vantagem desse modelo é que ele facilita a programação modular, evita que alterações em uma das camadas afetem outras camadas e permite a comunicação entre diferentes sistemas. Ao entender cada camada, podemos entender como o sinal de bit é transmitido, como é remontado, como chega ao seu destino, etc.

Assim, o modelo OSI representa todas essas características comuns e facilmente reconhecíveis na vida cotidiana. Em resumo, cada camada do modelo OSI tem uma função específica. Eles trabalham de forma dependente e a falha na transferência de informações de um para o outro pode afetar a funcionalidade da próxima camada. (BARRETO; ZANIN; SARAIVA, 2018, S.85).

**Modelo TCP/IP**

O modelo de referência OSI foi usado nos primórdios do surgimento das redes de computadores, onde as conexões eram muito simples, a interconexão de diferentes redes ainda não era prática e não havia outro meio de transmissão de dados além do cobre.

A partir do momento em que as redes de computadores começaram a evoluir e passaram a utilizar outros meios de comunicação, como satélites e rádio, a cobertura territorial da rede ampliou-se e começaram a surgir sub-redes. Este modelo de referência OSI começou a apresentar alguns problemas para realizar a comunicação entre hosts com essas características. (BAY; BLUNING 2016, p.81).

Como o modelo de referência OSI não atende mais eficientemente as redes de computadores, um novo modelo de comunicação foi desenvolvido. Isso é chamado de Modelo de Referência TCP/IP e sua estrutura pode ser melhor compreendida com a figura a seguir:

Figura 2 - Modelo De Referência TCP/IP

![Fonte: Adaptado de (MACEDO ET AL 2018, p.113).](https://paperx-dex-assets.s3.sa-east-1.amazonaws.com/images/1677702525350-zx37njgU7P.png "Fonte: Adaptado de (MACEDO ET AL 2018, p.113).")

Fonte: Adaptado de (MACEDO ET AL 2018, p.113).

Assim, podemos realizar uma comparação visual entre os dois modelos de desenvolvimento de redes de computador:

Figura 3: Comparativo Entre Modelo Osi E Modelo TCP/IP

![FONTE: O autor (MACEDO ET AL 2018, p.113).](https://paperx-dex-assets.s3.sa-east-1.amazonaws.com/images/1677702547011-j3zfLj6Dt3.png "FONTE: O autor (MACEDO ET AL 2018, p.113).")

FONTE: O autor (MACEDO ET AL 2018, p.113).

Uma característica importante do modelo TCP/IP é sua capacidade de permanecer operacional mesmo quando parte da rede está comprometida. A ARPANET consistia em um projeto militar e, na época, o Departamento de Defesa dos Estados Unidos temia um ataque da União Soviética. Switches e roteadores na União Soviética podem ficar inoperantes, impossibilitando a comunicação pela ARPANET.

Portanto, um requisito da arquitetura de interconexão proposta era suportar a perda de hardware de sub-rede. Para tanto, o desenho da arquitetura TCP/IP levou em consideração esse requisito e contribuiu para seu sucesso. (Macedo et al. 2018, p.113).

**Funcionalidades de cada camada**

A ideia por trás das camadas é de criar um roteiro de desenvolvimento para hardware e software de forma a mantermos um fato interessante sobre a Internet, por exemplo, o fato de ser apenas uma única rede, e desta forma, temos semelhanças e diferenças,

Embora o modelo TCP/IP e o modelo OSI se assemelhem, cada um deles possui uma forma de funcionamento. Dessa maneira, destaca-se cada uma das camadas e suas respectivas funções para melhor compreensão de ambos os modelos. (BARRETO; ZANIN; SARAIVA 2018, p.75)

Começando com as camadas do Modelo TCP/IP, temos a camada da Internet, onde a evolução geral das redes de computadores por meio da interconexão de redes exigiu o desenvolvimento de métodos para os hosts se comunicarem com todos os hosts conectados à rede à qual estão conectados. Assim, a camada de Internet atendeu a essa necessidade. Permite que certos hosts injetem pacotes destinados a várias redes/áreas de rede na rede. (BAY; BLUNING 2016, p.82).

A camada de transporte está dentro do modelo TCP/IP tal qual pode ser observada no modelo OSI, e possui como responsabilidade, a comunicação ponta a ponta entre os hosts na rede. Em outras palavras, essa camada sincroniza as conexões e determina como as transferências de dados entre os hosts participantes são realizadas. Para tanto, foram desenvolvidos dois protocolos de comunicação para uso nesta camada: o protocolo TCP (Transmission Control Protocol) e o protocolo UDP (User Datagram Protocol) [...]. (BAY; BLUNING 2016, p.82).

 Com a camada de aplicação, o modelo TCP/IP não possui camadas de sessão e apresentação. Eles foram retirados do novo modelo por serem considerados de pouca utilidade e desnecessários para o novo modelo. Aproximação. Esta nova camada de aplicação, como sua antecessora, continua gerenciando protocolos de comunicação de nível superior, ou seja, protocolos aos quais os usuários se conectam diretamente, como HTTP, DNS, FTP e POP.  Com a camada de acesso à rede, temos a conectividade física dos dispositivos, onde as informações a serem transmitidas no meio de comunicação são trabalhadas e executadas e as funções de enlace e camada física do modelo OSI. (Bay; BLUNING 2016, p.84)

**Camadas do modelo OSI:**

Começando com as camadas do modelo OSI temos a camada física, responsável por transportar um fluxo de bits específico em mídia física. Essa camada aborda tanto as especificações elétricas da interface quanto às especificações mecânicas do seu meio de transmissão. Também é função dessa camada definir as etapas e funções que um dispositivo físico deve executar para permitir a transferência de dados.

Também define as características da interface entre os meios de transmissão e a escolha do meio. Nela, os dados são um fluxo de bits, uma sequência entre 0 e 1, sem interpretação. Para fazer esta transmissão, os bits são codificados no sinal. Os sinais podem ser elétricos e ópticos. (BARRETO; ZANIN; SARAIVA, 2018, p.78).

Na camada de conexão temos a codificação das camadas antes do recurso de transmissão bruto em links autoritativos. Codifique os dados para que a próxima camada possa usar os dados fornecidos na sequência dos dados publicados pela camada anterior.

Agora na camada de rede, temos o envio de pacotes da origem ao destino. Esta transmissão pode atravessar várias redes (links). Enquanto a camada de enlace de dados monitora os pacotes enviados dentro do sistema, a camada de rede deve garantir que os dados saiam de seu destino e cheguem onde deveriam. Uma camada de rede não é absolutamente necessária se os dois sistemas estiverem conectados à mesma rede.

No entanto, como ambos os sistemas estão conectados à mesma rede (link), geralmente é necessária uma camada de rede para garantir o transporte da origem ao destino. Um roteador é um dispositivo de rede intermediário cuja função é definir e distribuir pacotes de dados com base em rotas IP. Desta forma, sua função está diretamente relacionada ao endereçamento IP da rede. (BARRETO; ZANIN; SARAIVA 2018, p.78)

Sobre a camada de transporte, representa um processo o envio processo por processo até que o tráfego de mensagens seja totalmente processado. Um processo é um programa executado em um host. Essa camada deve garantir que a mensagem chegue ao seu destino em sua totalidade, pois possui mecanismos para detectar erros na transmissão. (BARRETO; ZANIN; SARAIVA, 2018, p.79).

A camada de sessão executa uma caixa de diálogo existente em sua rede. Sua função também é estabelecer, manter e sincronizar as interações existentes entre os sistemas de comunicação. E a camada de aplicação permite que usuários finais e software acessem a rede. Essa camada também fornece a interface do usuário e suporte para serviços como e-mail e gerenciamento de dados compartilhados.

**Camadas dos modelos OSIxTCP/IP**

Existem diversas semelhanças conceituais, entre o modelo OSI e o modelo TCP/IP, pois ambos são baseados em camadas de protocolo que funcionam independentemente uma da outra. Dentro dessa função de múltiplas camadas encontramos suas semelhanças. Em qualquer um dos modelos, pode-se pensar que a próxima camada depende da anterior. É a camada anterior que envia as informações decodificadas para a próxima camada. Apesar dessas semelhanças, são modelos que se comportam de maneira muito diferente por si só. Você pode imaginar uma comparação por modelo de referência. (BARRETO; ZANIN; SARAIVA, 2018, p.79).

O modelo OSI é o modelo básico para comunicação em rede. Ele foi aprimorado e padronizado, portanto, é adotado pela indústria e desenvolvedores como um vital mecanismo de consulta. Este modelo possui sete camadas que se comunicam entre si. Três características podem ser consideradas como conceitos centrais e mais importantes para o funcionamento deste modelo, os serviços, interfaces e protocolos. É a função do modelo OSI que distingue cada uma dessas funções. (BARRETO; ZANIN; SARAIVA, 2018, p.80).

O modelo OSI possui sete camadas com diferentes funções. O modelo OSI distribui suas camadas e dá a cada camada a capacidade de agir sobre os dados que recebe. Uma camada depende da outra para pleno funcionamento. A função dessas sete camadas é decompor as comunicações da rede em partes menores e mais simples. Uma vantagem da camada do modelo OSI é que ela permite a comunicação entre diferentes hardwares e softwares de rede.

Esse modelo também evita que alterações em uma camada afetem outras camadas, aumentando a velocidade e agilidade do desenvolvimento. No modelo OSI, são as camadas inferiores que fornecem serviços às camadas superiores. Além disso, cada camada é responsável por atividades que são repassadas para outras camadas sucessivamente. (Barrett; Zanin; Saraiva, 2018)

Outra grande vantagem do modelo OSI é que qualquer protocolo pode ser utilizado desde que forneça o serviço solicitado. Também permite que o protocolo seja alterado sem alterar o software da camada superior. Mesmo considerando pares de protocolos, entende-se que cada protocolo associado a cada camada é totalmente responsável, pois cada camada possui operações específicas.

O modelo TCP/IP tem importância histórica para o seu desenvolvimento. A adoção desse padrão também permitiu o desenvolvimento da indústria de telefonia, da indústria eletrônica e de outras indústrias. O modelo TCP/IP originalmente não fazia distinção entre serviços, interfaces e protocolos. É importante observar que houve muitas tentativas de inverter essa estrutura e abordar o modelo OSI, mas essas tentativas foram menos eficientes. (Barrett; Zanin; Saraiva 2018)

No modelo TCP/IP, apenas dois serviços são fornecidos pela camada Internet: o envio de pacotes IP e o recebimento dos pacotes IP. Aqui vemos uma clara diferença com o modelo OSI. Porque essa camada de internet tem mais recursos à sua disposição. Neste ponto, podemos distinguir ainda mais entre os dois modelos. Isso ocorre porque o modelo OSI geralmente é mais geral. Isso porque ele é o mais adaptável ao seu meio e é aquele que melhor se forma em resposta à tecnologia. Um ponto chave que precisa ser enfatizado e representa uma grande diferença entre os dois modelos é que o modelo OSI tem alguns problemas para começar e adicione mais camadas para corrigi-los quando são identificados erros. Acabou sendo 7 camadas porque surgiu a necessidade.

Para Barreto, Zanin e Saraiva (2018, p.81), o modelo TCP/IP foi o oposto. Primeiro, identifiquei o que precisava e formei um modelo e suas camadas a partir daí. É claro que toda a pilha de protocolos não cabe em um modelo pronto para uso, portanto, esse conceito só serve para a operação TCP/IP.

Os modelos TCP/IP e OSI possuem camadas de rede, transporte e aplicação. Um aspecto muito importante da diferença entre os dois é que uma comunicação é feita sem conexão, enquanto a outra é para uma conexão direta. A camada de rede do modelo OSI suporta ambos os tipos de comunicação. No entanto, isso não ocorre no modelo TCP/IP. (BARRETO; ZANIN; SARAIVA, 2018, p.81).

Os serviços da camada de transporte OSI são transparentes, visíveis ao usuário e possuem apenas um COC, enquanto o modelo TCP/IP suporta ambos os tipos de transporte. O modelo TCP/IP, portanto, deixa a escolha para o usuário. Ao contrário do modelo OSI, o modelo TCP/IP é projetado em quatro camadas. Algumas camadas no modelo TCP/IP têm os mesmos nomes das camadas no modelo OSI e, em alguns casos, são funcionalmente equivalentes. (BARRETO; ZANIN; SARAIVA, 2018, p.81).

Outro fator notável é que o modelo TCP/IP combina aspectos das camadas de apresentação e sessão dentro da camada de aplicação. Esse é um fator importante porque no modelo OSI isso só é feito dentro das camadas que atendem a esse propósito. Além disso, o modelo TCP/IP combina as camadas física e de enlace em uma única camada. Eles também têm uma camada por recurso no modelo OSI.

É importante lembrar que o modelo TCP/IP parece simplista porque tem menos camadas, mas isso não é verdade. Ambos os modelos têm graus de complexidade. O modelo OSI não foi construído em torno de uma rede específica, mas o modelo TCP/IP foi baseado nos padrões da Internet nos quais foi construído. Obviamente, o modelo OSI é preferível ao modelo TCP/IP devido à sua adaptabilidade. (BARRETO; ZANIN; SARAIVA, 2018, p.81).

**Conteúdo bônus**

**Tópicos avançados**

Já ouviu falar sobre redes de Confiança Zero?

Os modelos de redes e seus protocolos ajudam a criar redes universais e seguras, mas assim como existe inovação nas redes, existe inovação nas formas de ataque à sua segurança. Desta forma, surgem metodologias, sistemas, equipamentos que aprimoram a segurança das redes.

Um tema crescente no universo das redes são as redes de confiança zero, e isso significa algo tão agressivo quanto parece: um sistema de autenticação de rede que não trata nenhum host ou conexão como conhecida, segura ou confiável, o que permite uma melhor avaliação de cada tentativa de conexão para que sejam evitados casos onde chaves seguras são usurpadas por hackers.

Que tal ler mais sobre isso?

Disponível em: <[https://paginajournal.com/desmistificando-o-acesso-a-rede-de-confianca-zero-2-0/](https://paginajournal.com/desmistificando-o-acesso-a-rede-de-confianca-zero-2-0/)> Acesso em 31/01/2023.

Observação: Este conteúdo não será cobrado nas avaliações e estará, obrigatoriamente, presente nas videoaulas. Fique tranquilo(a)!

Referência Bibliográfica

BARRETO, Jeanine dos Santos; ZANIN, Aline; SARAIVA, Maurício de Oliveira. **Fundamentos de redes de computadore**s. – Porto Alegre: SAGAH, 2018.

BAY; Edemilson; BLUNING, Paulo Henrique. **Fundamentos de redes de computadores**. UNIASSELVI, 2016.

MACEDO, Ricardo Tombesi ... [et al.]. **Redes de computadores**. – Santa Maria, RS: UFSM, NTE, 2018.