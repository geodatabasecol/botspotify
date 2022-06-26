## 1.0.1
# PROYECT BOTSPOTIFY
# RUTA DE DESARROLLO

## MODULO DE NEVER INSTALL
* Automatizar el loging a 10 cuentas DE NeverInstall 
* Automatizar el lanzamiento de VisialStudio Code, (1 cada hora, intercambiando el origen del servidor)
* Automatizar la instalacion de paquetes requeridos y verificar que es ok
* Automatizar para que no se cierre la ventana por falta de uso
* Automatizar el lanzamiento del modulo requerido:
  - Creación de cuentas
  - Creacion de lista de reproducción
  - Reproducción de canciones

## MODULO CREACION DE CUENTAS
* Obtener de la bd usuario email contraseña
* actualizar el campo de estado de la ac a 2
  - 0 no creado
  - 1 creado finalizado
  - 2 en creacion
* actualizar el registro de la bd el estado de   la acc a 1
### MODULO REIMTENTAR CREACION DE ACC  NO FINALIZADAS
* Verificar accounts con estado 2 y reintentar crearlas

## MODULO CREACION DE LISTAS DE REPRODUCCIÓN
* Obtener de la bd las account que no ha creado lista de reproduccion
* mientras el proceso se realiza actualizar el campo de estadocreacionlistareprod a 2:
  - 0 no creado
  - 1 creado finalizado
  - 2 en creacion
* si el proceso finaliza correctamente actualizar el estadocreacionlistareprod a 1
### MODULO DE BORRADO LISTAS DE REPRODUCCION NO COMPLETAS
  * Obtener de la bd las accouns en estado 2
  * ingresar y eliminar la lista de reproduccion 
  * actualizar el estado de la lista de reproduccion a 0

## MODULO DE REPRODUCCIÓN

* Reglas: cada account debe reproducirse 15 veces en el mes (pendiente logica)
* Obtener de la BD las account con estadocreacionlistareprod 1 
* Reproducir todas las listas de creadas 
* guardar en bd en : 
   - estadocreacionlistareprod - int
   - registrodeconeccionesfinalizadas[fecha - duracion - finalizadaok]

## BASE DE DATOS MONGODEDB
Schema:
{
estadocreacionacc - int
user - string,
email -string,
pass - string
estadoejecucion - int
estadocreacionlistareprod - int
cantidaddereproducciones - int
reportedeerror - string
registrodeconeccionesfinalizadas[fecha - duracion - finalizadaok]
}


