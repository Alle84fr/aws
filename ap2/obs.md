1. Primeira fase

Criar uma VPC com as seguintes características:

<i> para criar uma Virtual Privete Cloud deve entrar no site da AWS academy - AWS Academy Learner Lab [89219], neste caso, módulo - laboratório de aprendizagem da AWS Academy - Star lab </i>

* 1.1. A VPC deve ter a máscara de sub rede /16

<i> mascara de rede/subrede - calcula o tamanho de uma rede/ barramento - determinia que é rede e quem é host.

ip - 1° parte é rede, não muda, e o host é quantidade de máquina que pode conectar.

 "Imagine um prédio, ele tem 15 andares, cada andar é um rede, como cada andar tem seu n° próprio, o mesmo acontece com a rede, o numero é único.

Em cada andar há um número de apartamentos, estes apartamentos tem, como início do seu número a referência do andar, então, anda um inicia com um, andar quinze inicia com 15, e neste "endereço", no final, acrescenta o valor do "lote", que pode ser repetido nas outras redes, então, 1° andar tem apt 1.1, 1.2, 1.3 e 1.4, no andar 15° tem 15.1, 15.2, 15.3 e 15.4. (PMG Academy)

 mascara de rede fala quantos bits vai para cada lado, se para andar/rede ou se para host/apto
 
 A divisão é em 4, cada parte 8 bits que vai do 0 a 255. 

/8 - <span style="color:rgb(171, 255, 79);"> o n° nesta parte resprenta a rede, que é de 8 bitis . </span> <span style="color:rgb(8, 189, 189);"> os n°s nesta parte resprentam host/computadores, que é de 8 bitis cada . </span> ex: <span style="color:rgb(171, 255, 79);"> 14 .  </span> <span style="color:rgb(8, 189, 189);"> 0 . 0. 1. </span>

8bits + 0bits + 0bits + 0bits -   CiRD /8    Máscara é 255.0.0.0

&nbsp;

/16 - <span style="color:rgb(171, 255, 79);"> os 2 n°s resprentam a rede, que é de 16 bitis (8+8) . </span> <span style="color:rgb(8, 189, 189);"> os n°s nesta parte resprentam host/computadores, que é de 8 bitis cada . </span> ex: <span style="color:rgb(171, 255, 79);"> 130 . 10 . </span> <span style="color:rgb(8, 189, 189);">  0. 1. </span>

8bits + 8bits + 0bits + 0bits -   CiRD /16    Máscara é 255.255.0.0 

&nbsp;

/24 - <span style="color:rgb(171, 255, 79);"> os 3 n°s resprentam a rede, que é de 24 bitis (8+8+8) . </span> <span style="color:rgb(8, 189, 189);"> o n° nesta parte resprenta host/computador, que é de 8 bitis. </span> ex: <span style="color:rgb(171, 255, 79);"> 192 . 168 . 0 .  </span> <span style="color:rgb(8, 189, 189);">  1. </span>

8bits + 8bits + 8bits + 0bits -   CiRD /24    Máscara é 255.255.255.0

na prática fica IPva4 = 172.16.4.100 , a máscara da sub-rede é 255.255.0.0. e (<span style="color:rgb(255, 15, 123);"> rede </span> <span style="color:rgb(248, 155, 41);"> host</span>) <span style="color:rgb(255, 15, 123);"> 172.16. </span> <span style="color:rgb(248, 155, 41);">4.100</span>. 

O endereço da rede é 172.16.0.0.

O endereço do Host é 172.16.0.1.

O enderço de broadcast é 172.16.255.255

ip privado: "intranet", pode sair mas  não pode entrar.

|de | até | CIDR |estatus |
|---|-----|------|--------|
|10.0.0.0 |10.255.255.255 | 10.0.0.0/8 | privado |
|172.16.0.0 |172.31.255.255 | 172.16.0.0/12 | privado|
|192.168.0.0 |192.168.255.255 | 192.168.0.0/16 | privado |



" </i>

* Utilizando duas zonas de disponibilidade diferentes.

   a. Criar Duas subredes pública ( uma em cada zona de disponibilidade )

   <i> VPC - escolher região (ve se Sa-east-1) é muito cara (sp)
   
   criar vpc - vpc e muito mais 
   
   </i>

   b. Criar Duas subredes privadas ( uma em cada zona de disponibilidade )

   c. Cada sub rede deve ter máscara /24

* A VPC deve conter um NAT Gateway

* A VPC deve conter um Internet Gateway

* Criar 2 grupos de segurança na VPC criada anteriormente:

   a. Nome: ec2-sg. Deve permitir a conexão SSH e conexão HTTP de qualquer local

   b. Nome: bd-sg. Deve permitir a conexão Mysql e PostgreSQL somente se originada desta vpc.

Editem este Documento incluindo as seguintes evidências de entrega.

&nbsp;

Entregas:

1) a  Diagrama detalhando sua estrutura.

Utilize https://app.diagrams.net para fazer o desenho da arquitetura de forma que reflita exatamente o que foi implementado na AWS

2) b Prints dos painéis da AWS demonstrando

A VPC Criada

As subredes criadas

Os Grupos de segurança

As portas liberadas nos grupos de segurança 

