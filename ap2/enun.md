1. Primeira fase

Criar uma VPC com as seguintes características:

* 1.1. A VPC deve ter a máscara de sub rede /16

* Utilizando duas zonas de disponibilidade diferentes.

   a. Criar Duas subredes pública ( uma em cada zona de disponibilidade )

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

