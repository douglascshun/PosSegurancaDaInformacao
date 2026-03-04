[[Aula 2 Arquitetura de Segurança do Windows]]

Uma aplicação Windows Service pode rodar em servidor ou estação de trabalho.
Além disso são frequentemente usados para executar o monitoramento de algum sistema, ou auxiliar algum sistema em tarefas que não dependem da interação com usuários.

	Windows Services
- Não roda: Windows 95, 98 e ME.
- Roda: Windows 2000, XP, Vista 7, 8, 10 e 11.

# Acessando os serviços do Windows

Usando o conjunto de teclas `Win + R` para abrir o `executar`, apos isso digitar `sevices.msc` e dar `Enter` para iniciar. 

![[Acessando os serviços do Windows.png]]



# Tela de Serviços do Windows
![[Tela de Serviços do Windows.png]]

Os serviços do Windows são aplicações que rodam em segundo plano como:
- RPC Remonte Procedure Call
- Network
- Windows Defender Firewall
- Windows Update


Segundo a Microsoft (2022), a RPC (Chamada de Procedimento Remoto) da Microsoft define uma tecnologia avançada para criar programas de cliente?servidor distribuídos.

As bibliotecas e stubs de tempo de execução do RPC gerenciam a maioria dos processos relacionados a protocolos de rede e comunicação. Isso permite que você se concentre nos detalhes do aplicativo em vez dos detalhes da rede 