[[Aula 2 Arquitetura de Segurança do Windows]]

Internet Protocol Security é um conjunto seguro de protocolos de rede que autentica e criptografa pacotes de dados para fornecer comunicação criptografada e segura entre dois computadores em uma rede de protocolo da internet. É usado em redes privadas virtuais (VPNs)
- TLS  - Transport Layer Security
- SSH - Security Shell

O IPsec é um padrão aberto como parte do pacote IPv4 e utiliza os seguintes protocolos para executar várias funções: 

# Authentication Headers (AH)

- O cabeçalho de autenticação (AH) é um membro do conjunto de protocolos IPsec.

- Usage of IPsec Authentication Header format in Tunnel and Transport modes.

![[Pasted image 20260305084527.png]]

# Encapsulating Security Payloads (ESP):

- Usage os IPsec Encapsulating Security Payload (ESP) in Tunnel and Transport modes.

![[Pasted image 20260305084639.png]]
# Internet Security Association and Key Management Protocol (ISAKMP)

- Modelos de operações 
- Os Protocolos IPsec AH e ESP podem ser implementados em um modo de transporte host a host, bem como em um modeo de encapsulamento de rede.

![[Pasted image 20260305084858.png]]

Uma política IPsec é um conjunto de regras que determinam qual tipo de tráfego IP precisa ser protegido usado IPsec e como proteger esse tráfego. Apenas uma política IPsec pode estar ativa em um computador ao mesmo tempo.

	O Protocolo de Internet Autenticado (AuthIP) é um novo protocolo de troca de chaves que expande o IKE da seguinte maneira:

- Credenciais do usuário: NTLM, Kerberos, certificados.
- Certificados de integridade da NAP (proteção de Acesso à rede).
- Credenciais anônima, usada para autenticação opcional.
- Combinação de credenciais. Por exemplo uma combinação de credenciais Kerberos de computador e usuário.