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
Esse protocolo é contraponto do TCP, esse por sua vez quebra a confiabilidade, ele não confirma o recebimento de informações, o que por sua vez torna ele mais rápido, permitindo o envio de informações em maior quantidade porém permite um ataque:
### Como funciona o UDP Flood

O objetivo aqui não é esgotar a "memória de conexões" (como no SYN), mas sim **entupir a largura de banda** (bandwidth) e processamento do alvo.

1. O atacante envia uma avalanche de pacotes UDP para **portas aleatórias** no servidor alvo.

2. O servidor recebe o pacote e verifica se alguma aplicação está ouvindo naquela porta.

3. Ao perceber que não há aplicação ali, o sistema operacional do servidor gera um pacote de erro **ICMP "Destination Unreachable"**.

4. **O Resultado:** O servidor fica tão ocupado processando os pacotes inúteis e respondendo com erros ICMP que o link de rede satura e o processador (CPU) trava.
 
# A Variante Perigosa: Ataque de Amplificação

O UDP é o protocolo favorito para ataques de **Amplificação de DNS ou NTP**. Funciona assim:

- O atacante falsifica o IP da vítima (Spoofing).

- Envia uma pergunta pequena para um servidor DNS público ("Me dê a lista completa de registros de tal domínio").

- O servidor DNS responde com um pacote **muito maior** do que a pergunta, mas envia para o IP da vítima.

- Com pouco esforço, o atacante consegue gerar um tráfego de Gigabits por segundo contra o alvo.


### Estratégias de Defesa para UDP

Diferente do TCP, onde os _SYN Cookies_ resolvem muita coisa, o UDP é mais difícil de filtrar porque o tráfego legítimo (como VoIP, streaming e DNS) se parece muito com o ataque.

- **Taxa de Limite (Rate Limiting):** Configurar o roteador ou firewall para descartar pacotes ICMP e UDP se eles ultrapassarem um limite de volume por segundo.

- **Bloqueio de ICMP na Saída:** Impedir que o servidor responda "Destination Unreachable". Isso economiza CPU, embora não salve a largura de banda.

- **Serviços de Scrubbing (Nuvem):** Usar serviços como Cloudflare ou Akamai. Eles recebem todo o tráfego, filtram o que é lixo em uma rede gigantesca e só entregam o tráfego limpo para o seu servidor.

- **Anycast:** Distribuir o tráfego por vários servidores ao redor do mundo para que o ataque seja diluído.
