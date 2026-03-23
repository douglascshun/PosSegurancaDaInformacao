[[Aula 1 Arquitetura de Nuvem]]

Cada camada uma aplicação, portanto a implementação depende do conhecimento sobre o uso pretendido!
	Antes de se contratar um serviço de computação em nuvem ou até mesmo implementar um para uso, é necessário que seja feito um estudo sobre o tipo de nuvem que será utilizado, uma vez que as necessidades e requisitos de negócio são inúmeros e diversos.

1. Nuvem publica:
Acesso mais comum, via navegador web e usa cobrança conforme o uso.
	Isso reduz custos de operação de TI e custos de concessão de infraestruturas. Apesar da possibilidade de redução de custos de infraestrutura, este modelo esbarra em questões de segurança de dados (acesso e armazenamento), de rede e de privacidade. 
	Exemplos conhecidos deste tipo de modelo são a  AWS (Amazon Web Services) e IBM Cloud.

 2. Nuvem Privada:
Com foco em segurança e disponibilidade dos recursos. Imagine uma empresa de entregas com suas próprias ruas e avenidas...
	A organização possui os recursos relacionados à infraestrutura, cabendo apenas definir o acesso e esses recursos e às aplicações lá obrigadas através da rede interna. Isto significa que a própria organização detentora do data center é a responsável pela administração dos recursos físicos.

3.  Nuvem Híbrida:
É a implementação das melhores características da Nuvem Pública e da Nuvem Privada.
	Ela consiste em ligar um recurso em Nuvem Privada a um ou mais recursos em Nuvem Pública. A vantagem é o fato de a organização poder armazenar dados críticos e de relevância ao negócio em nuvem privada e, ao mesmo tempo, ter a flexibilidade de aumentar ou diminuir o poder computacional através das nuvens públicas.

Cada camada da nuvem representa um nível de serviços.
	A arquitetura em nuvem é normalmente dividida em quatro camadas (Hardware, Infraestrutura, Plataforma e Aplicação), onde uma camada fornece serviços, sob demanda, ara a camada imediatamente acima.

# Arquitetura baseada em camadas da computação em nuvem

- Aplicação
SaaS - Software a Service

- Infraestrutura
IaaS - Infraestructure as a Service

- Plataforma
PaaS - Platform as a Service

- Hardware

# A arquitetura em camadas de Cloud Computing

`Camada de aplicação`:
É a camada responsável pela entrega do serviço da SaaS (Software as a Service). Portanto, onde estão a maioria das aplicações web para o usuário final.
	Ela armazena as aplicações e fornece serviços específicos, como Multimídia, Web Service. Além disso, ela permite abstrair o acesso às aplicações através da Internet e de forma remota, eliminando assim a necessidade de instalação da aplicação localmente por parte de cada usuário. Como exemplo é possível citar o GSuite da Google.

`Camada de plataforma`:
Onde o