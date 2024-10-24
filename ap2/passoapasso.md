1. AWs Academy Leraner Lab [89219]

2. Módulo

3. Iniciar os laboratórios de aprendizagem da AWS Academy

4. Star Lab

5. VPC - Escolher região 

6. VPC

7. criar vpc

8. vpc e muito mais

9. em <i>geração automática da etiqueta de nome</i> 

   - gerar automaticamente

   - <i> valor do projeto</i> P2_Alle (julgo que é o nome da minha vpc)

   - IPv4 - 10.0.0.0/16 <i> só pensando seria 255.255.0.0?</i>

   - <i> numero de zonas de disponibilidade </i> 2

   - <i> n° sub redes pub </i> 2

   - <i> n° sub redes priv </i> 2

   -  mascara /24 

10. Nat gateway (fica dentro da route table o gateway e o nat na sub publ)

   - <i> gateway Nat </i> 

   - conter gateway da internte

11. Endpoint - nenhum
   
   - host dns ativas

   - resolução de dns ativa

12. 


11. dois grupos de segurança 

   - Nome: ec2-sg. Deve permitir a conexão SSH e conexão HTTP de qualquer local

   - Nome: bd-sg. Deve permitir a conexão Mysql e PostgreSQL somente se originada desta vpc.



