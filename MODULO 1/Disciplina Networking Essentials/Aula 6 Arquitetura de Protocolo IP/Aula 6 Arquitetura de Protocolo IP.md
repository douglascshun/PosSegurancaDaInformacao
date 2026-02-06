[[Networking Essentials]]
## Arquitetura de protocolo IP

**Introdução**

O protocolo IP é um serviço de transferência de dados que aplica regras de melhor esforço. Os datagramas não têm conexão e não são confiáveis. Melhor esforço significa que o protocolo IP não fornece nenhuma forma de verificação ou verificação de entrega, nem fornece monitoramento de erros.

É de conhecimento geral, que a confiabilidade não é garantida ao usar o protocolo IP. O protocolo faz todo o possível para levar os pacotes do remetente ao destinatário, mas não há garantia de que isso seja feito com perfeição. (BARRETO; ZANIN; SARAIVA, 2018, p.110).

Desta forma, nesta aula vamos trabalhar como o protocolo TCP/IP e sobre a sua confiabilidade e a integridade nas transações de comunicação sendo consideradas muito importantes, o protocolo IP deve ser combinado com outro protocolo confiável, como o protocolo TCP.

**Objetivos da aula**

- Conhecer o protocolo IP e seu datagrama;
- Compreender a necessidade de evolução do IPV4 para o IPV6;
- Compreender como é o processo de endereçamento do computador e perdendo dIPV4: Endereçamento;
- Compreender a necessidade e o funcionamento das Sub-redes.

**Resumo**

**O protocolo IP e seu datagrama**

De acordo com _Internet Protocol_ (IP) é o mecanismo de comunicação usado por todas as máquinas conectadas a uma rede usando o protocolo TCP/IP para transferir dados. Segundo Fourozan e Fergan (2008 apud Barreto e Zanin e Saraiva 2018, p.110), no protocolo TCP/IP, o protocolo IP reside em uma camada denominada camada de rede, conforme apresenta a figura a seguir:

Figura 1: Posição do protocolo IP dentro dos protocolos TCP/IP

![Fonte: Adaptada de Fourozan e Fergan (2008, p. 204 apud Barreto e Zanin e Saraiva 2018, p.110).](https://paperx-dex-assets.s3.sa-east-1.amazonaws.com/images/1677704118400-ivOK0LrGvw.png "Fonte: Adaptada de Fourozan e Fergan (2008, p. 204 apud Barreto e Zanin e Saraiva 2018, p.110).")

Fonte: Adaptada de Fourozan e Fergan (2008, p. 204 apud Barreto e Zanin e Saraiva 2018, p.110).

Com o protocolo IP, cada datagrama é processado individualmente e pode seguir caminhos diferentes até encontrar o destinatário. Isso significa que os datagramas enviados pelo mesmo remetente podem chegar ao destinatário fora de ordem. Além disso, alguns datagramas podem ser perdidos, modificados ou corrompidos durante uma transação. Novamente, a solução é usar um protocolo mais seguro e de maior qualidade em combinação com o protocolo IP.

Figura 2: Datagrama do protocolo IP

![Fonte: Adaptada de Fourozan e Fergan (2008, p. 205 apud Barreto, Zanin e Saraiva 2018, p.112).](https://paperx-dex-assets.s3.sa-east-1.amazonaws.com/images/1677704153740-1wAuswCJiz.png "Fonte: Adaptada de Fourozan e Fergan (2008, p. 205 apud Barreto, Zanin e Saraiva 2018, p.112).")

Fonte: Adaptada de Fourozan e Fergan (2008, p. 205 apud Barreto, Zanin e Saraiva 2018, p.112).

Um datagrama é um pacote de comprimento variável que consiste em duas partes: um cabeçalho e dados. O cabeçalho deve ter de 20 a 60 bytes e conter informações básicas sobre como o pacote deve ser roteado e enviado. Ao usar o protocolo TCP/IP, os cabeçalhos geralmente aparecem em seções divididas em blocos de 4 bytes. (BARRETO; ZANIN; SARAIVA 2018, S.111).

**IPV4 e IPV6** 

O elemento que mantém a Internet unida é o protocolo da camada de rede conhecido como Protocolo de Internet (IP). O protocolo foi desenvolvido desde o início para conectar redes entre si. Porque, como já sabemos, a Internet é apenas uma grande rede formada pela interligação de todas as redes menores existentes. (BAY; BLUNING 2016, p.101).

Atualmente existem duas versões do protocolo IP, versão 4 e versão 6. Entre as versões, primeiro destaque a versão 4. Isso ocorre porque é amplamente distribuído e usado. O protocolo IP versão 4 pode ser encontrado em todos os hosts conectados à rede. Sem eles, seria impossível realizar qualquer tipo de comunicação ou troca de dados entre dois ou mais dispositivos conectados.

Embora esta versão 4 esteja em uso há muitos anos, o rápido crescimento da Internet e o uso indevido desse protocolo atingiram rapidamente seus limites no que diz respeito à atribuição de endereços aos hosts dentro da rede. Todos os novos hosts para a Internet. A partir disso, podemos concluir que este protocolo atingiu seus limites. (BAY; BLUNING 2016, p.102).

Como a estrutura da Internet (rede) continuou a se expandir e novos dispositivos foram conectados à rede todos os dias, tornou-se necessário realizar o desenvolvimento de novos protocolos para atender à necessidade de alocação de novos hosts. (Bay; BLUNING 2016, p.102)

Chamado de protocolo IP versão 6, esse novo protocolo oferece um potencial de crescimento virtualmente ilimitado para as redes existentes. Desde o seu lançamento, foi realizado um processo de migração da versão 4 para a versão 6. Esse processo é gradativo para que todos os provedores de serviço (provedores de internet) e provedores de conteúdo (portais) possam fazer as mudanças necessárias sem que seus serviços ou clientes sofram com falta de conectividade ou informação.

Quadro 1: Comparativo entre IPv4 e IPv6

![Fonte: Adaptado de Muniz et al. (2017, p. 533).](https://paperx-dex-assets.s3.sa-east-1.amazonaws.com/images/1677704236544-JPgKjjK9wL.png "Fonte: Adaptado de Muniz et al. (2017, p. 533).")

Fonte: Adaptado de Muniz et al. (2017, p. 533).

Portanto, nesse processo de transição, que ocorre há anos, nem todo o conteúdo existente na Internet atualmente roda na versão 6 do protocolo. Essa pilha de protocolo duplo será usada até que todos os serviços e conteúdo estejam 100% versão 6.

**IPV4: Endereçamento**

Como vimos, dentro de uma rede de computadores, todo dispositivo, todo ativo de rede, precisa de um IP para se comunicar com outro ativo, encaminhar pacotes ou gerar pacotes. Os endereços IP são responsáveis ​​pela sincronização entre os hosts no sentido de que ambos estejam próximos um do outro no sentido lógico da rede para que possam se comunicar. (BAY; BLUNING 2016, p.105).

Portanto, todo ativo de rede deve ter uma interface de rede lógica ou física. Essa interface de rede é o limite entre o próprio host e a camada de rede, transferindo todos os dados gerados por esse host para a mídia física anexada. (BAY; BLUNING 2016, p.105).

O endereçamento é muito básico para redes de computadores, e desta forma, vada endereço IP tem 32 bits (equivalente a 4 bytes). Portanto, há um total de 232 endereços IP possíveis. Isso é cerca de 210 vezes 103 e é fácil ver que existem cerca de 4 bilhões de endereços IP possíveis.

Esses endereços são escritos em notação decimal com pontos. Neste caso, cada byte do endereço é escrito em formato decimal e separado dos demais bytes do endereço por um ponto. Por exemplo, considere o endereço IP 193.32.216.9. 193 é o número decimal correspondente aos primeiros 8 bits do endereço. 32 é o equivalente decimal do segundo conjunto de 8 bits no endereço. Portanto, a representação binária do endereço 193.32.216.9 é

11000001 00100000 11011000 00001001

Assim, conforme apresenta Kurose (2010; (BAY; BLUNING 2016, p.105), cada interface de cada host, roteador ou outro ativo de rede precisa de um endereço IP para poder se comunicar com outros dispositivos. No entanto, adicionar IPs a uma interface não pode ser aleatório.

É importante que seja respeitada a sub-rede à qual o host está atribuído, pois ao contrário dos endereços Ethernet, os endereços IP são hierárquicos. Cada endereço de 32 bits consiste em uma porção de rede de comprimento variável nos bits altos e uma porção de host nos bits baixos.

A parte da rede tem o mesmo valor para todos os hosts em uma rede. Isso significa que uma rede é um bloco contíguo de espaço de endereço IP. Esse bloco fixo de endereços comum a todos os hosts é chamado de prefixo. Endereços de rede são geralmente números de 32 bits escritos em notação decimal com pontos. Portanto, cada um dos 4 bytes é escrito em notação decimal de 0 a 255. O prefixo é escrito com o endereço IP mais baixo no bloco de endereços.

O comprimento do prefixo é determinado pelo número de bits na parte da rede. Os bits restantes fazem parte do campo do host e podem variar. Isso significa que o comprimento do endereço deve ser uma potência de 2. Por convenção, escreva o prefixo seguido de uma barra, seguido do comprimento em bits da máscara de rede. (BAY; BLUNING 2016, p.107).

A principal vantagem adicional de usar prefixos de rede é fornecida aos roteadores que só podem encaminhar pacotes com base neles. A última parte, aquela endereçada ao host, é irrelevante para os roteadores, pois eles devem atribuir todos os hosts usando o mesmo prefixo.

**Sub-redes**

Observe que, de tudo o que discutimos até agora, todos os dispositivos conectados a uma rede devem ter endereços conectados diretamente à rede ou sub-rede. Uma sub-rede é apenas uma rede dividida em vários pedaços onde cada fragmento dessa divisão produziu uma nova rede, não importando quantas vezes a rede original foi dividida. (BAY; BLUNING 2016, p.110).

Esse conceito de sub-redes surgiu da necessidade de armazenar endereços de rede. Uma rede pode criar várias outras redes, portanto, essas redes diferentes podem ser distribuídas em locais diferentes sem desperdiçar endereços IP. Conecte sua rede a um ou dois hosts. Dessa forma, você pode dimensionar corretamente com base no número de IPs necessários e criar uma sub-rede que atenda à demanda certa sem sobrar muitos IPs nessa rede.

Se você tem uma rede e decide subdividi-la, não é necessária a aprovação da ICANN ou de qualquer outra organização, pois o bloco ou a rede permanecem os mesmos. Em outras palavras, mesmo que você subdivida sua rede, a sensação de direcionar o tráfego permanece a mesma. Assim as alterações só terão efeito dentro da rede local e o split na verdade tem o efeito programado de isolar o tráfego entre as redes criadas e não permitir o acesso direto entre as sub-redes, mas sim realizar a transmissão, usamos o mesmo meio físico para armazenar seus dados. (BAY; BLUNING 2016, p.110).

Uma máscara de sub-rede deve ser usada para obter a divisão em sub-redes. Isso faz a divisão entre números de rede e sub-redes e hosts. Essas máscaras de sub-rede também são escritas em notação decimal com pontos, com uma barra vertical adicionada, seguida pelo número de bits na rede e a parte da sub-rede. A máscara de rede de uma sub-rede pode ser 255.255.252.0 ou outra notação /22 para indicar que a máscara de sub-rede tem 22 bits de comprimento [...].(BAY; BLUNING 2016, p.110).

Essa subdivisão da rede é fundamental para um bom planejamento e construção da rede com o intuito de não desperdiçar endereços IP. O particionamento de rede é feito de forma com que seja a primeira rede que conhecemos até agora, 192.168.1.0/24, tem 256 endereços, 254 dos quais estão disponíveis para hosts. Divida esta rede em 6 novas sub-redes com 30 hosts cada. (BAY; BLUNING 2016, p.110). A primeira etapa na subdivisão é determinar se a rede principal suportará essa nova rede. Para fazer isso, descubra quantos endereços IP você precisa para construir esta rede.

Observe que cada nova rede tem um endereço de rede e um endereço de broadcast, portanto, 32 endereços IP são emitidos para cada nova rede. Então 32 x 6 = 192 e precisamos de 192 endereços. Nossa rede principal suporta 254 endereços, portanto, a primeira suposição sobre a disponibilidade de IP é feita pela rede principal. (BAY; BLUNING 2016, p.110).

Após verificar a disponibilidade da rede principal, execute os cálculos de rede para a nova máscara de rede. Para ajudar a priorizar os requisitos de nível de PC, considere o diagrama a seguir para ajudar a identificar os bits. (BAY; BLUNING 2016, p.110).

Figura 3: Octetos De Endereço Ipv4

![Fonte: Bay e Bluning (2016, p.111).](https://paperx-dex-assets.s3.sa-east-1.amazonaws.com/images/1677704275983-Ws3ug3Xsxe.png "Fonte: Bay e Bluning (2016, p.111).")

Fonte: Bay e Bluning (2016, p.111).

Com base na imagem, sabemos que precisamos de pelo menos 32 endereços IP para cada nova rede (30 para hosts, 1 para rede e 1 para transmissão), portanto, decida qual das opções existentes melhor atende às suas necessidades. Com base nessa analogia, podemos mapear uma rede de 32 IPs em três possibilidades.

128, 64 ou 32. Porém, tendo em vista os conceitos já discutidos, se é a melhor escolha para economizar IPs, ou a melhor escolha para não desperdiçá-los, qual seria a melhor para nossa situação?32 opções válidas. Portanto, essas novas redes estão separadas por 32 endereços. (Bay; BLUNING 2016, p.111).

Agora que sabemos onde atribuir a nova máscara de rede, vamos fazer as contas. Anteriormente, a rede principal consistia em uma máscara de rede de 24 bits, ocupando 3 dos 4 octetos. Para subdividir esta rede, a nova máscara ocupa alguns bits no último octeto. Portanto, adicione o valor de ocupação deste último octeto ao valor atual da máscara para encontrar a nova máscara de rede. (BAY; BLUNING 2016, p.112).

Nossa máscara atual /24 é 255.255.255.0 , mas como escolhemos 32 acima, sabemos que o último octeto usa 3 bits. Ou seja, são marcados com os bits 1 até o valor 32. A elipse amarela, então 24 + 3 = 27. A nova máscara de rede é /27 ou 255.255.255.224 (lembre-se de que 224 é a soma de 128+64+32).

Cada uma dessas sub-redes agora pode ser identificada pela máscara de rede identificada e pelo número de hosts em cada nova sub-rede. Observe que um valor de 0 (zero) conta como um endereço de rede.

É assim que a tabela de rede é organizada. Começando com o endereço de rede, sempre adicione 32 para identificar a próxima rede, subtraia 1 do valor inicial da próxima rede para obter o endereço de broadcast da rede anterior e identifique-a como a próxima rede. visível da mesa. ((Bay; BLUNING 2016, S.112):

Figura 4: Endereços de Rede

![Fonte: Bay e Bluning (2016, p.112).](https://paperx-dex-assets.s3.sa-east-1.amazonaws.com/images/1677704305040-lpCiv1GqkE.png "Fonte: Bay e Bluning (2016, p.112).")

Fonte: Bay e Bluning (2016, p.112).

Com base nesta tabela que criamos, não só conseguimos atender às nossas necessidades iniciais de 6 novas sub-redes, como também criamos mais 2 novas sub-redes para um total de 8 sub-redes baseadas na rede principal. (BAY; BLUNING 2016, p.112).

**Conteúdo bônus**

**Tópicos avançados**

Do IPv4 para o IPv6, mas o que vem depois?

Saímos, ou melhor, estamos tentando sair do limitado IPv4 para o robusto e longo IPv6 e assim pretendemos resolver durante séculos a demanda por endereços IP, mas a indústria acredita que esse não é o único problema.

De acordo com Dias (2021), vários players do setor estão participando de discussões sobre mudança, inovação e transformação na Internet. São provedores de conteúdo, provedores de serviços de internet, desenvolvedores profissionais de navegadores, fabricantes de máquinas e dispositivos, pesquisadores e até usuários de internet. Em suma, alguém que é especialista em tudo o que faz e conhece o procedimento ou como usá-lo. Na verdade, esses personagens estão sempre identificando áreas de melhoria.

Então pergunto: o que virá a seguir?

Disponível em: <[https://www.ispblog.com.br/2021/01/04/reflexoes-sobre-a-proposta-de-um-novo-sistema-de-protocolo-ip-para-o-itu-t/](https://www.ispblog.com.br/2021/01/04/reflexoes-sobre-a-proposta-de-um-novo-sistema-de-protocolo-ip-para-o-itu-t/)> Acesso em 01/02/2023.     

Observação: Este conteúdo não será cobrado nas avaliações e estará, obrigatoriamente, presente nas videoaulas. Fique tranquilo(a)!

Referência Bibliográfica

BARRETO, Jeanine dos Santos; ZANIN, Aline; SARAIVA, Maurício de Oliveira. **Fundamentos de redes de computadore**s. – Porto Alegre: SAGAH, 2018.

BAY; Edemilson; BLUNING, Paulo Henrique. **Fundamentos de redes de computadores**. UNIASSELVI, 2016.

MUNIZ, Angelo Henrique Alves.... [et al.]. **Estudo de Caso Transição do Protocolo IPv4 para IPv6**. Revista Gestão em Foco - Edição nº 9 – Ano: 2017.  Disponível em: < [https://portal.unisepe.com.br/unifia/wp-content/uploads/sites/10001/2018/06/055_estudo8.pdf](https://portal.unisepe.com.br/unifia/wp-content/uploads/sites/10001/2018/06/055_estudo8.pdf)> Acesso em: 31/10/202.