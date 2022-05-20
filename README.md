# PythonProyectoFinal
Para empezar creamos un entorno virtual:
```py -m venv venv```

y creamos una app media:
```py manage.py startapp media```

Dentro de la app media:es necesario crear una carpeta
avatares y una carpeta blog

Activamos el entorno virtual
```. venv/Scripts/activate```

e instalamos lo que esta en requirements.txt
`pip install -r requirements.txt`

Ademas se debe descargar ckeditor
`pip install django-ckeditor`

O si ya esta instalado quizas se deba actualizar
`pip install django-ckeditor --upgrade`

Para correr el programa
`py manage.py runserver`

# Base de datos
Si se realizan grandes cambios en la base de datos
sera necesario realizar una migration:
`py manage.py makemigrations`
`py manage.py migrate`



# User
Si se desea crear un usuario desde el codigo:
`py manage.py createsuperuser`
y seguir las indicaciones.

# Sobre el programa
El usuario podra buscar su doctor y pedir turno. Ver sus turnos, editarlos y eliminarlos. Tambien podra
bloguear, modificar sus blog o eliminarlos.
La persona que no este logueda solo podra ver los blogs pero no podra editarlos, eliminarlos o agregar uno nuevo.

El usuario tmb puede modificar su avatar o su contraseña o sus datos como nombre y email.

El programa esta dividio en 3 Apps: indice, clase, accounts.
En la app indice observaremos la base del programa. Con sus plantillas iniciales.
En la app clases se podra ver los models Doctor, Turno, Paciente y Blog y en views.py se observaran las distintas funciones que se realizan con los models
En la app accounts tendremos el model Avatar y en views.py las funciones del usuario como login, logout, modificar datos de usuario y registrarse.


# Demostracion:
