[[Aula 1 Arquitetura de Segurança do Linux]]

Em sistemas UNIX ou GNU/Linux, arquivos de log são compostos de informações em texto puto e são continuamente acrescidos de novas informações.

# Usando o Tail para monitorar logs: 
O tail é um dos comandos clássicos usados para monitorar alterações em arquivos no sistema, o que inclui arquivos de log.

# Alguns exemplos para o aplicativo tail:

- tail -f meuarquivo.log | grep -qx "Finished: SUCCESS"
Serve para monitorar o sucesso de uma determinada operação, como rede 

- tail arquivo.txt -n 15


- tail -f access.log | grep 192.168.0.1