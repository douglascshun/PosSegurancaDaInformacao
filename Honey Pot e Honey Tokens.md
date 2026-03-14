[[Aula 7 Resposta a incidentes]]

Um Honeypot é um recurso computacional de segurança dedicado a ser sondado, atacado ou comprometido.

	Tipos de Honeypot:
	- Baixa interatividade 
	- Alta interatividade 

- Honeypot de baixa interatividade:
Em um honeypot de baixa interatividade são instaladas ferramentas para emular sistemas operacionais e serviços com os quais os atacantes irão interagir.
Desta forma, o sistema operacional real deste tipo de honeypot deve ser instalado e configurado de modo seguro, para minimizar o risco de comprometimento.

- Honeypot de alta interatividade:
Nos honeypots de alta interatividade os atacantes interagem com sistemas operacionais, aplicações e serviços reais.

# Honeynet:

- `Honeynet` :
Nada mais é do que um tipo de Honeypot. Especificamente, é um honeypot de alta interatividade, projetado para pesquisa e obtenção de informações dos invasores, é conhecido também como "honeypot de pesquisa", ele consiste em uma rede projetada especificamente para ser comprometida e que contém mecanismos de controle para prevenir que seja utilizada como base de ataques contra outras redes.

# Honeynet virtual x Honeynet Real

### Honeynet Real

	 Em uma honeynet real os dispositivos que a compõe, incluindo os honeypots, mecanismos de contenção, de alerta e de coleta de informações, são físicos.

- Diversos computadores, um para cada honeypot. Cada honeypot com um sistema operacional, aplicações e serviços reais instalados
- Um computador com um firewall instalado, atuando como mecanismo de contenção e de coleta de dados.
- Um computador com um IDS instalado, atuando como mecanismo de geração de alertas e de coleta de dados 

	Um IDS (Intrusion Detection System) é uma ferramenta de segurança que monitora redes ou sistemas em tempo real, alertando administradores sobre atividades maliciosas ou violações de política. Diferente do IPS (que bloqueia), o IDS atua passivamente, detectando e relatando ameaças, sendo essencial para identificar ataques e analisar logs de segurança.

- Um computador atuando como repositório dos dados coletados 
- Hubs/Switches e roteadores (se necessário) para fornecer a infraestrutura de rede da honeynet.


### Honeynet Virtual

	Uma honeynet virtual baseia-se na ideia de ter todos os componentes de uma honeynet implementados em um número reduzido de dispositivos físicos

Os softwares de virtualização permitem executar diversos sistemas operacionais com aplicações e serviços instalados, ao mesmo tempo. 

# Aplicabilidades para Honeypots e Honey Tokens 

-  Detectar ataques internos 
- Identificar varreduras e ataques automatizados
- Identificar padrões 
- Manter atacantes afastados de sistemas importantes
- Coletar assinaturas de ataques 
- Detectar máquinas comprometidas
- Coletar códigos maliciosos (Malware)
- Detectar máquinas com configurações negligenciadas 

Tabela comparativa que pode auxiliar na decisão sobre 
