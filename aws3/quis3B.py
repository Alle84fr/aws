# diconário com as perguntas - ex: perguta 1, dentro outro dicionário com perguntas e respostas

print("EXERCÍCOS TIRADOS DO MOD 3 DO CURSO BÁSICO DE AWS - Explicação das respotas pesquisadas conforme leitura, sujeitas a erros")

revisao = { 
          "quetao1":{ "pergunta": "Qual componente da infraestrutura global da AWs o Amazon CloudFront usa para garantir a entrada de baixa latência?", 
          "resposta":{
          "a": "regiões da AWS", 
          "b": "pontos de presença da AWS", 
          "c": "zonas de disponibilidade da AWS", 
          "d": "Amazon Virtual Private Cloud (Amazon VPC)",
          "solucao":{"b":
          "🤓 - A infraestrutura da Nuvem AWS é criada em torno das regiões,que é uma localização geográfica física com uma ou mais Zonas de Disponibilidade. As Zonas de Disponibilidade, por sua vez, consistem em um ou mais data centers (chafe de todos)  //   Zonas de Disponibilidade,  vários locais isolados,oferece a capacidade de operar aplicativos e bancos de dados mais altamente disponíveis, tolerantes a falhas e dimensionáveis do que seria possível em um único data center  // A base da infraestrutura da AWS são os data centers //  Os pontos de presença, serviço 'privado' da AWS estão localizados na maioria das principais cidades do mundo. Ao medir continuamente a conectividade, o desempenho e a computação com a Internet para encontrar a melhor maneira de rotear solicitações, os pontos de presença oferecem uma melhor experiência de usuário quase em tempo real. "},},},

          "quetao2":{ "pergunta": "Você pode executar aplicações e workloads de uma regição mais próxima dos usuários finais para _______ a latência",
          "resposta":{
          "a": "diminuir", 
          "b": "aumentar", 
          "solucao":{"b":
          "🤓 - pergunta": "Você pode executar aplicações e workloads de uma regição mais próxima dos usuários finais para diminuir a latência"},},},

          "quetao3":{ "pergunta": " Redes, armazenamentos, computação e banco de dados são exemplos de categoria de serviço que a AWs oferece.", 
          "resposta":{
          "a": "correta", 
          "b": "incorreta", 
          "solucao":{"a":
          "🤓 - Computação, Gerenciamento de custos, Banco de dados, Gerenciamento e governança, Redes e entrega de conteúdo, Segurança, Identidade e Conformidade e Armazenamento. (neste curso) "},},},

          "quetao4":{ "pergunta": "SQuais das seguintes áreas geográficas que hospedam duas ou mais zonas de disponibilidade?S", 
          "resposta":{
          "a": "origens da AWS", 
          "b": "regiões da AWS",
          "C": "zonas de computação", 
          "D": "pontos de presença",  
          "solucao":{"b":
          "🤓 -Uma Região AWSé uma localização geográfica física com uma ou mais Zonas de Disponibilidade  // As Zonas de Disponibilidade têm sua própria infraestrutura de energia e são fisicamente separadas por muitos quilômetros de outras Zonas de Disponibilidade, embora todas elas estejam a 100 km umas das outras.São interconectadas com redes de alta largura de banda e baixa latência por meio de fibra dedicada totalmente redundante que fornece alta vazão entre as Zonas de Disponibilidade. A rede faz a replicação síncrona entre as Zonas de Disponibilidade //  O Amazon CloudFront é uma rede de entrega de conteúdo(CDN) usada para distribuir conteúdo aos usuários finais para reduzir a latência. Os pontos de presença Ao medir continuamente a conectividade, o desempenho e a computação com a Internet para encontrar a melhor maneira de rotear solicitações, os pontos de presença oferecem uma melhor experiência de usuário quase em tempo real //  Origens - local de onde a AWs busca dos dados para entregar ao usuário ( ex: funções lambda, instâncias EC2, urls, Buckets S3) // Borda - limites da rede, pontos mais próximos dos usuários. Pense na internet como uma teia: a borda seriam os fios mais externos, que estão mais próximos de você, traz latência reduziada, maior disponibilidade e privacidade ."},},},

          "quetao5":{ "pergunta": " ____ significa que a infraentrutura tem redundância de componentes integradas. ______ significa que os recuros se ajustam sinamicamente para aumentos ou diminuições nos requisitos de capacidade.", 
          "resposta":{
          "a": "sem interveção humana, tolerante a falhas", 
          "b": "elásico e escalável, sem intervemção humana", 
          "c": "tolerante a falhas, sem intervenção humana", 
          "d": "tolerante a falhas, elástico e escalável",
          "e": "elástico e escalável, tolerante a falhas", 
          "solucao":{"d":
          "🤓 - Tolerante a falhas significa que a infraestrutura tem redundância de componentes integrada. Elástico e escalável significa que os recursos se ajustam dinamicamente para aumentos ou dimminuições nos requisitos de capacidade."},},},

          "quetao6":{ "pergunta": "As zonas de disponibilidade dentro da uma região são conectadas por meio de links de baixa latência?", 
          "resposta":{
          "a": "correta", 
          "b": "incorreta", 
          "solucao":{"b":
          "🤓 - Todas as Zonas de Disponibilidade são interconectadas com redes de alta largura de banda e baixa latência por meio de fibra dedicada totalmente redundante que fornece alta vazão entre as Zonas de Disponibilidade. A rede faz a replicação síncrona entre as Zonas de Disponibilidade."},},},

          "quetao7":{ "pergunta": "Quais dessas afirmações sobre zonas de disponibilidade não é verdadeira?", 
          "resposta":{
          "a": "as zonas de disponibilidade são projetadas para isolamento de falhas", 
          "b": "as zonas de disponibilidade são compostas por um ou mais datacenter", 
          "c": "um datacenter pode ser usado para mais de uma zona de disponibilidade", 
          "d": "as zonas de disponibilidade são conectadas umas às outras usando links privados de alta velocidade",
          "solucao":{"c":
          "🤓 -Cada Zona de Disponibilidade pode incluir vários data centers (normalmente três) e, em dimensão integral (não podendo uma data para mais de uma zona)"},},},

          "quetao8":{ "pergunta": "sobre as regiões:", 
          "resposta":{
          "a": "elas são as localizações físicas onde os datascenters estão,os clientes acessam a partir desta localidade", 
          "b": "região é um local geográfica física que tem várioas zonas de disponibilidade",
          "c": "cada região está localizada em uma região separada", 
          "b": "todas as regiões estão localizadas em uma área geográfica específica",  
          "solucao":{"b":
          "🤓 - As regiões estão sepradas por 34 regiões geográficas (não apenas uma), 108 zonas de disponibilidade com planos de crescimenro."},},},

          "quetao9":{ "pergunta": "O posicionamento de recursos de computação em ____ zona/s de disponibilidade é altamente recomendado pela AWS.", 
          "resposta":{
          "a": "nenhuma", 
          "b": "todas as", 
          "c": "uma única", 
          "d": "várias",
          "solucao":{"d":
          "🤓 - pergunta": "O posicionamento de recursos de computação em várias zona/s de disponibilidade é altamente recomendado pela AWS."},},},

          "quetao10":{ "pergunta": "Os pontos de presença só estão localizados na mesma área geral que as regiões", 
          "resposta":{
          "a": "correta", 
          "b": "incorreta", 
          "solucao":{"b":
          "🤓 - Pontos de Presença (PoPs): São locais estrategicamente distribuídos ao redor do globo, onde a AWS estabelece sua presença para conectar os usuários finais aos seus serviços em nuvem // - Cobertura global: A AWS possui uma rede global de PoPs para garantir uma latência mínima para seus clientes em todo o mundo // - Flexibilidade: A localização dos PoPs pode ser ajustada para atender às demandas dos clientes e às mudanças nas rotas de internet // - Performance: Ao colocar PoPs mais próximos dos usuários, a AWS pode entregar conteúdo e serviços com menor latência, o que é crucial para aplicações sensíveis ao tempo, como streaming de vídeo e jogos online."},},},

          "quetao11":{ "pergunta": "(minha) Disco, armazenamento, reservado tem cobrança, independentemete de usar. Máquina, poder computacional, tem cobrança, independente de estar ou não sendo usada. Dados de entrada na nuvem e na saída tem cobrança.", "resposta":{
          "a": "a frase está toda correta", 
          "b": "disco, armazenamento não é cobrado quando não usado e saida de dados da nuvem não tem cobrança", 
          "c": "saída de dados da nuvem tem cobrança, o resto está correto", 
          "d": "máquina, poder compjutacional não tem cobrança se não usado e entrada de dados na nuvem não tem cobrança",
          "e": "disco, armazenamento não é cobrado quando não usado e entrada de dados da nuvem não tem cobrança", 
          "solucao":{"d":
          "🤓 - A frase correta é Disco, armazenamento, reservado TEM cobrança, INdependentemete de usar. Máquina, poder computacional, NÃO tem cobrança, independente de estar ou não sendo usada. Dados de entrada na nuvem NÃO TEM COBRANÇA e na saída TEM cobrança."},},},

          "quetao12":{ "pergunta": "(minha) Disco, armazenamento, reservado tem cobrança, independentemete de usar. Máquina, poder computacional, tem cobrança, independente de estar ou não sendo usada. Dados de entrada na nuvem e na saída tem cobrança.", "resposta":{
          "a": "Cobrança consolidada em várias contas da AWS", 
          "b": "Automatizou a criação e o gerenciamento de contas AWS", 
          "c": "Políticas de acesso gerenciadas centralmente em várias contas da AWS", 
          "d": "Acesso controlado aos serviços AWS",
          "e": "todas anteriores", 
          "solucao":{"d":
          "🤓 - AWS Organizations é um serviço de gerenciamento de contas que permite consolidar várias contas da AWS em uma organização que você cria e gerencia de forma centralizada, inclui recursos de cobrança consolidada e gerenciamento de contas, que ajudam a atender melhor às necessidades orçamentárias, de segurança e de compatibilidade da sua empresa. Os principais benefícios do AWS Organizations são: // Políticas de acesso gerenciadas centralmente em várias contas da AWS //  Acesso controlado aos serviços AWS. //  Automatizou a criação e o gerenciamento de contas AWS //  Cobrança consolidada em várias contas da AWS"},},},
          
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
          De 12 você possui {correta} corretas e precisa revisar {errada}""")
