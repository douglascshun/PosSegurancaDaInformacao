[[Aula 7 Proteção de dispositivos móveis]]


**Vulnerabilidades

`No dispositivo do cliente`: Dispositivos móveis são físicos e logicamente vulneráveis, pois o dispositivo pode cair, pode ser roubado, quebrado..

`Na transmissão de dadsos pelo ar`: Sistemas de segurança utilizados no link sem fio nem sempre garantem a segurança suficiente. Não significa que por simplesmente você estar conectado a uma rede é existe um grau de segurança nisso. A transmissão pelo ar permite que agentes mal intencionados capturem os dados, por isso implemente medidas de segurança.

`No provedor de acesso ou dentro de redes internas`: Processos de acesso a rede nem sempre garantem a identificação correta do usuário. O provedor de internet tem acesso direto a sua rede, verifique sobre o provedor pois em casos extremos ele pode até conseguir acesso a sua rede.


# Sistemas Operacionais de Celulares

- `Android (Google)`
- `iOS (Apple)`
- `HarmonyOS (Huawei)`
- `HyperOS (Xiaomi)`

Quando falamos na escolha do sistema operacional de dispositivos móveis para as empresas, vale a pena citar o fato da grande diferença que cada um deles oferece, por exemplo, sistemas android possuem a maior dominância do mercado atualmente mas isso trás pontos maior numero de explorações a vulnerabilidades e as vezes baixa vida útil do aparelho. IOS, ainda uma das maiores do mercado, porém possuí o foco um pouco mais trabalhado na segurança, sendo compensado no valor do produto..


**Ameaças comuns em dispositivos moveis:
- Vírus
- Worms
- Cavalos de Troia



**Senha de Acesso:

- `Dispositivos sem senha`
Não devem existir

- `Senhas fáceis de serem descobertas`
1234,senha, entrar, admin...

- `Métodos de digitação `
Marcas na tela



**Múltiplas formas de ataques comumente exploradas por agentes mal intencionados:

- `Mensagens de SMS` (Engenharia Social)
Famoso clique aqui e ganhe algo, normalmente pedem dados pessoais do usuários, ou acessos privilegiados a recursos seus

- `Navegação na Internet` (phishing)
Sites que buscam pegar dados seus, estabelecer privilégios dentro de seus dispositivos, te induzem a baixar programas ou arquivos modificados.

- `Anexoss de e-mails`(phishing)
Segue o mesmo conceito do phishing em SMS, onde te induzem a clicar em um link malicioso, ou baixar um arquivo modificado, o diferencial desse caso é que grande parte das vezes buscam isso por meio da imposição de urgência como "você tem tal prazo para clicar", "é sua ultima chance", "modifique sua senha pois seu login expirou, ou acessaram sua conta"

- `Bluetooh`
Bluejacking considerada a forma mais "leve" de ataque. O invasor envia mensagens não solicitadas (como cartões de visita eletrônicos) para o seu dispositivo, com o objetivo de geralmente é usado para pegadinhas ou marketing invasivo considerado com o grau de risco baixo, mas serve como um alerta de que seu Bluetooth está visível para estranhos. Bluesnarfing, este já é bem mais perigos, pois o invasor consegue acessar seu dispositivo para roubar informações sensíveis, costumar capturar lista de contatos, mensagens SMS, fotos, vídeos e até o seu calendário, normalmente o atacante explora vulnerabilidades no protocolo de troca de informações do Bluetooth. Bluebugging considerado um nível avançado de invasão, onde o atacante estabelece uma conexão que permite controlar remotamente o aparelho, com isso ele pode fazer chamadas, enviar mensagens e até ouvir suas conversas usando o microfone do celular, tudo sem você perceber.
Bluetooth Is Any Shape (ou BIAS) o ataque mais moderno que foca na falha de autenticação. O invasor "engana" dois dispositivos que já foram pareados anteriormente, fazendo-os acreditar que ele é um deles, contornando a segurança do pareamento original.

- `Cartões de memória`
Pode inserir códigos, instalar softwares, roubar informações e ter controle total do dispositivo **nunca 