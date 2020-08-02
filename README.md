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

### ativando ambiente virtual no Windows com CMD

```sh
myvenv\Scripts\activate
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
cd hackgif-api
pip install -r requirements.txt
```

### fazendo migrations

```sh
python manage.py migrate
```

### criando superuser (no windows abra o terminal como administrador)

```sh
python manage.py createsuperuser
```

### rodar em localhost

```sh
python manage.py runserver
```

### base_url

rodando localmente
`base_url` => `localhost:8000`

### rotas django admin

CRUD `{base_url}/admin`

### rotas da api

listagem `{base_url}/api/hacker-gifs` verbo `GET`

detalhar `{base_url}/api/hacker-gifs/{idDoGif}` verbo `GET`

criar `{base_url}/api/hacker-gifs/` verbo `POST` params `{ gif_url: string, votes: int }`

editar `{base_url}/api/hacker-gifs/{idDoGif}` verbo `PUT` params `{ gif_url: string, votes: int }`

deletar `{base_url}/api/hacker-gifs/{idDoGif}` verbo `DELETE`
