1. Com as Amazon Virtual Cloud (Amazon VPC) qual é a MENOR sub-rede que pode ter?

R: A menor sub-rede é um VPC /28

2. Coma a Amazon Virtal Private Cloud (VPC), o MAIOR intervalo de endereço IP é:

R: o maior intervalo de endereço ip é 16


obs:  pensando que a rede é uma casa e as sub-redes são os cômodos, pode-se pensar que 16 seriam a sala, dividiu um espaço de toda casa só para a 

sala ficar garnde e receber muitos visitantes. já 28 seriam os quartos, teve que dividir em partes menores para caber o total de quartos,e por ser 

menor, comporta menos pessoas

3. Qual da opção DEVE ESTAR presente para permitir acesso que os recursos de uma sub-privada acessem a internet?

R: Gateway NAT

obs: GATEWAY - componente da VPC escalável, redundante e disponível,  permite a comunicação entre instâncias na VPC e a Internet. 

Tem duas finalidades: fornecer um destino nas tabelas de rotas da VPC para tráfego roteável pela Internet 

....................: executar a conversão de endereços de rede para instâncias que receberam endereços IPv4 públicos.

Para tornar uma sub-rede pública, anexe um gateway da Internet à VPC e adicione uma rota à tabela de rota para enviar tráfego não local por meio 

do gateway da Internet para a Internet (0.0.0.0/0).

- LISTA DE CONTROLE DE ACESSO DA REDE - ACLs de rede 2 de 2 - 

É uma CAMADA OPICIONAL DE SEGURANÇA para a VPC.

Atua como um FIREWALL para controlar o tráfego de entrada e saída de uma ou mais sub-redes. Para adicionar outra camada de segurança à sua VPC,

você pode configurar ACLs e rede com regras semelhantes às dos seus grupos de segurança.

Toda sub-rede em sua VPC deve ser associada com uma ACL de rede. Se você não associar explicitamente uma sub-rede a uma ACL de rede, as sub-redes 

serão associadas automaticamente à ACL de rede padrão. 

É possível associar uma ACL de rede a várias sub-redes; porém, uma sub-rede pode ser associada a apenas uma ACL de rede por vez. Quando uma ACL

de rede é associada a uma sub-rede, a associação anterior é removida.

Uma ACL de rede tem regras de entrada e de saída separadas, e cada regra pode permitir ou rejeitar tráfego. 

AsACLs de rede são stateless, o que significa que nenhuma informação sobre uma solicitação é mantida depois que ela é processada.

- GRUPO  SE SEGURANÇA:

Atua como um FIREWALL VIRTUAL da instância e controla o tráfego de entrada e saída. 

Os grupos de segurança atuam no nível da instância, NÃO no nível da sub-rede.

Cada instância em uma sub-rede na VPC pode ser atribuída a um conjunto diferente de grupos de segurança.

No nível mais básico, um grupo de segurança é uma maneira de filtrar o tráfego direcionado a suas instâncias.

Quando você cria um grupo de segurança, ele não tem regras de entrada. Portanto, nenhum tráfego de entrada originado de outro host para sua 

instância será permitido até que você adicione regras

Inclui uma regra de saída que permite todo o tráfego de saída. Você pode remover a regra e adicionar regras de saída que permitem somente tráfego 

de saída específico. Se o grupo de segurança não tiver nenhuma regra de saída, nenhum tráfego de saída originário da instância será permitido.

Osgrupos de segurança são stateful, o que significa que as informações de estado são mantidas mesmo depois que uma solicitação é processada.

- TABELAS DE ROTAS:

Contém um conjunto de regras (chamadas rotas) que direciona o tráfego de rede da sua sub-rede. Cada rota especifica um destino e um alvo. 

O destino é o bloco CIDR de destino para onde você deseja que o tráfego da sua sub-rede vá. 

O alvo é o destino pelo qual o tráfego de destino é enviado. 

Por padrão, cada tabela de rota que você cria contém uma rota local para comunicação na VPC. Você pode personalizar tabelas de rotas adicionando

rotas. Você NÃO pode excluir a ENTRADA DE ROTA LOCAL usada para COMUNICAÇÃO INTERNA.

A tabela de rota PRINCIPAL é atribuída automaticamente à sua VPC. Controla o roteamento de todas as sub-redes que não estejam explicitamente 

associadas a outra tabela de rota. Uma sub-rede só pode ser associada a uma única tabela de rota por vez, mas é possível associar árias sub-redes 

a uma mesma tabela de rota.


11. (minha) Uma rede de _________ cliente conectada para comprartilhar recursos

b. computadores com mais 3 ou mais máquinas


12. (minha) Uma rede _____ particionada logicamente em sub-redes

c. pode ser

13. (minha) A máquina cliente em uma rede tem um endereço IP (Internet Protocol) ______ .
O endereço IP é um rótulo numérico em formato ______. 


Cada máquina cliente em uma rede tem um endereço IP (Internet Protocol) exclusivo que o
identifica. Um endereço IP é um rótulo numérico em formato decimal. As máquinas convertem
esse número decimal em um formato binário.

14. r: ERRADO
Os endereços IP permitem que os recursos na VPC se comuniquem entre si e com os recursos pela internet. Ao criar uma VPC, você atribui um bloco CIDR IPv4 (um intervalo de endereços IPv4 privados) a ela. Depois de criar uma VPC, você NÃO poderá alterar o intervalo de endereços, portanto, é importante escolhê-lo com cuidado. O bloco CIDR IPv4 pode ser tão grande quanto/16 (que é 2** 16, ou 65.536 endereços) ou tão pequeno quanto/28 (que é 2**4, ou 16 endereços).