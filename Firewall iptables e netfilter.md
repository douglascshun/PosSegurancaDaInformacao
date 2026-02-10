[[Aula 5 Segurança Endpoint Linux]]

# O que e como funcionam ?


# Iptables:

`Iptables` é um código de firewall das versões 2.4 do kernel, que substituiu o ipchains (Presente nas séries 2.2 do Kernel). Ele Foi incluído no kernel na série 2.4 em meados de Junho/Julho de 1999.

O iptables não é essencialmente um firewall, mas um programa que, por meio de seus módulos, possibilita ao usuário configurar o kernel Linux e o conjunto de regras do filtro de pacotes - função típica do firewall.

Na prática, o administrador de sistemas tem de gerenciar quatro tabelas (Filter, NAT, Mangle e Security) com funções distintas e, com isso, aplica as regras desejadas.

Como a interação ocorre quase diretamente com o Kernel, praticamente não há limites quanto à aplicação de regras via ipatables.

`Exemplo de uso:` Na empresa não se poderá usar rede sociais, o iptable gera uma tabela com os principais sites bloqueando o acesso de redes como Instagram, X, Facebook..