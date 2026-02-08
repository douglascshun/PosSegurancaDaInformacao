[[Aula 4 Segurança Endpoint Windows]]

# Sumário

## 1 - Zero trust no Windows
o que é e como funciona ?

## 2 -Microsoft Defender Antivírus
O que é e como funciona?

## 3 - Microsoft Defender e Criptografia 
Entendendo a criptografia voltada para Microsoft.

## 4 - Windows Defender Firewall 
Funcionamento do firewall do Windows.

## 5 - Application Guard e Microsoft Defender SmartScreen
Entendendo as aplicações.

## 6 - Windows Defender Credential Guard
Entendendo as aplicações.




# Zero trust no Windows

`Confiança zero, verifíque.`

Não confie no usuário nem no sistema, sempre implemente medidas de segurança robustas.

Uma solução baseada em Zero Trust assume que não é possessível garantir que um usuário é confiável usando única e exclusivamente sua localização (perímetro).

É preciso garantir formas de verificação explicita de que o usuário X, é de fato o X e o não o Z. Para se garantir esse nível é preciso, focar na identidade.

`O NIST Públicos em 2020 um paper bem bacana falando sobre o modelo Zero Trust.`

Nele os autores defendem que uma solução deve focar em proteger recursos como ativos, serviços, contas, fluxos de trabalho, contas de rede e outros, não apenas segmentos de rede, visto que estes deixaram de ser a principal preocupação em um ambiente protegido. 



## Existem três princípios no modelo.

- `Verifique explicitamente`: Sempre autorize e autentique baseado em todas as informações disponíveis.

- `Use o menor provilégio de acesso o possível`: Não dê permissão além da necessária. Siga a ideia do JIT/JEA(Just-InTime / Just-Enough- Access).

- `Assuma que brechas existe`: Garanta, sempre que possível criptografia de ponta ponta e recursos para evitar movimentação lateral.


## Simbologia Zero Tust:
![[Simbologia Zero Trust.png]]

# Como iniciar rumo ao Zero Trust usando o Microsoft 365?

- `MFA` - Duplo fator de autenticação.

- `Acesso Condicional` - O coração do Zero Trust. Esse recurso será um de seus melhores amigos na missão Zero Trust, com ele é possível analisar 