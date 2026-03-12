[[CyberOps]]
Os algoritmos de criptografia são indispensáveis para quem procura impedir o acesso ilegal a dados corporativos, uma vez que eles usam chaves de segurança que permitem verificar a validade de uma  informação.

	Essa verificação pode ser por
	- Chave Simétrica
	- Chavebe Assimétrica

O ciframento simétrico de uma mensagem (processo em que m conteúdo é criptografado) é baseado em 2 componentes:

		Um algoritmo
								    = Criptografia simétrica 
		uma chave de segurança


# Algoritmo DES - Simétrico

Um algoritmo baseado em data encryption standard (DES ou padrão de criptografia de dados em tradução livre)

	Tem 56 bits, o que permite a criação de 72 quadrilhões de chaves diferentes.

# Algoritmo RC2 - Simétrico

Um sistema que utiliza o protocolo S/MIME

	Tem uma chave de tamanho variável. Ela pode ter entre 8 e 1.1240 bitis.
	
	Assim, as chances de alguém conseguir decifrar um conteúdo criptografado por meio de algortimos de força bruta diminuí consideravelmente.

# Criptografia simétrica 

Basicamente esta criptografia transforma um texto claro em texto cifrado, utilizando uma chave secreta e um algoritmo de criptografia.

Utilizando a mesma chave e um algoritmo de criptografia, é possível reverter o texto cifrado para o texto claro.

![[Criptografia simétrica.png]]


# Algoritmo RSA - Assimétrico

Um dos principais algoritmos que utiliza esse tipo de técnica é o RSA. 

	Ele é baseado na multiplicação de números primos de grande escala para geração de uma chave pública.
	
	Caso o número seja bem escolhido, o tempo necessário para a quebra de uma chave pode se tornar consideravelmente grande.

Em 1999, o Instituto Nacional de pesquisa da Holanda promoveu um trabalho com cientistas de 6 países.

Com 300 computadores e 7 meses de trabalho, foi possível quebrar uma chave RSA com 512 bits.

![[Pasted image 20260312114054.png]]