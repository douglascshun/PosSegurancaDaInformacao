[[Aula 1 Arquitetura de Segurança do Linux]]

Em sistemas UNIX ou GNU/Linux, arquivos de log são compostos de informações em texto puto e são continuamente acrescidos de novas informações.

# Usando o Tail para monitorar logs: 
O tail é um dos comandos clássicos usados para monitorar alterações em arquivos no sistema, o que inclui arquivos de log, atente-se que o tail lê apenas o final do arquivo.

# Alguns exemplos para o aplicativo tail:

- tail -f meuarquivo.log | grep -qx "Finished: SUCCESS"
Serve para monitorar o sucesso de uma determinada operação, como rede e outros arquivos

- tail arquivo.txt -n 15
Parâmetro "- n X" define a quantidade de linhas que você quer ler do arquivo. 

- tail -f access.log | grep 192.168.0.1


# Monitoramento ACLs

ACLs são utilizadas para obter controle mais refinado das permissões do sistema de arquivos do Linux

Entre os desafios de administrar o Linux no ambiente de negócios moderno, está a expectativa de que podemos e devemos gerenciar quem tem acesso a quais informações.



O sistema de arquivos Linux nos dá três tipos de permissões. Aquis está uma revisão simplificada:
- User (or user owner)
- Group (or owner group)
- Other (everyone else)

Com essas permissões, podemos conceder três (na verdade, cinco) tipos de acesso:
- `R`ead
- `W`rite
- e`X`ecute

Segue o panorama dos privilégios: 
![[Pasted image 20260303194421.png]]
