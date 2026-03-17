[[Network Defense]]

## Criptografia

**Introdução**

O objetivo deste módulo é entender o que é a criptografia, como pode ser implementada e como é usada para garantir a privacidade.

**Objetivos da aula**

- O que é Criptografia?
- Criptografia Simétrica e Assimétrica
- Chaves Criptográficas Públicas e Privadas
- Aplicações de Criptografia

**Resumo**

Vamos entender os componentes que constituem os elementos específicos de uma comunicação.

A comunicação sempre ocorre entre, no mínimo, dois atores.

Sendo o primeiro deles o **emissor** - aquele que transmite a mensagem.

O segundo é o **receptor** -  aquele que recebe a mensagem.

Como citado, temos uma **mensagem** - é tudo aquilo que o emissor quer enviar ao receptor.

Precisamos também de um **Canal** de comunicação – é o meio pelo qual é transmitida a mensagem, podendo ser pelo meio eletrônico, rádio, etc, ou seja, precisamos de um canal por onde esta mensagem será transmitida.

Emissor e receptor devem combinar um **código** - conjunto de sinais utilizados na comunicação para transmitir a mensagem, podendo ser de várias maneiras.

Com todos os elementos citados, a comunicação pode ocorrer e o emissor pode codificar uma mensagem, enviá-la por um canal até chegar ao receptor que ao receber consegue decodificar a mesma.

![Fonte: Autoria Própria, 2023.](https://paperx-dex-assets.s3.sa-east-1.amazonaws.com/images/1678143667844-eLgEwc4tFZ.png "Fonte: Autoria Própria, 2023.")

Fonte: Autoria Própria, 2023.

Qual o grande problema disso? Onde está o risco deste processo?

E se tivermos uma terceira pessoa? Alguém que tenha acesso ao canal de comunicação e conheça o código utilizado no canal? O que vai acontecer?

A pessoa vai ter acesso às mensagens e ouvi-las, pois a mensagem vai passar por ela.  E se o emissor não quiser que a mensagem seja interceptada? O que ele poderá fazer?

A solução é a criptografia. E o que seria esta criptografia? O Emissor deve embaralhar, mandar a mensagem de uma maneira que um terceiro não entenda o que está escrito, mas de forma que o receptor consiga ler.

![Fonte: Clube dos Geeks, 2014.](https://paperx-dex-assets.s3.sa-east-1.amazonaws.com/images/1678143694103-Z8X9QZfB4g.png "Fonte: Clube dos Geeks, 2014.")

Fonte: Clube dos Geeks, 2014.

Segundo Suetônio, Júlio César (Imperador Romano) utilizava uma técnica de criptografia para se comunicar com seus generais. Esta técnica ficou conhecida como cifra de César. Era composta de um anel, que tinha o alfabeto escrito em dois círculos, um interno e outro externo. Para cada general havia um anel diferente. O Imperador Romano dava uma destas cifras, que eram utilizadas para a comunicação que deveria ser secreta.

Embora César seja a primeira pessoa conhecida a usar esse sistema, outras cifras de substituição provavelmente foram usadas antes. 

Esse sistema era muito simples e consistia em substituir as letras na hora de escrever a mensagem, onde o emissor deveria, sempre que quisesse escrever uma letra, verificar no círculo interno e substituir pela correspondente no círculo externo. O receptor deveria fazer o processo inverso, verificar a letra no círculo externo e substituir no interno.

Com isso, a mensagem que César queria mandar para o General era ATAQUE, mas ao invés de escrever essa palavra em um bilhete, que poderia ser lido e interceptado no caminho, tendo a certeza de que a mensagem só pode ter vindo daquele usuário, ele mandava uma mensagem escrito ZSZPTD. Qualquer um que lesse não entenderia o que se tratava, mas ao chegar a mensagem no general, ele utilizaria o anel para decodificar. De forma que Z no círculo externo representava a letra A no círculo interno, S no círculo externo representava a letra T no círculo interno, P representa Q, T representava U e D representava E.

Assim, o general conseguiria saber que a mensagem era para ATACAR e que teria vindo de César e não escrita por qualquer outra pessoa.

Não se sabe o quão eficaz a cifra de César, realmente, era na época, mas deve ter sido razoavelmente segura, pois poucos dos inimigos dele seriam capazes de ler, muito menos realizar a criptoanálise necessária. Supondo que o invasor possa ler a mensagem, não há evidências de que existam técnicas para contornar esse tipo de criptografia.

Hoje, a descriptografia da cifra de Júlio César pode ser feita facilmente, mesmo que apenas um pequeno texto cifrado esteja disponível.

Curiosamente, refere-se ainda que o chefe da máfia, Bernardo Provenzano, recentemente detido, costumava comunicar, em pleno século XXI, notas escritas na máquina de escrever, codificadas com o uso deste algoritmo rudimentar, negando qualquer nova tecnologia como o celular ou a Internet. Apesar da natureza rudimentar do sistema, ele conseguiu manter a polícia confusa por anos.

Contudo, o importante é entender que a criptografia é uma técnica ou um conjunto de técnicas que foram pensadas para proteger a informação de maneira que apenas o emissor e receptor sejam capazes de compreendê-la.

Temos basicamente dois tipos de criptografia: a simétrica que utiliza uma única chave tanto para efetuar a criptografia quanto para executar o processo inverso (descriptografar). E a assimétrica que tem duas chaves: uma para criptografar e outra para descriptografar.

![Fonte: Autoria Própria, 2023.](https://paperx-dex-assets.s3.sa-east-1.amazonaws.com/images/1678143731904-iLfZFqFqFX.png "Fonte: Autoria Própria, 2023.")

Fonte: Autoria Própria, 2023.

Joana se encontra com Jonas sem a presença de Carla e combina que sempre que tiver que mandar uma mensagem e Carla estiver na sala, mandará a quantidade multiplicada por 2. Assim, basta Jonas dividir o valor por dois e terá o valor correto.

- Carla chega na sala.

- Jonas pede o número total de clientes para a Joana.

- Joana verifica que são 123123.

- A chave criptográfica é multiplicar por 2.

- Joana aplica a criptografia na mensagem.

- A mensagem agora ficou 246246. Assim, ela é enviada pelo canal para Jonas. Carla ouve e pensa que a empresa tem 246246 clientes.

- A mensagem que chega para Jonas é 246246, mas ele tem uma criptografia combinada com Joana e é só aplicar a operação inversa com o mesmo valor, ou seja, dividir 246246 por 2.

- Mensagem correta 123123 clientes.

  
Esse foi um exemplo de criptografia simétrica, onde o mesmo algoritmo é usado em ambas as pontas. O grande problema deste sistema é que Jonas e Joana precisaram se encontrar em particular para combinar esta criptografia, longe dos olhos de Carla. Como fazer isso é o grande X da questão. Como podem trocar esta chave secreta? Tudo bem que uma vez trocada a chave, a comunicação entre eles pode ser criptografada e se tornará segura, mas se eles estão na mesma sala que Carla, e combinarem este código, ela vai ouvir e de nada vai servir, pois se Carla descobre o código, o sigilo estará perdido, já que ela também será capaz de descriptografar a mensagem. Portanto, a grande dificuldade deste método é garantir a troca de chaves de forma segura, algo que não consegue responder de forma satisfatória. Como distribuir a chave secreta que precisa ser distribuída por um canal de comunicação inseguro?

Uma das principais vantagens da criptografia simétrica é a facilidade para configurar, além da simplicidade e implementação. 

![Fonte: Autoria Própria, 2023.](https://paperx-dex-assets.s3.sa-east-1.amazonaws.com/images/1678143756504-Rqm0dv8pNk.png "Fonte: Autoria Própria, 2023.")

Fonte: Autoria Própria, 2023.

O sistema de chaves criptográficas assimétricas resolvem o problema da troca de chaves que vimos no exemplo anterior. Naquele caso, a chave que criptografava e descriptografava era exatamente a mesma, no caso, o 2. Aqui, já temos um sistema que usa duas chaves, uma para criptografar, que chamamos de chave pública, podendo ser distribuída livremente pela Internet ou qualquer outro canal por mais inseguro que seja, pois ela só serve para criptografar uma mensagem para um destino específico. Já o processo de descriptografar só pode ser feito por uma outra chave que chamo de privada e só o destino a possui.

Assim, Jonas pode enviar sua chave pública para Joana pelo canal, sem a preocupação de Carla ouvir, pois com esta chave ela não é capaz de descriptografar as mensagens.

Com isso, Joana aprende a chave pública de Jonas, ou seja, a chave de criptografia de Jonas e a utiliza para criptografar a mensagem que quer mandar para ele. Enquanto a Carla ouve a mensagem, mas não tem a chave de descriptografia, apenas a de criptografia que não serve. Ao chegar a mensagem até Jonas, basta ele utilizar sua chave de descriptografia e conseguirá ler a mensagem enviada por Joana.

![Fonte: Autoria Própria, 2023.](https://paperx-dex-assets.s3.sa-east-1.amazonaws.com/images/1678143783741-z1tVM3Zc1q.png "Fonte: Autoria Própria, 2023.")

Fonte: Autoria Própria, 2023.

O usuário, no seu computador, gera duas chaves criptográficas assimétricas, sendo uma pública ou de criptografia e outra privada de descriptografia. Ele envia a chave pública para um RA - _Registation Authority._ Serão enviadas as suas informações pessoais e a chave pública. O Registration Authority verifica as informações e solicita a emissão do certificado para o CA - _Certification Authorities_. Depois de emitir o certificado, divulga em um diretório público e o remete para o RA, que envia o certificado para o usuário.

![Fonte: Autoria Própria, 2023.](https://paperx-dex-assets.s3.sa-east-1.amazonaws.com/images/1678143811483-CCAbU5LgpM.png "Fonte: Autoria Própria, 2023.")

Fonte: Autoria Própria, 2023.

Um usuário quer fazer uma compra com um lojista online. Para isso, ele usa o seu computador para acessar esta loja. Para confirmar a identidade do usuário, ele troca mensagens assinadas por ele, ou seja, criptografa com sua chave privada, como o lojista. Este lojista, para verificar a identidade do usuário, vai ao diretório, que é um servidor que armazena as chaves públicas das pessoas e quem alimenta este diretório é um CA. Quando o lojista encontra no diretório a chave pública daquele usuário, e usando ela consegue descriptografar a mensagem, tem a certeza de que a mensagem só pode ter vindo daquele usuário. Agora, eles podem trocar uma chave criptográfica simétrica, por ter um custo computacional menor e estabelecer uma conexão criptografada e segura onde a identidade do usuário foi confirmada.

![Fonte: Autoria Própria, 2023.](https://paperx-dex-assets.s3.sa-east-1.amazonaws.com/images/1678143829761-5O0oxvawfw.png "Fonte: Autoria Própria, 2023.")

Fonte: Autoria Própria, 2023.

Antônio tem a sua chave privada e quer se comunicar com Paula. Ela também tem sua chave privada. Antônio tem a chave pública de Paula que está disponível na internet, enquanto Paula também tem a chave pública de Antônio. Como Antônio quer mandar uma mensagem segura e assinada, ele pega a mensagem e criptografa com a sua chave privada, de forma que só a chave pública dele que qualquer um tem, pode ser usada para descriptografar. Isso se chama assinar a mensagem, ou seja, criptografar com a sua chave privada. Porém, se a mensagem fosse enviada dessa forma pela internet, qualquer um poderia ler o que está escrito, pois todos têm a chave criptográfica pública de Antônio. Porém, Antônio quer que apenas Paula seja capaz de ler a mensagem. Então, ele novamente criptografa a mensagem com a chave pública de Paula que todos têm, mas para descriptografar só Paula consegue, pois só ela tem a chave privada. Esta mensagem é enviada pela internet. A mensagem chega para Paula, que aplica sua chave privada e descriptografa a mensagem, mas ela ainda é ilegível. Agora, Paula aplica a chave Pública de Antônio, e a mensagem se torna legível, mostrando que quem gerou a mensagem foi Antônio. Este foi um exemplo de uma mensagem segura e assinada.

**Conteúdo bônus**

**Tópicos avançados**

Os sistemas de criptografia e certificação digital já estão ao alcance de todos. No Brasil temos um sistema aceito pelo governo federal, chamado e-CPF. Através dele podemos assinar digitalmente documentos públicos. Se quiser se aprofundar no assunto, sugiro que visite os sites a seguir:

[https://www.gov.br/iti/pt-br/assuntos/icp-brasil](https://www.gov.br/iti/pt-br/assuntos/icp-brasil)

[https://www.certisign.com.br/certificado-digital](https://www.certisign.com.br/certificado-digital)

[https://www.autenticacao.gov.pt/assinatura-digital/assinatura-digital-qualificada](https://www.autenticacao.gov.pt/assinatura-digital/assinatura-digital-qualificada)

[https://letsencrypt.org/](https://letsencrypt.org/)

Referência Bibliográfica

BENANTAR, Messaoud. **Introduction to the public key infrastructure for the Internet.** Upper Saddle River, N.J.: Prentice-Hall : PTR, 2002.

CORDEIRO, Luiz Gustavo. **Certificação digital: conceitos e aplicações: modelos brasileiro e australiano.** Rio de Janeiro: Ciência Moderna, 2008.

CHAPMAN D. BRENT; ZWICKY, ELIZABETH D. - **Building Internet Firewalls.** O’Reilly & Associates Inc., 2st Edition, 2000.

KIZZA, Joseph Migga. **Computer network security and cyber ethics.** 4nd ed. Jefferson: McFarland & Company, 2014.

KUROSE, James F.; ROSS, Keith W. **"Computer Networking"**, Pearson Education, 2012.

MENEZES, Josué das Chagas. **Gestão da segurança da informação.** Leme: J. H. Mizuno, 2006.

STALLINGS, W; **"Cryptography and Network Security";** Prentice Hall, 4th Edition, 2005.

STALLINGS, William. **Criptografia e segurança de redes: princípios e práticas**. São Paulo: Pearson Education do Brasil, 2010.

STINSON, D.; **Cryptography Theory and Practice - CRC Press**, ISBN: 1-584- 88508-4, 2005;

TANENBAUM, Andrew S.; FEAMSTER, Nick; WETHERALL, David J.; **Computer Network**. Rio de Janeiro: Pearson, 2020.