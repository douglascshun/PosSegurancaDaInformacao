[[Aula 3 Técnicas para proteção de redes]]

# TCP:

A Característica desse protocolo é a confiabilidade. Ele ele envia um pacote ao destino procurando saber principalmente duas informações, sendo elas saber se o destino é valido como se o dispositivo está ligado e pode ser acessado, e também se o dispositivo tem condições de processar a informação que será recebida, ou seja, se ele não está sobrecarregado com outros processos. Esse dispositivo que receberá o pacote mencionado chamado de SYN, ira reservar um espaço de memória e processamento para garantir que ira conseguira receber as informações do servidor.
	**No SYN Flood:** O atacante envia milhares de pacotes **SYN**, mas com endereços de IP falsificados (spoofed) ou simplesmente **nunca envia o último ACK**. O servidor fica "pendurado", esperando uma resposta que nunca vem, mantendo as portas abertas e consumindo toda a memória e recursos (a chamada _backlog queue_). Quando a fila enche, o servidor para de aceitar conexões legítimas.
	
### Estratégias de Mitigação

Se você está configurando um firewall ou um servidor para se defender disso, aqui estão as principais armas:

- **SYN Cookies:** É a defesa mais comum. O servidor não reserva recursos imediatamente. Ele envia o SYN-ACK com um "número de sequência" especial. A memória só é alocada se o cliente responder com o ACK correto.

- **Redução do Timeout:** Diminuir o tempo que o servidor espera pelo ACK final antes de descartar a conexão semiaberta.

- **Reciclagem de Conexões TCP semiabertas:** Forçar o descarte das conexões mais antigas para dar lugar a novas.

- **Filtros de Firewall/IPS:** Bloquear IPs que estão disparando requisições em uma velocidade anormal ou usar firewalls que fazem o "proxy" do handshake (o firewall completa o handshake antes de passar para o servidor real).


# UDP: 
Esse protocolo é contraponto do TCP, esse por sua vez quebra a confiabilidade, ele não confirma o recebimento de informações, o que por sua vez torna ele mais rápido, permitindo o envio de informações em maior quantidade porém permite um ataque 