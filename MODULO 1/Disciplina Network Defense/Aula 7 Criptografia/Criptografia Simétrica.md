[[Aula 7 Criptografia]]

# Como funcionam as Criptografias Simétricas:
![[Criptografia simetrica.png]]
A Criptografia Simétrica parte do principio de que por mais que a informação trafegue por um canal aberto onde outros agentes possam capturar a informação sendo transmitida, exista uma barreira impedindo que a informação seja entendida, por meio da ocultação onde o emissor e o receptor destinado a receber a mensagem saibam transformar tratar o código da mesma forma. 

Isso se exemplifica da seguinte forma, em um cenário onde há três indivíduos em uma sala a Clara, Ana e Bob. Clara quer falar a quantidade de clientes ativos na empresa para o Bob, sem que Ana tenha acesso a informação confidencial, então Ana e Bob cria uma equação simples para mascarar o número. Supondo que o número original seja 123.123 a Ana multiplica esse número por 2, o que resulta em 246.246. Ana fala para o Bob "olha Bob, o Número de hoje é 246.246", Bob ao escutar esse número divide ele por 2 e chega ao resultado que Ana queria chegar originalmente sem que a Clara saiba qual é esse numero, o que oculta a informação original, mesmo essa informação tendo sida transmitida em um canal aberto.

A criptografia simétrica consiste em que as duas partes tenham acesso ao mesmo algoritmo que embaralha e