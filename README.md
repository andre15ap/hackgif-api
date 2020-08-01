## HackGif Api

Este projeto consiste em fornocer uma api para listagem dos melhores Gifs de hackes da internet, podendo realizar o CRUD dos gifs, para isto foi utilizado as tecnologias Python, Django e Django-Rest-Framework, como banco foi utilizado o sqlit3.

### Instalação

Necessário [Python](https://www.python.org/) v3+ para rodar.

### criando ambiente virtual

```sh
python -m venv myvenv
```

### ativando ambiente virtual no Windows com git bash

```sh
source myvenv/Scripts/activate
```

### ativando ambiente virtual no linux

```sh
source myvenv/bin/activate
```

### atualizando pip

```sh
python -m pip install --upgrade pip
```

### instalando dependencias

```sh
cd hackgifs-api
pip install -r requeriments.txt
```

### fazendo migrations

```sh
python manage.py migrations
```

### criando superuser

```sh
python manage.py createsuperuser
```

### rodar em localhost

```sh
python manage.py runserver
```

### rotas em localhost

DJANGO ADMIN

CRUD `localhost:8000/admin`

DJANGO REST-FRAMEWORK

listagem `localhost:8000/api/gifs` verbo `GET`

detalhar `localhost:8000/api/gifs/{idDoGif}` verbo `GET`

criar `localhost:8000/api/gifs/` verbo `POST` params `{ gif_url: string, votes: int }`

editar `localhost:8000/api/gifs/{idDoGif}` verbo `PUT` params `{ gif_url: string, votes: int }`

deletar `localhost:8000/api/gifs/{idDoGif}` verbo `DELETE`
