## CD-Test-Martin

Este es el código de fuente para la prueba de Coding Dojo. La demo desplegada en EC2 se encuentra aquí: http://3.14.246.206/

## Requerimientos

Python 3.6+ y venv

## Instalación y uso

1. Clonar el repositorio (el mismo ya viene con la base de datos ```db.sqlite3```)

```git clone https://github.com/MartinSchere/CD-Test-Martin.git```

```cd CD-Test-Martin```

2. Crear ambiente virtual y activarlo

```python3 -m venv venv```

```source venv/bin/activate```

3. Instalar requerimientos y colectar archivos estáticos

``` pip install -r requirements.txt ```
``` python manage.py collectstatic --noinput ```

4. Correr servidor

```python manage.py runserver```

## Credenciales de prueba

Username: jackdoe123
Password: codingdojo
