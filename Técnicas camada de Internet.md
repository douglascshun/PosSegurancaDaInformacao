[[Aula 3 Técnicas para proteção de redes]]

# Camada de Internet 

- ` Aprofundando em IPv4 e IPv6`:

Embora incompatíveis, eles frequentemente coexistem através de técnicas de transição que podem gerar vulnerabilidades.

Dual Stack: Onde o dispositivo roda ambos os protocolos. O perigo aqui é configurar o firewall para IPv4 e esquecer de aplicar as mesmas regras ao IPv6.

Tunelamento: Encapsular pacotes IPv6 dentro de IPv4. Isso pode ser usado para contornar sistemas de detecção de intrusão (IDS) se não for monitorado.

ICMP (Internet Control Message Protocol): Essencial para o funcionamento da rede, mas deve ser limitado. Ataques como _Smurf Attack_ ou _Ping of Death_ utilizam esse protocolo.




- ` Endurecimento (Hardening) de Roteadores`:

Além do acesso físico e senhas, considere estes pontos críticos:

 Desativar o WPS (Wi-Fi Protected Setup): É uma porta de entrada comum para ataques de força bruta.

Gerenciamento Out-of-Band (OOB):*Garantir que a interface de gerenciamento do roteador não esteja acessível pela Internet (WAN), apenas por uma rede local segura ou VPN.

 Atualização de Firmware:Manter o SO do roteador atualizado para corrigir CVEs (vulnerabilidades conhecidas).

Protocolos de Roteamento:Implementar autenticação em protocolos como OSPF ou BGP para evitar que vizinhos maliciosos injetem rotas falsas


- `Segmentação de Rede (VLANs)`:

Não basta proteger o roteador; é preciso dividir a rede para conter danos.

VLANs (Virtual LANs):Isolar o tráfego de diferentes departamentos (ex: Financeiro separado do Wi-Fi de Visitantes).

DMZ (Zona Desmilitarizada):**Uma sub-rede isolada que contém os serviços externos da empresa (servidor web, e-mail), agindo como um "tampão" entre a internet pública e a rede interna privada.
    

### 4. Firewalls e Listas de Controle de Acesso (ACLs)

- **ACLs de Entrada e Saída:** Regras que definem quais IPs e portas podem entrar ou sair da rede.
    
- **Stateful vs. Stateless:** Firewalls modernos (Stateful) acompanham o estado das conexões, sendo muito mais seguros que filtros de pacotes simples.
    

### 5. IDS e IPS (Sistemas de Detecção e Prevenção)

- **IDS (Intrusion Detection System):** Monitora o tráfego e alerta sobre atividades suspeitas (passivo).
    
- **IPS (Intrusion Prevention System):** Toma medidas automáticas para bloquear o tráfego malicioso assim que detectado (ativo).