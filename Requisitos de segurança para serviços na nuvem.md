[[Aula 6 Proteção de serviços de nuvem]]

A segurança em ambiente disposto em nuvem exige, em princípio, grande parte dos controles em segurança dispostos e exigidos em ambiente de infraestrutura tradicional também conhecido como On Premisses.

Conhecendo as necessidades em jogo, espera-se que tecnologias, processos e pessoas colaborem para a adoção de um modelo de segurança a devida proteção destes dados em nuvem.

Essa proteção pode envolver adoção de soluções que visam evitar ou dificultar o vazamento de dados DLP (Data Loss Prevention), Assim como soluções que visam evitar o acesso aos dados por pessoas não autorizadas, incluindo controles de acesso e criptografia.

# DLP
Data Loss Prevention
## Como o DLP funciona?

O funcionamento do DLP baseia-se em três etapas principais: **Identificação**, **Monitoramento** e **Prevenção**.

### 1. Identificação (O que proteger?)

O sistema primeiro precisa saber o que é importante. Ele usa técnicas de inspeção de conteúdo para encontrar dados sensíveis:

- **Casamento de padrões:** Procura por estruturas específicas, como o formato de um CPF ou cartão de crédito.

- **Fingerprinting (Impressão Digital):** O sistema tira uma "foto" de um documento confidencial e bloqueia qualquer arquivo que se pareça com ele.

- **Palavras-chave:** Identifica termos como "Confidencial", "Projeto Secreto" ou "Demonstrativo Financeiro".


### 2. Monitoramento (Onde os dados estão?)

O DLP atua em três estados diferentes da informação:

- **Dados em repouso (Data at Rest):** Arquivos armazenados em servidores, bancos de dados ou na nuvem.

- **Dados em movimento (Data in Motion):** Informações trafegando pela rede, como e-mails, mensagens de chat ou transferências via FTP.

- **Dados em uso (Data in Use):** O que o usuário está fazendo no momento, como copiar arquivos para um USB ou dar um "Print Screen".


### 3. Prevenção (O que fazer?)

Quando uma violação de política é detectada, o DLP pode tomar ações automáticas:

- **Bloquear:** Impede o envio do e-mail ou a cópia para o pendrive.

- **Criptografar:** Permite o envio, mas protege o arquivo com senha automaticamente.

- **Notificar:** Envia um alerta para o administrador de TI e avisa o usuário sobre a política da empresa.


# Recomendações de Segurança

- `Gestão de identidade e acesso`: Implemente meios de verificar se quem é, de fato é quem diz ser.

- `Segurança física`: Só permita a entrada de funcionários na empresa que estiverem com seus crachás devidamente apresentados e verificados.

- `Inteligência, monitoramento e prevenção de ameaças`: Monitore as informações, tenha formas de conseguir acompanha-las, verifica-las, pode ser por meio de equipe interna ou externa.
  
  - `Criptografia`: Tenha sempre os dados e informações blindados para que não vazem.

- `Teste de Vulnerabilidade`: Sempre que possível faça testes de vulnerabilidades como o de phishing internamente na empresa, ou de penetração de software para não ter dados vazados dentro de suas aplicações.
  
  - `Microssegmentação`: Serviços em vários lugares, semente a rede em várias partes conforme a necessidade, por exemplo não misturar a rede do financeiro com a rede da produção.

- `Firewalls da próxima geração`: Bloqueios novos constantementes, tampando novas brechas e vetores de ataques explorados