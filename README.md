# loginpage

Este proyecto consiste en el desarrollo de un blog con CRUD de publicaciones, login y registro de usuarios, desarrollado en Django.
Las dependencias requeridas son Django, Bootstrap 5 y Pillow.

## Instalacion de dependencias:

pip install -r requirements.txt

## Iniciar aplicacion:

Deben correrse los siguientes comandos en la consola:

python manage.py migrate (para mapear los modelos a la base de datos)

python manage.py runserver (para correr el servidor)

## El proyecto cuenta con:

### Barra de navegacion (navbar):

Una barra de navegacion que cuenta con una barra de busqueda para encontrar blogs que los usuarios han ingresado y permite navegar entre distintas secciones dentro de la pagina, entre ellas el login, about, edit profile y el boton de home para regresar a la pagina principal.

### Boton de search:

En el navbar esta la herramienta de busqueda para localizar entradas que han añadido los usuarios registrados y logeados.

### Añadir blog (add blog):

El boton de add blog permite al usuario ingresado añadir entradas sobre actividades que va a realizar, es decir una "To Do List".

Estos blogs pueden ser editados, vistos en detalle, o borrados si el usuario ya completo la tarea especificada en el blog.

### Login y Register:

Si la persona ingresando a la pagina ya cuenta con usuario, puede logearse usando su usuario y contraseña registrados, si no, puede dar click al boton de Register para crear su nuevo usuario y tener su propio portal en la pagina.

### Edit profile (editar perfil):

El usuario que este logeado puede editar sus datos y modificarlos si desea hacer algun cambio, y tambien puede cambiar su contraseña vieja por una mas actualizada si asi lo quiere.