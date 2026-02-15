[[Aula 5 Firewalls]]


# Camada 1:
Camada 1 é constituída pela parte físcia, ou seja cabos de redes e portas, onde posso saber se a porta do cabo de rede está ligada ou desliga, consigo também saber se há a transmissão de energia elétrica por esse cabo. Esses são alguns parâmetros que se é possível medir na camada um, com esses parâmetros pode-se implementar um firewall que detecta se a porta está ligada ou desligada, no caso dela não dever estar ligada esse firewall bloqueia aquela porta.

![[Camada 1 portas.png]]



# Camada 2:
A camada 2 diferencialmente da camada 1, tem a capacidade de ler dados lógicos por atuar com endereçamento e MAC, pode-se também efetuar a leitura de dados binários, com base nisso é possível saber a origem e o destino dos pacotes para filtrar o que é desejado, e o que não for, aplicar filtros dentro dos caminhos da rede, por exemplo bloqueando endereços MAC que não existem dentro da minha tabela de endereços MAC dos dispositivos na rede. Na camada 2 também existe a Class of Service ou seja Classe de Serviço, o switch pode com isso analisar e definir prioridade em serviços, analisar também congestionamento na rede, descartar preferencialmente um pacote em relação ao outro, ou seja aplicar políticas que podem melhorar a segurança da rede. 

![[Camada 2.png]]

Ataques na camada 2, existem ataques exclusivos para a camada 2 onde só podem ser evitados com a implementação de firewall na mesma, um desses é o ataque de DHCP onde se tem o DHCP Spoofing, outro é o ARP Spofing, um roteador não tem a capacidade de bloquear esse tipo de ataque.

# ARP Spoofing (Envenenamento de Cache)
O protocolo ARP (Address Resolution Protocol) é o que traduz um endereço IP em um endereço MAC (físico). O problema? Ele é "confiado": se alguém enviar uma resposta ARP dizendo "Eu sou o roteador", o seu computador acredita sem questionar.

### Como acontece:

1. O atacante envia mensagens ARP falsas para o seu PC, dizendo que o MAC do atacante pertence ao IP do roteador.
    
2. Ao mesmo tempo, ele diz ao roteador que o MAC dele pertence ao IP do seu PC.
    
3. **Resultado:** Todo o tráfego que deveria ir para o roteador passa primeiro pela máquina do atacante.
    

- **Principal Risco:** Roubo de credenciais em sites sem HTTPS e monitoramento de atividades.