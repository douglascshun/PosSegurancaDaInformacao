[[Aula 3 Técnicas para proteção de redes]]

# Camada de Rede (Modelo OSI)

- `Switchs:`

Uma das técnicas de proteção é inicialmente partir de que o Switch deve estar fisicamente trancado em um armário ou sala com chaves. Após proteger a camada física, precisamos pensar em boas práticas, ou seja uma das coisas é deixar abertas as portas que estou usando, não se deve deixar uma porta ativa e fora de uso, o que impõe mais uma barreira impedindo que o atacante acesse a rede plugando em uma das portas do Switch.

Deve-se também trocar o IP, do usuário, o login e senha. Uma das formas de ataque mais normais de ataque é a negligencia nessa parte da configuração. O atacante pode fácil mente entrar na internet baixar o manual de configuração do dispositivo e obter as credenciais padrão, juntamente ao endereço logico de fabrica o que facilita direcionar um vetor de ataque.

Ativar configurações sem saber sobre suas funcionalidades e riscos, como o SNMP, que cria o compartilhamento de arquivos entre todos os dispositivos dentro daquela rede permitindo que qualquer um que consiga acesso a esse espaço lógico habilitado publique e acesse informações lá dentro, o que muita das vezes quando habilitado e não bem estabelecida uma cultura rígida sobre isso, acarreta em usuários internos poste informações sensíveis dentro desse espaço. 

- `MAC:`

Use a parte lógica ao favor da proteção aplique filtros de MAC e Firewall pra impedir acessos indevidos de dispositivos não autorizados.