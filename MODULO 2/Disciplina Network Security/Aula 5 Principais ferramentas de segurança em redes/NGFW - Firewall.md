[[Aula 5 Principais ferramentas de segurança em redes]]

# Firewall

- O Firewall é uma ferramenta, um software que trabalha inspecionando pacotes de rede, limitando acesso às portas, protocolos, serviços e redes.
- Ele pode ser um software de distribuição Linux instalado em um computador/servidor ou uma solução comercial embarcada em um hardware.
	- Proteção contra acessos da internet!!!


# várias visões de Firewall
![[visoes de firewall.png]]


# Visão generalista
![[Charge Firewall.png]]


a administração deste dispositivo requer conhecimentos sólidos em redes, mais especificamente nos protocolos da pilha TCP/IP.
	Stateless
	Statefull

# Recursos Firewall
- Web Filter / Controle de Conteúdo 
- Controle de Pactes TCP/UDP
- NAT
- VLAN / DMZ
- Proteções contra Malwares e Spam 
- Inspeção de protocolos HTTP/HTTPS e SMTP
- VPN/IPSec
- Proxy / Cache
- IPS / IDS SNORD

# Exemplo de configuração em Firewall:
![[Config Firewall.png]]


# Considerações importantes sobre Firewall

É a principal solução de proteção de rede; Deve ser precedida de uma política de SI; Não deve ser a única solução.

`NGFW` (Next Generation Firewall), Faz a inspeção a nível de porta Protocolo e aplicação. Inclui IDS?IPS e anti-malware.

`WAF` (Web Application Firewall) Security Group/VPC na AWS Azure Firewall