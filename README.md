# PythonProyectoFinal
Para empezar creamos un entorno virtual:
py -m venv venv

Activamos el entorno virtual
```. venv/Scripts/activate```

e instalamos lo que esta en requirements.txt
pip install -r requirements.txt

Para correr el programa
py manage.py runserver

# User
Si se desea crear un usuario desde el codigo:
py manage.py createsuperuser
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
