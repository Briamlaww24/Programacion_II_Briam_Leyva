# Python · Django · Odoo

Repositorio para proyectos, subproyectos y componentes desarrollados con **Python**, **Django** y **Odoo**.

## Estructura

```
.
├── python/
│   └── proyectos-python/
│
├── django/
│   └── proyectos-django/
│
├── odoo/
│   └── custom_addons/
│
├── .gitignore
└── README.md
```

## Tecnologías

- Python
- Django
- Odoo
- PostgreSQL
- Git
- Docker

## Python

Los proyectos Python pueden incluir:

```
python/
└── proyecto/
    ├── src/
    ├── tests/
    ├── requirements.txt
    ├── pyproject.toml
    └── README.md
```

## Django

Los proyectos Django pueden incluir:

```
django/
└── proyecto/
    ├── manage.py
    ├── config/
    ├── apps/
    ├── templates/
    ├── static/
    ├── media/
    ├── tests/
    ├── requirements.txt
    └── README.md
```

Las migraciones de Django deben mantenerse en el repositorio:

```
app/
└── migrations/
    ├── __init__.py
    └── 0001_initial.py
```

## Odoo

Los módulos personalizados de Odoo se organizan dentro de `custom_addons`:

```
odoo/
└── custom_addons/
    └── mi_modulo/
        ├── __init__.py
        ├── __manifest__.py
        ├── models/
        ├── views/
        ├── security/
        ├── data/
        ├── wizard/
        ├── reports/
        ├── static/
        └── tests/
```

### Estructura básica de un módulo

```
mi_modulo/
├── __init__.py
├── __manifest__.py
├── models/
│   ├── __init__.py
│   └── modelo.py
├── views/
│   └── modelo_views.xml
├── security/
│   ├── ir.model.access.csv
│   └── security.xml
└── data/
    └── data.xml
```

## Entornos virtuales

Se recomienda utilizar un entorno virtual independiente para cada proyecto Python o Django.

```
python -m venv .venv
```

Activación en Linux/macOS:

```
source .venv/bin/activate
```

Activación en Windows:

```
.venv\Scripts\Activate.ps1
```

Instalación de dependencias:

```
pip install -r requirements.txt
```

## Django

Crear un nuevo proyecto:

```
django-admin startproject config .
```

Crear una aplicación:

```
python manage.py startapp app
```

Ejecutar migraciones:

```
python manage.py migrate
```

Iniciar el servidor:

```
python manage.py runserver
```

Ejecutar pruebas:

```
python manage.py test
```

## Odoo

Ejemplo para iniciar Odoo utilizando una configuración local:

```
python odoo-bin -c odoo.conf
```

Actualizar un módulo:

```
python odoo-bin -c odoo.conf -d nombre_base -u mi_modulo
```

Instalar un módulo:

```
python odoo-bin -c odoo.conf -d nombre_base -i mi_modulo
```

## Dependencias

Los archivos de dependencias deben mantenerse versionados cuando formen parte del proyecto:

```
requirements.txt
requirements-dev.txt
pyproject.toml
poetry.lock
Pipfile
Pipfile.lock
```

No se deben versionar los entornos virtuales:

```
.venv/
venv/
env/
```

## Variables de entorno

Las credenciales y configuraciones sensibles deben almacenarse mediante variables de entorno.

Ejemplo:

```
.env
```

El archivo `.env` no debe subirse al repositorio.

En su lugar, utilizar:

```
.env.example
```

Ejemplo:

```
DEBUG=False
SECRET_KEY=
DATABASE_URL=
DB_HOST=
DB_PORT=
DB_NAME=
DB_USER=
DB_PASSWORD=
```

## Archivos que no deben versionarse

No deben incluirse en Git:

- Entornos virtuales.
- Cachés de Python.
- Archivos `.pyc`.
- Bases de datos locales.
- Logs.
- Archivos `.env`.
- Credenciales.
- Claves privadas.
- Filestore de Odoo.
- Archivos generados.
- Directorios de IDE.
- Dependencias descargadas como `node_modules`.

Consultar `.gitignore` para la lista completa.

## Git

Clonar el repositorio:

```
git clone <URL_DEL_REPOSITORIO>
cd <NOMBRE_DEL_REPOSITORIO>
```

Crear una rama:

```
git checkout -b feature/nombre-de-la-funcionalidad
```

Verificar cambios:

```
git status
```

Agregar cambios:

```
git add .
```

Crear un commit:

```
git commit -m "feat: descripción del cambio"
```

Actualizar la rama:

```
git pull
```

Enviar cambios:

```
git push origin feature/nombre-de-la-funcionalidad
```

## Convención de commits

Se recomienda utilizar Conventional Commits:

```
feat: nueva funcionalidad
fix: corrección de error
refactor: refactorización
docs: documentación
test: pruebas
chore: mantenimiento
perf: mejora de rendimiento
style: cambios de formato
build: cambios de compilación
ci: cambios de integración continua
```

Ejemplos:

```
git commit -m "feat: agregar módulo de facturación"
git commit -m "fix: corregir validación de usuario"
git commit -m "docs: actualizar documentación de instalación"
git commit -m "refactor: reorganizar servicios de clientes"
```

## Desarrollo

Antes de realizar cambios:

```
git pull
```

Crear una rama específica:

```
git checkout -b feature/nueva-funcionalidad
```

Realizar los cambios y ejecutar las pruebas correspondientes.

Antes de subir los cambios:

```
git status
git diff
```

Ejecutar las pruebas:

```
pytest
```

Para Django:

```
python manage.py test
```

Después crear el commit:

```
git add .
git commit -m "feat: descripción del cambio"
git push origin feature/nueva-funcionalidad
```

## Licencia

Definir la licencia correspondiente al proyecto antes de realizar una distribución pública.