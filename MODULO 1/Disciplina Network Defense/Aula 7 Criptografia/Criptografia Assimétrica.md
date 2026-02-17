[[Aula 7 Criptografia]]


# Ilustração de Criptografia Assimétrica: 
![[Criptografia Assimetrica.png]]
A criptografia assimétrica vem com o objetivo de resolver um problema existente da criptografia simétrica, na situação da criptografia simétrica precisávamos de um encontro entre o Emissor e o Receptor para compartilharem o código que iria criptografar e descriptografar a mensagem, ou seja em redes isso exponha o risco de alguém interceptar esse momento e obter acesso ao código que trabalha nessa criptografia.

Dada a circunstancias, veio como solução para contornar esse risco o uso de Chaves Públicas e Chaves Privadas. Esses par de chaves são características únicas da criptografia assimétrica, o receptor disponibiliza no canal comprometido, ou seja, onde todos podem ter acesso, uma chave pública, ela é usada para criptografar uma mensagem, onde o emissor carrega a informação com dados e esses dados ficam selados, dentro da chave pública, não podendo ser abertos por ninguém além de quem criou essa chave, pois somente quem criou tem a chave privada que abre essa informação. Isso permite que o emissor entregue de volta em um canal comprometido a informação de forma que quem obtenha ela não consiga ler