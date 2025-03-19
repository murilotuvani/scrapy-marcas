# Concluir o Crawler

Exercício: Concluir o Crawler:
- Obter todas as marcas de A a Z do site.
- Instalar a biblioteca PyMongo.
- Criar uma base de dados no MongoDB (local ou Atlas - mongodb.com/cloud) - Sugestão: MongoDB Local/Standalone = rodando no seu computador.
- Alimentar uma base de dados própria com as marcas obtidas.

Opção Iniciante.
- Obter todas as marcas de A a Z do site.
- Criar um arquivo CSV com as marcas obtidas automaticamente.

## Referências

https://goalkicker.com/PythonBook/

https://docs.python.org/3/tutorial/index.html

## Ferramentas

Utilizar a bibliotec Scrapy (https://scrapy.org) para baixar as marcas cadastradas no sistema


## MondoDB

Optei por utilizar o MondoDB no Docker na máquina local.

```bash
docker run -d -p 27017:27017 --name mongodb mongo
```

Acessando o MongoDB pelo terminal:

```bash
docker exec -it mongo /bin/bash
mongosh
```

```mongodb
show dbs
use brand_database;
show collections
db.brands.find();
db.brands.find({});
db.brands.find({'Country of Origin': 'Brazil'});
```
