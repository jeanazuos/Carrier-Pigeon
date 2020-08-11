# O que é o script?
Carrier pigeon é um script feito em python do tipo webcrawler, seu principal objetivo é coletar notícias rss do portal Valor Investe, 
"http://valorinveste.globo.com/rss/valorinveste/ultimas-noticias", ao processar o conteúdo é feito uma limpeza das tags html e no final do processo a persistência em mongoDB.

A ideia principal é que esse script seja parte de um conjunto de microserviços. Trata-se de uma "POC" que estou construindo para apresentar na companhia onde trabalho, entretanto, fique a vontade para utiliza-lo como parte de alguma ideia que venha a ter. #tamojunto

A intenção é que este microserviço seja a base de conteúdo para que outro serviço consuma e faça o disparo para APIS de redes sociais, isso traria um ganho na forma de entrega do conteúdo de forma automatizada (Twitter por exemplo), ente outras que aceitem integração via API.

# Tecnologias utilizadas
* Python;
* MongoDB;
* Scrapy (Framework);
* Regex (Expressão regular para limpeza de caracteres).
