# Tarefa 1: Criar um grupo de segurança para a instância de banco de dados do RDS

Criar um **security group** para permitir que o servidor web acesse a instância de banco de dados do RDS. O grupo de segurança será usado quando você executar a instância de banco de dados.

No Console de Gerenciamento da AWS, na caixa de pesquisa ao lado de  Serviços , pesquise e escolha VPC.

 

No painel de navegação à esquerda, escolha Grupos de segurança.

 

Selecione Criar grupo de segurança e configure:

Nome do grupo de segurança: DB Security Group

Descrição: Permit access from Web Security Group

VPC: Lab VPC

Dica: selecione o X ao lado da VPC que já está selecionada e escolha Lab VPC no menu.

 

No painel Regras de entrada, selecione Adicionar regra.

O grupo de segurança não tem regras. Você adicionará uma regra para permitir acesso pelo Web Security Group (Grupo de segurança da web).

 

Defina as configurações a seguir:

Tipo: MySQL/Aurora (3306)
Origem: coloque o cursor no campo à direita de Personalizar, digite sg e selecione Web Security Group (Grupo de segurança da web).
Isso configura o grupo de segurança do banco de dados para permitir tráfego de entrada na porta 3306 de qualquer instância do EC2 associada ao Web Security Group (Grupo de segurança da web).

 

Escolha Criar grupo de segurança.

Você usará esse grupo de segurança ao iniciar um banco de dados do Amazon RDS neste laboratório.

 

Tarefa 2: Criar um grupo de sub-redes de banco de dados
Nesta tarefa, você criará um grupo de sub-redes de banco de dados que é usado para informar ao RDS quais sub-redes podem ser usadas com o banco de dados. Cada grupo de sub-redes de banco de dados requer sub-redes em pelo menos duas Zonas de Disponibilidade.

No Console de Gerenciamento da AWS, na caixa de pesquisa ao lado de  Serviços , pesquise e escolha RDS.

 

No painel de navegação à esquerda, selecione Grupos de sub-redes.

 Se o painel de navegação não estiver visível, selecione o  ícone de menu no canto superior esquerdo.

 

Escolha Criar grupo de sub-redes de banco de dados e configure:

Nome: DB-Subnet-Group

Descrição: DB Subnet Group

VPC: Lab VPC

 

Role para baixo até a seção Adicionar sub-redes.

 

Expanda a lista de valores em Zonas de Disponibilidade e selecione as duas primeiras zonas: us-east-1a e us-east-1b.

 

Expanda a lista de valores em Sub-redes e selecione as sub-redes associadas aos intervalos de CIDR 10.0.1.0/24 e 10.0.3.0/24.

Essas sub-redes devem agora ser mostradas na tabela Sub-redes selecionadas.

 

Escolha Criar

Você usará esse grupo de sub-redes de banco de dados ao criar o banco de dados na próxima tarefa.

 

Tarefa 3: Criar uma instância de banco de dados do Amazon RDS
Nesta tarefa, você configurará e iniciará uma implantação multi-AZ do Amazon RDS de uma instância de banco de dados do MySQL.

As implantações multi-AZ do Amazon RDS fornecem disponibilidade e durabilidade aprimoradas para instâncias de banco de dados, o que as torna a solução ideal para cargas de trabalho de banco de dados de produção. Quando você provisiona uma instância de banco de dados multi-AZ, o Amazon RDS cria automaticamente uma instância de banco de dados primário e replica sincronicamente os dados para uma instância de espera em uma Zona de Disponibilidade (AZ) diferente.

No painel de navegação à esquerda, escolha Bancos de dados.

 

Selecione Criar banco de dados.

 Se aparecer Switch to the new database creation flow (Alternar para o novo fluxo de criação de banco de dados) na parte superior da tela, selecione essa opção.

 

Selecione  MySQL em Opções do mecanismo.

 

Em Modelos, selecione Dev/teste.

 

Em Disponibilidade e durabilidade, selecione Instância de banco de dados Multi-AZ.

 

Em Configurações, defina:

Identificador de instância de banco de dados: lab-db

Nome do usuário principal: main

Senha principal: lab-password

Confirmar senha: lab-password

 

Em Classe da instância de banco de dados, configure:

Selecione  Classes com capacidade de intermitência (inclui classes t).

Selecione db.t3.micro

 

Em Armazenamento, configure:

Tipo de armazenamento: Uso geral (SSD)

Armazenamento alocado: 20

 

Em Conectividade, configure:

Nuvem privada virtual (VPC): Lab VPC

 

Em Grupos de segurança da VPC existentes, na lista suspensa:

Selecione Grupo de segurança do banco de dados.

Desmarque a seleção padrão.

 

Em Monitoramento:

Desmarque Habilitar monitoramento avançado.

 

Na parte inferior da página, expanda  Configuração adicional e configure:

Nome do banco de dados inicial: lab

Desmarque Habilitar backups automáticos.

 Isso desativará os backups, o que normalmente não é recomendado, mas agilizará a implantação do banco de dados para este laboratório.

Desmarque Habilitar criptografia

 

Selecione Criar banco de dados.

 O seu banco de dados agora será executado.

  Se você receber um erro que menciona “not authorized to perform: iam:CreateRole” (não autorizado a executar: iam:CreateRole), desmarque Habilitar monitoramento avançado na etapa anterior.

 

Escolha lab-db (selecione o próprio link).

 Agora você precisará aguardar aproximadamente 4 minutos para que o banco de dados esteja disponível. O processo de implantação está implantando um banco de dados em duas zonas de disponibilidade diferentes.

  Enquanto aguarda, você pode revisar as Perguntas frequentes sobre o Amazon RDS ou tomar um café.

 

Aguarde até a opção Informações mudar para Modificando ou Disponível.

 

Role para baixo até a seção Conectividade e segurança e copie o campo Endpoint.

 Será semelhante a: lab-db.xxxx.us-east-1.rds.amazonaws.com.

 

Cole o valor de Endpoint em um editor de texto. Você o usará mais tarde no laboratório.

 

Tarefa 4: Interagir com o seu banco de dados
Nesta tarefa, você abrirá um aplicativo web executado em um servidor web criado para você. Você deverá configurá-lo para usar o banco de dados que acabou de criar.

Para descobrir o endereço IP de WebServer, selecione o menu suspenso  Detalhes da AWS acima destas instruções. Copie o valor do endereço IP.

 

Abra uma nova guia do navegador da web, cole o endereço IP de WebServer e pressione Enter.

O aplicativo web será exibido com informações sobre a instância do EC2.

 

Selecione o link do RDS no topo da página.

Agora, você configurará o aplicativo para se conectar ao banco de dados.

 

Defina as configurações a seguir:

Endpoint: cole o endpoint que você copiou em um editor de texto anteriormente
Banco de dados: lab
Nome de usuário: main
Senha: lab-password
Escolha Enviar
Uma mensagem será exibida explicando que o aplicativo está executando um comando para copiar informações para o banco de dados. Após alguns segundos, a aplicação exibirá um Address Book (Catálogo de endereços).

O aplicativo Address Book está usando o banco de dados do RDS para armazenar informações.

 

Teste o aplicativo web adicionando, editando e removendo contatos.

Os dados estão sendo mantidos no banco de dados e são replicados automaticamente para a segunda Zona de Disponibilidade.

 

Envio do trabalho
Para registrar seu progresso, selecione Enviar no topo destas instruções.

 

Quando solicitado, selecione Sim.

Depois de alguns minutos, o painel de notas é exibido e mostra quantos pontos você obteve em cada tarefa. Se os resultados não forem exibidos após alguns minutos, selecione Notas no topo destas instruções.

 Dica: você pode enviar seu trabalho várias vezes. Depois de fazer as alterações, selecione Enviar novamente. Seu último envio é registrado para o laboratório.

 

Para ver o feedback detalhado sobre seu trabalho, selecione Relatório de envio.

 Dica: se você não tiver recebido a pontuação total em alguma verificação, poderá haver detalhes úteis no relatório de envio.

 

Laboratório concluído
Parabéns! Você concluiu o laboratório.

Selecione Encerrar laboratório no topo da página e Sim para confirmar que você deseja encerrar o laboratório.  

Um painel será exibido com a mensagem: "DELETE has been initiated... You may close this message box now." (A EXCLUSÃO foi iniciada. Você pode fechar esta caixa de mensagem agora.)

 

Selecione o X no canto superior direito para fechar o painel.

 

© 2023 Amazon Web Services, Inc. e suas afiliadas. Todos os direitos reservados. Este trabalho não pode ser reproduzido nem redistribuído, parcial ou integralmente, sem a permissão prévia por escrito da Amazon Web Services, Inc. A cópia, empréstimo ou venda para fins comerciais é proibida.

Atribuições
Bootstrap v3.3.5 - http://getbootstrap.com/

A licença do MIT (MIT)

Copyright (c) 2011-2016 Twitter, Inc.

É concedida permissão, gratuitamente, a qualquer pessoa que obtenha uma cópia deste software e dos arquivos de documentação associados (o “Software”), para lidar com o Software sem restrições, incluindo, sem limitação, os direitos de usar, copiar, modificar, mesclar, publicar, distribuir, sublicenciar e/ou vender cópias do Software, além de permitir que as pessoas para as quais o Software é fornecido façam isso, contanto que as seguintes condições sejam atendidas:

O aviso de direitos autorais acima e este aviso de permissão devem ser incluídos em todas as cópias ou partes substanciais do Software.

O SOFTWARE É FORNECIDO “NO ESTADO EM QUE SE ENCONTRA”, SEM GARANTIA DE NENHUM TIPO, EXPRESSA OU IMPLÍCITA, INCLUINDO, ENTRE OUTRAS, GARANTIAS DE COMERCIALIZAÇÃO, ADEQUAÇÃO A UM PROPÓSITO ESPECÍFICO E NÃO VIOLAÇÃO. EM NENHUMA CIRCUNSTÂNCIA, OS AUTORES OU DETENTORES DE DIREITOS AUTORAIS DEVEM SER RESPONSABILIZADOS POR QUALQUER ALEGAÇÃO, DANO OU OUTRA OBRIGAÇÃO, SEJA EM CASO DE AÇÃO CONTRATUAL OU OUTRO ATO ILÍCITO PROVENIENTE DE OU ASSOCIADO AO SOFTWARE, AO USO OU A OUTROS PROCEDIMENTOS NO SOFTWARE.

