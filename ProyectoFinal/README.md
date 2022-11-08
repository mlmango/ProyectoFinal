
## Autores

* **Mariana Truelsegaard** - [mtruelse](https://github.com/mtruelse)
* **María Lucila Mango** - [mlmango](https://github.com/mlmango)

## Proyecto Final

_Web estilo blog en python utilizando el framework Django, con opciones de crear autor y artículos para el mismo, como así también la creación de usuarios (indispensable para poder acceder a todo el contenido)._

_El sitio solicita registrarse como usuario y loguearse para poder navegar por el blog. El usuario a su vez, cuando ya se encuentre registrado, puede editar su perfil y cargar un avatar. El desarrollo del proceso de registro, edición de perfil, carga de avatar y login/logout fue realizado por Maria Lucila (incluyendo modelado, vistas y templates) con soporte de Mariana en corrección de bugs y pruebas._ 

_Una vez que el usuario se encuentre registrado, podrá navegar por el sitio, permitiendo dar de alta artículos y autores, buscar artículos creados por el título o bien ver el listado completo de los artículos creados. Además, el usuario podrá editar los artículos que considere y eliminarlos si fuera necesario. Para crear un nuevo autor, se debe completar el nombre, el username y el email. Para dar de alta un articulo nuevo, deberá agregar un título, un subtítulo, el cuerpo o texto, una imagen relacionada, el username del autor y la fecha de publicación. El modelado de los articulos y autores fue desarrollado por Maria Lucila. Por su parte las vistas y templates fueron desarrolladas por Mariana. El buscador de artículos y el crud que permite crear articulos/autores, leer los artículos, editarlos y elimitarlos fue desarrollado por Mariana con la ayuda de Maria Lucila en mejoras y corrección de bugs._

_Además, se desarrolló un app adicional que permite guardar un mensaje a un determinado destinatario que será otro usuario del sitio. Esta app solo es manipulable desde el administrador, permitiendo allí agregar el mensaje y el destinatario. Esta app de mensajería fue desarrollada por Mariana con soporte de Maria Lucila en mejoras y seguimiento._

_El trabajo en equipo fue clave para ir puliendo el código, mejorando el sitio y corrigiendo errores._

## Pre-requisitos 📋 y Primeros pasos 🚀

_Para poder poner en funcionamiento el proyecto es imprescindible tener instalados de manera local Python, Git y Django._

_De esta forma, primero se debe clonar el repositorio a la maquina local. Luego, se debe correr el servidor y pegar la URL en el browser. Desde esta URL se podrá acceder a la pantalla de inicio y desde allí se podrá acceder a los diferentes links para navegar por el sitio*_ 

_*Recordar solo un usuario registrado y logueado podrá navegar por la página._

## Ejecutando las pruebas ⚙️

_Los casos de prueba se diseñaron para ejecutarse desde el archivo tests.py - tal cual se observó en clase - y permiten verificar el correcto funcionamiento al crear según el objeto Artículos. Uno de las pruebas consiste en crear un Artículo, una de ellas implica crear varios, y otra crear uno sin el atributo 'fecha'. También se creó un test el cual permite crear un objecto según el formato de Autores._

_Para correr los casos de prueba, es necesario hacer uso del comando # python manage.py test #._

## Video Tutorial del Sitio

https://www.youtube.com/watch?v=7FXsWZrvxSU 

