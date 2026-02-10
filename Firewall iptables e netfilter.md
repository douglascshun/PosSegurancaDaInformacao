[[Aula 5 Segurança Endpoint Linux]]

# O que e como funcionam ?


# Iptables:

`Iptables` é um código de firewall das versões 2.4 do kernel, que substituiu o ipchains (Presente nas séries 2.2 do Kernel). Ele Foi incluído no kernel na série 2.4 em meados de Junho/Julho de 1999.

O iptables não é essencialmente um firewall, mas um programa que, por meio de seus módulos, possibilita ao usuário configurar o kernel Linux e o conjunto de regras do filtro de pacotes - função típica do firewall.

Na prática, o administrador de sistemas tem de gerenciar quatro tabelas (Filter, NAT, Mangle e Security) com funções distintas e, com isso, aplica as regras desejadas.

Como a interação ocorre quase diretamente com o Kernel, praticamente não há limites quanto à aplicação de regras via ipatables.

`Exemplo de uso:` Na empresa não se poderá usar rede sociais, o iptable gera uma tabela com os principais sites bloqueando o acesso de redes como Instagram, X, Facebook e Reddit. Posso bloquear portas na tabela de cada usuário.

# Netfilter

O Netfilter é um módulo que fornece ao sistema operacional Linux as funções de firewall, NAT e log dos dados que trafegam por rede de computadores de funcionalidades do netfilter.

O IP tables é o nome da ferramenta que permite a criação de regras de firewall e NAT's. Apesar de, tecnicamente, ser apenas uma ferramenta que controla o módulo netfilter, o nome "IPtables" é frequentemente utilizado como referência ao conjunto completo de funcionalidades de netfilter.


# Implementar

Iniciar um por meio de definições conversadas diretamente com a empresa, um conjunto de regras que impedem e definem o que pode ser potencialmente arriscado de se acessar dentro da empresa.

Após o norte de regras serem discutidos, destrinchar o conteúdo e definir o que pode ser cortado ou implementado, e posteriormente configurar regra a regra manualmente com cautela. 

# Dica:

Existe uma documentação hospedada em um site chamado netfilter.org, onde por meio desse é possível ter um passo a passo de regras a serem definidas e como configura-las.

Outro site que pode ajudar é o linux.die.net, site esse que hospeda toda a documentação de como definir as regras e configurar as tabelas