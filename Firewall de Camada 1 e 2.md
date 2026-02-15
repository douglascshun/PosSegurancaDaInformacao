[[Aula 5 Firewalls]]


# Camada 1:
Camada 1 é constituída pela parte físcia, ou seja cabos de redes e portas, onde posso saber se a porta do cabo de rede está ligada ou desliga, consigo também saber se há a transmissão de energia elétrica por esse cabo. Esses são alguns parâmetros que se é possível medir na camada um, com esses parâmetros pode-se implementar um firewall que detecta se a porta está ligada ou desligada, no caso dela não dever estar ligada esse firewall bloqueia aquela porta.

![[Camada 1 portas.png]]



# Camada 2:
A camada 2 diferencialmente da camada 1, tem a capacidade de ler dados lógicos por atuar com endereçamento e MAC, pode-se também efetuar a leitura de dados binários, com base nisso é possível saber a origem e o destino dos pacotes para filtrar o que é desejado, e o que não for, aplicar filtros dentro dos caminhos da rede, por exemplo bloqueando endereços MAC que não existem dentro da minha tabela de endereços MAC dos dispositivos na rede. Na camada 2 também existe a Class of Service ou seja Classe de Serviço, o switch pode com isso analisar e definir prioridade em serviços

![[Camada 2.png]]