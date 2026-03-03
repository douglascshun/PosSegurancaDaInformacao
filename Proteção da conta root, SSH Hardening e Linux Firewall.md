[[Aula 1 Arquitetura de Segurança do Linux]]

Acesso de root pode gerar problemas:	
 - `Máquinas`: Usuários com acesso root podem abrir buracos na segurança sem saber.
 - `Serviços`: Usuários com acesso root podem rodar serviços inseguros, como FTP  ou Telnet.
 - `Anexando Arquivos em Emails como root`: Apesar de raros, existem vírus de e-mail que afetam o Linux.


Impedindo acesso do usuário root:
- `Alterar a shell root`: editar `/etc/passwd` e mude `/bin/bash` para `/sbin/nologin`
- Desativar acessos root via console (tty): um arquivo `/etc/securetty` va