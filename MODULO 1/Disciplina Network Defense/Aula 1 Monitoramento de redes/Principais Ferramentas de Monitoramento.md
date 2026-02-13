[[Aula 1 Monitoramento de redes]]
# Zabbix

![[Zabbix.png]]
Ferramenta (Open Source)que monitora, servidores, sites, redes, dispositivos usa ISCMP, SSH, entre outros protocolos, tem Agent, possuí a opção de alertas por sms, whatsapp, email, é programado por php e usa mySQL.

# Nagio
![[Nagio.png]]
Faz o mesmo que o Zabbix o problema é ser mantido pela comunidade e possuir uma interface menos amigável. 


# Cacti
![[Cacti.png]]
é usado para fazer gráficos, vários softwares utilizam ele como os próprios Zabbix e Nagio, sua vantagem é usar o banco de dados que usa o armazenamento cíclico , um exemplo do uso disso é ele configurado para sempre ter o período de um ano, se configurado no dia 12 de janeiro de 2025, no dia 12 de janeiro de 2026 ele vai apagar o dado do mesmo dia do ano anterior, o que acaba não superando o limite de armazenamento pois você consegue saber quando de dados você vai guardar e quanto de dados será usado.



	Os banco de dados do Cacti, Nagio e Zabbix, são banco de dados abertos, isso signifíca que podem ser contextados júridicamente, ou seja, por conta de os dados serem armazenados por você, eles podem ser modifícados propositalmente, causando alguma falha ou algum outro problema com os dados sensíveis, diferencialmente da seguinte ferramenta:


# PRTG
![[PRTG.png]]
Usa banco de dados criptografado, onde você não tem acesso as informações do banco de dados deles. Esse Software é um software pago, faz tudo o que os anteriores fazem. Bom para compliance, auditoria em empresas externas e em empresas de grande escala. 