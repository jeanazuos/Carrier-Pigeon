from datetime import datetime
import re

# mock 
item = {'title': '<title xmlns:atom="http://www.w3.org/2005/Atom" xmlns:media="http://search.yahoo.com/mrss/">Dados do 2º trimestre no mundo indicam retomada penosa</title>', 'link': '<link xmlns:atom="http://www.w3.org/2005/Atom" xmlns:media="http://search.yahoo.com/mrss/">https://valorinveste.globo.com/mercados/internacional-e-commodities/noticia/2020/07/31/dados-do-2o-trimestre-no-mundo-indicam-retomada-penosa.ghtml</link>',
        'description': '<description>'
            '<![CDATA[ <img src="https://s2.glbimg.com/uCRciA26JaM4frr5vUnrwu57IHQ=/i.s3.glbimg.com/v1/AUTH_f035dd6fd91c438fa04ab718d608bbaa/internal_photos/bs/2019/U/1/chqx0vTEWD9BBVb1HCrw/natura.jpg" /><br /> ]]>'
            'Para o segundo trimestre, o banco entende que foi um período difícil para a companhia, especialmente para a Avon O banco americano Goldman Sachs elevou o preço-alvo das ações da Natura&Co de R$ 29 para R$ 30,'
            ' mantendo a recomendação de venda dos papéis, que estão sendo negociados hoje na B3 a R$ 46,20, em queda de 0,88%. Para o segundo trimestre, o banco entende que foi um período difícil para a companhia, especialmente para a Avon Brasil e Avon Internacional, que deverão apresentar uma contração de dois dígitos em suas receitas no período. “Prevemos uma retração anual de 15% na Avon Brasil e de 25% na Avon International, '
            'pressionadas pelas restrições de distanciamento social e pelos ataques cibernéticos relatados em 9 de junho, e só foram resolvidos em 26 de junho”, diz o relatório. O Goldman Sachs espera que a Natura Brasil seja uma das divisões com melhor desempenho da Natura&Co em termos de crescimento em moeda local. “No entanto, haverá uma contração superior a 10% no comparativo anual, com a venda eletrônica compensando as perdas do mercado social”, diz. Leia também Sobre os resultados que a Natura&Co deve apresentar no dia 13 de agosto, o banco revisou a estimativa e projeta um crescimento do Ebitda (lucro antes de juros, impostos, depreciações e amortizações) da ordem de 3%, contra uma mediana de 11% de seus concorrentes. O relatório diz que a companhia pode apresentar uma resiliência maior que a esperada na demanda do consumidor final, se o aumento da demanda por produtos de higiene pessoal mais do que compensar a queda em categorias como fragrâncias e maquiagens. O banco diz também que os efeitos cambiais foram favoráveis para a companhia na conversão do dólar para o real e o aumento do comércio eletrônico, que pode gerar uma compensação nas perdas maiores do que as esperadas. Conteúdo originalmente publicado pelo Valor PRO, serviço de notícias em tempo real do Valor Econômico Mais Lidas'
            '</description>',
            '<media:content url="https://s2.glbimg.com/U1y1bq4r5aXyxZoQV3l9gMoNcoc=/i.s3.glbimg.com/v1/AUTH_f035dd6fd91c438fa04ab718d608bbaa/internal_photos/bs/2019/v/M/eSyAZESee2Q7HqSW6Cdw/lojas-americanas.jpg" medium="image"/>'
}

def processing_date():
    now = datetime.now()
    today = now.strftime("%d/%m/%Y %H:%M:%S")
    return today

def tags_remover(content):
    cleaner = re.compile('<.*?>|(&.+;)')
    content = re.sub(cleaner,'',content)
    return content

def cleaner(item):
    try:
        content = {}
        if item.get('title'):
            title = item.get('title')
            content['title'] = tags_remover(title)

        if item.get('link'):
            link = item.get('link')
            content['link'] = tags_remover(link)
        
        if item.get('description'):
            description = item.get('description')
            content['description'] = tags_remover(description)
        
        if item.get('media:content')
            print(item)

        
        content["processing_date"] = processing_date()
        print(content)
        return content
    

    except ValueError:
        #implementar lib de log
        print("Nao foi possivel encontrar a tag title no xml")




cleaner(item)
