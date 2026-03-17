[[Aula 2 Proteção de Arquivos]]

O processo de certificação digital se dá por meio de uma espécie de "selo de confiabilidade", denominado `certificado digital`, que é concedido por uma autoridade certificadora a uma pessoa física ou jurídica.

A intenção dessa certificação é garantir a autenticidade, a confidencialidade e a integridade às informações eletrônicas que estão transmitindo no universo cibernético.

`Um exemplo disso é o acesso do site da receita federal onde o acesso normalmente é atrelado ao CPF da pessoa.`

A maneira como o certificado digital comprova a identidade de alguém ou de uma empresa é praticamente inviolável, sendo aceita legalmente.

O sistema utiliza um par de chaves criptográficas que nunca se repete:
as chaves privadas e as chaves públicas.

A `chave privada` serve para criptografar dados que atestam a identidade sobre a pessoa ou a empresa, seja para acessar um sistema, seja para assinar um documento eletrônico. Só conhece essa chave quem está autorizado a usar o certificado que a gerou.

Já a `chave pública` é compartilhada com que precisa decodificar a criptografia das informações que atestam a identidade para que seja reconhecida e aceita. A chave só serve para decodificar o que foi criptografado usando a chave privada criada junto dela.

Para validar uma assinatura digital, o certificado vincula a ela um arquivo eletrônico com dados sobre a pessoa e/ou empresa para atestar a quem ela pertence e que foi feita por quem pode utilizá-la legalmente. 

Tanto a assinatura digital quanto esse arquivo são protegidos por criptografia pelo certificado digital, que precisa, obrigatoriamente, ter sido emitido por uma autoridade certificadora credenciada pelo Instituto Nacional de Tecnologia da Informação - ITI.

# Certificados digitais permitem:
- Assinar documentos digitais
- Acessar sistemas com dados restritos
- Trabalhar em sistemas virtuais

