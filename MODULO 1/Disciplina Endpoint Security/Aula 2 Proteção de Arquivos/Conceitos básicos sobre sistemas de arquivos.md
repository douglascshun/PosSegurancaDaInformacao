[[Aula 2 Proteção de Arquivos]]

## Sumário

# 1 - Conceitos básicos sobre sistemas de arquivos
O que é e como funciona um sistema de arquivos?

## 2 -Criptografia de arquivos
Conceito de criptografia.

## 3 - Controles de acesso 
Como controlar o acesso dos usuários?

## 4 - Controle de integridade, Hash
Como funciona a Hash?

## 5 - Certificados digitais
Como funciona os certificados digitais?

## 6 - Backup e restore 
A importância do backup e restore.



# Conceitos básicos sobre sistemas de arquivos

Na prática, um sistema de arquivo (file system, do inglês) é um conjunto de estruturas lógicas, ou seja, feitas diretamente via software, que permite ao sistema operacional ter acesso e controlar os dados gravados no disco.

`É criado durante o processo de formatação de uma partição!`

# Funções dos sistemas de arquivos

- Gerenciamento do espaço
- Organização de arquivos e diretórios
- Permissão e restrição de acessos
- Busca e recuperação de dados

`Gerenciamento do espaço`: Um exemplo disso é dividir/particionar um HD de 1 TB em duas partições de 500GB.


`Organização de arquivos e diretórios`: Criar pastas e acessos para viabilizar e facilitar a navegação entre as informações.

`Permissão e restrição de acessos`: Posso criar níveis de permissão, onde só quem é de determinado cargo ou função acessa, exemplos como só o pessoal do RH pode ver dados sensíveis de outros funcionários, só o pessoal da diretoria poder acessar documentos de valor da empresa.

`Busca e recuperação de dados`: Dependendo do sistema de arquivo, existir uma forma de recuperação e busca dos dados.


## Exemplo de sistemas de arquivos:

- FAT12, FAT16, FAT32
- NTFS
- ext2, ext3, ext4
- ZFS
- HFS, HFS+
- UDF


# FAT
A sigla FAT significa FIle Allocation Table (Tabela de Anotação de arquivos), sistema esse quer era comumente utilizado em disquetes.

`FAT normalmente é utilizado quando se tem um numero grande de informação para ser processada naquele disco, fácil de trabalhar fácil de formatar, porém fácil de dar problema.`

# NTFS
O NTFS (New Technology File System) é o sistema de arquivos padrão para o Windows NT e seus derivados.

# Outros exemplos de sistemas de arquivos

- Sistemas de arquivos de rede - NFS, AFS
- Sistemas de arquivos de bando de dados
- Sistemas de arquivos de dispositivos - devfs udev
- Sistemas de arquivos fita -LTFS

