# diconário com as perguntas - ex: perguta 1, dentro outro dicionário com perguntas e respostas

print("EXERCÍCOS TIRADOS DO MOD 5 DO CURSO BÁSICO DE AWS - Explicação das respotas pesquisadas conforme leitura, sujeitas a erros")

revisao = { 
          "quetao1":{ "pergunta": "Com as Amazon Virtual Cloud (Amazon VPC) qual é a MENOR sub-red que pode ter?", "resposta":{
          "a": "/28", 
          "b": "/30", 
          "c": "/24", 
          "d": "/26",
          "e": "todas", 
          "solucao":{"a":
          "🤓 - Amazon VPC aceita cinco intervalos de endereço IP, um principal e quatro secundários para IPv4. Cada um desses intervalos pode ter um tamanho entre /28 (em notação CIDR) e /16. Os intervalos de endereço IP da VPC não devem sobrepor os intervalos de endereço IP da rede atual."},},},

          "quetao2":{ "pergunta": "Coma a Amazon Virtal Private Cloud (VPC), o MAIOR intervalo de endereço IP é:",
          "resposta":{
          "a": "/16", 
          "b": "/24", 
          "c": "/30", 
          "d": "/28",
          "solucao":{"a":
          "🤓 - Amazon VPC aceita cinco intervalos de endereço IP, um principal e quatro secundários para IPv4. Cada um desses intervalos pode ter um tamanho entre /28 (em notação CIDR) e /16. Os intervalos de endereço IP da VPC não devem sobrepor os intervalos de endereço IP da rede atual."},},},

          "quetao3":{ "pergunta": "Qual da opção DEVE ESTAR presente para permitir acesso que os recursos de uma sub-privada acessem a internet?", 
          "resposta":{
          "a": "lista de controle de acesso à rede", 
          "b": "grupo de segurança", 
          "c": "tabela de rotas", 
          "d": "Gateway NAT",
          "solucao":{"d":
          "🤓 - GATEWAY - componente da VPC escalável, redundante e disponível,  permite a comunicação entre instâncias na VPC e a Internet.Tem duas finalidades: fornecer um destino nas tabelas de rotas da VPC para tráfego roteável pela Internet. Para tornar uma sub-rede pública, anexe um gateway da Internet à VPC e adicione uma rota à tabela de rota para enviar tráfego não local por meio do gateway da Internet para a Internet (0.0.0.0/0). // - LISTA DE CONTROLE DE ACESSO DA REDE - ACLs de rede 2 de 2 - É uma CAMADA OPICIONAL DE SEGURANÇA para a VPC.Atua como um FIREWALL para controlar o tráfego de entrada e saída de uma ou mais sub-redes. Para adicionar outra camada de segurança à sua VPC, você pode configurar ACLs e rede com regras semelhantes às dos seus grupos de segurança.Toda sub-rede em sua VPC deve ser associada com uma ACL de rede. Se você não associar explicitamente uma sub-rede a uma ACL de rede, as sub-redes serão associadas automaticamente à ACL de rede padrão.É possível associar uma ACL de rede a várias sub-redes; porém, uma sub-rede pode ser associada a apenas uma ACL de rede por vez. Quando uma ACL de rede é associada a uma sub-rede, a associação anterior é removida.Uma ACL de rede tem regras de entrada e de saída separadas, e cada regra pode permitir ou rejeitar tráfego. AsACLs de rede são stateless, o que significa que nenhuma informação sobre uma solicitação é mantida depois que ela é processada. // - GRUPO  SE SEGURANÇA: Atua como um FIREWALL VIRTUAL da instância e controla o tráfego de entrada e saída.Os grupos de segurança atuam no nível da instância, NÃO no nível da sub-rede. Cada instância em uma sub-rede na VPC pode ser atribuída a um conjunto diferente de grupos de segurança. No nível mais básico, um grupo de segurança é uma maneira de filtrar o tráfego direcionado a suas instâncias. Quando você cria um grupo de segurança, ele não tem regras de entrada. Portanto, nenhum tráfego de entrada originado de outro host para sua instância será permitido até que você adicione regras Inclui uma regra de saída que permite todo o tráfego de saída. Você pode remover a regra e adicionar regras de saída que permitem somente tráfego de saída específico. Se o grupo de segurança não tiver nenhuma regra de saída, nenhum tráfego de saída originário da instância será permitido.Osgrupos de segurança são stateful, o que significa que as informações de estado são mantidas mesmo depois que uma solicitação é processada.// - TABELAS DE ROTAS:Contém um conjunto de regras (chamadas rotas) que direciona o tráfego de rede da sua sub-rede. Cada rota especifica um destino e um alvo.O destino é o bloco CIDR de destino para onde você deseja que o tráfego da sua sub-rede vá. O alvo é o destino pelo qual o tráfego de destino é enviado.Por padrão, cada tabela de rota que você cria contém uma rota local para comunicação na VPC. Você pode personalizar tabelas de rotas adicionando rotas. Você NÃO pode excluir a ENTRADA DE ROTA LOCAL usada para COMUNICAÇÃO INTERNA.A tabela de rota PRINCIPAL é atribuída automaticamente à sua VPC. Controla o roteamento de todas as sub-redes que não estejam explicitamente associadas a outra tabela de rota. Uma sub-rede só pode ser associada a uma única tabela de rota por vez, mas é possível associar árias sub-redes a uma mesma tabela de rota. "},},},

          "quetao4":{ "pergunta": "Qual serviço de rede da aws permite que uma empresa crie uma rede virtual dentro da AWS?", 
          "resposta":{
          "a": "Amazon Route 53", 
          "b": "Amazon VPC", 
          "c": "Amazon direct Connect", 
          "d": "AWS Config", 
          "solucao":{"b":
          "🤓 - A Amazon VPC permite provisionar nuvens privadas virtuais (VPCs). Uma VPC é uma rede virtual isolada logicamente de outras redes virtuais na Nuvem AWS. Uma VPC é dedicada à sua conta. As VPCs pertencem a uma única região da AWS e podem abranger várias zonas de disponibilidade e pertencem a uma única zona de disponibilidade.Depois de criar, você pode dividi-la em uma ou mais sub-redes, que é um intervalo de endereços IP em uma VPC. //  - AMAZON ROTE 53: Serviço web de sistema de nomes de domínio (DNS) na nuvem disponíve e dimensionável.Oferecer a desenvolvedores e empresas uma maneira confiável e econômica de direcionar os usuários para aplicações de Internet ao converter nomes como www.example.com em endereços IP numéricos (como 192.0.2.1)  Além disso, o Amazon Route 53 é totalmente compatível com IPv6. O Amazon Route 53 conecta as solicitações de usuários com a infraestrutura executada na AWS, como instâncias do Amazon EC2, balanceadores de carga do Elastic Load Balancing e buckets do Amazon S3, e também pode ser usado para direcionar usuários a infraestruturas fora da AWS.Você pode usar para configurar verificações de integridade do DNS para que rotear o tráfego para endpoints íntegros ou monitorar de forma independente a integridade do seu aplicativo e de seus endpoints.O fluxo de tráfego do Amazon Route 53 ajuda a gerenciar o tráfego globalmente por meio de vários tipos de roteamento, que podem ser combinados com failover de DNS para habilitar diversas arquiteturas de baixa latência e tolerantes a falhas.Também oferece registro de nome de domínio. Você pode comprar e gerenciar nomes de domínio (como example.com), e o Amazon Route 53 definirá automaticamente as configurações de DNS para seus domínios. // - DIRECT CONECT :O desempenho poderá ser afetado negativamente se o data center estiver localizado longe da região da AWS. Para essas situações, a AWS oferece o AWS Direct Connect ou o DX. O AWS Direct Connect permite estabelecer uma conexão de rede dedicada e privada entre a rede e um dos locais do DX. Essa conexão privada pode reduzir os custos de rede, aumentar a taxa de transferência de largura de banda e fornecer uma experiência de rede mais consistente do que as conexões baseadas na Internet. // - AWS CONFIG:AWS Config fornece uma visão detalhada da configuração dos AWS recursos em sua AWS conta,como os recursos estão relacionados um com o outro e como eles foram configurados no passado, de modo que você possa ver como os relacionamentos e as configurações foram alterados ao longo do tempo.É uma entidade com a qual você pode trabalhar AWS, como uma instância do Amazon Elastic Compute Cloud (EC2), um volume do Amazon Elastic Block Store (EBS), um grupo de segurança ou uma Amazon Virtual Private Cloud (VPC)."},},},

          "quetao5":{ "pergunta": "Sube-rede privada têm acesso direto à intenet.", 
          "resposta":{
          "a": "correta", 
          "b": "incorreta", 
          "solucao":{"b":
          "🤓 - A Amazon VPC oferece controle sobre seus recursos de rede virtual, incluindo a seleção do seu próprio intervalo de endereços IP, a criação de sub-redes e a configuração de tabelas de rotas e gateways de rede. Você pode usar IPv4 e IPv6 na VPC para acesso seguro a recursos e aplicativos.Pode personalizar a configuração de rede da VPC. Por exemplo, você pode criar uma sub-rede pública para seus servidores web que podem acessar a Internet pública. Você pode colocar seus sistemas de back-end (como bancos de dados ou servidores de aplicativos) em uma sub-rede privada sem acesso público à Internet.Pode usar várias camadas de segurança, incluindo grupos de segurança e listas de controle de acesso à rede (ACLs de rede), para ajudar a controlar acesso às instâncias do Amazon Elastic Compute Cloud (Amazon EC2) em cada sub-rede."},},},

          "quetao6":{ "pergunta": "Locais de borda da AWS é componente da infraestrutura global da AWS o Amazon CloudFront usa para garantir a entrega de baixa latência", 
          "resposta":{
          "a": "correta", 
          "b": "incorreta", 
          "solucao":{"a":
          "🤓 - Computação de borda é o processo de aproximar o armazenamento de informações e as habilidades de computação dos dispositivos que produzem essas informações e dos usuários que as consomem. Tradicionalmente, as aplicações transmitiam dados de dispositivos inteligentes, como sensores e smartphones, a um datacenter central para processamento. Entretanto, a complexidade e a escala sem precedentes dos dados superaram a capacidade da rede. Aproximando os recursos de processamento dos usuários e dispositivos, os sistemas de computação de borda melhoram significativamente a performance das aplicações, reduzem os requisitos de largura de banda e proporcionam insights mais rápidos em tempo real."},},},

          "quetao7":{ "pergunta": "--", 
          "resposta":{
          "a": "-", 
          "b": "-", 
          "c": "-", 
          "d": "-",
          "e": "-t", 
          "solucao":{"c":
          "🤓 - ---."},},},

          "quetao8":{ "pergunta": "--.", 
          "resposta":{
          "a": "-", 
          "b": "-", 
          "solucao":{"b":
          "🤓 - ---."},},},

          "quetao9":{ "pergunta": "--", 
          "resposta":{
          "a": "--", 
          "b": "--", 
          "c": "--", 
          "d": "--",
          "solucao":{"b":
          "🤓 - ---"},},},

          "quetao10":{ "pergunta": "--", 
          "resposta":{
          "a": "--", 
          "b": "--", 
          "c": "--", 
          "d": "--",
          "e": "--", 
          "solucao":{"c":
          "🤓 - --"},},},
          
          "quetao11":{ "pergunta": "(Minha) Cada máquina cliente em uma rede tem um endereço IP (Internet Protocol) exclusivo que o identifica. Um endereço IP é um rótulo numérico em formato decimal. As máquinas convertem esse número decimal em um formato binário.", 
          "resposta":{
          "a": "correta", 
          "b": "incorreta", 
          "solucao":{"b":
          "🤓 - Os endereços IP permitem que os recursos na VPC se comuniquem entre si e com os recursos pela internet. Ao criar uma VPC, você atribui um bloco CIDR IPv4 (um intervalo de endereços IPv4 privados) a ela. Depois de criar uma VPC, você NÃO poderá alterar o intervalo de endereços, portanto, é importante escolhê-lo com cuidado. O bloco CIDR IPv4 pode ser tão grande quanto/16 (que é 2** 16, ou 65.536 endereços) ou tão pequeno quanto/28 (que é 2**4, ou 16 endereços)"},},},

          "quetao12":{ "pergunta": "(Minha) Uma rede de computadores com mais 3 ou mais máquinas cliente conectada para comprartilhar recursos.", 
          "resposta":{
          "a": "correta", 
          "b": "incorreta", 
          "solucao":{"a":
          "🤓 ---"},},},

          "quetao13":{ "pergunta": "(Minha) A máquina cliente em uma rede tem um endereço Ip (internet procotocolo) exclusivo que o identifica. Um endereço IP é um rótulo numérico em formato decimal. As máquinas convertem esse número em um formato binário.", 
          "resposta":{
          "a": "correta", 
          "b": "incorreta", 
          "solucao":{"a":
          "🤓 ---"},},},

          "quetao14":{ "pergunta": "(Minha) Uma local pode possuir um único ip real, como rota de entrada e saída, mas, internamente pode ter vários ips de intranet para concecta outros computadores", 
          "resposta":{
          "a": "correta", 
          "b": "incorreta", 
          "solucao":{"a":
          "🤓 Para chegar na internet usa-se protocólo de indereçamento (IP), que é composto por 4 partes, cada vai de 0 a 255, cada bloco de internet tem em tamanho 8 bits, totalizando 32 bits. Algumas redes não podem usar alguns números, ips que iniciam com 192, 168 ou 10 são indereços internos/privado/intranet e não existem na internet global/pública/real (endereço de rota de saída e chegada, como se fosse o endereço do local, da casa, empresa) "},},},


}


correta = 0
errada = 0

# pega a chave questão e seus valores - pergunta - ok
for quest, val_quest in revisao.items():
          print(f"\n {quest}: {val_quest['pergunta']}\n")

# dentro da chave resposta e seus valore
          for opcao, resp in val_quest["resposta"].items():
                    if opcao != "solucao": 
# imprime o valor real da resposta
                              print(f"\n {opcao}: {resp} \n")
          
          escolha = input("Digite uma das opções: ") 

          if escolha in val_quest["resposta"]["solucao"]:
                    print("\n 😃 Isso! \n")
                    correta += 1
          else: 
                    print("\n Vamos ver 🧐 \n")
                    errada += 1

          print(f"""{val_quest['resposta']['solucao']}
          De 11 você possui {correta} corretas e precisa revisar {errada}""")
