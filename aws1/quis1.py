# diconário com as perguntas - ex: perguta 1, dentro outro dicionário com perguntas e respostas

print("EXERCÍCOS TIRADOS DO MOD 1 DO CURSO BÁSICO DE AWS - Explicação das respotas pesquisadas conforme leitura, sujeitas a erros")

revisao = { 
          "quetao1":{ "pergunta": "Quais as vantagens da computação em nuvem em relaçâo à computação ON-PREMISES?", "resposta":{
          "a": "evitar grandes compras de capital", 
          "b": "usar capacidade sob demanda", 
          "c": "ter alcance global em minutos", 
          "d": "aumentar a velocidade e a agilidade",
          "e": "todas", 
          "solucao":{"e":
          "🤓 - Finaceira - pagar o que usar, foco no software e cliente - , capacidade de demanda - usar o que e como precisa ou pode pagar, poder tirar e por as demandas, produtos quando precisa -, alcance global em minutos, velocidade, agilidade, economia de escala, capacidade flexíveis."},},},

          "quetao2":{ "pergunta": "Qual é o modelo de definição de preço que permite que os clientes da AWS paguem pelos recuroso conforme necessário?",
          "resposta":{
          "a": "pagamento conforme a desativação", 
          "b": "pagamento conforme o uso", 
          "c": "pagamento conforme compra", 
          "d": "pagamento conforme a reserva",
          "solucao":{"b":
          "🤓 - Computação em nuvem é a entrega sob demanda de poder computacional, banco de dados, armazenamento, aplicativos e outros recursos de TI pela Internet com uma definição de preço conforme o uso"},},},

          "quetao3":{ "pergunta": "Qual destes NÃO  é um modelo de computação em nuvem?", 
          "resposta":{
          "a": "plataforma como serviço", 
          "b": "infraestrutura como um serviço", 
          "c": "administração de sistema como serviço", 
          "d": "software como serviço",
          "solucao":{"c":
          "🤓 - Administração de sistema como serviço NÃO É modelo de computação em nuvem, SÃO : - Infraestrutura como serviço (IaaS) - fornecem acesso (virtual ou no hardware dedicado) a recursos de rede e computadores, espaço para o armazenamento de dados, oferece o mais alto nível de flexibilidade e controle de gerenciamento sobre seus recursos de TI // - Plataforma como serviço (PaaS)- os serviços reduzem a necessidade de gerenciar a infraestrutura subjacente (geralmente hardware e sistemas operacionais // - Software como serviço (SaaS)- fornecem um produto completo que o provedor de serviços executa e gerencia."},},},

          "quetao4":{ "pergunta": "A propriedade e a manuteção do hadware conectado à rede, necessário para serviços de aplicação, são DA AWS, você provisiona e usa o que precisa.", 
          "resposta":{
          "a": "correta", 
          "b": "incorreta", 
          "solucao":{"a":
          """🤓 - Quando você usa um provedor de serviços em nuvem do AWS, ela é o proprietária dos computadores que você está usando.
          A computação em nuvem ajuda desenvolvedores e departamentos de TI a evitar trabalhos genéricos, como aquisição, manutenção e planejamento de capacidade, permitindo que se concentrem no que realmente importa"""},},},

          "quetao5":{ "pergunta": "Qual destes não é benefício da computação em nuvam em vez da computação on-premise?", 
          "resposta":{
          "a": "aumentar a velociddade e a agilidade", 
          "b": "pagar pelo armazenamento em rack, empilhamento e alimentação de serviço", 
          "c": "eliminar as suposições ao determinar sua necessidade de capacidade de infraestrutura", 
          "d": "trocar despesas de capital por despesas variáveis",
          "e": "beneficiar-se de grandes economias de escalas", 
          "solucao":{"b":
          "🤓 - Pagar pelo armazenamento em rack, empilhamento e alimentação de serviço, isso é parte da AWS."},},},

          "quetao6":{ "pergunta": "Quais das alternativas não são benefícios da computação em nuvem?", 
          "resposta":{
          "a": "vários ciclos de aquisição", 
          "b": "alta disponibilidade", 
          "c": "baixa latência", 
          "d": "recursos temporários e descartáveis",
          "e": "banco de dados tolerantes a falhas", 
          "solucao":{"a":
          "🤓 - Na computação tradicional, o ciclo longo de aquisição de hardware envolve a aquisição, o provisionamento e a manutenção de infraestrutura local.Na computação em nuvem permite considerar que a infraestrutura é composta por software."},},},

          "quetao7":{ "pergunta": "Qual das opções da seguir é um serviço computacional?", 
          "resposta":{
          "a": "Amazon VPC", 
          "b": "Amazon S3", 
          "c": "Amazon EC2", 
          "d": "Amazon cloudFront",
          "e": "Amazon Redshift", 
          "solucao":{"c":
          "🤓 - Amazon Elastic Compute Cloud (Amazon EC2) computacional, de maquina virtual -Capacidade computacional segura e redimensionável para praticamente qualquer workload // - Amazon Redshift - banco de dados, analise - Data warehousing (repositório central de informações que podem ser analisadas para tomar decisões mais adequadas.Analistas de negócios, engenheiros de dados, cientistas de dados e tomadores de decisões acessam os dados por meio de ferramentas de business intelligence (BI), clientes SQL e outras aplicações de análise // - Amazon Virtual Private Cloud (Amazon VPC) -Rede e entrega de conteúdo, fundamentos - personaliza e controla ambinete de rede // - Amazon Simple Storage Service (Amazon S3)- Tecnologia sem servidor, aramazenamento de dados - armazena e protege todos os volumes de dados // - Amazon CloudFront - redes de entrega de conteúdo, rede de borda - é um serviço de rede de entrega de conteúdo (CDN) criado para alta performance, segurança e conveniência do desenvolvedor."},},},

          "quetao8":{ "pergunta": "A computação em nuvem oferece uma forma simples de acessar servidores, armazenamento, banco de dados e um conjunto amplo de serviços de aplicações pela Internet. Você é o proprietário do hardware concectado à rede necessário pera esses serviços e a Amazon Web Services provisiona o que precisal.", 
          "resposta":{
          "a": "correta", 
          "b": "incorreta", 
          "solucao":{"b":
          "🤓 - A AWS que é proprietária e não o clliente . Quando usa um provedor de serviços em nuvem do AWS, ela é o proprietária dos computadores que você está usando."},},},

          "quetao9":{ "pergunta": "Economias de escala resultam de ________ .", 
          "resposta":{
          "a": "ter muitos provedores de nuvens diferentes", 
          "b": "ter centenas de milhares de clientes agregados na nuvem", 
          "c": "ter centenas de serviços de nuvens disponíveis pela internet", 
          "d": "ter que investir pesadamente em data centers e servidores",
          "solucao":{"b":
          "🤓 - Ter centenas de milhares de clientes agregados na nuvem // Beneficie-se da grande economia de escala: o uso da computação em nuvem permite obter um custo variável inferior ao de ambientes locais. Considerando que o uso de centenas de milhares de clientes é agregado na nuvem, provedores como a AWS conseguem obter economias de escala maiores, resultando em preços mais baixos com pagamento conforme o uso."},},},

          "quetao10":{ "pergunta": "São maneiras de acessar os principais serviços da AWS?", 
          "resposta":{
          "a": "chamadas suporte e AWS marketplace", 
          "b": "AWS marketplace, AWS Command Line Interface (AWS CLI), Kit de desenvolvimento de software (SDKs)", 
          "c": "Console de gerenciamentode AWS, AWS Command Line Interface (AWS CLI), Kit de desenvolvimento de software (SDKs)", 
          "d": "AWS marketplace, Console de gerenciamentode AWS, AWS Command Line Interface (AWS CLI)",
          "e": "apenas chamadas de suporte não é", 
          "solucao":{"c":
          "🤓 - Console de Gerenciamento da AWS: fornece uma interface gráfica avançada para a maioria dos recursos oferecidos pela AWS // - Interface da linha de comando da AWS (CLI da AWS):fornece um conjunto de utilitários que podem ser executados a partir de um script de comando no Linux, macOS ou Microsoft Windows // - Software Development Kits (SDKs):fornece pacotes que permitem acessar a AWS em uma variedade de linguagens de programação populares. Isso facilita o uso da AWS em seus aplicativos existentes e permite a criação de aplicativos para implantar e monitorar sistemas complexos inteiramente por meio de código NÃO SÃO MANEIRAS DE ACESSAR // - AWS Support - oferece soluções tradicionais de TI, acelerar sua recuperação de interrupções operacionais, fornecemos planejamento e comunicação proativos, consultoria, automação e experiência em nuvem // - AWS Marketplace é um catálogo digital com milhares de ofertas de provedores independentes de software"},},},
          
          "quetao11":{ "pergunta": "(Minha) A Infraestrutura como serviço (IaaS) não é responsável por: ", "resposta":{
          "a": "O/S (sistema operacional)", 
          "b": "virtualização/ gerenciamento", 
          "c": "serviço", 
          "d": "rede/networking",
          "e": "armazenamento", 
          "solucao":{"a":
          "🤓 - Em Iaas (usa EC2)- a AWs é responsável pela virtualização, serviços, redes, armazenamentos // o cliente,contratante fica responsável pelo O/S (Linux, Windows, McOs, Android...), O middleware (software que  funciona como uma camada oculta de tradução, permitindo a comunicação e o gerenciamento de dados), Data (dados, conjunto de dados), aplicativos e Runtime (tempo de execução)"},},},

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
