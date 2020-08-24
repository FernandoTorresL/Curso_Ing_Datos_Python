# Curso de Ingeniería de Datos con Python, Platzi
# Data Engineering with Python, Platzi

## Description
Create a profesional web scraper follow the typical workflow of a Data Engineering

---

## Important
Check first the configuration on config.yaml file. This file defines where are the urls, titles and body from each article and url

Example config.yaml:
```cmd
eluniversal:
    url: https://www.eluniversal.com.mx
    queries:
      homepage_article_links: '.field-content a'
      article_title: '.Encabezado-Articulo h1'
      article_body: '.field-name-body'
```
**homepage_article_links** : Tags containing the urls to the articles

**article_title**: Inside each article, here define the tag for each article title

**article_body**: Inside each article, here define the tag for each article body

---

This project use:
- Python
- Jupyter Notebook

## Installation

### Clone this repo

You can use and change *<my_folder>* on this instruction to create a new folder

```cmd
git clone git@github.com:FernandoTorresL/Curso_Ing_Datos_Python.git <my_folder>
```

### How to test Web Scrapper

```cmd
cd web_scraper_curso_data_eng/final_project_live
python pipeline.py
```

This create an newspaper.db database file

To query:
```cmd
sqlite3
.open newspaper.db
.tables // articles
select * from articles;
```

---

## Test some particular ETL process

### Extract process
```cmd
cmd extract
```

Execute:
```cmd
python main.py <argument>
```
This create an csv file named *[argument]*_[*fecha*]_articles.csv with the data from url configured on **config.yaml**, on this example, "eluniversal2"

```cmd
python main.py eluniversal2
```

### Transform process

```cmd
cmd transform
```

Execute:
```cmd
python main.py <dirty_csv_filename_from_extract_process>
```

Example:
```cmd
python main.py eluniversal_2020_08_22_articles.csv
```

### Load process

```cmd
cmd load
```

Execute:
```cmd
python main.py <clean_csv_filename_from_transform_process>
```

Example:
```cmd
python main.py clean_eluniversal.csv
```

This create a newspaper.db file to read using sqlite

---

## Follow me

### [fertorresmx.dev](https://www.fertorresmx.dev/)

#### :globe_with_meridians: Twitter, Instagram: [@fertorresmx](http://www.twitter/fertorresmx)
