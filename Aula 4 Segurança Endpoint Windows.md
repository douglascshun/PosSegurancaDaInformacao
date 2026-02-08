Observação: este site inclui um sistema de acessibilidade. Pressione Control-F11 para ajustar o site para pessoas com deficiências visuais que usam um leitor de tela; Pressione Control-F10 para abrir um menu de acessibilidade.

## Segurança Endpoint Windows

**Introdução**

Nesse módulo abordaremos os temas de Zero trust no Windows, falaremos da aplicação do Microsoft defender antivírus e suas aplicações de criptografia. O sistema operacional Windows é o sistema operacional com maior quantidade de usuários no mundo. Seja pelas suas versões que sempre se mostram inovadoras, quanto pela facilidade e usabilidade.

**Objetivos da aula**

Analisar as ferramentas e recursos disponíveis no Windows para proteção de endpoint. Assim como aplicá-las de forma correta aproveitando todos os seus recursos.

**Resumo**

**Definição de Zero Trust**

O conceito de Zero Trust nos ensina a “nunca confiar, sempre verificar”. Cada solicitação de acesso é totalmente autenticada, autorizada e criptografada antes de conceder acesso. Os princípios de micro segmentação e acesso menos privilegiado são aplicados para minimizar o movimento lateral. Inteligência e análises avançadas são utilizadas para detectar e responder a anomalias em tempo real.

Uma abordagem compreensiva para Zero Trust deve se estender a todo o patrimônio digital – incluindo identidades, endpoints, redes, dados, infraestrutura e aplicativos. A arquitetura Zero Trust serve como uma estratégia abrangente de ponta a ponta e requer integração entre todos estes elementos.

**Microsoft Defender Antivírus**

Microsoft Defender é um programa que tem como objetivo remover malware, spyware, trojan e adware instalados no computador. Monitoriza o computador para evitar que estes softwares perigosos alterem as configurações tanto do navegador, como do sistema operacional.

O Windows Update interage com o Windows Defender fornecendo atualizações.

O Microsoft Defender Antivírus funciona monitorando o comportamento dos aplicativos em seu dispositivo em tempo real e comparando-os com uma base de dados de ameaças conhecidas. Se o software detectar um comportamento suspeito, ele bloqueia a ameaça e pode tomar medidas para removê-la do dispositivo. Além disso, o Microsoft Defender Antivírus também usa inteligência artificial e aprendizado de máquina para identificar novas ameaças em tempo real, mesmo que elas ainda não estejam presentes na base de dados de ameaças conhecidas.

O software também permite que você configure as configurações de segurança de acordo com suas preferências e necessidades, como ativar ou desativar a proteção em tempo real, escolher ações para tomar em caso de detecção de ameaças, e ver o histórico de segurança de seu dispositivo. Tudo isso pode ser gerenciado através do Microsoft Defender Security Center.

**Microsoft Defender e Criptografia**

O Microsoft Defender Antivirus não afeta a criptografia de arquivos ou dispositivos. O software é projetado para proteger contra ameaças externas, como malware e vírus, sem interferir nas operações normais do dispositivo, incluindo a criptografia de arquivos ou dispositivos. No entanto, se o software detectar uma ameaça em um arquivo criptografado, ele pode tomar medidas para remover a ameaça, como bloquear o acesso ao arquivo ou removê-lo do dispositivo. Além disso, o Microsoft Defender Antivírus pode ser configurado para ignorar determinadas pastas ou arquivos, incluindo arquivos criptografados, para evitar quaisquer interferências desnecessárias.

**Windows Defender Firewall**

O Windows Defender Firewall é o firewall integrado ao Windows 10. Ele controla o tráfego de rede em seu dispositivo, permitindo ou bloqueando o acesso de aplicativos e dispositivos à rede e à Internet. O Windows Defender Firewall ajuda a proteger seu dispositivo contra ataques externos, como malware e vírus, e permite que você configure regras de firewall para ajustar as configurações de segurança de acordo com suas preferências. Além disso, o Windows Defender Firewall também pode ser gerenciado através do Microsoft Defender Security Center.

O Windows Defender Firewall funciona estabelecendo regras de firewall que controlam o tráfego de rede em seu dispositivo. Quando um aplicativo ou dispositivo tenta se conectar à rede ou à Internet, o Windows Defender Firewall verifica se essa conexão está autorizada pelas regras de firewall. Se a conexão estiver autorizada, ela é permitida; caso contrário, é bloqueada.

O Windows Defender Firewall permite que você configure as regras de firewall para ajustar as configurações de segurança de acordo com suas preferências. Por exemplo, você pode permitir que um aplicativo acesse a Internet, mas bloquear que ele acesse a rede local. Além disso, o Windows Defender Firewall pode ser configurado para notificá-lo quando um aplicativo tenta se conectar à rede ou à Internet, permitindo que você autorize ou bloqueie a conexão manualmente. Tudo isso pode ser gerenciado através do Microsoft Defender Security Center.

**Application Guard e Microsoft Defender SmartScreen**

Application Guard e Microsoft Defender SmartScreen são dois recursos de segurança diferentes integrados ao Windows 10.

O Application Guard é um recurso de segurança de navegação da Microsoft que permite que você navegue na web de forma mais segura. Ele cria uma instância de navegador isolada e protegida para que você possa navegar em sites desconhecidos ou suspeitos sem colocar em risco o resto de seu dispositivo. O Application Guard usa uma combinação de hardware e software para fornecer esse nível adicional de segurança.

Já o Microsoft Defender SmartScreen é um recurso de proteção contra phishing e ameaças de download que ajuda a proteger contra ataques online. Quando você tenta baixar um arquivo ou acessar um site, o Microsoft Defender SmartScreen verifica se o arquivo ou site estão em uma lista de ameaças conhecidas e, caso estejam, impede que você acesse ou baixe o arquivo. O Microsoft Defender SmartScreen também pode ser configurado para avisá-lo quando ele detecta comportamento suspeito, permitindo que você tome uma decisão informada sobre se deseja prosseguir.

Ambos os recursos são integrados ao Windows 10 e podem ser gerenciados através do Microsoft Defender Security Center.

**Windows Defender Credential Guard**

O Windows Defender Credential Guard é uma tecnologia de segurança de identidade integrada ao Windows 10 Enterprise. Ele protege as credenciais do usuário contra ameaças externas, como malware e vírus, mantendo-as em um ambiente seguro e isolado chamado "container". Isso ajuda a impedir que ataques tenham acesso a essas informações sensíveis e as usem para comprometer a segurança do dispositivo ou da rede.

O Windows Defender Credential Guard funciona criando um ambiente de segurança virtualizado e isolado chamado "container" para armazenar informações sensíveis, como credenciais do usuário. Quando o usuário faz login no dispositivo, as credenciais são armazenadas no container, e qualquer aplicativo ou processo que tente acessar essas informações deve passar por uma série de verificações de segurança antes de ser concedido acesso.

O Windows Defender Credential Guard usa tecnologias como a virtualização de segurança para fornecer esse nível adicional de segurança para as credenciais do usuário. Além disso, ele pode ser integrado a soluções de gerenciamento de identidade, como o Microsoft Azure Active Directory, para oferecer uma camada adicional de segurança para as informações de identidade.

O Windows Defender Credential Guard é uma tecnologia avançada de segurança de identidade e está disponível apenas para usuários do Windows 10 Enterprise.

**Tópicos Avançados**

- Implementação de políticas de autenticação multifatorial (MFA).
- Proteção de identidade com uso de certificados digitais.
- Uso de análise de comportamento para detecção de ameaças.
- Microssegmentação de rede para isolamento de sistemas críticos.
- Monitoramento constante de atividades de usuários e dispositivos.

Ferramentas adicionais do Windows 10:

- PowerShell: shell de linha de comando do Windows, usado para automação de tarefas administrativas;
- Hyper-V: plataforma de virtualização nativa do Windows 10, usada para criar máquinas virtuais;
- BitLocker: ferramenta de criptografia de disco que protege dados armazenados em discos rígidos;
- Remote Desktop: permite conexão remota a outros computadores;
- Windows Subsystem for Linux (WSL): permite a execução de aplicativos Linux diretamente no Windows 10.

PowerShell: é uma ferramenta de linha de comando usada para automatizar tarefas administrativas. Ele permite que os administradores do sistema criem scripts para executar tarefas repetitivas de gerenciamento de sistemas. Com o PowerShell, é possível automatizar tarefas de manutenção, gerenciamento de usuários, backups e muito mais.

Hyper-V: é uma plataforma de virtualização nativa do Windows 10 que permite criar máquinas virtuais. Com o Hyper-V, é possível criar vários sistemas operacionais em um único computador. Ele é usado para testar sistemas operacionais, aplicativos e outras configurações de sistema em Zero Trust é uma abordagem de segurança de rede que assume que tudo, incluindo usuários, dispositivos e aplicativos, são potencialmente não confiáveis e, portanto, não podem ser automaticamente confiáveis apenas por estarem na rede. Alguns tópicos avançados sobre Zero Trust incluem:

Implementação de políticas de autenticação multifatorial (MFA): as políticas de MFA exigem que os usuários forneçam mais de uma forma de autenticação, como uma senha e um código enviado por mensagem de texto, para acessar os recursos da rede. Isso adiciona uma camada extra de segurança, pois mesmo que a senha seja comprometida, o invasor não poderá acessar a rede sem o segundo fator de autenticação.

Proteção de identidade com uso de certificados digitais: os certificados digitais são usados para autenticar a identidade de usuários e dispositivos em uma rede. Eles criptografam o tráfego de rede, tornando mais difícil para um invasor interceptar e ler informações sensíveis.

Uso de análise de comportamento para detecção de ameaças: as soluções de análise de comportamento são usadas para detectar atividades maliciosas na rede, analisando o comportamento dos usuários, dispositivos e aplicativos. Eles procuram por padrões de atividade que possam ser indicativos de um ataque cibernético em andamento.

Microssegmentação de rede para isolamento de sistemas críticos: a microssegmentação envolve a criação de zonas distintas dentro de uma rede para isolar sistemas críticos. Isso ajuda a minimizar a superfície de ataque, tornando mais difícil para um invasor se mover lateralmente na rede.

Monitoramento constante de atividades de usuários e dispositivos: o monitoramento constante é essencial para detectar e responder rapidamente a atividades suspeitas. Ele também ajuda a garantir que as políticas de segurança estejam sendo cumpridas e a identificar vulnerabilidades que precisam ser corrigidas.

Referência Bibliográfica

BADDINI, Francisco Carlos; VALLE JUNIOR, Reinaldo do. **Implantação e Gerenciamento de Redes com Microsoft Windows 10 Pro**. 1. ed. Érica. 2015.