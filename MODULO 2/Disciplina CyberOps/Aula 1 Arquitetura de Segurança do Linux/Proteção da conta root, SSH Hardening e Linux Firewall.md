[[Aula 1 Arquitetura de Segurança do Linux]]

# Acesso de root pode gerar problemas:	

 - `Máquinas`: Usuários com acesso root podem abrir buracos na segurança sem saber.
 - `Serviços`: Usuários com acesso root podem rodar serviços inseguros, como FTP  ou Telnet.
 - `Anexando Arquivos em Emails como root`: Apesar de raros, existem vírus de e-mail que afetam o Linux.


# Impedindo acesso do usuário root:

- `Alterar a shell root`: editar `/etc/passwd` e mude `/bin/bash` para `/sbin/nologin`

- `Desativar acessos root via console (tty)`: um arquivo `/etc/securetty` vazio não permite acesso root.

- `Desativar autenticações root SSH`: em `/etc/ssh/sshd_config` com parâmetro `PermitRootLogin > no`

- `Utilizar o PAM e limitar serviços`: `/etc/pam.d/pam_listlife.so`


# 10 Ações para executar SSH Hardening

1 - Permitir acesso SSH apenas a usuários selecionados
2 - Desativar o encaminhamento X11
3 - Mitigar ataques de força brita automaticamente
4 - Desativar o login SSH baseado em senha
5 - Autentificação em dois fatores com SSH
6 - Permitir ae