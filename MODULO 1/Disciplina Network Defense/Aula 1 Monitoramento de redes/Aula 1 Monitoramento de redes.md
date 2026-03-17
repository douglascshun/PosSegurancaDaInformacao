[[Network Defense]]

## Monitoramento de redes

**Introdução**

O objetivo deste módulo é passar a importância de se monitorar redes, e como fazer, apresentando as principais ferramentas disponíveis no mercado, além dos erros mais comuns em Monitoramento de Redes.

  
**Objetivos da aula**

- A importância de se monitorar redes.
- O que monitorar?
- Como monitorar?
- Principais Ferramentas de Monitoramento.
- Erros comuns em Monitoramento de Redes.

  
**Resumo**

Inicialmente, o que é monitorar? É um verbo que representa uma ação. E qual o seu significado? Vigiar, verificar algo, visando um determinado fim, acompanhar o decurso de uma operação, uma máquina, etc. Monitorar é o primeiro passo para se poder gerenciar.

Segundo William Edwards Deming (1950), “Não se gerencia o que não se mede, não se mede o que não se define, não se define o que não se entende, e não há sucesso no que não se gerencia”.

Agora, vou listar 5 motivos:  
 

1. Análise de Tendências

Quando se monitora uma rede, temos a coleta de dados que pode ser utilizada para se verificar tendências, como no exemplo do gráfico abaixo, onde a empresa em questão tem um link de internet de 1Gbps ou 1000Mbps, e que está atendendo ao consumo, pois em Janeiro o pico de consumo foi de 98 Mbps. Em fevereiro subiu para 205Mbps, em março chegou a 289Mbps, em abril 408Mbps, em maio 510Mbps, em junho 615Mbps e julho 701Mbps. Se plotarmos estes dados num gráfico, vamos observar que temos uma tendência de aumento de aproximadamente 100Mbps por mês e, com isso, podemos prever que em outubro a banda contratada não será suficiente para atender a essa demanda, o que nos dá um prazo para providenciar um aumento, evitando problemas por falta de banda. Observe o gráfico:  
 

![Fonte: Autoria Própria, 2023](https://paperx-dex-assets.s3.sa-east-1.amazonaws.com/images/1680040541727-BQOI0rI2tt.png "Fonte: Autoria Própria, 2023")

Fonte: Autoria Própria, 2023

2. Economia Financeira

Pelo gráfico abaixo, observamos que o consumo de banda de internet no momento de pico em janeiro foi de 160Mbps, em fevereiro foi de 205Mbps, em março 187Mbps, em abril foi de 208Mbps, maio 195Mbps, junho 201Mbps e julho 189Mbps e nossa banda contratada é de 1000Mbps, ou seja, estamos desperdiçando dinheiro e recursos, pois o monitoramento nos prova que podemos reduzir o link para 400Mbps ou 500Mbps e ainda assim todas as atividades da empresa serão muito bem executadas.

![](https://paperx-dex-assets.s3.sa-east-1.amazonaws.com/images/1680040620156-Myd22b6MYD.png)

3. Maior Segurança

Na tela abaixo podemos observar que se monitoramos uma rede, teremos, por exemplo, tentativas de invasão por força bruta. O IP 143.0.87.107 e o IP 183.245.35.35 estão tentando descobrir um usuário e senha válidos no roteador, esse ataque de força bruta vai surtir efeito, pois uma hora eles vão acertar uma combinação de usuário e senha. Porém, se estamos monitorando a rede, podemos tomar uma ação, bloqueando estes hackers. Já uma rede sem monitoramento vai ser invadida, é só uma questão de tempo.

![](https://paperx-dex-assets.s3.sa-east-1.amazonaws.com/images/1678131533484-oRWRulsEuV.png)

4. Prevenção de Quedas no Desempenho da Rede

Para uma ligação de telefonia IP funcionar adequadamente, a latência da rede deveria ser de no máximo 150 ms, de acordo com a recomendação G.114 da ITU-T. Se monitoramos a latência da rede, podemos evitar que ela chegue acima deste valor, o que prejudicaria o desempenho dos usuários que precisam deste serviço. Ou podemos, verificando que este valor está sendo atingido, tomar ações preventivas para  resolver o problema, evitando que volte a ocorrer, implementando mecanismos de QoS, por  exemplo.

Quando encontramos atrasos acima desse valor, teremos sobreposição entre as falas das chamadas, ou seja, perderemos sincronismo. A aparição de eco em chamadas telefônicas também pode ser causada devido ao atraso de fim a fim. Isso pode ter como causa o atraso de propagação do sinal, através do meio de transmissão (Ar no caso de wireless, cabos metálicos ou de fibra óptica) e o tempo utilizado no processamento da digitalização e na compressão de voz, feito pelo _codec_ implementado. Só o monitoramento pode dizer qual a causa e como resolver.

5. Redução de Tempo e Custos de TI

Quando se monitora as tarefas executadas, sabemos quanto tempo é utilizado em cada uma, de forma que podemos trabalhar na automatização de tarefas simples e repetitivas, que podem levar até a economia de tempo e dinheiro, além de reduzir erros humanos, liberando a força humana para trabalhar em projetos mais complexos e estratégicos. A mão de obra tem um custo e as tarefas têm um tempo para serem executadas. Por isso, só o monitoramento pode nos ajudar a reduzir o tempo e o custo destas ações.

O que monitorar?

![](https://paperx-dex-assets.s3.sa-east-1.amazonaws.com/images/1678131598622-js6CSBMnh0.png)

Como Monitorar?

Podemos monitorar os dispositivos e serviços de rede principalmente por dois métodos:

Ativo - onde vamos buscar nos dispositivos ou equipamentos as informações que desejamos monitorar, em intervalos de tempo definidos.

Passivos - onde são os dispositivos que nos informam alterações nos parâmetros previamente definidos, assim que ocorrem.

Existem no mercado diversos softwares de monitoramento de rede com opções pagas, por exemplo, o PRTG e gratuitas como o Zabbix, Nagios, The Dude e Cacti, por exemplo.

Alguns erros comuns em Monitoramento de Redes e que devemos evitar são:

- Ser reativo às ameaças de Segurança: não basta reagir a uma ameaça, devemos evitar que o problema venha a ocorrer.
- Não assistir dispositivos e aplicações: alguns monitoram apenas os dispositivos, outros só as aplicações, porém o correto é monitorar ambos.
- Não coletar e analisar logs: os sistemas sempre nos fornecem logs de todas as ações que são executadas. Contudo, devido ao grande número de dados, muitos simplesmente não coletam ou não analisam essas informações.
- Negligenciar as principais atualizações de rede: novas falhas são descobertas todos os dias, e são emitidas atualizações para a correção delas. Muitos ainda negligenciam isso e não aplicam regularmente as atualizações.
- Não impor práticas de higiene social aos usuários: as equipes que fazem o gerenciamento da rede devem promover com regularidade reuniões de higiene digital, informando e treinando os funcionários sobre senhas inteligentes, utilização de códigos e protocolos para o acesso à rede.

**Conteúdo bônus**

**Tópicos avançados**

Sobre os softwares de monitoramento citados, apenas o PRTG é pago, porém tem uma versão de testes que pode ser utilizada gratuitamente com algumas limitações. As páginas têm muitas informações sobre os procedimentos de instalação e monitoramento, sendo um excelente ponto de partida para os estudos. Seguem as sugestões abaixo:  
 

Zabbix: [https://www.zabbix.com/](https://www.zabbix.com/) **(Acesso em 23/01/2023)**

Nafgios: [https://www.nagios.org/](https://www.nagios.org/)  **(Acesso em 23/01/2023)**

Cacti: [https://www.cacti.net/](https://www.cacti.net/)  **(Acesso em 23/01/2023)**

The Dude: [https://mikrotik.com/thedude](https://mikrotik.com/thedude)  **(Acesso em 23/01/2023)**

PRTG: [https://www.paessler.com/](https://www.paessler.com/)  **(Acesso em 23/01/2023)**

Referência Bibliográfica

ABNT NBR ISO/IEC 27003:2011 – **Diretrizes para implantação de um sistema de gestão da segurança da informação.**

ABNT NBR ISO/IEC 27007:2012 - **Diretrizes para auditoria de sistemas de gestão da segurança da informação.**

ABNT NBR 16167:2013 - **Diretrizes para classificação, rotulação e tratamento da informação.**

COULOURIS, G. F. **Distributed systems: concepts and design.** 5nd. ed. London: Addison-Wesley, 2011.

KUROSE, James F.; ROSS, Keith W. **"Computer Networking"**, Pearson Education, 2012.

MITNICK, K.; SIMON, W. **The Art of Deception - Controlling the human element of security**. Wiley Publishing Inc, 2013.

MENEZES, Josué das Chagas. **Gestão da segurança da informação**. Leme: J. H. Mizuno, 2006.

PEIXOTO, MÁRIO CÉSAR P. - **Engenharia Social e Segurança da Informação na Gestão Corporativa**. Ed. Brasport, 2006.

TANENBAUM, Andrew S.; FEAMSTER, Nick; WETHERALL, David J.; **Computer Network**. Rio de Janeiro: Pearson, 2020.