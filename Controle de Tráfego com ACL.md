[[Aula 4 Controles de Segurança, Gestão de Identidade e Controle de Tráfego]]

- São listas sequenciais de controle de pacotes de rede da camada superior, in ou out.
- Podem permitir ou negar recursos da rede como protocolos, direções e interfaces.
- ACL aumenta a segurança, administração e QoS da rede, através de filtragem e classificação
	- Controle do tráfego por uma direção
	- Controle do tráfego por protocolo
	- Controle do tráfego por interface

# Ex: Analisar e bloquear todos os passageiros que chegarem do país de destino: Mordor/TM

![[Exemplo de bloqueio de passageiros.png]]

	#access-list 1400 deny host 10.0.0.1


# Controle de acesso por equipamento CISCO

![[Controle de acesso CISCO.png]]

Controle de Segurançla