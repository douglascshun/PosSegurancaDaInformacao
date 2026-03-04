[[CyberOps]]

**Introdução**

O módulo Arquitetura de Segurança do Windows apresenta conceitos básicos dos artefatos e tecnologias de segurança no sistema Windows, inicialmente abordando os pontos elementares de serviços do sistema, juntamente com a abordagem de configuração segura do Active Directory. Na sequência foram estudados os fundamentos e segurança do Windows Firewall. Em continuidade aos temas abordados, foram vistas as funcionalidades de segurança do Windows, bem como seus conceitos de VPN e padrões de segurança Wi-Fi. A evolução desse estudo aborda estratégias de Network Access Protection e apresentou os detalhes do protocolo IPSec, juntamente com elementos básicos e avançados de sua implementação no Windows.

**Objetivos da aula**

- Analisar a arquitetura de segurança do Windows, apresentando inicialmente uma visão geral dos principais serviços do sistema;
- Abordar estratégias de configurações seguras do Active Directory;
- Compreender as funcionalidades do Windows Firewall e apresentar os conceitos de usos de VPN e padrões de segurança Wi-Fi;
- Identificar os aspectos tecnológicos de network access protection e visualizar o uso e funcionalidades do IPSec no Windows.  

**Resumo**

Nesse módulo, foram contemplados os conceitos de arquitetura de segurança do Windows, inicialmente, abordando estratégias de configuração segura para o Active Directory e buscando compreender como o Firewall Windows atua na proteção do sistema como um todo, bem como sobre os serviços e aplicativos do sistema Windows. No interregno dos conteúdos estudados, vimos as boas práticas e padrões de segurança de redes Wi-Fi. Os últimos tópicos desse módulo complementam os conhecimentos dos aspectos tecnológicos de Network Access Protection, consequentemente, propõem uma visualização do protocolo IPSec, bem como seu uso e funcionalidades.

Na abordagem sobre os principais serviços do Windows é importante relembrar que o Windows Service atua como gerenciador de serviços em um servidor ou estação de trabalho Windows, que estende sua aplicação no processo de monitoramento e auxílio de algumas tarefas, sem a necessidade de interação do usuário.

Podemos destacar os principais serviços do Windows que na verdade são aplicações que executam em segundo plano (background), como sendo: RPC – Remote Procedure Call, Network, Windows Defender Firewall e Windows Update.

O RPC define os parâmetros e técnicas para o desenvolvimento de aplicativos do tipo Cliente/Servidor no Windows, sendo assim a Chamada de Procedimento Remoto – RPC, encapsula os protocolos de rede característicos desse tipo de aplicação, permitindo-lhe se concentrar nos detalhes do seu aplicativo.

O Windows Defender é um tipo de firewall de host, isto é, está dimensionado para atuar na defesa de um computador pessoal ou workstation, permitindo a criação de regras que determinam o tráfego de rede para seu dispositivo. Outro serviço que merece destaque é o Windows Update, pois assim o sistema conserva a aplicação dos patches de segurança e correções de vulnerabilidades atuais.

Em continuidade aos temas definidos neste módulo, a análise de uma configuração segura do Active Directory nos permite optar por duas maneiras: por meio de contas de usuários ou contas de computador. Esse tema ofereceu uma abordagem prática ampla, no intuito de apresentar as melhores ações durante o processo de configuração de domínio,  gerenciamento de credenciais, atribuição de permissões, definição de grupos de usuários, etc.

A partir do Windows 10, foi incorporado oficialmente um firewall nativo para o sistema operacional que ficou conhecido como Windows Defender Firewall. Sua funcionalidade primordial é controlar o tráfego de rede de um host, tanto na entrada como na saída, obedecendo um conjunto de regras que estabelecem quais conexões e que tipo das mesmas, podem ser aceitas ou recusadas.

Um ponto que merece destaque nas definições de configuração do Windows Defender Firewall, são os três conjuntos básicos de regras pré-definidas:

1. Perfil de domínio: usado em redes com autenticação de domínio;
2. Perfil privado: usado em redes privadas; e
3. Perfil público: ideal para redes públicas, pois define mais proteção para ambientes de redes públicas como Wi-Fi, cafeterias, aeroportos, etc.

Com relação a implementação do VPM´s no Windows, podemos utilizar aplicativos comerciais e de código fonte aberto. Contudo o sistema operacional Windows possui soluções nativas por meio do uso de: VPN IPSec ou VPN SSL/TLS.

A abordagem sobre padrões de segurança em redes sem fio (Wi-Fi) revisitou os principais protocolos:

- Wired Equivalent Privacy (WEP) – 1997;
- Wi-Fi Protected Access (WPA) – 2003;
- Wi-Fi Protected Access II (WPA2) – 2004;
- Wi-Fi Protected Access III (WPA3) – 2018.

Em cada padrão, fica o destaque para o desenvolvimento tecnológico nos algoritmos de criptografia que, historicamente, aumentaram os níveis de proteção em redes Wi-Fi.

Por fim, nosso módulo apresentou duas tecnologias muito importantes que a Microsoft oferece como produto para o aumento no nível de segurança do sistema Windows. O primeiro é o Network Access Protection (NAP), que fundamentalmente cuida do acesso a uma rede, seguindo parâmetros de conformidade e integridade definidos previamente. O NAP realiza suas operações de controle por meio de múltiplos métodos de imposição ao sistema.

O IPSec (Internet Protocol Security), descrito no RFC (request for comments) de número 6071, descreve com riqueza essa tecnologia que é um conjunto de protocolos que provê conexão criptografada na internet. Essa tecnologia fornece a empresas e usuários, transações mais seguras.

**Como aplicar na prática o que aprendeu**

No site oficial da Microsoft, o artigo “Microsoft Defender for Endpoint” explica a fundo as funcionalidades desta tecnologia. Para aplicar na prática os conhecimentos já apresentados aqui, sugiro a leitura do artigo no link: “Microsoft Defender for Endpoint” Disponível em: <[https://learn.microsoft.com/en-us/microsoft-365/security/defender-endpoint/microsoft-defender-endpoint?view=o365-worldwide](https://learn.microsoft.com/en-us/microsoft-365/security/defender-endpoint/microsoft-defender-endpoint?view=o365-worldwide)>. **(Acesso em 16/02/2023)**

Na seção “Training for security analysts”, você pode escolher e praticar alguns laboratórios disponíveis. Disponível em:  <[https://learn.microsoft.com/en-us/microsoft-365/security/defender/?view=o365-worldwide](https://learn.microsoft.com/en-us/microsoft-365/security/defender/?view=o365-worldwide)>. **(Acesso em 16/02/2023)**

**Conteúdo bônus**

**Tópicos avançados**

IPsec é um grupo de protocolos usados, juntos, para configurar conexões criptografadas entre dispositivos. Ele ajuda a manter seguros os dados enviados por redes públicas. O IPsec costuma ser usado para configurar VPNs e funciona criptografando pacotes IP, além de autenticar a origem de onde vêm os pacotes. Dentro do termo "IPsec", "IP" significa "Internet Protocol" e "sec" para "seguro". O Internet Protocol é o principal protocolo de roteamento usado na Internet; ele designa para onde os dados irão usando endereços IP. O IPsec é seguro porque adiciona criptografia* e autenticação a esse processo. A leitura do artigo “VPN work” da empresa CloudFlare amplia os conhecimentos vistos sobre essa tecnologia. Disponível em: <[https://www.cloudflare.com/learning/network-layer/what-is-ipsec/](https://www.cloudflare.com/learning/network-layer/what-is-ipsec/)>. **(Acesso em 16/02/2023)**

Referência Bibliográfica

**Bibliografia Básica**

RICCI, Bruno. **Rede Segura:** VPN Linux, Editora Ciência Moderna, 2007.

TANENBAUM, A. S., **Redes de Computadores**. Rio de Janeiro, Campus, 2003.

COSTA, Daniel Gouveia. **Administração de Redes com Scripts**, 2ª Edição, Editora Brasport, 2010.

**Bibliografia Complementar**

SMITH, Rodercik W**. Linux:** Ferramentas Poderosas, 1ª Edição, 2004, Editora Ciência Moderna.

NAKAMURA, E. T., e GEUS, P. L., **Segurança de Redes em Ambientes Cooperativos**,2 ed. Ed. Berkley, São Paulo, 2007.

MORAES, Alexandre F. **Redes de Computadores**. 7ª Edição, Editora Érica, 2008.

MENDES, Douglas Rocha, **Redes de Computadores**, Ed. Novatec, 1ª Edição, 2007

STARLIN, Gorki, **Conceitos, Protocolos e Uso Tcp/Ip: Redes de Computadores.** 1ª Edição, Alta Books, 2004.