[[Cybersecurity Essentials]]
## Procedimentos adequados para a disponibilidade e o sigilo dos dados

**Introdução**

Se dados são o novo ouro, como podemos garantir seu sigilo nos sistemas de informação? Por diversas vezes, estes dados são informações sensíveis e por necessidades regulatórias devemos preservar sua confidencialidade. Nesta aula iremos explorar como os mecanismos de segurança podem ser utilizados para aumentar os níveis de disponibilidade e sigilo dos dados.

**Objetivos da aula**

- Descrever como usar o firewall para mitigar ataques que diminuem a disponibilidade dos dados em um sistema de informação;
- Descrever como a criptografia pode ser utilizada para suportar a confidencialidade dos dados sensíveis;
- Associar conceitos da LGPD e GDPR a novos requisitos que os sistemas da informação devem cumprir;
- Justificar por que uma política de gestão de dados é importante para uma plataforma digital.

**Resumo**

Quando ouvimos falar da Era dos Dados, estamos muitas vezes pensando como dados podem se transformar em informações úteis para suportar tomadas de decisão estratégicas em negócios.

Gestores de empresas podem associar um monitoramento em tempo real com estimativas precisas sobre possíveis cenários futuros para priorizar tarefas e traçar planos de ação de curto, médio e longo prazo.

Por trás deste valor agregado às empresas, estão tecnologias como Big Data para coletar e manipular conjuntos gigantescos de dados, Internet das Coisas para automatizar a coleta de dados do mundo físico, e Inteligência Artificial para realizar análises complexas sobre o passado e estimar cenários futuros. Contudo, todo este ciclo virtuoso pressupõe que estes dados estão sendo coletados com sucesso.

Há duas barreiras para o sucesso na coleta de dados sob a perspectiva de privacidade e segurança da informação. A primeira é o uso de mecanismos eficientes para garantir a disponibilidade destes dados, das ferramentas e plataformas digitais em geral.

Afinal de contas, de nada adianta um sistema que não consegue receber os dados mais atuais ou disponibilizar suas análises para seus usuários. Esta incapacidade pode ser traduzida como eventos de indisponibilidade dos sistemas.

É claro que estes eventos de indisponibilidade podem ser consequência de _bugs_ ou outros problemas internos de desenvolvimento da empresa, mas nesta aula estamos nos preocupando com as indisponibilidades causadas por agentes externos, isto é, ataques cibernéticos.

A segunda barreira é empregar mecanismos que garantam a confidencialidade dos dados. Considerando que há usuários legítimos do sistema, somente estes usuários devem ter acesso aos dados registrados e às análises realizadas.

Além disso, os dados sensíveis devem ser confidenciais apenas ao usuário específico que os possui e os forneceu para a plataforma.

Podemos exemplificar mecanismos para suportar a disponibilidade dos dados a partir do cenário hipotético com Alice, Bob e Carlos (vide Figura 1).

O tipo de ataque que estamos considerando é aquele em que Carlos ataca o canal de comunicação usado por Alice e Bob, de forma que a Alice não consegue mandar um e-mail a partir do seu dispositivo móvel comercial, e/ou o Bob não consegue receber um e-mail usando seu computador pessoal.

Figura 1 – Cenário hipotético com Alice, Bob e Carlos

![Fonte: Autoria própria, 2022.](https://paperx-dex-assets.s3.sa-east-1.amazonaws.com/images/1674138195330-DTb1V55GlO.png "Fonte: Autoria própria, 2022.")

Fonte: Autoria própria, 2022.

Outro tipo de controle de acesso é o ABAC (do inglês Attribute-Based Access Control), o controle de acesso baseado em atributos.

Um mecanismo para aumentar a disponibilidade do sistema e, consequentemente, dos dados nele contidos, é o firewall. Relembrando, o firewall pode limitar o acesso ao canal de comunicação, de forma que somente os clientes de IP X e Y (Alice e Carlos, respectivamente) sejam aceitos. Desta forma, mesmo que Carlos tente utilizar a credencial de Bob, ele não conseguiria usar o canal de comunicação pois seu IP é Z, que é diferente de X e Y, conforme ilustrado na Figura 2.

Figura 2 – Cenário de aplicação do firewall

![Fonte: Autoria própria, 2022.](https://paperx-dex-assets.s3.sa-east-1.amazonaws.com/images/1674138224461-GV6UsthaAF.png "Fonte: Autoria própria, 2022.")

Fonte: Autoria própria, 2022.

Outro mecanismo para aumentar a disponibilidade dos dados é utilizar _backups_ dos dados. De preferência, estas cópias dos dados devem estar em máquinas, redes e até em outro fornecedor de computação em nuvem, de forma que se um deles for atacado, a cópia esteja de fato disponível para realizar uma recuperação. Em conjunto com uma estratégia de recuperação de um ataque, estas cópias podem aumentar a disponibilidade dos dados ao reduzir o _downtime_ do sistema.

Para tornar os dados sensíveis confidenciais apenas a Alice e Bob, no nosso exemplo, podemos usar o mecanismo de criptografia simétrica, que é mais leve, mas pressupõe uma chave compartilhada entre Alice e Bob, ou então usar uma criptografia assimétrica, porém, com maior custo computacional associado (uso maior de memória e processamento, por exemplo). Com a criptografia fim a fim, é possível que somente Alice e Bob saibam das informações confidenciais trocadas em uma mensagem, de forma que a própria plataforma não tenha como obter o texto às claras, pois não possui acesso às chaves criptográficas de Alice ou Bob.

Observe que utilizamos o termo dado sensível para destacar o tipo de dado que merece uma atenção maior em termos de confidencialidade. A Lei Geral de Proteção de Dados (LGPD) possui esta definição de o que é um dado sensível, e também destaca outros aspectos importantes como obter consentimento do usuário para coletar seus dados, deixar claro para este usuário a finalidade da coleta dos dados, e permitir que este usuário obtenha uma cópia destes dados quando solicitado.

Adicionalmente, a GDPR (_General Data Protection Law_) também possui alguns aspectos interessantes, como o direito de ser informado, ou seja, trabalhar para que os sistemas e plataformas sejam transparentes em relação a quais dados utilizam e com que finalidade, de forma geral. Outro aspecto relevante é o direito de ser esquecido, ou seja, o direito que o usuário tem de pedir que a plataforma digital exclua todos seus dados. A depender da arquitetura da plataforma, os dados podem estar distribuídos ou podem existir diversas cópias (lembram do mecanismo de _backup_ para garantir disponibilidade dos dados?), o que pode dificultar o cumprimento deste requisito.

Por fim, uma plataforma digital também deve possuir uma política de Gestão de Dados, que é uma forma de tentar aplicar os conceitos da LGPD e GDPR. Por exemplo, considere que Alice e Bob são usuários de uma plataforma digital. É interessante que a política de gestão de dados desta plataforma deixe claro quais dados estão sendo coletados, que esta política preveja o consentimento do usuário em ter seus dados coletados, e para quais finalidades. Além disso, deve também ser descrito como o usuário pode obter cópia de todos os seus dados presentes na plataforma em determinado momento, e destacar quais mecanismos de proteção são utilizados para garantir a disponibilidade e o sigilo dos dados.

**Como aplicar na prática o que aprendeu**

Observe exemplos de controle de plataformas digitais que utiliza com frequência, obtenha suas políticas de gestão de dados e tente identificar como os requisitos da LGPD e/ou GDPR estão sendo cumpridos, ou se possivelmente há pontos de melhoria.

**Conteúdo bônus**

**Tópicos avançados**

Para aprofundar seus conhecimentos sobre LGPD, utilize a referência (GOOGLE, 2022) para entender a perspectiva de um fornecedor de computação em nuvem sobre o tema. Por outro lado, aspectos de privacidade ainda são desafios para as novas interfaces de assistentes de voz (TECHTUDO, 2022).

Observação: Este conteúdo não será cobrado nas avaliações e estará, obrigatoriamente, presente nas videoaulas. Fique tranquilo(a)!

Referência Bibliográfica

Google. **Lei Geral de Proteção de Dados (LGPD).** Disponível em: < [https://cloud.google.com/security/compliance/lgpd?hl=pt-br](https://cloud.google.com/security/compliance/lgpd?hl=pt-br)> Acesso em 15/12/2022.

TECHTUDO. **Amazon confirma que Alexa guarda todos os dados de conversas com usuários**. Disponível em: < [https://www.techtudo.com.br/noticias/2019/07/amazon-confirma-que-alexa-guarda-todos-os-dados-de-conversas-com-usuarios.ghtml](https://www.techtudo.com.br/noticias/2019/07/amazon-confirma-que-alexa-guarda-todos-os-dados-de-conversas-com-usuarios.ghtml)> Acesso em 15/12/2022.