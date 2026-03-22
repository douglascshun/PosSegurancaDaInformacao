Antivírus é um programa/software instalado em desktops, notebooks, servidores, capazes de detectar, remover ou enviar para quarentena de, forma preventiva, agentes maliciosos e nocivos que roubam informações, danificam os computadores ou sequestram dados.
	- Endpoints: pontos de extremidade ou dispositivos
	- Agent ou Client: Software responsável pela coleta análise e tratamento dos riscos encontrados no dispositivos. Exemplo: Agentes de Censo do IBGE

# Antivírus de Primeira geração

- Primeiro antivírus foi desenvolvido em 1983 pelo Acadêmico Fred Cohen.
- Jhon MvAfee programador da NASA e da Lockheed desenvolveu um software de scanner automatizado de vírus. Gringo: The Dangerous Life os John McAffe -2016
- O funcionamento da engine do antivírus é uma metodologia de varredura ou escaneamento de arquivos, dlls, softwares em busca de códigos maliciosos através de assinaturas. 
# Post

![[Novos antivírus.png]]
	atenção: a técnica de detecção de ameaças através de `assinaturas já está defasada` há anos na indústria do AV - 2006

# Considerações sobre AV

- Quarentena / Exceções / Exclusões / Falso Positivo / Capacidade de Detecção
- Assinaturas atualizadas em hora e a importância da internet
- Consumo de recursos de hardware pela engine do antivírus e a análise do custo benefício.
- Senha para a desinstalação e usuário admin.

# Exemplo de um antivírus na cloud:
![[Bitdefender.png]]

# Análise Heurística
A análise de Heurística(Arte de inventar, de fazer descobertas; ciência que tem por objeto a descoberta dos fatos) é a engine de nova geração, é uma metodologia nova e proativa de detectar ameaças pelo seu comportamento (behavor), conjunto de processos e serviços é uma camada á ,ais na segurança. muitas vezes é utilizado IA /machine Learning (telemetria) para comparações e aprendizado de novas ameaças.

# Heurística

![[Logica da heuristica.png]]

![[heuristica.png]]

- NGAV - Nest Generation Antivírus - Versão Top de linha das principais fabricantes

- EDR / XDR - Endpoint Detection Response - Conjunto de módulos e IA que transforma o antigo AV em uma console de defesa unificada, repleta de ferramentas e recursos. É uma Suíte de aplicativos de Segurança

- Maior capacidade de detecção e menor falso positivo 

- Módulos, serviços e recursos: Análise por comportamento - Antimalware (proteção especifica contra ransomware) - Cofre de Senhas - Anti-Spam - Firewall Pessoal - VPN - Atualização Automática de Software e SO - Modulo Internet/Navegação - Limpeza e TuneUP - Dashboard Reports - Policy - IAM - DLP SandBox - Console de Gerenciamento - Suporte.

- Desenvolvimento seguro, segurança por padrão, pois AV atua a nível de aplicação. Exemplo: SQL Injection.

# Pago ou gratuito?

Gratuito:
Anúncios, baixa frequência de atualizações, recursos mínimos, falta de suporte, mas é melhor que nenhum AV.

Pago:
Console de Gerenciamento, últimos recursos e atualizações, mais módulos omo cofre de senha, antiSpam, VPN e anti-ransomware. Apenas as versões pagas são cloud native, ou seja, apenas pagando você terá acesso a um antivírus e suporte especializado por chat ou telefone