[[Cybersecurity Essentials]]
## Políticas de Segurança

**Introdução**

Além dos mecanismos de autenticação, criptografia, firewall, sistemas de detecção de intrusão e estratégias de recuperação de um ataque, outra contramedida relevante está associada ao controle de acesso e gestão de credenciais. Um processo efetivo de autorização pode auxiliar a limitar as consequências dos ataques, de forma que os usuários legítimos tenham um acesso limitado aos recursos que são necessários para execução de suas funções.

**Objetivos da aula**

- Comparar a autenticação e a autorização e seu relacionamento;
- Descrever tipos diferentes de controle de acesso, seus benefícios e limitações;
- Descrever o ciclo de vida de credenciais.

**Resumo**

Após entender as vulnerabilidades presentes na arquitetura de um sistema de informação, os possíveis vetores de ataque e motivações dos atacantes, priorizar ataques de acordo com uma avaliação de risco e compreender algumas contramedidas como a criptografia para embaralhar as mensagens, firewall para limitar o acesso ao canal de comunicação, possivelmente empregar sistemas de detecção de intrusão e definir estratégias para recuperação de um ataque, é importante também ter conhecimento sobre o controle de acesso e a autorização. Estes mecanismos, se bem aplicados, podem suprir um bom compromisso entre limitar o usuário legítimo a acessar somente os recursos necessários para exercer suas tarefas do dia a dia, e limitar consequências de ataques como o roubo de credenciais de funcionários de uma empresa.

Podemos começar entendendo o que é o processo de autorização. Este procedimento é dependente do processo de autenticação visto anteriormente, mas é fundamentalmente diferente.

Relembrando, a autenticação é o processo de um usuário provar sua identidade, de provar que ele ou ela é quem diz ser. Este processo pode se basear em algo que o usuário sabe (uma senha, por exemplo), algo que o usuário tem (um cartão de acesso) ou algo que o usuário é (digital do dedão direito, por exemplo).

Se a pergunta no processo de autenticação é “Você é quem diz ser?”, então a pergunta no processo de autorização é “Você está autorizado a fazer isso?”. Muitas vezes no cotidiano o processo de autorização ocorre em conjunto com a autenticação, por isso pode passar despercebido. Porém, pense no acesso a informações sigilosas em uma pasta compartilhada. É comum que você consiga realizar o login (isto é, se autenticar) com sucesso na plataforma de compartilhamento de arquivos em nuvem, mas ainda não ter acesso a esta pasta compartilhada, e ter de pedir acesso a algum colega ou chefe. Neste caso, a autenticação foi realizada com sucesso, mas enquanto a pasta não estava compartilhada com você, você não estava autorizado a acessar este recurso. Neste exemplo, observamos que é necessário que o sistema acredite que você é quem diz ser, para depois autorizar o acesso a algum recurso. Ou seja, a autenticação é necessária para que a autorização ocorra.

Prosseguindo, o que faz o processo de autorização ocorrer é uma política de controle de acesso. De forma simplificada, o controle de acesso possui as regras que devem ser seguidas para definir quais usuários autenticados devem ter acesso a quais recursos, sejam estes recursos arquivos compartilhados, e-mails, ou até acesso físico a lugares. Por exemplo, para entrar em prédios comerciais e residenciais é necessário se identificar com um documento de identificação com foto, e depois algum morador ou empregado autorizar o acesso de determinado visitante. Até festas possuem controle de acesso para evitar o acesso de pessoas que não pagaram pelo ingresso da festa, e autorizar o acesso a pessoas que pagaram o ingresso e, portanto, devem ter acesso autorizado à festa. Inclusive, é possível ter lugares diferentes em festas e jogos a depender do tipo de ingresso que foi adquirido.

Podemos ter diversos tipos de controle de acesso. O primeiro deles é o mais simples, que é o controle por meio de lista de controle de acesso (ACL – do inglês _Access Control List_). Vamos considerar um exemplo para facilitar a explicação. Pense que nossos personagens Alice e Bob são convidados legítimos de uma festa, e Carlos é uma pessoa não autorizada a entrar na festa. Na entrada da festa, podemos ter uma pessoa da segurança que possui uma lista de convidados e deve deixar somente os convidados presentes na lista entrarem no local da festa. O procedimento é simples: conforme a fila da Figura 1, Bob pode ser o primeiro a chegar. Neste caso, o encarregado da segurança deve primeiro verificar que o Bob é quem ele diz ser, e depois ver se o nome está na lista de convidados.

O mesmo procedimento padronizado deve ser feito por Carlos e Alice. No caso de Carlos, por mais que ele prove que ele é quem diz ser apresentando um documento de identificação com foto, ele não deve ter acesso concedido pois não está na lista de convidados. A Alice deve ter o acesso autorizado, porém observe que se ela não conseguir se identificar com sucesso por ter esquecido seu documento de identificação, então ela não será autorizada.

Mais uma vez, fica evidente que a autenticação é necessária para a autorização ser realizada com sucesso. O encarregado pela segurança não pode deixar Alice entrar neste caso pois então alguém poderia estar tentando se passar pela Alice para entrar na festa.

Figura 1 – Cenário hipotético do Controle de Acesso

![Fonte: Autoria própria, 2022.](https://paperx-dex-assets.s3.sa-east-1.amazonaws.com/images/1674070366446-460yUo6pw2.png "Fonte: Autoria própria, 2022.")

Fonte: Autoria própria, 2022.

Outro tipo de controle de acesso é o ABAC (do inglês _Attribute-Based Access Control_), o controle de acesso baseado em atributos. A ideia é que a regra de autorização fique baseada em algum atributo dos usuários. Lembrando que a pergunta em relação à autorização é “os usuários autenticados têm autorização para acessar o recurso?”, podemos considerar novamente o exemplo da festa com Alice, Bob e Carlos. O encarregado da segurança pode utilizar outra regra de autorização: que somente maiores de 18 anos podem entrar na festa. Neste caso, após se identificarem com o documento de identificação com foto e verificando a similaridade da foto do documento com a face de cada pessoa, Alice, Bob e Carlos têm de provar que são maiores de 18 anos, o que também pode ser feito com a apresentação do documento de identificação.

Há também o controle de acesso RBAC (do inglês _Role-Based Access Control_), ou controle de acesso baseado em perfis. Uma limitação do controle de acesso ACL é sua gestão para um número muito grande de usuários e recursos. Se há muitos recursos e muitos usuários, estas listas de controle de acesso se tornam maiores, e em maior quantidade. A cada usuário novo, seria necessário cadastrá-lo em todas as listas de controle de acesso, o que se torna um processo trabalhoso. Já no controle de acesso RBAC a ideia é que os usuários pertencem a perfis diferentes. A autorização aos recursos ocorre a depender do perfil ao qual o usuário pertence. Voltando ao exemplo da festa, podemos ter uma festa somente para moradores, e no caso o encarregado da segurança pode autorizar o acesso apenas aos usuários que estão no perfil de morador de um determinado condomínio.

O último conceito importante é de ciclo de vida de credenciais. Imagine que em uma empresa a gerente Alice possui credenciais de acesso (login1, senha1) para ter acesso ao prédio comercial de uma empresa que possui documentos confidenciais em sua sede. Podemos ter a contratação de um analista, o Bob, que deverá receber novas credenciais (login2, senha2). Alice pode ter perfil de administradora, e Bob o perfil de usuário comum. Se Bob for desligado da empresa, é importante que ocorra a revogação da credencial de Bob, para que sua credencial não seja utilizada em um eventual ataque. Além disso, este controle de acesso mais granular pode fazer com que o acesso a áreas mais reservadas da sede da empresa seja acessível apenas para usuários com perfil administrador, o que pode minimizar eventuais danos de um ataque com as credenciais de Bob. Neste exemplo, fica evidente a importância da criação, revogação e gestão de credenciais para que o controle de acesso seja efetivo e contribua para a segurança do sistema.

**Como aplicar na prática o que aprendeu**

Observe exemplos de controle de acesso no seu cotidiano para acesso a arquivos, prédios comerciais ou residenciais, entre outros recursos, e tente identificar como ocorrem os processos de autenticação e autorização.

**Conteúdo bônus**

**Tópicos avançados**

Para aprofundar seus conhecimentos sobre ABAC, que é o tipo de controle de acesso mais novo, consulte (AWS, 2022) e (MICROSOFT, 2022).

Observação: Este conteúdo não será cobrado nas avaliações e estará, obrigatoriamente, presente nas videoaulas. Fique tranquilo(a)!

Referência Bibliográfica

AWS. **O que é ABAC para a AWS?**. Disponível em: < [https://docs.aws.amazon.com/pt_br/IAM/latest/UserGuide/introduction_attribute-based-access-control.html](https://docs.aws.amazon.com/pt_br/IAM/latest/UserGuide/introduction_attribute-based-access-control.html)> Acesso em 15/12/2022.

Microsoft. **O que é o ABAC do Azure (controle de acesso baseado em atributo do Azure)?**. Disponível em: < [https://learn.microsoft.com/pt-br/azure/role-based-access-control/conditions-overview](https://learn.microsoft.com/pt-br/azure/role-based-access-control/conditions-overview)> Acesso em 15/12/2022.