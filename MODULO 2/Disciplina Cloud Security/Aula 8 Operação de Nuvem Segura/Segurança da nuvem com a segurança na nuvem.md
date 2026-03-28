[[Aula 8 Operação de Nuvem Segura]]

A segurança na computação em nuvem depende do provedor e do usuário. 
	Portanto vamos colocar a mão na massa e conhecer os casos e atos onde provedor e usuário falham na segurança na computação em nuvem, e como fazer para evitar esses problemas. 

# # Modelo de responsabilidade compartilhada AWS

Acesse:
https://aws.amazon.com/pt/compliance/shared-responsibility-model/

## Visão geral
Segurança e conformidade constituem uma responsabilidade compartilhada entre a AWS e o cliente. Esse modelo compartilhado pode auxiliar a reduzir os encargos operacionais do cliente à medida que a AWS opera, gerencia e controla os componentes do sistema operacional do host e a camada de virtualização, até a segurança física das instalações em que o serviço opera. O cliente assume a gestão e a responsabilidade pelo sistema operacional convidado (inclusive atualizações e patches de segurança), por outros softwares de aplicativos associados e pela configuração do firewall do grupo de segurança fornecido pela AWS. Os clientes devem examinar cuidadosamente os serviços que escolherem, pois suas respectivas responsabilidades variam de acordo com os serviços utilizados; a integração desses serviços ao seu ambiente de TI e as leis e regulamentos aplicáveis. A natureza dessas responsabilidades compartilhadas também oferece a flexibilidade e o controle do cliente necessários para a implantação. Como pode ser visto no gráfico abaixo, esta distinção entre responsabilidades é denominada normalmente como segurança “da” nuvem versus segurança “na” nuvem.
![[Modelo de responsabilidade compartilhada AWS.png]]