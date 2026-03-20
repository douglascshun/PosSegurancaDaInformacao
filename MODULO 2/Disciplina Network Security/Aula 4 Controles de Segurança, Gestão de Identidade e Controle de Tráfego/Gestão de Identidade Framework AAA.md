[[Aula 4 Controles de Segurança, Gestão de Identidade e Controle de Tráfego]]

Gestão de identidade é uma forma de gerenciar administrar credenciais (usuário + senha) de forma segura e organizada.

O Framework AAA é uma metodologia é uma estrutura um paradigma de administração de identidades, focando no AAA de: 
- Autenticação
- Autorização
- Auditoria

# Autenticação

- É a identidade de um usuário no sistema.
- Quem é você, seus dados e informações.
- Pode ser composta pelo nome de usuário e senha ou token e senha, ou uma combinação: Usuário, Senha, 2FA.
- É o controle mais implementado

	Ao chegar em uma portaria de prédio, você se apresenta, informa identidade e recebe um crachá. Ou seja, vocês está se autenticando.

Identificação <--> Verificação

- Sabe    =     Senha 
- Possui =     Token
- É           =     Biometria
- Faz       =     Padrão de voz / Assinatura 

# Procolos utilizados para autenticação atualmente: 
- LADP
- WPA / WEP
- OAUTH 2.0
- KERBEROS
- RADIOS
- ikeV2/IPsec

# Autorização

- São seus direitos de acesso em sistema
- Os recursos que você tem previamente estabelecido seja para ler, escrever ou apagar
- O acesso pode ser negado, parcial ou total

	Você informa que deseja cer o presidente da empresa, porém foi estabelecido que você terá acesso somente até a secretária. Você foi autorizado parcialmente.

# Auditoria

- Registra eventos e logs em ordem cronológica para rastreabilidade e investigação posterior.
- Tudo  que você fizer no sistema será monitorado e armazenado para futuras consultas ou investigações.
- Registram datas, horários, credenciais, acessos e alterações no sistema.

	Durante seu trajeto, você passou o crachá na catraca que registrou a data e hora de entrada, vinculando o ID do crachá a sua identidade e sua movimentação foi registrada pelo CFTV.

# Gestão de Identidade Framework AAA

- Autenticação:
Credencial do Active Directory Domains Service; Usuário e senha

- Autorização:
Nível do Usuário; Permissões em pastas do FileServer ou sistema que tenha integrado LADP

- Auditoria:
No Windows, você pode utilizar o Event Viewer para verificar logs e eventos ocorridos no SO