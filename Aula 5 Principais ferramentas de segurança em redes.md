[[Ne]]

**Introdução**

Conhecer ferramentas importantes de segurança de rede: NGFW - Firewall, IPS/IDS, VPN e NGAV - AV EDR.

**Objetivos da aula**

- NGFW – Firewall - Vamos aprofundar no funcionamento dos Firewall
- IPS e IDS - Entender como trabalha a proatividade dos IPS e IDS
- VPN – Quando e porque implantar uma VPN
- AV - Chega de amadorismo, vamos virar experts em antivírus!

**Resumo**

![https://www.sonicwall.com/pt-br/products/firewalls/entry-level/. Acesso em 14/02/2023.](https://paperx-dex-assets.s3.sa-east-1.amazonaws.com/images/1677708647279-88ifiZ2h5T.png "https://www.sonicwall.com/pt-br/products/firewalls/entry-level/. Acesso em 14/02/2023.")

[https://www.sonicwall.com/pt-br/products/firewalls/entry-level/](https://www.sonicwall.com/pt-br/products/firewalls/entry-level/). Acesso em 14/02/2023.

Firewall Comercial

Quando o assunto é defesa de perímetro, este é o principal ativo de segurança da sua rede. O Firewall é responsável pela proteção da sua rede interna corporativa com dados sensíveis, com a rede externa, aberta para a internet. Equipamento de extrema relevância, complexo e que deve ser implementado por profissionais experientes, com políticas de segurança e monitorado com assiduidade. Podem ser comercializados por empresas de segurança ou OpenSource mantido pela comunidade.

Um firewall é um dispositivo de segurança da rede que monitora o tráfego de entrada e saída e decide permitir ou bloquear o envio de dados, de acordo com um conjunto definido de regras de segurança. Diferente de um Firewall convencional, o Next Generation Firewall permite que sejam criadas regras inteligentes, sendo possível identificar qual tipo de aplicação está trafegando dados, independentemente da porta TCP/IP utilizada.

A primeira geração do Firewall remonta à década de 80. Baseados apenas em filtros de pacotes, analisavam apenas protocolos e portas e não eram capazes de analisar informações a nível de aplicação. Já a segunda geração, é capaz de inspecionar até o nível de aplicação como os protocolos: FTP, DNS e HTTP. A terceira geração é o de inspeção de estado, inteligente o bastante para inspecionar o estado de cada sessão aberta ou fechada. Note que cada recurso é herdado da geração anterior.

Como dito no início, o ideal é posicionar o firewall na borda da sua rede, ou seja, entre sua rede corporativa interna e entre a internet mundo externo sem fronteiras, limites ou regras, quase uma terra de ninguém. Somente o firewall não é capaz sozinho de proteger toda sua rede corporativa; integrado com outras ferramentas, ele pode ajudar a criar camadas adicionais, porém ele não é uma bala de prata, existem ataques impossíveis de serem bloqueados ou mitigados pelos Firewalls, como o SQL Injection, cuja causa é uma falha na aplicação, que tem um vulnerabilidade que pode ser explorada mesmo como o melhor firewall implementado.

Um Firewall de Aplicação Web ou WAF segundo a OWASP é um appliance (hardware+software) ou um filtro que aplica uma série de regras nas conversações HTTP. Estas regras geralmente cobrem os ataques mais comuns; temos WAF em cloud computing como AWS, Azure e GCP.

O IDS é um módulo que pode ser habilitado nos Firewalls para detectar uma exploração de vulnerabilidades. É um sistema de monitoramento passivo auditar e enviar alertas, eventos, notificações, falso positivo e negativo, estes alertas são enviados para outro módulo.

O IPS é responsável por agir: depois de receber as informações dos logs e eventos do IDS, o IPS é quem aplica uma ação, seja ela bloquear, ou liberar uma solicitação. Baseado em regras previamente estabelecidas, ele pode causar muitos falsos positivos, deve-se implementar com cuidado e muita análise do tráfego de rede. Para incrementar a análise dos dados, esse sistema é atualizado por serviços de Inteligência de Ameaças (Threat Intelligence) de fornecedores de segurança ou via OSINT (Open Source Intelligence). Dessa maneira, obtém-se mecanismos de proteção adicionais como por exemplo, rejeição de conexões cujo endereços de origem não são confiáveis (baixa reputação).

![https://www.canalti.com.br/seguranca-da-informacao/ids-ips-conceitos-e-diferencas/. Acesso em 14/02/2023.](https://paperx-dex-assets.s3.sa-east-1.amazonaws.com/images/1677708689392-Ch5wKdNPf2.png "https://www.canalti.com.br/seguranca-da-informacao/ids-ips-conceitos-e-diferencas/. Acesso em 14/02/2023.")

[https://www.canalti.com.br/seguranca-da-informacao/ids-ips-conceitos-e-diferencas/](https://www.canalti.com.br/seguranca-da-informacao/ids-ips-conceitos-e-diferencas/). Acesso em 14/02/2023.

VPN ou Virtual Private Network – é a forma correta de interligar dois hosts em redes diferentes através da internet. Digamos que você trabalha em uma empresa que tem uma rede interna com vários computadores, servidores e impressoras, um funcionário vai para casa e precisa acessar uma pasta compartilhada no FileServer, que são pastas compartilhadas com setores. Para realizar esta conexão de forma segura é necessário configurar um VPN entre a rede doméstica do funcionário e a rede corporativa da empresa. Existem soluções VPN apartadas dos Firewall, mas o mais comum é configurar este módulo dentro dos UTM, que são Firewalls que agregam várias funções de segurança em uma única console, para gerenciamento centralizado. Em geral, sua função é impedir que o ambiente fique diretamente exposto para a Internet, onde ficará suscetível aos scans de hackers ou robôs buscando por portas lógicas (tcp/udp) abertas, vulnerabilidades, enumeração de serviços e suas versões, entre outros.

Sim, os Antivírus são a ponta de lança da segurança da informação, são os soldados do mundo corporativo, são estes agentes que fazem o trabalho de inspecionar estações de trabalho, em busca de vírus e processos maliciosos. Quando questionado, qualquer profissional de TI vai saber explicar o que é um antivírus, mas talvez apenas 30% deles saibam exatamente como sua engine funciona, qual é a melhor solução, os tipos e modelos existentes e qual o melhor custo benefício para as empresas. Antivírus sozinho não faz verão, assim como o Firewall esta ferramenta precisa de outras ferramentas para conter em conjunto muitas ameaças e vulnerabilidades, mais uma vez estamos falando de segurança em camadas. Não é mais possível um empresa de porte pequeno, médio ou grande operar em suas estações de trabalho sem um ótimo antivírus, sim isso mesmo, um ótimo pois um gratuito, um bom não serve, porque caso a empresa seja atacada por um ransomware, a diferença de valor entre um bom antivírus e um ótimo vai ser irrisória. Soluções pagas contam com suporte, console de gerenciamento, machine learning, IA, assinaturas em tempo real, VPN, anti-spam, análise por comportamento entre inúmeras outras soluções profissionais de ponta embarcadas.

A solução de EDR (Endpoint Detection and Response) é a nova geração de Antivírus, uma vez que identifica ameaças baseadas em comportamento e machine learning em nuvem, e não somente em assinaturas como as primeiras gerações de Antivírus. Como resultado, essa solução é mais performática que os Antivírus tradicionais, consumindo menos poder computacional. Além disso, tem a capacidade de identificar ameaças ainda não catalogadas, justamente pelo fato do EDR monitorar o comportamento de todos os processos e serviços executados dentro do servidor de nossos clientes. Portanto, o EDR é responsável pela detecção de malwares, rootkits, ransomware, vírus, trojans, backdoors, entre outros códigos maliciosos.

![https://blog.tripletech.com.br/qual-e-o-melhor-antivirus-pago/. Acesso em 14/02/2023.](https://paperx-dex-assets.s3.sa-east-1.amazonaws.com/images/1677708737033-cpryKPVg7O.png "https://blog.tripletech.com.br/qual-e-o-melhor-antivirus-pago/. Acesso em 14/02/2023.")

[https://blog.tripletech.com.br/qual-e-o-melhor-antivirus-pago/](https://blog.tripletech.com.br/qual-e-o-melhor-antivirus-pago/). Acesso em 14/02/2023.

**Tópicos avançados**

PODCAST – O Antivírus realmente está morto? [**https://www.segurancalegal.com/2014/07/episodio-53-o-antivirus-realmente-esta-morto**](https://www.segurancalegal.com/2014/07/episodio-53-o-antivirus-realmente-esta-morto)**.** **Acesso em 14/02/2023.**

Site de notícias e atualidades sobre ameaças e vulnerabilidades.

[**https://www.virusbulletin.com**](https://www.virusbulletin.com/)**. Acesso em 14/02/2023.**

Aula completa sobre Firewall

[**https://www.youtube.com/watch?v=Af0zAx5ypU8**](https://www.youtube.com/watch?v=Af0zAx5ypU8)**. Acesso em 14/02/2023.**

**Referência Bibliográfica**

LYRA, Maurício R. **Segurança e auditoria em Sistemas de Informação**. Rio de janeiro. 2ª edição Editora Ciência Moderna Ltda, 2017.

FONTES, Edison **Segurança da informação. O usuário faz a diferença**. 1ª edição. São Paulo, Editora Saraiva; 2016.