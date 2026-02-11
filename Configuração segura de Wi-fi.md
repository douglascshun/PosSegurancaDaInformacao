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
- `Chave Compartilhada`
- `Troca de chaves automatizadas (Temporal Key Integrity Protocol - TKIP)`
- Vetor de inicialização de 48 bits