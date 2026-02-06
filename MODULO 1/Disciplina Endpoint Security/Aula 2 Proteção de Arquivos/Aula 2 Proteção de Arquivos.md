[[Endpoint Security]]

## Proteção de Arquivos

**Introdução**

Nesse módulo abordaremos os conceitos básicos sobre sistemas de arquivos, o funcionamento de criptografia de arquivos, controle de acesso, controle de integridade, certificados digitais e a importância do backup.

**Objetivos da aula**

Analisar as técnicas para proteção do sistema de arquivos, bem como as formas de se proteger de possíveis falhas que possam ocorrer.

**Resumo**

**Conceitos básicos sobre sistemas de arquivos**

A proteção de arquivos é uma parte importante da segurança cibernética. Os arquivos confidenciais, como informações financeiras, dados pessoais ou informações comerciais, devem ser protegidos contra acesso não autorizado ou vazamento.  
Para proteger os arquivos, as organizações podem usar técnicas como criptografia, gerenciamento de acesso e políticas de segurança rigorosas para controlar o acesso aos arquivos. Além disso, as organizações devem realizar backups regulares e manter cópias de segurança de seus arquivos em locais separados para garantir a recuperação de dados em caso de falha de hardware ou ataques cibernéticos.  
Um sistema de arquivos é um método usado por um sistema operacional para armazenar, organizar e acessar arquivos em um dispositivo de armazenamento. Aqui estão alguns conceitos básicos sobre sistemas de arquivos:  
- Diretório: um diretório, também chamado de pasta, é uma unidade organizacional básica em um sistema de arquivos. Ele contém arquivos e outros diretórios.  
- Arquivo: um arquivo é um conjunto de informações armazenadas em um dispositivo de armazenamento. Os arquivos têm nomes e extensões que indicam seu tipo e conteúdo.  
- Extensão de arquivo: a extensão de arquivo é um conjunto de caracteres que vem após o nome do arquivo e indica o tipo de arquivo.  
- Caminho: o caminho é a localização de um arquivo ou diretório em um sistema de arquivos. Ele pode ser um caminho absoluto, que começa na raiz do sistema de arquivos, ou um caminho relativo, que começa no diretório atual.  
- Permissões de arquivo: as permissões de arquivo controlam quem pode acessar, ler, gravar ou executar um arquivo. As permissões de arquivo podem ser definidas para o proprietário do arquivo, o grupo de usuários e outros usuários.  
- Formatação de disco: a formatação de disco é o processo de preparar um dispositivo de armazenamento para ser usado como um sistema de arquivos. A formatação cria uma estrutura para armazenar arquivos e diretórios e pode apagar todos os dados existentes no dispositivo.  
- Fragmentação de arquivos: a fragmentação de arquivos ocorre quando um arquivo é dividido em pedaços e armazenado em diferentes partes do disco. Isso pode ocorrer quando o espaço livre no disco não é grande o suficiente para armazenar o arquivo inteiro em um só lugar. A fragmentação pode afetar o desempenho do sistema de arquivos, tornando a leitura e gravação de arquivos mais lenta.  
Esses são apenas alguns conceitos básicos sobre sistemas de arquivos. Há muitos outros aspectos envolvidos, como diferentes tipos de sistemas de arquivos, sistemas de arquivos em rede e sistemas de arquivos distribuídos, que podem ser mais complexos.

Alguns exemplos de sistemas de arquivos incluem:

NTFS (New Technology File System): É o sistema de arquivos padrão para o Windows. Ele permite a criação de pastas e subpastas, bem como a gestão de permissões de arquivos e diretórios.

HFS (Hierarchical File System): É o sistema de arquivos padrão para o MacOS. Ele permite a organização de arquivos em pastas e subpastas, além de fornecer suporte a arquivos grandes e compressão de dados.

EXT4 (Fourth Extended File System): É o sistema de arquivos padrão para o Linux. Ele permite o gerenciamento de arquivos grandes, além de suportar a fragmentação e a compressão de dados.

FAT32 (File Allocation Table 32-bit): É um sistema de arquivos antigo que foi usado em dispositivos de armazenamento externos e unidades flash USB. Ele é compatível com muitos sistemas operacionais, mas não suporta arquivos grandes ou pastas com muitos arquivos.

exFAT (Extended File Allocation Table): É um sistema de arquivos que permite a compatibilidade com dispositivos de armazenamento externos e unidades flash USB em diferentes sistemas operacionais, além de suportar arquivos grandes.

A criptografia é uma técnica usada para proteger informações confidenciais de acesso não autorizado ou divulgação durante a transmissão e armazenamento. Ela envolve o uso de algoritmos matemáticos para codificar e decodificar dados, tornando-os ilegíveis para pessoas que não possuam a chave de criptografia correta.

**Criptografia**

Existem dois tipos de criptografia: criptografia simétrica e criptografia assimétrica.  
A criptografia simétrica é um tipo de criptografia em que a mesma chave é usada para criptografar e descriptografar os dados. Isso significa que a chave precisa ser compartilhada entre as partes que desejam se comunicar com segurança. Esse método é eficaz, mas pode ser menos seguro, pois a chave deve ser compartilhada entre as partes, o que aumenta o risco de comprometimento.  
A criptografia assimétrica, também conhecida como criptografia de chave pública, é um tipo de criptografia que usa duas chaves diferentes - uma chave pública e uma chave privada. A chave pública é usada para criptografar os dados, enquanto a chave privada é usada para descriptografar os dados. A chave pública é amplamente distribuída, enquanto a chave privada é mantida em segredo. Esse método é mais seguro do que a criptografia simétrica, pois a chave privada não precisa ser compartilhada.  
A criptografia é amplamente usada na internet para proteger informações confidenciais, como senhas, informações financeiras e dados pessoais. A criptografia é usada em muitas tecnologias, como SSL (Secure Sockets Layer) e TLS (Transport Layer Security), que criptografam a comunicação entre um navegador da web e um servidor, garantindo que as informações sejam protegidas contra interceptação e violação de dados. A criptografia também é usada em aplicativos de mensagens instantâneas, e-mails e outras formas de comunicação eletrônica.

**Criptografia de arquivos**

A criptografia de arquivos é o processo de codificar informações confidenciais em arquivos para protegê-los de acesso não autorizado. Isso pode ser feito usando uma chave secreta ou um algoritmo de criptografia. A decodificação dos arquivos só pode ser realizada com acesso à chave ou senha correta. A criptografia de arquivos é uma forma importante de proteger a privacidade e a segurança de dados.

**Criptografia clássica**

O conceito mais simples de criptografia é a de que se trata da ciência que estuda as técnicas que transformam dados em códigos que só podem ser decifrados por quem tenha a chave de acesso.

Criptografia vem do grego:

Kryptós (cripto) = secreto

gráphein (grafia) = escrita

A criptografia trata-se de técnicas mais elaboradas que a esteganografia, pois na esteganografia, como visto anteriormente, não há tratamento do dado, a preocupação é apenas a de escondê-la bem para que não possa ser encontrada, já a criptografia não se preocupa tanto em esconder o dado, mas sim a de transformá-la de tal forma que se encontrada e/ou interceptada não possa ser decifrada senão por aquele que possua a chave.

A força da criptografia está, portanto, na força de sua chave, no entanto, esta também é a sua fragilidade, já que caso ela seja descoberta a decifragem se torna um processo simples, revelando assim a informação no seu formato puro.

A criptografia pode ser entendida como processo sistematizado de transformação da mensagem original em uma mensagem ininteligível com uso de técnica específica que requer uma chave.

A mensagem, não pode ser entendida a não ser pelas pessoas que sabem ou conhecem a chave de forma a recuperar a mensagem original.

Assim, a mensagem, mesmo sendo interceptada em seu trânsito, resiste à decifragem, caso a chave não seja conhecida pelo agente estranho.  
  
Os componentes que envolvem a criptografia são:

- Mensagem limpa: mensagem antes de ser criptografada;
- Técnica de criptografia: método utilizado para criptografar;
- Chave: agente utilizado pela técnica para criptografar e descriptografar;
- Mensagem criptografada: mensagem cifrada que será enviada ao receptor pelo emissor.

Alguns exemplos de criptografia não computacional:

- Escrita: só entendida por quem a conhece e usa;
- Idioma: só entendida por quem a conhece e usa;
-  Máquina Enigma.

Alguns exemplos de criptografia computacional:

- Certificação digital.
- DES;
- 3DES;
- Blowfish.

**Hash**

Hash, em criptografia, é uma técnica que transforma uma mensagem ou arquivo de dados de tamanho variável em uma sequência de caracteres de tamanho fixo, chamado de hash ou valor de resumo. Essa sequência de caracteres é gerada a partir de um algoritmo matemático específico que calcula o hash usando os dados da mensagem.

A principal finalidade de um hash é permitir que grandes quantidades de dados sejam verificadas de forma rápida e eficiente. Quando um arquivo é transmitido pela internet, por exemplo, pode haver o risco de o arquivo ser corrompido durante a transmissão. Com o uso de um hash, o destinatário pode verificar rapidamente se o arquivo que recebeu é idêntico ao original, comparando o valor de hash gerado a partir do arquivo recebido com o valor de hash original.

Além disso, os hashes são amplamente utilizados em criptografia para garantir a integridade e autenticidade dos dados. Eles são usados para garantir que os dados não foram alterados ou adulterados durante o armazenamento ou a transmissão, e também são usados para verificar a autenticidade dos dados, permitindo que as partes envolvidas verifiquem a identidade do remetente e a autenticidade dos dados.

Os algoritmos de hash mais comuns incluem MD5, SHA-1, SHA-256 e SHA-3. No entanto, alguns desses algoritmos são considerados obsoletos e vulneráveis a ataques de segurança, e recomenda-se o uso de algoritmos mais fortes e seguros, como SHA-3 e SHA-256.

**Função Hash**

A matemática sempre esteve intimamente relacionada à esteganografia e criptografia, e desta forma o hashing não poderia ficar distante deste contexto. O hash pode ser explicado de forma didática pela matemática, já que se trata de uma função matemática. As funções matemáticas básicas como injetora, sobrejetora e bijetora serão abordadas de forma bastante simples para que o contexto de hash seja entendido também de uma forma simples.

**Algoritmo Hash**  
  
Um algoritmo Hash é um conjunto de instruções matemáticas que convertem dados de entrada de tamanho variável em um valor de tamanho fixo, chamado de hash ou valor de resumo. O objetivo de um algoritmo de hash é fornecer uma forma rápida e eficiente de verificar a integridade dos dados e a autenticidade das informações transmitidas.  
O processo de criação de um hash começa com a entrada dos dados a serem processados, que são passados pelo algoritmo de hash. O algoritmo processa esses dados e produz um valor de hash, que é uma sequência de caracteres alfanuméricos. Esse valor de hash é geralmente representado como uma sequência hexadecimal, que consiste em uma combinação de números e letras.  
A principal propriedade de um algoritmo de hash é a sua capacidade de produzir um valor de hash único para cada conjunto de dados de entrada. Isso significa que dois conjuntos diferentes de dados sempre gerarão valores de hash diferentes. Além disso, qualquer alteração nos dados de entrada irá produzir um valor de hash completamente diferente.  
Os algoritmos de hash são amplamente utilizados na criptografia e segurança da informação. Eles são usados para verificar a integridade dos dados durante a transmissão e armazenamento, bem como para garantir a autenticidade dos dados. Os algoritmos de hash mais comuns incluem MD5, SHA-1, SHA-256, SHA-512 e SHA-3. No entanto, alguns desses algoritmos são considerados obsoletos e vulneráveis a ataques de segurança, e recomenda-se o uso de algoritmos mais fortes e seguros, como SHA-256 e SHA-3.

**Certificado digital**

Certificado digital é um documento eletrônico que contém informações sobre a identidade de uma pessoa, empresa ou instituição, e é usado para verificar a autenticidade dessas informações na Internet. Ele é emitido por uma autoridade certificadora (AC) que atesta a autenticidade da identidade do titular do certificado, por meio de uma assinatura digital.  
O certificado digital funciona como uma identidade eletrônica, que permite a realização de transações digitais seguras, como a autenticação de usuários em sistemas, a assinatura eletrônica de documentos, o envio de mensagens criptografadas, entre outras atividades.  
O processo de emissão de um certificado digital envolve a verificação da identidade do titular, que é feita por meio de documentos de identificação pessoal e comprovantes de endereço. Uma vez verificada a identidade do titular, a autoridade certificadora emite o certificado digital, que é armazenado em um dispositivo físico, como um token USB ou smart card, ou pode ser instalado diretamente no computador do titular.  
O uso de certificados digitais é amplamente adotado em diversos setores, como no comércio eletrônico, na área bancária, no governo eletrônico, na saúde, entre outros. A sua utilização garante a autenticidade e integridade dos dados, além de fornecer segurança para as transações realizadas na Internet.

**Backup e restore**

Backup é uma cópia de segurança dos dados armazenados em um dispositivo, como um computador, servidor, dispositivo móvel ou outro dispositivo de armazenamento. O backup é uma medida de segurança essencial para proteger os dados contra perda acidental, corrupção ou danos ao dispositivo original.  
O processo de backup envolve a cópia dos dados armazenados em um dispositivo e a transferência para um local de armazenamento secundário, como um disco rígido externo, um servidor de backup ou a nuvem. O backup pode ser realizado manualmente ou com o uso de software de backup automatizado, que permite a configuração de agendamentos para que o processo de backup seja feito periodicamente, sem a necessidade de intervenção do usuário.  
Existem diferentes tipos de backup, que variam de acordo com a frequência de execução e o nível de proteção dos dados. Entre os tipos de backup mais comuns, estão:

- Backup completo: cópia de todos os dados armazenados em um dispositivo.
- Backup incremental: cópia dos dados que foram alterados ou adicionados desde o último backup.
- Backup diferencial: cópia dos dados que foram alterados desde o último backup completo.

O backup é uma prática recomendada para garantir a segurança dos dados importantes. É importante armazenar as cópias de backup em locais seguros e fora do local onde os dados originais estão armazenados, para que em caso de desastres naturais, incêndios, roubos ou outras situações, os dados possam ser recuperados a partir da cópia de backup.  
Restore, também conhecido como recuperação de dados, é o processo de restaurar os dados salvos em uma cópia de backup para o dispositivo original ou para um novo dispositivo. O restore é necessário quando os dados originais são perdidos, corrompidos ou danificados, ou quando é necessário transferir os dados para um novo dispositivo. O processo de restore pode ser realizado manualmente ou com o uso de software de backup automatizado, que permite a recuperação dos dados em poucos cliques. Em geral, os programas de backup possuem opções para a seleção dos dados a serem restaurados e para a escolha do local de destino dos dados recuperados. O processo de restore é importante para garantir a disponibilidade e a integridade dos dados. É importante lembrar que o processo de restore só é eficiente se o backup foi feito corretamente e se a cópia de backup está armazenada em um local seguro e confiável. Além disso, é importante testar regularmente o processo de restore, para verificar se ele está funcionando corretamente e se os dados podem ser recuperados em caso de necessidade.

**Tópicos avançados**

A proteção de arquivos é um tópico importante para garantir a segurança e a privacidade dos dados armazenados em dispositivos eletrônicos. Alguns tópicos avançados relacionados a proteção de arquivos incluem:  
Criptografia de arquivos: A criptografia é o processo de codificar dados de forma que só possam ser lidos por pessoas autorizadas que possuem a chave de descriptografia correta. A criptografia de arquivos pode ser realizada usando algoritmos de criptografia avançados, como AES (Advanced Encryption Standard) ou RSA (Rivest-Shamir-Adleman).  
Controle de acesso: O controle de acesso é uma técnica que limita o acesso aos arquivos apenas para usuários autorizados. Isso pode ser feito definindo permissões de acesso para usuários ou grupos de usuários específicos.  
Backup e recuperação de arquivos: É importante ter um plano de backup e recuperação de arquivos em caso de perda de dados, corrupção de arquivos ou ataques cibernéticos. Os backups devem ser realizados regularmente e armazenados em locais seguros.  
Autenticação multifator: A autenticação multifator (MFA) é um método de segurança que exige que os usuários forneçam mais de uma forma de autenticação para acessar um arquivo ou dispositivo. Por exemplo, pode ser necessário fornecer uma senha e um código enviado por mensagem de texto.  
Firewall de arquivos: Um firewall de arquivos é um software que monitora o tráfego de rede em busca de tentativas de acesso não autorizadas a arquivos. Ele pode ser usado para bloquear tentativas de acesso suspeitas ou permitir apenas conexões de dispositivos e usuários autorizados.

Esses são alguns exemplos de tópicos avançados em proteção de arquivos. A segurança cibernética é um campo em constante evolução, e é importante manter-se atualizado com as melhores práticas e tecnologias disponíveis para proteger seus dados.

Referência Bibliográfica

BARROS, Eulan. **Entendendo os Conceitos de Backup, Restore e Recuperação de Desastres (+ Estudo de Caso com o Software Livre Bacula).** 1. ed. Ciência Moderna, 2007.