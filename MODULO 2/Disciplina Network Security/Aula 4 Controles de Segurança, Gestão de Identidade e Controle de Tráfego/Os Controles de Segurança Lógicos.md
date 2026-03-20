[[Aula 4 Controles de Segurança, Gestão de Identidade e Controle de Tráfego]]

- Firewall
- Antivírus
- VPN
- Proxy - Content Filter
- DLP
- SIEM
- IPS / IDS
### 1. Defesa de Perímetro e Tráfego

- **Firewall:** É a primeira linha de defesa. Filtra o tráfego de entrada e saída com base em regras de segurança predefinidas (bloqueia ou permite portas e IPs).

- **VPN (Virtual Private Network):** Cria um "túnel" criptografado para que dados trafeguem com segurança em redes públicas (como a internet), garantindo privacidade e autenticidade.

- **Proxy / Content Filter:** Age como intermediário entre o usuário e a internet. É usado para controlar o acesso a sites (bloqueio de categorias como redes sociais ou sites perigosos) e fazer cache de conteúdo.


### 2. Detecção e Monitoramento

- **IPS / IDS (Intrusion Prevention/Detection System):** * **IDS:** Monitora a rede em busca de atividades suspeitas e gera alertas.

- **IPS:** Vai além; ele detecta e tenta **bloquear** a ameaça automaticamente.

- **SIEM (Security Information and Event Management):** Como vimos, ele centraliza logs de todos os outros dispositivos (Firewall, Servidores, etc.) para correlacionar eventos e identificar ataques complexos.


### 3. Proteção de Dados e Endpoints

- **Antivírus (EPP/EDR):** Protege o dispositivo final (computador, servidor) contra softwares maliciosos (malware, ransomware).

- **DLP (Data Loss Prevention):** Focado em evitar o vazamento de informações sensíveis. Ele monitora se dados confidenciais (como números de cartão ou arquivos de projeto) estão sendo enviados para fora da empresa indevidamente.
