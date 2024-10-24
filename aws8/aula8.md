Armazenamento 

1. vai cair na prova

diferença entre armazenamento na nuvem

a. BS - blocos - disco mais usado em note, c: de uma máquina
se tem um arquivo grande,e altera um pedaço, qunado é armazenado, altera apenas a parte modedificada, checkpoint do git(que guarda)
econômico e rápido
altíssima performance
Iops - input output per second 
aguentar múltiplas operações

elastic store tem - 

gp2 - família de armazenamento padrão

gp3 - família de armazenamento padrã - esta é mais recente, resolveu problemas da GP2, mas trouxe outros

provisionado - ter auto custo para ter maior performance - nível de excelência alto
tem sub categorarias e usa o IOPS

hdd -  maquinético, menor custo, menor performance - mas ainda tem de ter disco que trabalhe em bloco
que são discos provisonados

capacidade.........|</br>
 2000gb         ...............|</br>
...............................|</br>
...............................|</br>
100gb...................|</br>
armazenamento._____________  6000iops

limite de dados que serão levado - throughput - dados movendo por segundo

gp2 -  ele é alto, o throughput
.......................300iops.........

1 tb (terabye) += 100 dolares por mês gp2
no gp3 é que o valo cai para 80 - throughput 125Mbs

elastic bloc store quer maior performace e tem alto custo

inclui leitura e incrita

coloca as máquinas que tem

A AWs dá um disco, se quiser mais, pode pedir mais um só que o segundo vc que cuida, em relação a segurança

&nbsp;

b. S3 - simples -  de objetos

ex: google drive

faz controle de versão, mas ele altera todo o arquivo

Disco oferecido como plataformaa, a AWs cuida por tudo que está por trás do armazenamento

Aquela pasta terá o arquivo quando precisa

tem baixo custo, 

ele vira um caminho, um atalho, uma pasta oline, que pode ter acesso restrito porém pode ser público , tipo https:/

comum usar quando usa codigo fonte, textos e imagens web

acesso de leitura  é muito rápido

são casos de conteúdos que possui poucas alterações

A própria AWs que garante a segurança

&nbsp;

1. 1. Bucket

Bugt (ver se é este o nome)

ele tem várias cópias de arquivos, e pode ter a cópia em vários buguetes

a. cai na prova - drive caminho de chegar em uma conta - no AWS o nome do caminho é Bucket - endereço
SÃO ÚNICOS NO MUNDO (QUESTÃO 13) - APENAS nós temos o nosso

para acessar http://s3. código da região.site . bucket-name
para acessar https:// nome-bucket.s3.(voltarvaqui)

...

b. prova - o s3 é o standart - preço padrão para armazenar de forma padrão

para abaixar o preço, pode ir para locar mais baixo - ex: Standard - Infrequent Acess - aqui tem pouco acesso (30dias sem uso) não precisa de alta frequância - usa-se para backup 
tem limitação de acesso

política de vida

duas leituras no ano - bem mais barato - S3 Glacier - se 60 dias sem uso - seria o arquivo morto. 

política de contenção de backup (voltar aqui) - capitação, onde gera dados - vai para standard - aí entra o ciclo de vida
30dias sem usar Infrequent access, 365 dias glader, depois analisa e deleta, se precisar.
...

Elastic file System -  ele é para Linux - sistema de armazenamento - não é um diasco -  pode montar em multiplas máquinas, como que fosse disco compartilhado

...................

Snaphots - imagens de disco e é uma forma de recuperar a qualquer momento

sistema operacional - imagem de disco