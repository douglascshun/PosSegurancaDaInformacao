[[Aula 1 Arquitetura de Segurança do Linux]]

O SHELL é o interpretador de linha de comando, ele funciona como uma interface entre o usuário e o Kernel.

# Conhecendo as estruturas de um terminal Linux:

- Fulano -> nome do usuário logado
-       ~      -> diretório home
-      @     -> separador entre usuário e nome da máquina 
-  deTal  -> nome da máquina 
-       $      -> usuário comum
-       #      -> super usuário (usuário Root)
-        :       -> separador do nome da maquina e do diretório atual


	Para descobrir qual shell tem instaldo na distro atualo comando a seguir deve ser usado:

- cat /etc/shells


# Arquitetura/Camadas do SO Linux
![[Camadas do SO Linux.png]]
Shell: Interface que acessa o Kernel diretamente.



# Principais indicações de Shell

- Zsh
- Terminator
- Bash

# Linguagem de Script:
Um script shell é um programa de computador projetado para ser executado 