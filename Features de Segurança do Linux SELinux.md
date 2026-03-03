[[Aula 1 Arquitetura de Segurança do Linux]]

De acordo com o Debian HandbookSELinix, Security Enhanced Linux é um sistema de controle de acesso obrigatório construído sobre a interface LSM (Linux Security Modules) do Linux. Na prática, o kernel consulta o SELinux antes de cada chamada do sistema para saber se o processo esta autorizado a fazer a operação dada.

SELinuz estabelece:
- Autoriza/proíbe operações
- Gestão de permissões

# Contexto de segurança/usuários
O contexto é definido pela identidade do usuário que iniciou o processo, o papel e o domínio que o usuário realizará naquele momento.

Os diretos realmente dependem do domínio, mas transições entre os domínios são controladas pelos papéis. 
Transições possíveis entre os papéis dependem da identidade.

# Configurando o SELinux
- apt install selinux-basics selinux-policy-defalti auditd
- somedule: habilita módulos
- semanage: permissões aos usuários
- /etc/selinux/default (onde fica todas essas regras)

# Módulos SELinux disponíveis são armazenados no 