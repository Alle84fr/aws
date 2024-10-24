acertos = 0

print("1. Qual componente da infraestrutura global da AWs o Amazon CloudFront usa para garantir a entrada de baixa latência?\n")
per1 = input("""a - regiões da AWS
b - pontos de presença da AWS
c - zonas de disponibilidade da AWS
d - Amazon Virtual Private Cloud (Amazon VPC)
resposta: """)
if per1 == "b" :
          print ("correta\n".center(100))
          acertos += 1
else: print( "Incorret\n".center(100))
print ("Explicação".center(99),"""
a) Regiões - local físico em todo o mundo onde agrupamos datacenters (zona de disponibilidade).
Cada região da AWS consiste no mínimo em três AZs isoladas e separadas fisicamente em uma área geográfica.
c) Uma zona de disponibilidade (AZ) é um ou mais datacenters distintos com energia, rede e conectividade 
redundantes em uma região da AWS.
d) Amazon VPC - Amazon Virtual Private clound - Serviço de rede e entrega de conteúdo - permiteprovisionar seções logicamente isoladas
da nuvem AWS. 
b) correta - O Amazon CloudFront usa pontos de presença da AWS para garantir a entrada de baixa latência.
Serviço de rede e entrega de conteúdos como dados, videos, aplicativos, interface de APIs para clientes
CDN - Amazon CloudFront - REDE DE ENTRAGA DE CONTEÚDO - Distribui conteúdo ao usuário final com baixa latência e alta velocidade de
transferência
obs **DNS - Amazon Route53** - /_SERVIÇO DE SISTEMA DE NOME DE DOMÍNIO/_ - As solicitações serão roteadas automaticamente para o ponto 
de presença mais próximo para diminuir a latência\n""")

print("\n 2. Você pode executar aplicações e workloads de uma regição mais próxima dos usuários finais para _______ a latência\n")
per1 = input("""a - diminuir
b - aumentar
resposta: """)
if per1 == "a" :
          print ("correta\n".center(100))
          acertos += 1
else: print( "Incorreta\n".center(100))
print ("Explicação".center(99),"""
obs: Workload - conjunto de códigos e recursos que agrega valor empresarial, como uma aplicação voltada para o cliente ou um processo de back-end.
A página Workloads (Cargas de trabalho), fornece informações sobre as suas cargas de trabalho e todas as cargas de trabalho que foram 
compartilhadas com você.
Ao executar de uma região mais próxima do usuário e do sistema a (AZ - zona de distribuição) ajudará a reduzir a latência 
""")