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



	-`Vetor de inicialização de 48 bits`