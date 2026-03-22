[[Network Security]]

**Introdução**

Compreender o que é monitoramento, gerenciamento e gestão de log e eventos de redes com SIEM e conhecer o NOC/SOC.

**Objetivos da aula**

- Quem não monitora não mede, vamos aprender a monitorar!
- SIEM, ferramenta importante para gerenciamento e observabilidade;
- Definir NOC e quando usar;
- Definir SOC e entender sua finalidade.

**Resumo**

O monitoramento contínuo de sistemas é outro fator que não apenas ajuda a trazer visibilidade de um determinado problema, mas também ajuda nas tarefas proativas e reativas.

Seja esse monitoramento feito por meio de um sistema que usa protocolo SNMP, seja feito por meio de outros softwares de gerenciamento que usam características específicas de sistema operacional para obter informações de disponibilidade, o importante é ter uma visão contínua do sistema e do que está ocorrendo. Assim como existe a necessidade de se criar uma linha de base de segurança, também se faz necessário uma linha de base de performance. Geralmente a criação de uma linha de base de performance permite estabelecer o que é normal em um determinado ambiente. Monitorar traz os benefícios da prevenção e da melhoria contínua. Ferramentas como Nagios, Grafana, Zabbix, Prometheus e o Site24x7 podemos monitorar sistemas, recursos, hosts, redes, links de internet, sites etc.

O SIEM, ainda dentro do monitoramento, é um software extremamente versátil, útil e ao mesmo tempo complexo de ser implementado. O SIEM nada mais é do que um coletor de logs e eventos de vários dispositivos de hardware ou sistemas, ele agrega em uma única console, informações provenientes de vários dispositivos e sistemas, depois consolida essas informações, ou seja, realiza uma sanitização destas informações pois muitas são repetidas ou desnecessárias, depois agrega as informações de mesma categoria, classifica e faz a correlação em sua parte final onde pode gerar insights para os analistas de ocorrências presentes e futuras, essa remediação faz do SIEM um monitor contínuo de performance e disponibilidade. Muito utilizado em grandes centros de operações como NOC e SOC.

![https://safewayconsultoria.com/siem-seguranca-em-rede/. Acesso em 14/02/2023.](https://paperx-dex-assets.s3.sa-east-1.amazonaws.com/images/1677710466117-eGi9f6MNs4.png "https://safewayconsultoria.com/siem-seguranca-em-rede/. Acesso em 14/02/2023.")

[https://safewayconsultoria.com/siem-seguranca-em-rede/](https://safewayconsultoria.com/siem-seguranca-em-rede/). Acesso em 14/02/2023.

Os NOC são centros de operações de rede, eles monitoram e gerenciam a infraestrutura de rede de sua corporação ou de um cliente específico. O time é composto por especialistas em redes de computadores, podem monitorar redes de dados como de VoIP, cuidam para manter a qualidade do serviço de rede em alto nível de SLA com disponibilidade e velocidade, além, é claro, de manter o ambiente seguro e prevenir invasões, monitorando acessos indevidos e antecipando-se a vários problemas no ambiente.

Os SOC também são centros de operações, porém de segurança. Aqui o escopo é mais abrangente além da rede os analistas, monitoram sistemas, hardware, sites, aplicações e ERP em busca de atividades maliciosas ou tentativas de invasão, podem realizar testes de capacidade e têm um protocolo para agirem em caso de incidente: outro time é acionado, o CIRT, uma equipe de especialista para resposta a incidentes, que segue várias medidas, frameworks e normal para melhorar a maturidade de segurança da empresa, mas se um violação é detectada esta equipe é capaz de atuar e mitigar a ameaça, investigar a causa, reportar e analisar a causa raiz para que o erro não se repita.

Monitoramento é fundamental para uma empresa que não quer ser surpreendida por ataques, vazamento de dados ou indisponibilidade de sistemas. Não é um processo barato, mas pode compensar, dependendo do risco em que sua empresa esteja.

**Tópicos avançados**

**Importância do Monitoramento:** [https://www.strongsecurity.com.br/blog/importancia-de-monitorar-a-seguranca-da-informacao-para-sua-gestao/](https://www.strongsecurity.com.br/blog/importancia-de-monitorar-a-seguranca-da-informacao-para-sua-gestao/). **Acesso em 14/02/2023.**

**SIEM:** [https://seginfo.com.br/2020/09/03/o-que-e-siem-e-quais-suas-principais-funcionalidades/](https://seginfo.com.br/2020/09/03/o-que-e-siem-e-quais-suas-principais-funcionalidades/). **Acesso em 14/02/2023.**

**SOC NOC e CIRT:** [https://www.youtube.com/watch?](https://www.youtube.com/watch?v=0yYySTtyCxM)[v=0yYySTtyCxM](https://www.youtube.com/watch?v=0yYySTtyCxM). **Acesso em 14/02/2023.**

**Referência Bibliográfica**

TANENBAUM, FEAMSTER & WETHERALL. **Redes de Computadores**. 6ª Edição. São Paulo, Bookman; 2021.

FONTES, Edison **Segurança da informação. O usuário faz a diferença**. 1ª edição. São Paulo, Editora Saraiva; 2016.

HINTZBERGEN, Jule; HINTZBERGEN, Kees. **Fundamentos de Segurança da Informação: com base na ISO 27001 e na ISO 27002**. 1ª edição, São Paulo, Ed.Brasport, 2018.