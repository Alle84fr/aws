# diconário com as perguntas - ex: perguta 1, dentro outro dicionário com perguntas e respostas

print("EXERCÍCOS TIRADOS DO MOD 4 DO CURSO BÁSICO DE AWS - Explicação das respotas pesquisadas conforme leitura, sujeitas a erros")

revisao = { 
          "quetao1":{ "pergunta": "No modelo de responsabilidade compratilhada, a AWS é responsável por forncer:", "resposta":{
          "a": "Segurança da nuveml", 
          "b": "seguranla à núvem", 
          "c": "segurança para a núvem", 
          "d": "segurança na nuvem",
          "e": "todas", 
          "solucao":{"a":
          "🤓 - Da Nuvem é que segurança Da AWS, que é Data Center e sua segurança e funcionamento, regular segurança de computador,  proteção global // Na nuvem é segurança na mão do usuário, como formato do conteúdo, grupos de segurança, onde irá armazenar os dados // No modelo de responsabilidade compartilhada, a AWs é responsável por fornecer a segurança da nuvem"},},},

          "quetao2":{ "pergunta": "No modelo de responsabilidade compatilhada, são exemplos de 'segurança na nuvem',
          "resposta":{
          "a": "Conformidade com padrões e regulamentos de segurança de computação e formato e a estrutura desse conteúdo e se ele é mascarado, anonimizadoou criptografado", 
          "b": "segurança física das intalações em que os serviços operam e infraestrutura de dispositivos de armazenamento", 
          "c": "Configuração de grupo se segurança e Criptografia de dados ociosos em trânsito", 
          "d": "ptoteção da infraestrutura global e qual país o conteúdo é armazenado",
          "solucao":{"c":
          "🤓 - A AWS opera, gerencia e controla os componentes desde a camada de virtualização de software até a segurança física das instalações em que os serviços da AWS operam. É responsável pela roteção da infraestrutura que executa todos os serviços oferecidos < DA > Nuvem AWS. Essa infraestrutura é composta por hardware, software, redes e instalações que executam os Serviços de nuvem AWS. //  O cliente é responsável pela criptografia de dados em repouso e em trânsito <NA NUVEM>. O cliente também deve garantir que a rede esteja configurada para segurança e que as credenciais e os logins de segurança sejam gerenciados de maneira segura.É responsável pela configuração de grupos de segurança e pela configuração do sistema operacional que é executado nas instâncias de computação que ele executa (incluindo atualizações e patches de segurança)."},},},

          "quetao3":{ "pergunta": "Qual das seguintes opções é responsável da AWs de acordo con o modelo de responsabilidade compatilhada?", 
          "resposta":{
          "a": "configuração de aplicações de terceiros", 
          "b": "manutenção de hardaware físico", 
          "c": "acesso de dados de aplicações de segurança", 
          "d": "gerenciamento de imagens de máquina da Amazon (AMIs)",
          "solucao":{"b":
          "🤓 - A AWS é responsável pela segurança da nuvem.opera, gerencia e controla os componentes do sistema operacional host bare metal e da camada de virtualização do hipervisor até a segurança física das instalações em que os serviços operam. A infraestrutura global inclui zonas de disponibilidade, pontos de presença e regiões da AWS. É responsável pela infraestrutura física que hospeda seus recursos, como, - segurança física de datacenters, - infraestrutura de hardware com acesso controlado e baseado em necessidades, - infraestrutura de softwares, como servidores, dispositivos de armazenamento,etc, - infraestrutura de rede, como roteadores, firewall, cabeamento etc // A manutenção de hardware físico é responsabilidade da AWs sob o modelo de responsabilidade compartilhada"},},},

          "quetao4":{ "pergunta": "Ao criar uma política do AWs Identity and Acess Management (IAM), quais são os dois tipos de acesso que podem ser concedidos a um usuário?", 
          "resposta":{
          "a": "acesso institucional", 
          "b": "acesso autorizado",
          "c": "acesso programático",
          "d": "acesso ao Console de Gerenciamento da AWS",
          "e": "acesso raiz administrativo", 
          "solucao":{"d e c":
          "🤓 - Qu"},},},

          "quetao5":{ "O AWS Organizations permite consolidar várias contas da AWS para que você as gerencie de maneira centralizada.":{
          "a": "correta", 
          "b": "incorreta", 
          "solucao":{"a":
          "🤓 - Ao criar uma política de IAM, um usuário pode receber acesso ao Console de Gerenciamento da AWS e acesso proramático . "},},},

          "quetao6":{ "pergunta": "Quais das seguintes opções são melhores práticas para proteger sua conta usando o AWS Identity and Access Management (IAM)", 
          "resposta":{
          "a": "fornecer ao usuário privilégio administrativo padrão", 
          "b": "deixar credenciais e usuários não utilizados e desnecessários em vigor", 
          "c": "gerenciar o acesso ao recursos da AWS", 
          "d": "evitar o uso de grupos do IAM para conceder as mesmas permissões de acesso a vários usuários",
          "e": "definir direitos de acesso refinados", 
          "solucao":{"c e e":
          "🤓 - Gerenciar o acesso aos recursos da AWs e definir direitos de acesso refinados são melhores práticas para proteger contas com o AWS IAM"},},},

          "quetao7":{ "pergunta": "Qual das seguintes ações deve ser tomada pelo usuário raiz da conta da AWS?.", 
          "resposta":{
          "a": "acesso seguro para aplicações", 
          "b": "integrar a outros serviços da AWS", 
          "c": "alterar permissões granulares", 
          "d": "alterar o plano do AWS Support",
          "solucao":{"d":
          "🤓 - Somente o usuário raiz da conta pode alterar o plano do AWS Support // As outras são realizadas com o IAM"},},},

          "quetao8":{ "pergunta": "Após o login inicial, o que se recomenda como melhor prática para o usuário raiz da conta AWS?":{
          "a": "excluir o usuário raiz da conta da AWS", 
          "b": "revogar todas as permissões no usuário raiz da conta da AWS",
          "c": "restringir a permissão no usuário raiz da conta da AWS", 
          "d": "excluir as chaves de acesso do usuário raiz da conta da AWS", 
          "solucao":{"d":
          "🤓 - Após o login inicial, a AWS recomenda excluir as chaves de acesso do usuário raiz da conta da AWS como melhor prática"},},},

          "quetao9":{ "Como um administrador de sistema incluiria uma camada adicional de segurança de login ao Console de Gerenciamento da AWS de um usuário.", 
          "resposta":{
          "a": "usar o Amazon Cloud Directory", 
          "b": "auditar funções do AWS Identity and Access Management (IAM)", 
          "c": "habilitar autenticação multifator", 
          "d": "habilitar o AWs CloudTrail",
          "solucao":{"c":
          "🤓 - Para incluir uma camada adicional de segurança do login ao Console de Gerenciamento da AWS de um usuário, habilite a autenticação multifator"},},},

          "quetao10":{ "pergunta": "O AWS Key Management Service (AWs KMS) permite acessar, auditar e avaliar as configurações dos recursos da AWS", 
          "resposta":{
          "a": "correta", 
          "b": "incorreta", 
          "solucao":{"b":
          "🤓 - O AWS Key Management Service (AWS KMS) é um serviço que permite criar e gerenciar chaves de criptografia e controlar o uso da criptografia em muitos serviços da AWS e em sua aplicações"},},},
          
          "quetao11":{ "pergunta": "(Minha) Exemplos de segurança da internet", 
          "resposta":{
          "a": "plataformas, api, criptografia do tráfego de rede(criptografia, integridade, identidade)", 
          "b": "software, computação, armazenamento, rede, criptografia do lado do servidor(sistema de arquivos ou dados)", 
          "c": "infraestrutura global de hardware/aws e software", 
          "d": "dados do cliente, rede e direwall",
          "e": "todas estão corretas", 
          "solucao":{"c":
          "🤓 - DA nuvem - software, computação, armazenamento, banco de dados, rede, Infraestrutura global de hardware/aws - regiões, zonas de disponibilidade, pontos de presença."},},},

          "quetao12":{ "pergunta": "(Minha) Plataforma, rede e firewall, criptografia de dados no lado do cliente e autentificação da integridade, proteção de rede (criptografia, integridade, identidade), api entre outros, são segurança na internet.", 
          "resposta":{
          "a": "correta", 
          "b": "incorreta",  
          "solucao":{"a":
          "🤓 - NA nuvem - Plataforma, rede e firewall, criptografia de dados no lado do cliente e autentificação da integridade, proteção de rede (criptografia, integridade, identidade), api, criptografia do lado do servidor(sistema de arquivos ou dados), gerenciamento de idantidade e acesso e configuração do sistema operacional."},},},

          "quetao13":{ "pergunta": "(Minha) Sobre Confiabilidade da informação e medição disponibilidade ", 
          "resposta":{
          "a": "confidencialidade - garantia de acesso restrito à informação (excludividade e privacidade)", 
          "b": "integridade - garantia de preservação de estado (autenticidade, não repúdio e auditaabilidade)",
          "c": "disponibilidade - garantia de uso contínuo da informação (pontualidade, continuidade e robustez)",
          "d": "Uptime do servidor - tempo no ar, ativo - seguraça de 9 - quanto maior os 9 menor o tempo de downtime",
          "e": "todas estão corretas",     
          "solucao":{"e":
          "🤓 - Obs uptime - tempo de sistema operando // downtime - tempo de sistema inativo  //  SLA - Service Level Agreement - acordo com previsão de multa, de garantia de tempo de uptime em percentual - ex disponibilidade de 95% - pode ter downtime de 18 dias e 6h (fora do ar), 99,999% este tempo cai para 0 dias e 5h:15nim e 36seg // esta métrica pode ser dividida entre computadores, que unidos tem este total"},},},


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
          De 13 você possui {correta} corretas e precisa revisar {errada}""")
