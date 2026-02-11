[[Aula 7 Proteção de dispositivos móveis]]

# WPA-PSK


	 `Similar ao WEP`

##### 1. O Algoritmo de Criptografia (RC4)

Ambos utilizam o **RC4**, um algoritmo de cifragem de fluxo.

- **No WEP:** O RC4 era usado de forma muito ingênua, com chaves estáticas que nunca mudavam. Isso permitia que hackers quebrassem a senha em minutos apenas coletando pacotes.

- **No WPA:** Ele ainda usa o RC4, mas adicionou uma "camada" chamada **TKIP** (_Temporal Key Integrity Protocol_). O TKIP muda a chave de criptografia para cada pacote de dados, o que é muito mais seguro que o WEP, mas a base (o motor RC4) continua sendo a mesma.


### 2. Vulnerabilidade a Ataques de Dicionário

O sufixo **PSK** significa _Pre-Shared Key_ (Chave Pré-Compartilhada). É aquela senha que você digita no roteador.

- Tanto no WEP quanto no WPA-PSK, se um invasor capturar o processo de autenticação (o _handshake_), ele pode tentar descobrir a senha "offline" testando bilhões de combinações por segundo. Se a sua senha for simples, ambos caem da mesma forma.


### 3. Compatibilidade de Hardware

O WPA foi desenhado para ser uma **atualização de software** para dispositivos que rodavam WEP. Por causa dessa retrocompatibilidade, ele não pôde usar algoritmos muito pesados (como o AES, que veio só no WPA2), o que o torna tecnicamente "primo" do WEP em termos de estrutura de hardware.




	`Chave Compartilhada`

##### 1. O que é o WPA-PSK?

O termo significa **Wi-Fi Protected Access with Pre-Shared Key**. Diferente do modo "Enterprise" (que usa um servidor RADIUS e logins individuais), o modo PSK utiliza a mesma senha para todos os dispositivos.

##### 2. O Processo de "Fritura" da Chave (PBKDF2)

A senha que você digita no roteador (ex: `MinhaSenha123`) não é a chave que criptografa os dados. Para tornar o sistema mais seguro, o WPA-PSK utiliza um algoritmo chamado **PBKDF2** (_Password-Based Key Derivation Function 2_).

O processo funciona assim:

- **Input:** Sua Senha + o SSID da rede (o nome do Wi-Fi).

- **Processamento:** O algoritmo realiza **4096 iterações** de Hashing (SHA-1).

- **Output:** Gera uma **PMK (Pairwise Master Key)** de 256 bits.


> **Importante:** Como o nome da rede (SSID) faz parte do cálculo, usar o mesmo nome de rede do vizinho ("Wi-Fi-Casa", por exemplo) torna você mais vulnerável a ataques de **Rainbow Tables** (tabelas de senhas pré-computadas).

---

##### 3. O "Four-Way Handshake" (O aperto de mão)

Quando seu celular se conecta ao roteador, eles iniciam um processo de 4 etapas para provar que ambos conhecem a PSK, sem nunca enviá-la "pelo ar".

1. **Passo 1:** O roteador envia um número aleatório (**ANonce**) para o celular.

2. **Passo 2:** O celular cria seu próprio número (**SNonce**) e calcula um código de integridade. Ele envia isso ao roteador.

3. **Passo 3:** O roteador verifica se o código está certo e envia a chave de grupo (para broadcast).

4. **Passo 4:** O celular confirma que está pronto.


A partir daqui, é gerada uma chave temporária (**PTK**) que muda constantemente para criptografar o tráfego.

---

##### 4. Vulnerabilidades e Riscos

Vale destacar os pontos fracos:

- **Ataques de Dicionário:** O maior risco. O invasor captura o "Four-Way Handshake" e tenta descobrir a senha offline usando força bruta.

- **WPS (Wi-Fi Protected Setup):** Aquele botãozinho ou PIN de 8 dígitos. Se estiver ativo, ele permite que a PSK seja descoberta em minutos, ignorando a complexidade da senha.

- **KRACK Attack:** Uma vulnerabilidade descoberta em 2017 que explorava justamente o passo 3 do Handshake para reinstalar chaves já usadas.




	-`Troca de chaves automatizadas (Temporal Key Integrity Protocol - TKIP)`


O **TKIP** foi a grande "mágica" que salvou o Wi-Fi no início dos anos 2000. Como vimos, o WEP era um desastre porque a chave era estática: se você descobrisse a chave uma vez, conseguia ler todo o tráfego para sempre.

O TKIP introduziu a **troca de chaves automatizada**, funcionando como um sistema que troca o "segredo" da conversa a cada poucos segundos.

Aqui está como esse processo de troca funciona dentro do WPA-PSK:

##### O Mecanismo de Chaves Dinâmicas

Diferente do WEP, onde a chave que você digitava era a mesma usada para criptografar os dados, no WPA-PSK com TKIP existem níveis de chaves:

1. **Chave Mestra (PMK):** É gerada a partir da senha (passphrase) que você digita no Wi-Fi. Ela nunca é transmitida pelo ar.

2. **Chave Temporal (TK):** É aqui que o TKIP brilha. A partir da chave mestra, o protocolo gera uma chave única para cada cliente conectado.

3. **Chave por Pacote:** O TKIP mistura o endereço MAC do dispositivo e o número de sequência do pacote com a Chave Temporal.


**O resultado:** Cada pacote de dados enviado pelo ar possui uma chave de criptografia diferente. Mesmo que um hacker consiga quebrar a chave de _um_ pacote, ela já terá mudado no pacote seguinte.

#### As 3 defesas principais do TKIP:

- **Hashing de Chaves:** Mistura a chave base com um contador de pacotes, garantindo que a mesma chave nunca seja usada duas vezes.

- **Message Integrity Check (MIC):** Apelidado de "Michael", é um código adicionado ao pacote para garantir que ninguém alterou os dados no meio do caminho (evita ataques de injeção).

- **Sequence Counter:** Impede ataques de "Replay" (onde um hacker captura um comando legítimo, como "abrir porta", e o reenvia mais tarde), pois o receptor descarta pacotes com números de sequência fora de ordem ou repetidos.


---

### Por que o TKIP "aposentou"?

Apesar de ser genial para a época, o TKIP ainda rodava sobre o algoritmo **RC4**. Com o tempo, matemáticos encontraram formas de prever partes dessa "mistura" de chaves. Além disso, o processo de ficar misturando chaves via software pesava muito no processador dos roteadores, limitando a velocidade da rede a **54 Mbps**.

Por isso, ele foi substituído pelo **CCMP (AES)** no WPA2, que faz tudo isso por hardware e de forma muito mais segura.

> **Curiosidade:** Se você configurar seu roteador moderno como "WPA2-TKIP", sua velocidade provavelmente será limitada a níveis de internet antiga (802.11g), mesmo que seu Wi-Fi seja de última geração.




	-`Vetor de inicialização de 48 bits`

O WEP usava um Vetor de Inicialização (IV) de apenas 24 bits. Era como ter um segredo que se repetia a cada 16 milhões de frases. Para um hacker, era como montar um quebra-cabeça com peças repetidas.

O WPA2 elevou o jogo para **48 bits**. Parece pouco? Matematicamente, saltamos de milhões para **281 TRILHÕES** de combinações.

Esse número é tão grande que garante que cada pacote de dados enviado pelo seu Wi-Fi seja único e, mais importante, protege você contra ataques de 'Replay' (quando um invasor tenta reenviar seus dados para ganhar acesso).

No mundo da cibersegurança, os detalhes invisíveis no nível do bit são o que mantêm os seus dados bancários seguros enquanto você navega no Wi-Fi do aeroporto.


# Infraestrutura

- Requer um servidor de autenticação (RADIUS);
Programa que vem dentro do roteador, dentro desse programa costuma vir o protocolo, a senha e mais informações, permitindo também configurações, como limitar o numero de dispositivos conectados.

- Opcionalmente pode necessitar de uma infraestrutura de chaves públicas (PKI/ICP);


- Isola o tráfego da rede sem fio, para a rede cabeada (DMZ - Zona Desmilitarizada)
Um exemplo prático de onde pode ser interessante é uma loja com wifi aberto, onde você isola a rede interna da loja, com seus dispositivos da rede que você disponibiliza para os clientes acessarem.

- Provê autenticação para usuários da rede sem fio terem acesso a rede cabeada