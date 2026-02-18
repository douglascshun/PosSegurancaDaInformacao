[[Aula 7 Criptografia]]


# Obtenção de certificado digital
![[Processo para obtencao de certificado digital.png]]O processo para a obtenção de um certificado digital consiste um usuário criar em seu computador um par de chaves usando a criptografia assimétrica, ou seja, uma chave privada e uma chave pública. Com a posse de ambas as chaves o usuário leva a sua chave pública até uma Autoridade de Registro (AR/RA), juntamente com dados que comprovem sua autenticidade como RG, CPF e outros documentos pessoais, a Autoridade de Registro valida essas informações e encaminha para uma Certificatge Auhorithy (CA), essa entidade emite um certificado digital e armazena em um diretório para quando houver a necessidade do usuário fazer o uso do certificado digital os dados poderem ser validados, a CA também encaminha de volta a chave pública certificada para o RA que repassa para o usuário. 


# Compras com chaves certificado digital:
![[Compras com chaves certificado digital.png]]
Partindo da situação de que agora o usuário vá comprar em uma loja online, e esse item é caro, como por exemplo um carro de luxo, é bem possível que a loja online solicite uma assinatura digital ao usuário concordar com os termos do contrato de compra, essa assinatura é um dado que a chave privada gera, esse dado é encaminhado para o lojista que verifica a compatibilidade com o resultado do calculo de resultados comparando com a chave pública armazenada no diretório que a CA disponibilizou ao criar o certificado digital.