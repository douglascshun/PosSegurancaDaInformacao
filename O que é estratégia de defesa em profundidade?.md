[[Aula 4 Abordagem de Defesa de Segurança em Rede]]

Ela é usada para cobrir todos os ângulos de segurança de uma empresa, sendo redundante quando necessário.

Se uma linha de defesa for comprometida, camadas adicionais de defesa ficam a postos para garantir que as ameaças não passem por nenhuma brecha de segurança.

# Esses três controles formam a arquitetura de uma estratégia de Defesa em Profundidade

- Os `controles físicos` são as medidas de segurança que protegem sistemas de TI contra danos físicos. Exemplos de controles físicos incluem guardas de segurança e tranca nas portas.

- Os `controles administrativos` se referem a políticas e procedimentos implementados por uma organização para seus funcionários.

- Os `controles técnicos` são métodos de proteção em camadas que protegem sistemas de rede. A proteção de hardwares, softwares e redes fazem parte dos controle técnicos específicos de uma empresa.



`Segurança física `
Proteção de entrada dos prédios comerciais, guardas, muros, câmeras de segurança, controle de acesso e restrição de acesso ao data center do prédio, sistema de supressão de fogo. 

`Identidade de acesso`
 Gerenciamento eficiente do Active Directory e do Azure Active Directory, que adota principio de menor privilegio e fornece recursos de identificação de usuário multi-fator.

`Perímetro`
O principal sistema de proteção no perímetro é o firewall, um sistema de segurança de rede que monitora e controla o tráfego de entrada e saída com base em regras de segurança predeterminadas.

`Rede`
Podemos fazer uso das zonas desmilitarizadas  (DMZ) ou controlar o acesso com Virtual Private Network (VPN), proteção de comunicações com criptografia do transporte. Uso de Intrusion Detection Systems (IDS) ou Intrusion Preventivo Systems (IPS).

`Computer/host`
Refere-se a atividades, aplicativos ou cargas de trabalho que requerem mais recursos de processamento.
Não podemos pensar somente em um  computador pois podemos nos referir a sistemas na Nuvem. Como esse "layer" é muito vasto, podemos imaginar um host mesmo onde temos Patch Management, antivírus, politicas e controle de acesso.

`Aplicação`
Com relação as aplicações podem ter um Aplication Gateways ou Web Application Firewall (WAF) além de controle de acesso e monitoramento de uso.

`Dados`
Muitos dos controles acima já ajudaram a proteger de certa forma os dados, mas ainda sim, temos que periodicamente, aplicar a verificação de acesso, auditoria, criptografia e classificação.
Atenção especial aos dados que são de backups e dos dados em descanso (Data -At-Rest).

`Acesso com o menor privilégio`
É o princípio de conceder aos usuários permissão para acessar apenas os sistemas e recursos de que precisam para sua função. Isso ajuda a minimizar o risco para o resto da rede se as credenciais de um usuário forem comprometidas e um usuário não autorizado tentar realizar um ataque ou acessar dados sensíveis.

`Autenticação multifator (MFA)`
Como o próprio nome sugere, reque várias formas de autenticação para verificar a identidade de um usuário ou dispositivo antes de permitir o acesso a uma rede ou aplicativo.

`Segmentação de rede`
Ajuda a limitar a exposição de sistemas e dados internos a fornecedores, contratados e outros usuários externos.
Por exemplo, configurar redes sem fio separadas para usuários internos e externos permite que as organizações protejam melhor as informações confidenc