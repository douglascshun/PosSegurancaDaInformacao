[[Aula 1 Monitoramento de redes]]

## Camada 7 - Aplicações

- `HTTP`
Um exemplo é a quantidade de requisição pois se as requisições de acesso ao meu servidor forem maior do que a quantidade permitida e configurada o servidor começará a apresentar problemas

- `DNS`
Segue o mesmo principio pois também é necessário um servidor para fazer a transformação de IP (192.168.x.x) em um WWW da vida.
 
- `SSH`
Monitorar acessos indevidos pois o SSH assim com o TELNET é um protocolo para acessar dispositivos, acessos indevidos podem ser bloqueados e mitigados com o monitoramento desse recurso 

- `E-mail`
O e-mail diferente dos anteriores é tolerante a atrasos, porém pode-se ter como implemento o monitoramento de Spam.

- `SIP`
O protocolo que faz voIP, se monitorado é possível prever quedas em serviços de telefone IP.


# Camada 6 - Apresentação

- `TLS`
- `SSL`

A camada que principalmente faz a criptografia dos dados, o TLS e SSL são dois protocolos que exercem esse papel, sendo o TLS mais antigo o SSL mais novo. se é possível implementar o monitoramento de certificados, vendo se quem os assinou, qual a origem, o que sendo o caso abriria um vetor de ataque ao atacante se os certificados forem negligenciados.


# Camada 5 - Sessão

- `SCP`
Uma página HTTP, não tem uma conexão solo, ela tem várias conexões dento da página como, Banner, Videos.. muitas vezes  cada um desses levando a servidores diferentes, se todas essas conexões fossem feitas soltas iria-se gastar muito recurso do processador, então se é o usado o SCP, protocolo esse que cria uma conexão como um túnel, diminuindo o fluxo de processamento. Se é interessante monitorar esse recurso pois, se um servidor tiver muitas requisições é mais fácil chegar a raiz do problemas, como botnets feitas por um atacante, as vezes o servidor mal configurado.. 

- `RTCP`
O RTCP é um protocolo de comunicação em tempo real, ele por si só, já avalia, latência, perda de pacote.. pois é um protocolo que já é feito para isso, comunicações em tempo real, e isso trás exigências, então com o monitoramento desse protocolo você já consegue obter essas informações.

- `NetBIOS`
Um protocolo criado pela Microsoft para facilitar o compartilhamento de arquivos, porém a segurança dele é muito baixa por se tratar de um protocolo de criação de rede para usuários que não entendem tanto do assunto, por isso se é interessante monitorar ele para não ocorrer na exposição de dados sensíveis por meio deste.

# Camada 4 - Transporte

- `UDP`
Não confiável

- `TCP`
Confiável

Monitorar as portas abertas e fechadas em cada um dos dois


# Camada 3 - Rede

- `IPv4
- `IPv6`
Parâmetros

- `ICMP`
Monitorar o protocolo de mensagens 

- `IGMP`
Protocolo de Grupos

- `X.25`
Protocolo antigo que se era utilizado em operações de cartões de credito.


# Camada 2 - Link Dados

- `Ethernet 802.3`
- `Wi-Fi 802.11`
- `PPP`
