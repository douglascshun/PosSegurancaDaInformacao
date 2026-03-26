[[Aula 6 Segurança de Aplicação na Nuvem]]

As soluções de nuvem representam uma revolução em termos de tecnologia.
	No entanto, embora a computação em nuvem tenha sido enaltecida por sua promessa de redução de custos, muitos hesitam em utiliza-la por incertezas quanto à segurança.
		Como toda tecnologia, a nuvem traz algumas vulnerabilidades, e já existem ataques mal-intencionados

A grande maioria sabe que existem vulnerabilidades, portanto suas formações profissionais já trabalham com os processos que visam mitigar os problemas.

# Visão geral da computação em nuvem
![[visao geral da computacao em nuvem.png]]

Seria a a aversão a nuvem uma vulnerabilidade?
	Mesmo diante das várias possibilidades de fazer economias, as lideranças das organizações relutam em mover informações, softwares e outros serviços para a nuvem. Isso deve à necessidade de considerar todos os riscos envolvidos.

A virtualização e o compartilhamento de recursos são pontos fracos da Computação na Nuvem:
	Discos compartilhados, computadores virtuais ou redes virtuais (VLANs)
		Drivers genéricos que emulam hardware
			Vulnerabilidades no hypervisor, pois permitem a execução de códigos no hosts com privilégio do hypervisor 
				Rootkits, baseados em máquinas virtuais 
					Execução de ataques de negação de serviço em uma maquina virtual

Se os dados ou outros recursos exigem um ambiente protegido devido a leis, normas ou regulamentos do segmento específico em que a empresa atua, a abordagem utilizada precisará respeita-los.
	A solução mais recomendável para esse cenário é uma nuvem privada ou, possivelmente uma nuvem hibrida, com dados confi