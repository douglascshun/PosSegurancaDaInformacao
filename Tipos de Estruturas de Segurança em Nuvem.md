[[Aula 6 Segurança na nuvem]]

Organização Internacional para Padronização (ISO)
Essa Instituição padroniza o padrão de comportamento para empresas. Como a ISO 9001, essa Certificação tem como intuito verificar a qualidade da empresa em determinados requisitos impostos pela ISO. Essa instituição possuí um fórum de auditores que fazem simpósios, trocam informações e constroem juntos por meio de aceitação da maioria documentos que possibilitam o chamado de auditorias buscando estabelecer o padrão no documento descrito.

A segurança em nuvem baseada em normas ISO concentra-se principalmente na ISO/IEC 27017 funcionando como extensões da ISO/IEC 27001 Elas definem responsabilidades compartilhadas entre provedores e clientes, abordando riscos, privacidade e conformidade técnica. 

# Principais Normas ISO para Segurança em Nuvem

- **ISO/IEC 27017 (2015):** É um código de conduta que fornece diretrizes adicionais de segurança para provedores e clientes de serviços em nuvem, baseando-se na ISO/IEC 27002. Ela aborda quem é responsável pelo quê, remoção/devolução de ativos e proteção de ambiente virtual.

- **ISO/IEC 27018 (2019):** Focada na proteção de Dados Pessoais (PII) na nuvem, atuando como um código de conduta para provedores que atuam como processadores de dados. Ela garante a conformidade com leis de privacidade.

- **ISO/IEC 27001:** A norma base para Gestão de Segurança da Informação, necessária para a extensão da ISO 27017.

Enquanto as normas ISO são focadas em certificações internacionais, as normas e publicações do National Institute of Standards and Technology (NIST) são amplamente reconhecidas como o padrão ouro técnico para definir a arquitetura e segurança da nuvem. 




Aqui estão os pilares do NIST para computação em nuvem:

# 1. Definição e Conceitos (NIST SP 800-145)

Esta é a "bíblia" da nuvem. Ela estabelece a linguagem comum utilizada por quase todos os provedores (AWS, Azure, Google Cloud). Define: 

-  Características Essenciais: Autosserviço sob demanda, amplo acesso à rede, pool de recursos, elasticidade rápida e serviço mensurável.
- Modelos de Serviço: SaaS (Software), PaaS (Plataforma) e IaaS (Infraestrutura).
- Modelos de Implantação: Nuvem pública, privada, híbrida e comunitária. 

# 2. Segurança e Privacidade (NIST SP 800-144)

Fornece diretrizes práticas para a segurança em **nuvens públicas**. Foca em: 

- Gestão de Riscos: Como avaliar a segurança do provedor antes da contratação.
- Isolamento de Dados: Orientações sobre criptografia e multi-tenancy (compartilhamento de hardware por vários clientes). 

#  3. Arquitetura de Referência (NIST SP 500-292)

Define quem é quem no ecossistema de nuvem através de **5 atores principais**: 

- **Cloud Consumer**: Quem usa o serviço.
- **Cloud Provider**: Quem fornece a infraestrutura/serviço.
- **Cloud Auditor**: Quem avalia a segurança e o desempenho.
- **Cloud Broker**: Quem gerencia o uso e a entrega entre diferentes provedores.
- **Cloud Carrier**: Quem provê a conectividade física (telecom). 

# 4. Controles de Segurança (NIST SP 800-53)

Embora seja um padrão geral de cibersegurança para o governo dos EUA, é o catálogo de controles mais robusto utilizado por provedores de nuvem para obter certificações de alto nível (como o FedRAMP).