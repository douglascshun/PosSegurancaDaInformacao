[[Network Defense]]

**Introdução**

Hoje, vamos aprender os conceitos de defesa de redes e a sua importância.

**Objetivos da aula**

- Conceituar Defesa de Redes
- Importância da Defesa de Redes
- Tipos de defesa de Redes

**Resumo**

**O que é uma rede?**

A primeira coisa que precisamos conceituar é o termo rede. Existem diversos tipos de redes, cada uma com suas próprias características e todas precisam ser defendidas de ações não autorizadas.

**Redes de computadores:**

Vamos começar com um exemplo. Eu decidi abrir uma pequena empresa, comprar um computador e uma impressora, para poder imprimir meus boletos e propostas. Agora, preciso de uma conexão, de uma ligação entre o computador e a impressora e, para isso, vou passar um cabo. Até aí tudo funciona bem e eu atingi meu objetivo que é acessar a impressora. Contudo, com o tempo, a empresa cresce, eu preciso contratar uma colaboradora e comprar um outro computador para ela. E agora? Como compartilhar esta impressora entre nós dois? Posso passar um cabo, mas como emendar este cabo? Na realidade, para compartilhar este recurso que é a impressora, vou precisar de um switch, um dispositivo que faça a emenda destes cabos, assim, conectá-los. Com isso, eu tenho agora uma rede local que compartilha um recurso, a impressora, entre dois dispositivos ou computadores. Agora, eu contrato um link de internet. Vem a operadora e instala um modem em minha empresa. Como já tenho uma rede local, é só ligar ao meu switch e todos os dispositivos ligados a ele compartilham este recurso. Já a minha rede que é baseada em cabos não consegue compartilhar a internet que eu contratei com o meu celular nem com o meu tablet, pois eles não têm conector para ligação. Nesse caso, a solução é comprar um roteador wi-fi e montar uma rede sem fio para atender a minha empresa e ligar este roteador ao meu switch. Neste cenário, tenho uma rede cabeada e outra sem fio. Assim, uma rede é um mecanismo através do qual dispositivos se conectam e compartilham recursos.

Figura: Rede IP (cabeada e wireless)  
 

![Fonte: Autoria Própria, 2023.](https://paperx-dex-assets.s3.sa-east-1.amazonaws.com/images/1678132746175-sOMnIjyStc.png "Fonte: Autoria Própria, 2023.")

Fonte: Autoria Própria, 2023.

**Redes de telefonia**

Eu peço para minha empresa uma linha de telefone da Embratel, por exemplo, para que os clientes façam contato comigo. Uma vez instalada a linha, conecto ela a um telefone, e tudo funciona corretamente, eu posso ligar para os clientes e receber as chamadas. No entanto, devido ao crescimento da empresa, decidi contratar dois auxiliares para ajudar a atender as chamadas e comprar dois aparelhos telefônicos. Pronto! Agora, tenho um problema! Como compartilhar esta linha, para que todos possamos utilizá-la ao mesmo tempo? Eu preciso que a atendente receba as chamadas, que o meu comercial ligue para os clientes e eu também preciso fazer uso desta linha, ou seja, preciso montar uma rede de telefonia, para poder compartilhar este recurso. Para isso, compro um PABX que fará um serviço semelhante ao do switch como no nosso exemplo anterior. Visto que todos se ligam ao PABX, todos podemos compartilhar a linha que eu contratei e ainda temos a possibilidade de falarmos uns com os outros via ramal. Só que esta rede de telefonia interna está sujeita a ataques, por exemplo, um atacante ou espião pode acessar a minha rede e interceptar um cabo de telefonia que vai de um dos meus ramais até o PABX e ouvir as conversas deste ramal. Assim, vemos que redes de telefonia também podem ser atacadas e precisam ser defendidas.

Figura: Rede de Telefonia  
 

![Fonte: Autoria Própria, 2023.](https://paperx-dex-assets.s3.sa-east-1.amazonaws.com/images/1678132795135-IJl1KSRnIf.png "Fonte: Autoria Própria, 2023.")

Fonte: Autoria Própria, 2023.

**Redes de CFTV**

Comprei para minha empresa quatro câmeras e um monitor para poder filmar e acompanhar o que acontece nela, comprei também um equipamento DVR para poder gravar as imagens. Agora, para que tudo funcione, eu preciso ligar estas câmeras ao gravador, passar um cabo, que pode ser coaxial ou de par trançado. Feito isso, ligo as câmeras ao DVR. As imagens estão sendo gravadas, mas como posso vê-las? Preciso de uma conexão também entre o DVR e um monitor. Faço isso e conecto eles. Agora sim eu tenho uma rede de CFTV, onde posso visualizar as imagens e gravá-las.

Porém, ainda tenho um problema. Só consigo acessar as imagens ou visualizá-las se eu for até a sala onde se encontra o meu DVR e o meu monitor, minha rede é local, uma rede de CFTV privada, mas eu quero poder acessar a minha rede de CFTV da minha casa, e de lá visualizar as câmeras. Para isso, preciso ligar a minha rede na Internet, e basta ligar o DVR à Internet, ligar estas duas redes, a de CFTV a da Internet, para que isso seja possível. Um exemplo de um outro tipo de rede são as de CFTV e como ela pode se ligar a outra para expandir os seus serviços e capacidades.

Figura: Rede de Circuito Fechado de TV (CFTV)  
 

![](https://paperx-dex-assets.s3.sa-east-1.amazonaws.com/images/1678132877736-hMTqWcdw6K.png)

**Rede Mista**

Vamos rever essa minha empresa hipotética. Ela tem uma rede de telefonia, composta de aparelhos de telefone, PABX, uma rede de CFTV composta de Câmeras e DVR, uma rede de computadores composta de PCs, switches e impressoras. Mais uma rede sem fio composta de um roteador, mais telefones celulares, tablet e notebooks. Cada uma dessas redes é completamente independente e usam cabos diferentes, por exemplo, a rede de computadores usa cabos UTP azuis, a rede de telefonia cabos de telefonia amarelos e a rede de CFTV cabos coaxiais vermelhos, e elas não estão interligadas.

Eu posso interligar as diferentes redes,por exemplo, passar um cabo de rede do PABX ao switch ligando a rede telefônica de ramais analógicos até a rede de computadores e sem fio. Agora, eu posso comprar um Telefone IP, que vai ser conectado via cabo de rede UTP ao meu switch e, com isso, este ramal IP poderá falar com os ramais analógicos. Também posso comprar uma nova câmera sem fio IP e interligá-la na minha rede utilizando o meu roteador wi-fi. Tudo isso pode ser conectado à internet. Essa é uma rede mista e cada segmento usa uma tecnologia diferente, um cabo diferente e que precisa de proteção, pois todos estão expostos a um ataque vindo da internet.

Figura: Rede Mista (IP, Telefonia e Câmeras)

![](https://paperx-dex-assets.s3.sa-east-1.amazonaws.com/images/1678132893289-hA4pquQauR.png)

Qual é a importância da defesa de redes?

Atender às leis é uma obrigação legal.  
 

  
**Lei nº 12.965/2014**

Estabelece princípios, garantias, direitos e deveres para o uso da Internet no Brasil.

Art. 3º A disciplina do uso da internet no Brasil tem os seguintes princípios:

II - proteção da privacidade;

III - proteção dos dados pessoais;  
 

**Lei nº 13.709/2018**

Lei Geral de Proteção de Dados Pessoais (LGPD)

Art. 6º As atividades de tratamento de dados pessoais deverão observar a boa-fé e os seguintes princípios:

VII - segurança: utilização de medidas técnicas e administrativas aptas a proteger os dados pessoais de acessos não autorizados ...

VIII - prevenção: adoção de medidas para prevenir a ocorrência de danos em virtude do tratamento de dados pessoais;

X - responsabilização e prestação de contas: demonstração, pelo agente, da adoção de medidas eficazes e capazes de comprovar a observância e o cumprimento das normas de proteção de dados pessoais e, inclusive, da eficácia dessas medidas

  
**Seção I - Das Sanções Administrativas**

Art. 52. Os agentes de tratamento de dados, em razão das infrações cometidas às normas previstas nesta Lei, ficam sujeitos às seguintes sanções administrativas aplicáveis pela autoridade nacional:

II - multa simples, de até 2% (dois por cento) do faturamento da pessoa jurídica...

IV - publicização da infração.  
 

  
Como vimos, a defesa e proteção das redes e dos dados que trafegam nelas é uma imposição legal, que pode inclusive ser punida com multas e publicização da infração, para aqueles que não implementarem, ou fizerem de forma ineficaz.

**As defesas de rede podem ser de três tipos:**

Preventiva – Quando já é conhecido um tipo de ataque e como ele é executado, conseguimos implementar medidas para prevenir que ocorra.

Preditiva – Quando se identifica alguma evidência ou sintoma ainda em estágios iniciais, ou seja, quando ainda são falhas potenciais.

Reativa – Quando o ataque já se consumou e vai tentar minimizar os efeitos ou parar o mesmo.

**Conteúdo bônus**

**Tópicos avançados**

Existe dentro do Comitê Gestor da Internet no Brasil (CGI.br) uma entidade que é o Centro de Estudos, Resposta e Tratamento de Incidentes de Segurança no Brasil (CERT.br), sendo uma das mais importantes fontes de informação e estatísticas de segurança.

Sugiro que entre na página do CERT.br e verifique as estatísticas de ataques nos últimos três anos, além das boas práticas de segurança recomendadas por eles. Verifique, por exemplo, os tipos de ataque mais frequentes.

Referência Bibliográfica

ABNT NBR ISO/IEC 27001:2006 - **Sistemas de gestão de segurança da informação.**

ABNT NBR ISO/IEC 27002:2005 - **Código de prática para a gestão da segurança da informação.**

ABNT NBR ISO/IEC 27003:2011 – **Diretrizes para implantação de um sistema de gestão da segurança da informação.**

ABNT NBR ISO/IEC 27007:2012 - **Diretrizes para auditoria de sistemas de gestão da segurança da informação.**

BEAL, Adriana. **Segurança da informação: princípios e melhores práticas para proteção dos ativos de informação nas organizações.** São Paulo: Atlas, 2005.

BRASIL. **Lei n° 12.965**, **de 23 de abril de 2014**. Diário Oficial da União, Brasília, DF, 24 abr. 2014.  
BRASIL. **Lei n° 13.709, de 14 de agosto de 2018.** **Lei Geral de Proteção de Dados Pessoais (LGPD)**. Diário Oficial da União, Brasília, DF, 15 ago. 2018.

DIAS, Cláudia. **Segurança e auditoria da tecnologia da informação.** Rio de janeiro: Axcel Books do Brasil, 2000.

FERREIRA, Fernando Nicolau Freitas**,. Segurança da informação.** Rio de Janeiro: Ciência Moderna, 2008.

FONTES, Edison. **Vivendo a segurança da informação – Orientações práticas para pessoas e organizações**. São Paulo: Sicurezza, 2000.

KUROSE, James F.; ROSS, Keith W. **"Computer Networking"**, Pearson Education, 2012.

MENEZES, Josué das Chagas. **Gestão da segurança da informação**. Leme: J. H. Mizuno, 2006.

SCHNEIER, Bruce. **Segurança.com: segredos e mentiras sobre a proteção na vida digital.** Rio de Janeiro: Campus, 2001.

TANENBAUM, Andrew S.; FEAMSTER, Nick; WETHERALL, David J.; **Computer Network**. Rio de Janeiro: Pearson, 2020.