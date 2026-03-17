[[Cybersecurity Essentials]]
## Pensamento crítico

**Introdução**

Ao implantar políticas e mecanismos para aumentar a segurança da informação e garantir os requisitos de segurança cibernética, é importante ter um pensamento crítico. Não convém aplicar todo e qualquer tipo de mecanismo de segurança pois a usabilidade pode ficar comprometida e, a depender das tecnologias emergentes da transformação digital, é possível que novos desafios estejam presentes. Nesta aula, considerações sobre estes desafios e uma análise crítica sobre o conflito entre Segurança e Usabilidade será apresentada.

**Objetivos da aula**

- Listar Desafios de Segurança em Aprendizado de Máquina;
- Listar Desafios de Segurança em Internet das Coisas;
- Listar Desafios de Segurança em Computação em Nuvem;
- Listar Desafios de Segurança na Computação Quântica;
- Descrever o Trade Off entre Segurança e Usabilidade.

**Resumo**

Para sermos pioneiros da Transformação Digital nas empresas e na sociedade de maneira geral, é necessário um pensamento crítico sobre a adoção de tecnologias emergentes como Inteligência Artificial e os novos desafios de segurança da informação. Estas tecnologias emergentes agregam muitas oportunidades de possíveis ganhos para os negócios, mas é necessário ponderar sobre as novas necessidades de segurança para que a implantação destas novas tecnologias não signifique um aumento significativo de ameaças aos sistemas de informação.

A começar pelo Aprendizado de Máquina, este é um tipo de Inteligência Artificial que pode automatizar tarefas como classificação de itens, agrupamento de usuários, predição de séries temporais, entre outros. Para isso, podemos ter um aprendizado supervisionado, em que os dados são rotulados, ou não-supervisionado em que os dados não são rotulados a priori.

Para que o Aprendizado de Máquina ocorra com sucesso, portanto, são necessários dados. Estes dados devem estar disponíveis e serão confidenciais se forem sensíveis. Vale considerar os mecanismos de _firewall_, _backup_ e criptografia para garantir níveis satisfatórios de disponibilidade e confidencialidade. Outro ponto importante é garantir o acesso a dados históricos e análises realizadas apenas a usuários autenticados e autorizados, o que justifica um controle de acesso granular para auxiliar nesta gestão de risco. Por fim, pode ser necessário anonimizar dados a depender do tipo de consentimento obtido do usuário.

Seguindo para a Internet das Coisas (IoT), esta é uma tecnologia que fornece às máquinas a capacidade de sentirem e atuarem no mundo físico. Com o IoT, é possível realizar a automação de coleta de dados do mundo real e contribuir para a redução de custos, otimização e manutenção nas empresas.

Para garantir a confidencialidade dos dados coletados por dispositivos IoT, uma ideia inicial pode ser aplicar a criptografia para embaralhar e desembaralhar as mensagens. Contudo, temos dois tipos de criptografia: simétrica e assimétrica, sendo que a criptografia assimétrica necessita de mais recursos computacionais (como memória e processamento) que a criptografia simétrica. Como dispositivos IoT possuem restrições de energia, processamento e memória, o sugerido é a aplicação de criptografia simétrica ao invés de criptografia assimétrica neste caso, se for para escolher entre estas duas alternativas.

A computação em nuvem é outra tecnologia que facilita o trabalho remoto, ao facilitar o acesso a arquivos e programas de qualquer lugar, em qualquer momento. Porém, também é necessário ponderar se após a migração de um sistema para a nuvem, o controle de acesso e demais controles de segurança estão presentes e bem configurados, pois se houver vulnerabilidades relevantes é possível que um atacante utilize um mecanismo próprio da criptografia contra a segurança da informação ao realizar um ataque de _ransomware_.

Por falar em criptografia, há um novo paradigma de computação que pode ameaçar a criptografia assimétrica. Considerada, hoje, mais segura que a criptografia simétrica, em termos de resiliência, a determinados tipos de ataque, quando computadores quânticos forem viáveis, é possível que problemas, antes difíceis, se tornem fáceis. E o problema de fatoração de números primos, um dos alicerces da criptografia assimétrica, infelizmente, está ameaçado. A computação quântica ainda está em desenvolvimento, mas possui um grande potencial.

Por fim, cabe uma reflexão sobre o conflito entre usabilidade e segurança. Ao tomar decisões durante o desenvolvimento de um sistema, aspectos de qualidade diferentes podem ser conflitantes. Mesmo que usuários e desenvolvedores possam querer tudo, muitas vezes é necessário escolher. Relembrando, estas decisões estarão representadas no modelo do sistema que denominamos de arquitetura.

Veja o exemplo de autenticação: se desejar utilizar todos os 3 fatores (o que você é, o que você tem e o que você faz), é possível aumentar o nível de segurança relacionado à autenticação de um sistema, mas o usuário pode considerar muito trabalhoso sempre se autenticar de 3 formas diferentes. No controle de acesso, regras muito restritas podem dificultar o acesso de pessoas a recursos que elas precisam ter acesso para desempenhar novas tarefas, outrora fora de seu escopo. A gestão de credenciais, se realizada de forma efetiva, é um processo que demanda tempo e pessoas treinadas e disciplinadas para sua execução.

De forma geral, o que podemos refletir é que não há receita pronta para toda e qualquer ameaça à segurança de sistemas da informação (não há bala de prata). Por isso, neste curso é apresentado um método que pode ser aplicado para melhorar a segurança de um sistema da informação, desde o entendimento de sua arquitetura, necessidades e segurança da informação, até priorização por meio da avaliação de risco e reflexão sobre contramedidas efetivas. Porém, é válida a reflexão de que assim como os sistemas são diferentes, são variadas as suas vulnerabilidades e ameaças

**Como aplicar na prática o que aprendeu**

Observe notícias sobre cenários de aplicação das tecnologias emergentes destacadas nesta aula, e associe quais dos desafios levantados fazem sentido para os cenários de aplicação descritos.

O filme “O Jogo da Imitação” também é uma boa referência para ilustrar o uso da criptografia na segunda guerra para garantir a confidencialidade das informações, e como foi feita a análise de cifras alemãs para desvendar o Enigma.

**Conteúdo bônus**

**Tópicos avançados**

Para aprofundar seus conhecimentos sobre Segurança, consulte o livro “Segurança em IoT: Entendendo os Riscos e Ameaças em Internet das Coisas” (MORAES; HAYASHI, 2021). Também há uma palestra online no evento corporativo Mind The Sec sobre o tema (HAYASHI, 2022a).

Um evento acadêmico interessante sobre Segurança da Informação é o Simpósio Brasileiro de Segurança da Informação (SBSeg), onde também há palestras e publicações disponíveis (HAYASHI, 2022b).

Observação: Este conteúdo não será cobrado nas avaliações e estará, obrigatoriamente, presente nas videoaulas. Fique tranquilo(a)!

Referência Bibliográfica

MORAES, A.; Hayashi, V. H. **Segurança em IoT: Entendendo os riscos e ameaças em Internet das Coisas**. São Paulo: Alta Books, 2021.

HAYASHI, Victor. **Desafios de segurança em sistemas de Internet das Coisas (IoT)**. Disponível em: < [https://www.youtube.com/watch?v=AybnhuXK9ME](https://www.youtube.com/watch?v=AybnhuXK9ME)> Acesso em 15/12/2022.

HAYASHI, Victor. **Autenticação não-invasiva para transações financeiras hands-free em locais conectados confiáveis**. Disponível em: <[https://www.youtube.com/watch?v=bYjU8rJtD6Y](https://www.youtube.com/watch?v=bYjU8rJtD6Y)> Acesso em 15/12/2022.