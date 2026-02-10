[[Aula 5 Segurança Endpoint Linux]]

O Linux é um sistema multiusuário, cujas raízes remetem aos sistemas Unix.

O sistema pode ser usado por inúmeros usuários simultaneamente, sem que um atrapalhe as atividades do outro, nem que possa alterar seus arquivos.

# Como manipular usuários e grupos no Linux (Distro usada: Ubunto)

- `Criar usuário`:

Ao entrar no terminal, logue como super usuário digitando o comando `Sudo su`, após isso digite a senha do super usuário, após isso digite o comando `useradd` seguindo na mesma linha com o nome do usuário que você quer criar, no exemplo usarei `Joao`, então ficará na linha: `useradd Joao`.  Será solicitada a criação de uma senha, lembre-se de usar mais de 8 caracteres, não deixar de lado os caracteres especiais e o uso de números para criar essa senha. Após confirmação da senha, está feito, o usuário foi criado.


- `Deletar usuário`:

Para deletar o usuário criado, no nosso exemplo o usuário `Joao`, basta usar o comando `userdel` seguido do nome do usuário que pretende deletar, ficando `userdel Joao`, feito isso o usuário terá sido deletado do sistema.


- `Criar Grupos`:

Para criar grupos, bastará digitar `groupadd` seguido do nome que você quer que o grupo receba, no caso usarei 