1. No modelo de responsabilidade compratilhada, a aAWS é responsável por forncer 

resposta correta:

- Segurança DA nuvem - significa que a AWS, o provedor de serviço da nuvem que garanye

 a segrurança da infraestrutura subjacente 

 obs:

 - Seguranla NA nuvem - medidas e práticas implementadas pelo usuário para proteger os dados, app e interações na nuvem

 os outros não saberia explicar 


 fonte https://www.portalinsights.com.br/perguntas-frequentes/e-seguro-o-armazenamento-em-nuvem

 2. No modelo de responsabilidade compatilhada, são exemplos de " segurança na nuvem"....

 Resposta correta:
 
 - Criptografia de dados ociodos e dados em trânsito

 - Configuração do grupo de segurança

 obs

da nuvem (AWs):

- conformidade com diversos padrões e regulamentos de segurança de computadores

- Segurança física de datacenters

- infraestrutura de dispositivos de armazenamento

- ptoteção da infraestrutura global

na nuvem (Usuário):

- formato e a estrutura desse conteúdo e se ele é mascarado, anonimizadoou criptografado

- Configuração de grupo se segurança

- Criptografia de dados ociosos em trânsito

- qual país o conteúdo é armazenado

3. Qual das seguintes opções é responsável da AWs de acordo con o modelo de responsabilidade compatilhada?

resposta: 

manutenção de hardaware físico

4. Ao criar uma política do AWS Identity and Access Management (IAM), quais são os dois tipos de acesso que podem ser conceddios e um usuário?

resposta: 

acesso programático

console de gerenciamento da AWs

obs:
Uma política do IAM é uma declaração formal de permissões que serão concedidas a uma entidade. As políticas podem ser anexadas a qualquer entidade do IAM. As entidades incluem usuários, grupos, funções ou recursos.

A ordem em que as políticas são avaliadas não tem efeito no resultado da avaliação. Todas as políticas são avaliadas, e o resultado é sempre que a solicitação é permitida ou negada. Quando há um conflito, a política mais restritiva se aplica.

políticas baseadas em identidade :

- pode anexar a uma entidade principal (ou identidade), como um usuário, função ou grupo do IAM

- controlam quais ações essa identidade pode realizar, em quais recursos e em que condições

podem ser categorizadas como:

•Políticas gerenciadas: políticas independentes baseadas em identidade que você pode anexar a vários usuários, grupos e funções em sua conta da AWS

•Políticas em linha: políticas que você cria e gerencia e que são incorporadas diretamente em um único usuário, grupo ou função

políticas baseadas em recursos:

documentos de política JSON que você anexa a um recurso, como um bucketdo S3. Essas políticas controlam quais ações uma entidade principal pode realizar nesse recurso e em que condições.

O elemento NotResourceajuda a garantir que os usuários não possam usar nenhuma outra ação ou recurso do DynamoDBou do S3, exceto os especificados na política, mesmo que as permissões tenham sido concedidas em outra política. Uma instrução de negação explícita tem precedência sobre uma instrução de permissão.

pode usar funções para delegar acesso a usuários, aplicativos ou serviços, Por exemplo

Também pode permitir que um aplicativo móvel use recursos da AWS, mas não incorporar chaves da AWS no aplicativo (quando for difícil alterá-las e quando os usuários poderão extraí-las e usá-las indevidamente). Além disso, às vezes você deseja conceder acesso à AWS a usuários que já têm identidades definidas fora da AWS, como no diretório corporativo. Você também pode conceder acesso à sua conta a terceiros, para que eles possam realizar uma auditoria em seus recursos.

5. O AWs Organizations permite consolidar várias contas da AWs para que você as gerencie de manera centralizada.

resposta - verdade

6. Quais são as melhores práticas para proteger sua conta usando o AWS Identity and Access Managemnte (IAM)?

resposta

gerenciar o acesso ao recurso da AWS

definir direitos de acesso refinados

obs: 

7. Qual das seguintes ações deve ser tomada pelo usuário raiz da conta da AWs

respota:

alterar plano de suport

Somente o usuário raiz da conta pode alterar o plano do AWs Support

As outras tarefas são realizadas com o IAM