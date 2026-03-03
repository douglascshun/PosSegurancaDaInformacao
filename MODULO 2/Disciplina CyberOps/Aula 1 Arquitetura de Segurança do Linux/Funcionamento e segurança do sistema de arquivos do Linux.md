[[Aula 1 Arquitetura de Segurança do Linux]]

O Linux é um sistema operacional multiusuário, usuários podem utilizar o sistema operacional ao mesmo tempo, sem que seus arquivos e personalizações estejam acessíveis a outros usuários.
	Destaque:
	- Controle de permissão
	- Controle de privilégio

O usuário root é o principal/administrador de um sistema linux e é o único com permissão total de manipulação.

- Usuário: /etc/passwd
- Grupos do sistema: /etc/group
- cada usuário e gripo possuem um numero único associado, chamado respectivamente de UID e GID.
- comandos: who

Exemplo
![[search user.png]]
- Nome de Login
- Senha ('x' quando usando o arquivo /etc/shadow).
- Numero de identificação do usuário (UID).
- Numero do grupo do usuário (opcional).
- Diretório pessoal para o usuário.
- Shell inicial do usuário (se vazio, o arquivo padrão /bun/sh será usado).




# Hierarquia do sistema linux no diretório raiz
![[Hierarquia do sistema linux no diretório raiz.png]]


# Exemplo de captura de níveis de permissão
![[captura de niveis de permissao.png]]

Para arquivos e diretórios, há três níveis de permissão:

- U
