[[Aula 7 Criptografia]]


# Mensagem Segura e Assinada
Você pode criptografar uma mensagem usando a chave privada. O sentido consistem no fato de que sua chave pública, disponível para qualquer um no mundo acessar, ao você enviar essa mensagem para alguém e esse alguém descriptografar sua mensagem usando a chave pública, você consegue comprovar que essa mensagem foi enviada pelo autor original, ou seja assinar que aquele conteúdo foi enviado por você, objetivo disso não é ser seguro, mas sim autentico. É algo como "de fato foi o Douglas que enviou essa mensagem" por mais que essa mensagem possa ser lida por outras pessoas usando a chave pública.
Se quiser implementar segurança nesse processo, é possível usar a chave pública da pessoa que você está enviando a mensagem e criptografar a sua mensagem antes de enviar, nisso só a pessoa que você enviou a mensagem pode ter acesso ao conteúdo. Como na imagem a seguir:
![[Pasted image 20260218143624.png]]
O Antonio assina usando sua chave privada (onde posteriormente a Paula vai  abrir usando a chave publica de Antonio), Antonio usa a chave publica da pessoa e criptografa (pra quando a mensagem navegar na internet ninguém ter acesso) então você envia, nisso a pessoa usa a chave privada dela pra abrir a mensagem, e depois ela usa a sua chave publica pra abrir a mensagem e obter acesso ao dado original