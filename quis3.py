acertos = 0

print("1. Qual componente da infraestrutura global da AWs o Amazon CloudFront usa para garantir a entrada de baixa latência?"\n)
per1 = input("""a - regiões da AWS
b - pontos de presença da AWS
c - zonas de disponibilidade da AWS
d - Amazon Virtual Private Cloud (Amazon VPC)
resposta: """)
if per1 == "b" :
          print ("correta")
          acertos += 1
else: print( "Incorreta")
print ("")