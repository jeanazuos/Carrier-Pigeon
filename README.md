# O que é o script?
Carrier pigeon é um script feito em Python do tipo webcrawler, seu principal objetivo é coletar notícias rss do portal Valor Investe, 
"http://valorinveste.globo.com/rss/valorinveste/ultimas-noticias", ao processar o conteúdo é feito uma limpeza das tags html e no final do processo a persistência em mongoDB.

A ideia principal é que esse script seja parte de um conjunto de microserviços e esse conjunto tenha como objetivo enviar conteúdo (notícias) para redes sociais de forma automatizada, porém, caso ache interesssante alguma funcionalidade, fique à vontade para utiliza-lo como parte de alguma ideia que venha a ter. #tamojunto

# Tecnologias utilizadas
* Docker e Docker Compose;
* Python;
* MongoDB;
* Scrapy (Framework);
* Regex (Expressão regular para limpeza de caracteres).

# Como executar a aplicação?
* Clone o repositório e entre no diretório raiz;
* Execute o comando "docker build . -t basilisco/flask";
* Execute o comando "docker-compose up".

Realizando os três passos acima vamos ter 2 aplicações rodando no Docker, uma sendo a app responsável por realizar o crawler e persistir os dados, a outra o próprio banco mongoDB.
