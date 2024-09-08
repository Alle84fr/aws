1. MODELO DE RESPONSABILIDADE COMPARTILHADA DA AWS:

a. Projetado para ajudar a reduzir a carga operacional do cliente, para oferecer a flexibilidade e o controle do cliente que permitem a implantação de soluções de clientes na AWS, o cliente permanece responsável por alguns aspectos da segurança geral. A diferenciação de quem é responsável pelo quê normalmente se dá pelas expressões segurança "da" nuveme segurança "na" nuvem.

A AWS opera, gerencia e controla os componentes desde a camada de virtualização de software até a segurança física das instalações em que os serviços operam.É responsável pela proteção da infraestrutura que executa todos os serviços oferecidos na Nuvem. Essa infraestrutura é composta por hardware, software, redes e instalações que executam os Serviços de nuvem AWS.

segurança da nuvem:

AWS opera, gerencia e controla os componentes do sistema operacional host baremetal e da camada de virtualização do hipervisoraté a segurança física das instalações em que os serviços operam.

 é responsável pela infraestrutura física que hospeda seus recursos, incluindo:
 
 •Segurança física de datacenters com acesso controlado e baseado em necessidades; autenticação de dois fatores; revisão e registro em log de acesso; vigilância por vídeo; e desmagnetização e destruição de discos.
 
 •Infraestrutura de hardware,como servidores, dispositivos de armazenamento e outros dispositivos dos quais a AWS depende.
 
 •Infraestrutura de software,que hospeda sistemas operacionais, aplicativos de serviço e software de virtualização.
 
 •Infraestrutura de rede, como roteadores, switches, load balancers, firewalls e cabeamento. Monitora continuamente a rede em limites externos, protege pontos de acesso e oferece infraestrutura redundante com detecção de intrusão.A Amazon fornece vários relatórios de auditores terceirizados que verificaram nossa conformidade com diversos padrões e regulamentos de segurança de computadores
 


b. O cliente é responsável pela criptografia de dados em repouso e em trânsito.Também deve garantir que a rede esteja configurada para segurança e que as credenciais e os loginsde segurança sejam gerenciados de maneira segura. Além disso, o cliente é responsável pela configuração de grupos de segurança e pela configuração do sistema operacional que é executado nas instâncias de computação que ele executa (incluindo atualizações e patches de segurança)

segurança da nuvem:

O cliente é responsável pelo que é implementado com o uso dos serviços da AWS e pelos aplicativos conectados à AWS. As etapas de segurança que você deve seguir dependem dos serviços que você usa e da complexidade do seu sistema.

As responsabilidades do cliente incluem selecionar e proteger qualquer sistema operacional de instância, proteger os aplicativos executados em recursos da AWS, configurações de grupos de segurança, configurações de firewall, configurações de rede e gerenciamento seguro de contas. 

Quando os clientes usam os serviços da AWS, eles mantêm controle total sobre o conteúdo. Os clientes são responsáveis por gerenciar requisitos críticos de segurança de conteúdo, incluindo: 

•Qual conteúdo eles escolhem armazenar na AWS

•Quais serviços da AWS são usados com o conteúdo

•Em qual país esse conteúdo é armazenado

•O formato e a estrutura desse conteúdo e se ele é mascarado, anonimizadoou criptografado

•Quem tem acesso a esse conteúdo e como esses direitos de acesso são oncedidos, gerenciados e revogados


Os clientes mantêm o controle da segurança que escolhem implementar para proteger seus próprios dados, ambiente, aplicativos, configurações do IAM e sistemas operacionais. 

3.

resposta: 

Segurança física de datacenters com acesso controlado e baseado em necessidades; localizados em instalações não identificadas

Plataforma como serviço (PaaS) refere-se a serviços que eliminam a necessidade de o cliente gerenciar a infraestrutura subjacente (hardware, sistemas operacionais etc.)

obs:

cliente - Na nuvem 


° AWS IdentityandAccess Management (IAM)permite controlar o acesso a serviços de computação, armazenamento, banco de dados e aplicativos na Nuvem AWS -  pode ser lidar com autenticação e para especificar e aplicar políticas de autorização para que possa especificar quais usuários podem acessar quais serviços.

O IAM é uma ferramenta que gerencia de maneira centralizada o acesso à execução, configuração, gerenciamento e encerramento de recursos em sua conta da AWS. 

Fornece controle granular sobre o acesso a recursos, incluindo a capacidade de especificar exatamente quais chamadas de API o usuário está autorizado a fazer para cada serviço. Com o IAM, você pode gerenciar quais recursos podem ser acessados por quem e como esses recursos podem ser acessados. Você pode conceder permissões diferentes a pessoas distintas para recursos variados

não achei imagem de maquina da amazon (AMIs) , sei que contém as informações necessárias para iniciar uma ou mais instância./ julgo que é o usuário que cria