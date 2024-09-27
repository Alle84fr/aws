1. Serverless Computing" é o termo utilizado para a arquitetura de execução de serviços sem a necessidade de um servidor dedicado em "espera 24/7" pelos comandos. O serviço da AWS que nativamente lhe permite implantar serviços de computação sem servidor é:

a - AWS Elastic Beanstalk

b - N.D.A

c - Amazon EC2

d - AWS Lambda

e - Amazon Elastic Container Service

resposta: d - AWS Lambda

&nbsp;

2. Por que é recomendado dividir uma VPC em sub-redes pública e privada ?

a - N.D.A

b - Para garantir um número par de sub-redes, ou seja, se uma cair a outra atuará como contingência em caso de falha
 
c - Para permitir o acesso direto às máquinas da sub-rede privada por um agente externo, por padrão uma VPC apenas permite o acesso à 1 sub-rede

d - Para permitir a organização e distribuição de serviços entre os ambientes de desenvolvimento, por exemplo, QA/Testes fica na pública e Produção fica na privada

e - Não é recomendado segregar as sub-redes em pública e privada, isso só aumenta a complexidade de dificulta a administração do ambiente

Resposta: a - N.D.A.

&nbsp;

3. Sua aplicação WEB precisa de quatro instâncias para oferecer suporte a tráfego o tempo todo. No último dia do mês, o tráfego triplica. Qual é a maneira mais econômica de lidar com esse padrão ?

a - Execute quatro instâncias sob demanda constantemente e adicione mais oito instâncias reservadas no último dia de cada mês

b - Execute 12 instâncias reservadas o tempo todo.
 
c - Execute quatro instâncias sob demanda constantemente e adicione mais oito instâncias sob demanda no último dia de cada mês 

d - N.D.A

e - Execute quatro instâncias reservadas constantemente e adicione mais oito instâncias sob demanda no último dia de cada mês

Resposta: e - Execute quatro instâncias reservadas constantemente e adicione mais oito instâncias sob demanda no último dia de cada mês

&nbsp;


4. Na AWS, dentro de uma VPC, ao sub dividir uma sub-rede com uma máscara de IP 192.168.10.0/24 quantos IPs serão permitidos para serem distribuídos entre as máquinas daquela sub-rede ?

a - N.D.A

b - No IP, cada parte vai de 0 a 999, porém, o /24 limita a quantidade de máquinas, de 192.168.10.0 até 192.168.10.24, ou seja, 24 máquinas

c - No IP uma máscara de /24 significa que são aceitos 24bits ou 2^24, ou seja, 16.777.216 máquinas

d - No IP, cada parte tem 8 bits, então o /24 fixa os primeiros 24 bits ( ou 3 partes de 8 bits cada ). Uma parte permite números de 0 a 256, mas, a AWS libera apenas 251 IPs por bloco, reservando alguns para uso ou controle interno, ou seja, 251 máquinas

e - No IP, cada parte tem 8 bits, então o /24 fixa os primeiros 24 bits ( ou 3 partes de 8 bits cada ). Uma parte permite números de 0 a 256, ou seja, 256 máquinas.
 
Resposta: d - No IP, cada parte tem 8 bits, então o /24 fixa os primeiros 24 bits ( ou 3 partes de 8 bits cada ). Uma parte permite números de 0 a 256, mas, a AWS libera apenas 251 IPs por bloco, reservando alguns para uso ou controle interno, ou seja, 251 máquinas

5. Assinale a alternativa INCORRETA sobre os modelos de contratação na AWS:

a - PaaS - refere-se à contratação de Plataforma como serviço. Significa que o cliente recebe da AWS toda a parte de rede, armazenamento, servidores e instalação do serviço que desejar, mas fica responsável por parte da configuração e o uso daquela aplicação

b - IaaS - refere-se à contratação de Infraestrutura como serviço. Significa que o cliente recebe da AWS toda a parte de rede, armazenamento e servidores, mas fica responsável pela instalação e configuração dos serviços e aplicações que desejar usar

c - N.D.A

d - SaaS - refere-se à contratação de Software como serviço. Significa que o cliente recebe da AWS um serviço completo, pronto para ser utilizado

e - CaaS - referese à contratação de Cloud como serviço. Significa que o cliente recebe da AWS todos os serviços disponíveis para serem utilizados conforme sua necessidade imediata

resposta: e - CaaS - referese à contratação de Cloud como serviço. Significa que o cliente recebe da AWS todos os serviços disponíveis para serem utilizados conforme sua necessidade imediata

&nbsp;

6. Sobre Os planos de contratação e reserva de instâncias na AWS, assinale a alternativa INCORRETA:

a - N.D.A

b - AURI ( All Upfront Reserved Instance ) refere-se à contratação de serviços por 1 ou 3 anos, onde toda a quantia é paga à vista. É o modelo de reserva com o maior desconto, mas requer o maior investimento inicial

c - PURI ( Partial Upfront Reserved Instance ) refere-se à contratação de serviços por 1 ou 3 anos, onde metade da quantia é paga à vista. É o modelo de reserva com o desconto intermediário, precissa de algum investimento inicial e o restante é pago em parcelas mensais

d - OURI ( OnDemand Upfront Reserved Instance ) refere-se à contratação de serviços por 5 ou 7 anos, onde o pagamento à vista é feito sob demanda. É o modelo de reserva onde o cliente paga quando quiser e quando puder, baseado em suas disponibilidades financeiras e capacidade de investimento
 
e - NURI ( No Upfront Reserved Instance ) refere-se à contratação de serviços por 1 ou 3 anos, onde nenhuma quantia é paga à vista. É o modelo de reserva com o menor desconto, mas permite um pagamento mensal mais flexível, sem a necessidade de investimento inicial.

resultado: d - OURI ( OnDemand Upfront Reserved Instance ) refere-se à contratação de serviços por 5 ou 7 anos, onde o pagamento à vista é feito sob demanda. É o modelo de reserva onde o cliente paga quando quiser e quando puder, baseado em suas disponibilidades financeiras e capacidade de investimento

&nbsp;

7. Ao a calculadora de preços da AWS se deparou com a seguinte descrição para máquinas EC2 "T3.Medium", o que se podem concluir sobre esta sigla ? 
Assinale a alternativa INCORRETA:

a - O "medium" indica que há uma escala de tamanho dentro daquela família, indicando sua força em termos computacionais ( número de núcleos, memória, banda de rede, etc ) provavelmente a T3.Medium é superior à T3.Small e Inferior à T3.Large

b - O "T" indica que há uma geração de máquinas, ou seja, a T é uma geração superior à "S" e é de uma geração inferior à "U", seguindo uma ordem alfabética de evolução ou progressão de poder computacional
 
c - "T" refere-se à família da máquina indicando que a máquina é recomendada para fins de computação geral, ou seja, ela não faz parte das famílias de usos específicos como memória, uso computacional, etc

d - O "3" em "T3" refere-se à versão ou geração daquela família. Em sua especificação estão detalhes como o tipo de processador e tecnologias utilizadas por aquele tipo de máquina. Pode existir ou ter existido uma geração anterior "T2" e existe ou pode existir uma geração posterior "T4"

e - N.D.A

resposta: b - O "T" indica que há uma geração de máquinas, ou seja, a T é uma geração superior à "S" e é de uma geração inferior à "U", seguindo uma ordem alfabética de evolução ou progressão de poder computacional

&nbsp;

8. Como uma empresa com infraestrutura híbrida, ou seja, com máquinas e serviços  em um datacenter externo à nuvem, pode ser capaz de acessar as máquinas localizadas em sua sub-rede privada ?

a - A AWS não permite a adoção de infraestrutura híbrida, ou seja, metade da rede dentro e metade fora da nuvem, isto seria uma grande falha de segurança

b - É possível clonar as máquinas entre as sub-redes privada e pública de forma que acessar a máquina pública é o mesmo que acessar a máquina privada

c - Se uma sub-rede privada foi criada com o propósito de isolar e proteger os serviços mais críticos, impedindo que um agente externo inicie conexões e acesse diretamente tais máquinas, é impossível que a empresa acesse tais máquinas na sub-rede privada simplesmente por uma questão de segurança

d - É possível abrir uma VPN para uma das máquinas internas da sub-rede publica, e desta acessar de forma segura as máquinas da sub-rede privada.
 
e - N.D.A

resposta: d - É possível abrir uma VPN para uma das máquinas internas da sub-rede publica, e desta acessar de forma segura as máquinas da sub-rede privada.

&nbsp;

9. Como um administrador de sistema incluiria uma camada adicional de segurança de login ao Console de Gerenciamento da AWS de um usuário ?

a - Usar o Amazon Cloud Directory

b- Habilitar o AWS CloudTrail

c- N.D.A.

d - Auditor funções do AWS Identity and Access Management ( IAM)
 
e - Habilitar autenticação multifator ( MFA )

Resposta: e - Habilitar autenticação multifator ( MFA )

&nbsp;

10. Sobre a portabilidade ou utilização de licenças de software na AWS, asssinale a alternativa INCORRETA:

a -A AWS lhe permite adquirir licenças diretamente com os fabricantes/desenvolvedores e utilizá-las, por exemplo, em serviços de computação como máquinas EC2. Por exemplo, você pode comprar licenças de um anti-virús e utilizá-la em suas máquinas EC2 sem intermediação da AWS

b - A AWS tem a opção de aquisição de licenças juntamente com seus serviços, por exemplo, é possível alocar um serviço computacional EC2 que já venha com a licença do Windows embutida no preço a ser pago 'por hora'

c - A AWS não permite utilização de nenhum tipo de licença de software que ela não venda, se aquele serviço não for oferecido pela AWS ele não pode ser utilizado em sua núvem. Por exemplo: o único anti virús permitido na núvem da AWS é o vendido por ela mesma
 
d - A AWS não se responsabiliza para utilização de software não licenciado em suas máquinas, ou seja, utilizar software pirateado é de responsabilidade do cliente, assim como quaisquer penalidades legais

e - N.D.A

resposta: c - A AWS não permite utilização de nenhum tipo de licença de software que ela não venda, se aquele serviço não for oferecido pela AWS ele não pode ser utilizado em sua núvem. Por exemplo: o único anti virús permitido na núvem da AWS é o vendido por ela mesma

&nbsp;

11. Qual ferramenta da AWS permite explorar os serviços da AWS e criar uma estimativa para o custo de seus casos de uso na AWS?

a - Relatório de custos e uso da AWS.

b- Painel de faturamento da AWS.

c - N.D.A.

d - Orçamento da AWS.

e - Calculadura de preços da AWS.

resposta: e - Calculadura de preços da AWS

&nbsp;

12. Sobre containers e como eles se diferenciam de máquinas virtuais tradicionais.
Assinale a alternativa INCORRETA:

a - Containers são equivalentes à máquinas virtuais em sua concepção, porém, as imagens das máquinas virtuais são chamadas de AMIs e as imagens de containers são chamadas de Dockers

b - Containers se diferenciam de máquinas virtuais por não precisarem da emulação completa de um sistema operacional dentro de sua instância para permitir a execução e operação de seu conteúdo, tornando-se bem mais leves em sua natureza
 
c - N.D.A

d - Soluções como ECS ( Elastic Container Service ) são capazes de orquestrar/gerenciar a criação e distribuição dos containers, realizando inclusive o balanceamento de carga entre entre múltiplas máquinas que hospedam containers

e - Containers são instâncias gerenciadas e controladas pelo Docker. São capaz de executar dentro de seus ambientes simulados, quaisquer comandos que uma máquina virtual executaria.

Resposta: e - Containers são equivalentes à máquinas virtuais em sua concepção, porém, as imagens das máquinas virtuais são chamadas de AMIs e as imagens de containers são chamadas de Dockers

&nbsp;

13. Sobre as vantagens e desvantagens de utilização de serviços na nuvem, assinale a alternativa INCORRETA:

a - A contratação de serviços na nuvem lhe proporciona a contratação de recursos sob demanda, ou seja, lhe permite alocar mais ou menos recursos baseado em sua necessidade imediata

b - A maior desvantagem na aquisição de serviços na nuvem é que não é possível ter uma arquitetura mista, ou seja, parte dos recursos ou servidores dentro e outra fora da nuvem. Também não é possível utilizar duas núvens ( AWS, azure, google, etc ) ao mesmo tempo, uma vez escolhando uma, você é obrigado a ficar apenas com ela
 
c - A contratação de serviços na nuvem lhe proporciona flexibilidade e alcance global em instantes, permitindo a alocação de servidores em múltiplas regiões/países

d - Não é necessário um investimento incial tão alto em comparação com serviços OnPremisses como compra de equipamentos, licenças e alocação física dos servidores.

e - N.D.A.

resposta: b - A maior desvantagem na aquisição de serviços na nuvem é que não é possível ter uma arquitetura mista, ou seja, parte dos recursos ou servidores dentro e outra fora da nuvem. Também não é possível utilizar duas núvens ( AWS, azure, google, etc ) ao mesmo tempo, uma vez escolhando uma, você é obrigado a ficar apenas com ela

&nbsp;

14. Sobre a cobrança de serviços na AWS, assinale a alternativa INCORRETA:

a - Há cobrança por computação, ou seja, máquina ligada/ativa

b - Há cobrança por envio de dados para fora daquela região da AWS, ou seja, transferência de dados externos

c - Há cobrança pelo número de usuários que vão utilizar o serviço do cliente, ou seja, quanto mais clientes tiver, mais terá que repassar uma parte dos lucros à AWS

d - N.D.A.
 
e - Há cobrança por armazenamento, ou seja, espaço em disco alocado/reservado

Resposta: c - Há cobrança pelo número de usuários que vão utilizar o serviço do cliente, ou seja, quanto mais clientes tiver, mais terá que repassar uma parte dos lucros à AWS

&nbsp;

15. Sobre a definição de AMIs e o que está incluído dentro de uma AMI, assinale a alternativa INCORRETA:

a - N.D.A.

b - AMIs vem do termo Amazon Machine Image ou Imagem de modelo, são moldes cuja cobrança é realizadas apenas pelos bits de armazenamento ( espaço ) que elas ocupam, não há cobrança pela geração das AMIs em si. Um modelo pode ser utilizado para a geração de N novas instâncias.

c - AMIs são backups de máquinas, que podem ser ligados/desligados quando necessário para assumirem o papel ou função da máquina original de quem foram clonados. Cada Imagem se torna uma, e apenas uma, instância, então, ao precisar de 10 máquinas, você precisa gerar 10 modelos e promover cada um destes à uma instância.

d - AMIs são modelos de imagens da Amazon, que salvam um modelo para o volume raiz da Instância, permitindo que novas instâncias sejam geradas a partir deste modelo.

e - AMIs são moldes de Instâncias que contém todas as informações relevantes da instância original como volumes e permissões de execução. Mas a AMI em si não é uma máquina virtual em si.
 
Resposta: c - AMIs são backups de máquinas, que podem ser ligados/desligados quando necessário para assumirem o papel ou função da máquina original de quem foram clonados. Cada Imagem se torna uma, e apenas uma, instância, então, ao precisar de 10 máquinas, você precisa gerar 10 modelos e promover cada um destes à uma instância.

&nbsp;

16. Sobre as definições e diferenças entre grupos de segurança e ACLs ( Access Control List ), assinale a alternativa INCORRETA:

a - ACLs permitem a especificação de rotas e regras de entrada e saída nas portas específicas dos serviços habilitados. Similar à um "firewall" mas atuando no nível da sub-rede.

b - N.D.A.

c - Grupos de segurança e ACLs são ambas opções de "firewall" quem podem ser usadas para proteger sua VPC.

d - Seja usando grupos de segurança ou ACLs é possível bloquear o acesso à todas as portas de uma máquina ou sub-rede exceto às portas 80 (http) ou 443 (https).
 
e - Grupos de segurança permitem a especificação de regras de entrada e saída nas portas específicas dos serviços habilitados. Similar à um "firewall" mas atuando no nível da instância.

Resposta: b - N.D.A.

&nbsp;

17. Qual o nome do serviço de hospedagem de sites na nuvem oferecido na modalidade PaaS , poupando o desenvolvedor do trabalho de instalar e gerenciar o servidor web ?

a - Amazon Elastic Container Service

b - N.D.A.
 
c - AWS Opswork

d - AWS Elastic Beanstalk

e - AWS CloudFormation

Resposta: AWS Elastic Beanstalk

&nbsp;

18. Sobre a arquitetura entre VPCs, sub-redes e as zonas de disponibilidade de uma região específica. Assinale a alternativa correta:

a - N.D.A.

b - Uma sub-rede contém N VPCs distribuídas em N zonas de disponibilidade que estão distribuídas em N regiões. Ou seja, é recomendado espalhar o máximo possível suas zonas entre as VPCs, zonas e regiões.

c - Uma zona de disponibilidade não pode conter mais do que uma VPC, ou seja, vão existir tantas zonas de disponibilidade quantas VPCs criadas pelos clientes.

d - Uma VPC não pode ser distribuída entre múltiplas zonas de disponibilidade, portanto, todas as sub-redes de uma VPC obrigatoriamente estão dentro de uma única zona de disponibilidade.

e - Uma VPC poderia ( ou deveria ) ter suas sub-redes divididas entre múltiplas zonas de disponibilidade por uma questão de segurança, ex: Uma sub-rede publica na zona 1a e outra sub-rede publica na zona 1b, se a 1a cair, as máquinas na sub-rede localizadas na zona de disponibilidade 1b devem assumir para evitar a queda dos serviços.

resposta: e - Uma VPC poderia ( ou deveria ) ter suas sub-redes divididas entre múltiplas zonas de disponibilidade por uma questão de segurança, ex: Uma sub-rede publica na zona 1a e outra sub-rede publica na zona 1b, se a 1a cair, as máquinas na sub-rede localizadas na zona de disponibilidade 1b devem assumir para evitar a queda dos serviços.

&nbsp;

19. É um tipo de serviço contratado na AWS na modalidade IaaS:

a - Amazon RDS - O Amazon Relational Database Service é um serviço web que facilita a configuração, a operação e a escalabilidade de um banco de dados relacional na nuvem. Lhe é entregue um banco de dados já pronto, garantindo-lhe a capacidade de administração daquele banco de dados.

b - CloudFront - O Amazon CloudFront é um serviço de entrega de conteúdo ( CDN ) que ajuda você a melhorar o desempenho, a confiabilidade e a disponibilidade de seus sites e aplicativos.

c - N.D.A.

d - Amazon EC2 - O Amazon Elastic Compute Cloud é um serviço web para lançamento e gerenciamento de Linux/UNIX e Windows Server instânciasnos data centers da Amazon. Lhe é entregue uma máquina pronta para uso com administração à nível do sistema operacional.
 
e - Amazon S3 - O Amazon S3 é o armazenamento para a Internet. Você pode usá-lo3 para armazenar e recuperar qualquer volume de dados, a qualquer momento, de qualquer lugar na Web. Lhe é entregue um espaço para armazenamento pronto, com a capacidade de gerenciamento dos arquivos

resposta: d - Amazon EC2 - O Amazon Elastic Compute Cloud é um serviço web para lançamento e gerenciamento de Linux/UNIX e Windows Server instânciasnos data centers da Amazon. Lhe é entregue uma máquina pronta para uso com administração à nível do sistema operacional.

&nbsp;

20. No modelo de responsabilidade compartilhada a definição que NÃO faz parte da segurança da nuvem é:

a - N.D.A.

b - Criptografia de dados em repouso e dados em trânsito das 
aplicações instanciadas pelo contratante
 
c - Proteção da infraestrutura global

d - Segurança física das instalações em que os serviços operam

e  - Conformidade com padrões e regulamentos de segurança da computação

resposta: Criptografia de dados em repouso e dados em trânsito das aplicações instanciadas pelo contratante