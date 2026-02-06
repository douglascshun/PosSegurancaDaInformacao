[[Cybersecurity Essentials]]
## Controles de Segurança para redes, servidores e aplicativos

**Introdução**

Já entendemos as necessidades de segurança cibernética, quais ataques são possíveis e como realizar uma avaliação de risco. Agora, podemos elencar controles de segurança e outras contramedidas para aumentar o nível de segurança de sistemas de informação, priorizando as contramedidas que mitiguem os ataques com maior risco.

**Objetivos da aula**

- Listar mecanismos de autenticação;
- Descrever mecanismos de criptografia e firewall;
- Descrever o que é um sistema de detecção de intrusão;
- Propor uma estratégia de recuperação de um ataque.

**Resumo**

Com a avaliação de risco, é possível entender não somente quais os pontos fracos de um sistema em desenvolvimento, mas também identificar e priorizar quais ataques possuem maior risco associado. Sabendo desta priorização, convém entender alguns mecanismos de segurança que podem ser adicionados aos sistemas de informação para torná-los mais seguros.

Desta forma, ao invés de realizar uma ação sem justificativa, podemos ter um método para identificar vulnerabilidades, reconhecer possíveis ataques, avaliar seu risco associado e selecionar as contramedidas que são mais eficazes para mitigar os ataques com maior risco. Ao controlar o risco, podemos ter uma gestão mais efetiva e empregar recursos de acordo com sua necessidade, evitando inclusive a adoção de medidas de segurança que detraem a usabilidade sem aumentar de forma relevante o nível de segurança.

A primeira barreira contra atacantes e usuários não-autorizados é a autenticação. Este processo de verificação de identidade está associado ao conceito de autenticidade, e se baseia em três fatores principais: o que você é, o que você possui e o que você sabe.

Para comprovar que você é quem você diz ser, ou no nosso cenário hipotético, que a Alice é realmente a Alice e não o Carlos tentando se passar pela Alice, podemos usar algum traço único da fisionomia da Alice, como uma digital ou sua face. Estas e outras formas de autenticação por biometria fazem parte da categoria de autenticação baseada em algo que você é.

Também é possível utilizar um _token_ no dispositivo móvel ou um cartão para se autenticar. Estas formas de comprovar sua identidade fazem parte da categoria de algo que você possui. Por fim, se autenticar usando um segredo (senha, por exemplo) é uma forma de verificar sua identidade usando algo que você sabe (e está pressuposto que somente você tem acesso a esta informação).

Para entender o segundo tipo de contramedida, a criptografia, podemos utilizar o cenário hipotético com a Alice, Bob e Carlos, conforme representado pela Figura 1.

Alice envia uma mensagem para Bob com informações sigilosas. Bob recebe a mensagem e somente ele deveria ter acesso a estas informações sigilosas, que podem conter um segredo industrial por exemplo. O que chamamos de texto às claras está presente na Alice e no Bob após o envio e recebimento da mensagem. Ou seja, Alice e Bob conseguem ler a mensagem original sem maiores problemas.

A ideia principal da criptografia está relacionada em embaralhar bem a mensagem para que um terceiro não-autorizado não consiga entender a mensagem em trânsito, mesmo que consiga obtê-la. Esta mensagem em trânsito embaralhada é denominada texto cifrado, ou seja, é um texto que o Carlos não consegue entender, mesmo que obtenha a mensagem ao invadir o canal de comunicação e interceptar a mensagem.

Figura 1 – Cenário hipotético com Alice, Bob e Carlos

![Fonte: Autoria própria, 2022.](https://paperx-dex-assets.s3.sa-east-1.amazonaws.com/images/1674066807290-pudGiyQbu2.png "Fonte: Autoria própria, 2022.")

Fonte: Autoria própria, 2022.

A criptografia simétrica de forma simplificada pressupõe que ambos, Alice e Bob, compartilham uma mesma chave (vide Figura 2). Esta chave é usada pela Alice para cifrar o texto, isto é, embaralhar o texto às claras e transformá-lo no texto cifrado. Após receber a mensagem, Bob pode utilizar a chave compartilhada para desembaralhar a mensagem, ou seja, obter o texto às claras a partir do texto cifrado.

Figura 2 – Criptografia simétrica no exemplo hipotético

![Fonte: Autoria própria, 2022.](https://paperx-dex-assets.s3.sa-east-1.amazonaws.com/images/1674066830705-GsGPeG5BZj.png "Fonte: Autoria própria, 2022.")

Fonte: Autoria própria, 2022.

Já a criptografia assimétrica pressupõe uma chave única de cada pessoa, uma chave privada para a Alice e uma chave privada para o Bob (vide Figura 3). Há também uma chave pública, que é uma chave que qualquer um pode ter acesso, e que possui uma analogia com um cadeado aberto. A ideia é que se Alice quiser enviar algo para Bob, ela pode usar a chave pública de Bob (o cadeado aberto de Bob) para embaralhar a mensagem de forma que apenas o Bob consiga desembaralhar a mensagem após seu recebimento com sua chave privada.

Figura 3 – Criptografia assimétrica no exemplo hipotético

![Fonte: Autoria própria, 2022.](https://paperx-dex-assets.s3.sa-east-1.amazonaws.com/images/1674066857665-ldfVyM9aX8.png "Fonte: Autoria própria, 2022.")

Fonte: Autoria própria, 2022.

Relembrando o requisito de disponibilidade, podemos considerar que Carlos pode também atacar o canal de comunicação e tornar inviável o envio e recebimento da mensagem. Um mecanismo possível para proteger uma rede (relacionado a este canal de comunicação) é o firewall. Este mecanismo pode restringir o acesso à rede de forma que somente alguns endereços específicos podem ter acesso a este canal de comunicação. Na comunicação utilizando o protocolo TCP/IP, podemos ter endereços IP estáticos para os clientes a depender do provedor de acesso à Internet. Alice e Bob podem ter endereços X e Y, respectivamente. No caso, um firewall pode permitir acesso apenas dos endereços X e Y ao canal de comunicação. Se Carlos, do endereço IP Z tentar acessar o canal de comunicação, ele será bloqueado pelo firewall. Desta forma, mesmo que a credencial usada para autenticação da Alice tenha sido obtida por Carlos, ele não conseguirá acessar o sistema pois seu endereço IP não está autorizado.

Detalhando um pouco mais o roubo de credenciais, se Carlos conseguir obter estas credenciais é possível que Carlos tente fingir ser a Alice, ou que Carlos tente fingir ser o Bob. Estas credenciais podem ter sido obtidas por meio de engenharia social ou então por má prática de algum usuário legítimo (senha em _post-it_, por exemplo). Além do firewall, há algo adicional que podemos fazer neste caso?

É possível utilizar também sistemas de detecção de intrusos. Estes sistemas podem usar padrões de acesso, acesso a sites não usuais, acesso com frequência muito além do comum, além de acesso, modificação e exclusão de arquivos não-usuais para identificar que, mesmo com as credenciais corretas, o comportamento de um usuário em específico está muito incomum, e que pode ser um atacante personificando um usuário legítimo.

Por fim, também é necessário elaborar estratégias para tratar cenários em que o sistema está sendo atacado. Com hackers cada vez mais sofisticados e ameaças emergentes, é imperativo especificar um plano de ação no caso de ataques para mitigar os eventuais danos causados. Por exemplo, é possível tentar isolar a parte do sistema que está sob ataque (neste caso a arquitetura do sistema se torna muito útil), utilizar backups (de preferência em outro servidor) e tomar um cuidado para neste procedimento de recuperação não reincidir no mesmo erro e consequentemente no mesmo ataque. Nesta estratégia, alguns pontos de atenção são a descrição de procedimentos padronizados para serem seguidos de forma calculada mesmo no calor da situação, e utilizar ferramentas de diagnóstico, pois não há como se recuperar de um ataque e realizar um isolamento se não conseguir entender que parte do sistema está sendo de fato atacada.

**Como aplicar na prática o que aprendeu**

Obtenha ataques veiculados na mídia e tente identificar quais contramedidas listadas nesta aula poderiam ser empregadas para evitar ou mitigar os ataques.

**Conteúdo bônus**

**Tópicos avançados**

Tipos diferentes de biometria para autenticação estão descritos em (GOGONI, 2022). Para maiores detalhes sobre firewall, consulte (KASPERSKY, 2022).

Observação: Este conteúdo não será cobrado nas avaliações e estará, obrigatoriamente, presente nas videoaulas. Fique tranquilo(a)!

Referência Bibliográfica

Gogoni, Ronaldo. **O que é biometria? Os 6 tipos mais usados na tecnologia**. Disponível em: <[https://tecnoblog.net/responde/o-que-e-biometria-tecnologia](https://tecnoblog.net/responde/o-que-e-biometria-tecnologia)> Acesso em 15/12/2022.

Kaspersky. **O que é um firewall? Definição e explicação**. Disponível em: <[https://www.kaspersky.com.br/resource-center/definitions/firewall](https://www.kaspersky.com.br/resource-center/definitions/firewall)> Acesso em 15/12/2022.