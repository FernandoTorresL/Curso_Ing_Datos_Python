# Curso de Ingeniería de Datos con Python, Platzi
# Carpeta web_scrapper_curso_data_eng

## Description
Crear un Web Scrapper profesional siguiendo el flujo de trabajo de un Ingeniero de Datos

---

## Importante
Revisar la configuración de config.yaml para que funcione correctamente. Si los sitios configurados aquí han cambiado su estructura de html, podría no funcionar o dar resultados inesperados

Extracto de config.yaml:
```cmd
eluniversal:
    url: https://www.eluniversal.com.mx
    queries:
      homepage_article_links: '.field-content a'
      article_title: '.Encabezado-Articulo h1'
      article_body: '.field-name-body'
```
**homepage_article_links** : Tags que contienen los artículos para revisarlos a detalle después.

**article_title**: Tags dentro de cada artículo en particular que tiene el título.

**article_body**: Tags dentro de cada artículo en particular que tiene el cuerpo de la noticia.

---

Éste proyecto utiliza:

- Python
- Jupyter Notebook

## Installation

### Clone this repo

You can use and change *<my_folder>* on this instruction to create a new folder

```cmd
git clone git@github.com:FernandoTorresL/Curso_Ing_Datos_Python.git <my_folder>
```

### Change to working directory

```terminal
cd final_project_live
```

---
## Branch using_databases
```cmd
git checkout using_databases
```

### How to test Web Scrapper

Utilizar algún argumento configurado en **config.yaml**
Ejemplo: eluniversal, elpais

```cmd
cd final_project_live
python pipeline.py
```

Esto generará un archivo newspaper.db de sqlite

Para consultar la base de datos:

```cmd
sqlite3
.open newspaper.db
.tables // articles
select * from articles;
```

---

## Follow me

### [fertorresmx.dev](https://www.fertorresmx.dev/)

#### :globe_with_meridians: Twitter, Instagram: [@fertorresmx](http://www.twitter/fertorresmx)
