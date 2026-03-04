[[Aula 2 Arquitetura de Segurança do Windows]]

A funcionalidade básica de um firewall é controlar o tráfego de entrada e saída e escolher se deseja bloquear uma conexão específica ou deixá-la passar com base no conjunto definido de regras de segurança.

# Lógica de um Firewall:
![[Logica de um Firewall.png]]

Ao abrir o Windows Defender Firewall pela primeira vez, você poderá ver as configurações padrão aplicáveis ao computador local.


# Diferenças de perfil no firewall do Windows:

1 - Perfil de Domínio: usado para redes em que há um sistema de autenticação de conta em um controlador de domínio de Active Directory.

2 - Perfil Privado: projetado para rede menores e melhor usado em redes pessoais, como uma rede inicial.

3 - Perfil Público: projetado com maior segurança em mente para redes públicas, como hotspots Wi-Fi, cafeterias, aeroportos, hotéis ou lojas.


# Configuração de I/O padrão:
![[Configuracao de I O padrao.png]]





# Regras de I/O, selecionando novas regras
A Interface para adicionar uma nova regra tem esta aparência:
![[Regras de I O selecionando novas regras.png]]




# Caixa de diálogo para permitir o acesso à um determinado aplicativo:

![[permitir o acesso a um determinado aplicativo.png]]



# Windows Defender por padrão bloqueia tudo, ao menos que se configure uma exceção:  

![[excecao para evitar bloqueio.png]]

	As configurações de mesclagem de regras permitem ou impedem que os administradores locais criem suas próprias regras de firewall, além das regras obtidas na Política de Grupos

# Customização do perfil: 
![[Pasted image 20260304160401.png]]