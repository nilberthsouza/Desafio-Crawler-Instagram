# Desafio-Crawler-Intagram
O Gabriel me desafiou a dada uma tag do instagram estrair dos post's descrição e comentarios


### Descrição:
Criação de um crawler em python que coleta dados do instagram (post's e seus respectivos comentarios), dada uma hashtag como parâmentro, e armazena os dados em um banco de dados (preferencialmente mongoDB), o programa deverá ter a opção de pesquisa de dados no banco de dados de uma hashtag especifica.

Dica: Os dados do instagram podem ser retornados em formato json, para isso basta colocar o sufixo ?_a=1 no final da URL.

Exeplo: URL deposts contendo cruzeiro:

https://wwww.instagram.com/explore/tags/cruzeiro/

mesma URL retornando os dados em json:

https://wwww.instagram.com/explore/tags/cruzeiro/?_a=1

Para melhor vizualização dos dados json, há extensões de navegadores que melhoram a visuazação dos dados: exemplo:

```Json Formatter```

Links úteis: 

pythonforbeginners.com/requests/using-requests-in-python 

mongodb.com/blog/post/getting-started-with-python-and-mongodb


