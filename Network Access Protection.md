[[Aula 2 Arquitetura de Segurança do Windows]]

NAP é uma tecnologia da Microsoft para controlar o acesso à rede de um computador, com base em sua integridade. O NAP pode restringir ou negar o acesso à rede para computadores que não estejam em conformidade com os requisitos de integridade definidos 

#### O NAP possui suporte para múltiplos métodos de imposição (tecnologia utilizada para o acesso em uma rede), dentre eles, temos:
- Internet Protocol Security (IPSec)
- Conexões de rede autenticadas pelo padrão 802.1x do IEEE
- Conexões VPN ou Terminal Service
- Dynamix Host Configuration Protocol (DHCP)


# NAP Arquitetura de Funcionamento:

![[Pasted image 20260305083001.png]]

# Componentes no lado do cliente:
`Cliente` são os computadores ou notebooks que possuem os componentes do NAP instalados e configurados. Devem enviar o seu estado de integridade para o servidor.

`Agente de integridade do sistema`, Também conhecido como SHA, é o componente responsável por verificar o estado de integridade do sistema.

`Agente NAP` processas as declarações de integridade do cliente e as envia para o servidor de administração do NAP.