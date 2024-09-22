# diconário com as perguntas - ex: perguta 1, dentro outro dicionário com perguntas e respostas

print("EXERCÍCOS TIRADOS DO MOD 2 DO CURSO BÁSICO DE AWS - Explicação das respotas pesquisadas conforme leitura, sujeitas a erros")

revisao = { 
          "quetao1":{ "pergunta": "Para definir serviços, como Amazon EC2 - Amazon Elastic Computer claund e Amazon RDS - Amazom relational Database Servec é possíver investir em reserva, com instâncias reservadas. Qual intância paga totalmente antecipada, não tem que paga antecipadamente e paga antecipação parcial, nesta orde?:", 
          "resposta":{
          "a": "AURI - MURI - NURI", 
          "b": "MURI - NURI - PURI", 
          "c": "AURI - NURI - PURI", 
          "d": "AURI - PURI - DURI",
          "solucao":{"c":
          "🤓 - AURI - All Upfront Reserved Instance - o usuário PAGA ANTECIPADAMENTE POR TODA a duração do período de reserva, o que normalmente é um ou três anos. Essa opção proporciona o maior desconto. é adequado para aqueles que podem pagar antecipadamente para obter o máximo desconto, // -  NURI  - No Upfront Reserved Instances -  o usuário NÃO PRECISA FAZER UMA PAGAMENTO INICIAL, eles pagam uma taxa de reserva menor ao longo do tempo.A taxa horária da instância reservada é um pouco mais alta do que na opção AURI.Pode ser vantajosa para usuários que não têm capital inicial para investir ou preferem manter sua liquidez. // - PURI  - Partial Upfront Reserved Instances - o usuário faz um PAGAMENTO PARCIAL ANTECIPADO e, em seguida, paga uma taxa de reserva menor ao longo do tempo. O pagamento inicial é menor do que no caso do AURI, mas ainda oferece um desconto significativo em comparação com instâncias sob demanda.// NURI e PURI oferecem opções para aqueles que preferem distribuir os custos ao longo do tempo ou têm limitações financeiras iniciais.   (brainly.com.br)"},},},

          "quetao2":{ "pergunta": "O que um cliente pode acessar para obeter DETALHES SOBRE ATIVIDADE DE ATURAMENTO do AMAZON EC2 (Amazon Elastic Computer Clound) que ocorreu há 3 meses?",
          "resposta":{
          "a": "Painel do AmazonEC2", 
          "b": "AWS Cost Explore", 
          "c": "Painel do AWS TRsuted Advisor", 
          "d": "Logs do AWS CloudTrail armazenados no Amazon S3 (Amazon Simple Storage Servece)",
          "solucao":{"b":
          "🤓 - O - AWS Cost explorer - pode oferecer mais detalhes sobre a atividade de faturamento do Amazon EC2 nos últimos 3 meses. // > O console do AWS Billing and Cost Management inclui a página - Cost Explorer -  para visualizar seus dados de custo da AWS como um gráfico, pode visualizar, entender e gerenciar os custos e o uso da AWS ao longo do tempo. Inclui um relatório padrão que visualiza os custos e o uso dos serviços mais econômicos. O relatório mensal de custos de execução fornece uma visão geral de todos os seus custos dos últimos 3 meses. Ele também fornece números previstos para o próximo mês, com um intervalo de confiança correspondente. // O Cost Explorer é uma ferramenta gratuita que permite •Visualize gráficos de seus custos •Visualize os dados de custo dos últimos 13 meses. •Preveja o quanto você provavelmente gastará nos próximos 3 meses •Descubra padrões de gastos com recursos da AWS ao longo do tempo e identifique áreas problemáticas de custos •Identificar os serviços que você mais usa •Visualize métricas, como quais zonas de disponibilidade têm mais tráfego ou qual conta vinculada da AWS é mais usada."},},},

          "quetao3":{ "pergunta": " Para a receber a taxa com desconto associada às instâncias reservadas você deve fazer um pagamento antecipado completo pelo período de vigência do contrato.", 
          "resposta":{
          "a": "correta", 
          "b": "incorreta", 
          "solucao":{"b":
          "🤓 - Para receber a taxa com desconto associada às instâncias reservadas, você NÃO precisa fazer pagamento antecipado completo. FORMAS DE DESCONTO NURI - 'NUNE UPFRONT RESERVED INSTANCE - - NENHUM' No Upfront Reserved Instances -  o usuário não precisa fazer um pagamento inicial, eles pagam uma taxa de reserva menor ao longo do tempo.A taxa horária da instância reservada é um pouco mais alta do que na opção  //  - PURI - 'PARTIAL UPFRONT RESERVED INSTANCE' - Partial Upfront Reserved Instances -  o usuário faz um pagamento parcial antecipado e, em seguida, paga uma taxa de reserva menor ao longo do tempo. O pagamento inicial é menor do que no caso do AURI, mas ainda oferece um desconto significativo em comparação com instâncias sob demanda.  //  -AURI 'ALL UPFRONT RESERVED INSTANCE' é adequado para aqueles que podem pagar antecipadamente para obter o máximo desconto. "},},},

          "quetao4":{ "pergunta": "Sobre o modelo de precificação da AWS", 
          "resposta":{
          "a": "Na mairoia dos casos, há uma cobrança por gigabyte para transferência de dados de entrada", 
          "b": "O armazenamento normalmente é cobrado por gigabyte",
          "C": "A computação geralmente é cobrada mensalmente, com base no tipo de instância", 
          "D": "não há cobrança de saída desde que esteja dentro do limite da conta",  
          "solucao":{"b":
          "🤓 - a - NÃO há cobrança de saída desde que esteja dentro do limite da conta  //  C - eu diria que cobrança é conforme pacote, se pago All <AURI>, paga-se adiantado, neste caso pagou-se usando ou não, se pegar parcial (PURI), paga metade a vista e depois, mês a mês durante o ano e NURI paga quando aluga, pelo tempo de aluguel  //  d - HÁ cobrança para sair, não há para entrar  // b - o armazenamento é cobrado por gigabyte. Para serviços como o Amazon Simple Storage Service (Amazon S3), a definição de preço é estratificada, o que significa que você paga menos por GB quando usa mais."},},},

          "quetao5":{ "pergunta": "Quais são os 4 planos de suporte oferecido pelo AWS Support?", 
          "resposta":{
          "a": "Basic, Developer, Business, Entreprise", 
          "b": "Basic, Startup, Business, Enterprise", 
          "c": "Free, Bronze, silver, Gold", 
          "d": "Todos são gratuítos",
          "e": "Basic, Startup, Developer, Business", 
          "solucao":{"a":
          "🤓 - AWS Support oferece cinco planos de suporte -   Basico  - Basic Suport - gratuíto, tira dúvidas sobre contas e faturamento e aumento de contas de serviços -   Desenvolvedor  - adiciona - orientação sobre mellhores práticas, diagnóstico do lado cliente, suporte de arquitetura básica, suporte a um n° ilimitado de casos -   Business/ Emterprise ON-Ramp/ Enterprise  - tem acesso outro recursos como orientação de caso de uso, AWS TRUSTED ADVISOR (inspeciona os ambientes dos clientes e identifica oportuniodades de economia, segurança, confiabilidade e desempenho de sistema), entre outros. Enterprise On-Ramp e Enterprise tem acesso a mais recuros  // Alguns serviços são gratuítos, como Amazon VPC  •Elastic Beanstalk  •AWS CloudFormation  •IAM  •Serviços de auto scaling  •AWS OpsWorks•Cobrança consolidada // Embora os serviços em si sejam gratuitos, os recursos que eles provisionam PODEM não ser gratuitos."},},},

          "quetao6":{ "pergunta": "Qual ferramenta da aws permite esplorar os serviços da AWS e CRIAR uma estimativa para o CUSTO de seus casos de uso na AWS?", 
          "resposta":{
          "a": "calculadora de preço da AWS", 
          "b": "AWS Bugest", 
          "c": "AWS relatório de uso e custo",
          "d": "Painel de faturamento da AWS", 
          "solucao":{"a":
          "🤓 - Calculadora de Preços da AWSpode ajudar você a estimar a fatura mensal da AWS. Você pode usar essa ferramenta para explorar os serviços da AWS e criar uma estimativa para o custo de seus casos de uso na AWS. Permite que você dê um nome à sua estimativa e crie e nomeie grupos de serviços. Grupossão contêineres em que você adiciona serviços para organizar e criar sua estimativa // Faturas da AWS lista os custos incorridos no mês passado para cada serviço da AWS, com um detalhamento adicional por região da AWS e conta vinculada.Oferece acesso às informações mais atualizadas sobre seus custos e uso, incluindo sua fatura mensal e a discriminação detalhada dos serviços da AWS que você usa  // AWS Budgets usa a visualização de custos fornecida pelo Cost Explorer para mostrar o status de seus orçamentos e para fornecer previsões de seus custos estimados  //  Relatório de custos e uso da AWS é um local único para acessar informações abrangentes sobre custos e uso da AWS. Lista o uso de cada categoria de serviço usada por uma conta da AWS (esta parte não apareceu)(e seus usuários) em itens de linha por hora ou diariamente, e qualquer imposto ativado para fins de alocação de impostos.  "},},},

          "quetao7":{ "pergunta": "À medida que a AWS cresce, o custo de fazer negócios é reduzido, e as economias são repassadas para o cliente por meio de preço mais baixo. Como é chamada essa orimização?", 
          "resposta":{
          "a": "visibilidade de custo", 
          "b": "economia de escala", 
          "c": "corespondência entre oferta e demanda", 
          "d": "dimensioamente correto de EC2",
          "solucao":{"b":
          "🤓 - Economia de escala (não consegui achar informações para correção e fixação)."},},},

          "quetao8":{ "pergunta": "A AWS oferece diversos serviços gratuítos, como Amazzon Virtual Private Cloud, AWS Identity and Access Management (IAM), Cobramça consolidade, AWS Elastic BEanstalk, Auto scaling, AWS OpsWork e AWS CloudFormation. No entando, você pode ser cobrado por outros serviços da AWS usados em conjunto com este serviços.", 
          "resposta":{
          "a": "correta", 
          "b": "incorreta", 
          "solucao":{"a":
          "🤓 - Alguns serviços são gratuítos, como Amazon VPC  •Elastic Beanstalk  •AWS CloudFormation  •IAM  •Serviços de auto scaling  •AWS OpsWorks•Cobrança consolidada // Embora os serviços em si sejam gratuitos, os recursos que eles provisionam PODEM não ser gratuitos."},},},

          "quetao9":{ "pergunta": "São os benefícios de usar o AWs Organization:", 
          "resposta":{
          "a": "Não substitui as políticas existente do AWs Identity and Access Management (IAM) por políticas de controle de serviço (SCPs), que são mais fáceis de gerenciar", 
          "b": "fornece a habilidade de criar grupos de contas e anexar políticas a eles", 
          "c": "fornece a habilidade de criar um n° ilimitado de unidades organizacionais(UOs) aninhadas para dar suporte à estrutura que se deseja", 
          "d": "simplifica a automatização da criação e gerenciamento de contas usando APIs",
          "e": "evita que qualquer restrição seja aplicada ao usuário-raiz que está associado à organização principal em uma conta",
          "solucao":{"e":
          "🤓 - O AWS Organizations NÃO substitui a associação de políticas do AWS Identity and Access Management (IAM)a usuários, grupos e funções em uma conta da AWS  //  USA políticas de controle de serviço (SCPs) para permitir ou negar acesso a determinados serviços da AWS para contas individuais da AWS ou para grupos de contas em uma UO. As ações especificadas de uma SCP anexada afetam TODOS os usuários, grupos e funções do IAM de uma conta, INCLUINDO o usuário raiz da conta da AWS  // O AWS Organizations é um serviço de gerenciamento de contas que permite consolidar várias contas da AWS em uma organizaçãoque você cria e gerencia de forma centralizada // a e deveria ser PERMITE ualquer restrição seja aplicada ao usuário-raiz que está associado à organização principal em uma conta"},},},

          "quetao10":{ "pergunta": "Os serviços ilimitados estão disponíveis com o nível gratuíto da AWS para novos clientes por 12 meses após a data de cadastro na AWS", 
          "resposta":{
          "a": "correta", 
          "b": "incorreta", 
          "solucao":{"B":
          "🤓 - AWS oferece um nível gratuito para novos clientes por até um ano. O nível gratuito da AWS se aplica a determinados DETERMINADOS SERVIÇOS E OPÇÕES (SÃO SERVIÇOES LIMITADOS, LISTADO). Se você for um cliente novo da AWS, poderá executar uma microinstância T2 gratuita do Amazon Elastic Compute Cloud (Amazon EC2) por um ano, além de usar um nível gratuito para o Amazon S3, o Amazon Elastic Block Store (Amazon EBS), o Elastic Load Balancing, a transferência de dados da AWS e outros serviços da AWS"},},},

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
