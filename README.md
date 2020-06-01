# votacionesapiprueba

## Python + Django + Rest Framework

### Methods
- GET
- POST
- PUT 
- DELETE

### Creating and login users

| Entity  |Endpoint  | GET  | POST  | PUT | DELETE  |
| :------------ | :------------ | :------------ | :------------ | :------------ | :------------ |
|  Users | /api/v1/users/signup/  | - | Registra usuarios  Nuevo usuario <br>{"username": "","first_name": "","last_name": "","email": "",  "numero_celular": "","direccion": "","municipio": "","foto": ""}| - | - |  
|   |  /api/v1/rest-auth/login/ |  - |  Login user <br>{'username':'', password:''}  | -  |  - |

*Required authentication
```
headers: {
	'Authorization': 'Token <token-generado-al user>',
	'Content-Type': 'application/json'
}
```
## Funcionalidad disponible
```
Creacion de usuario y generacion de token (solo admin) <br>
Login de usuario lider (solo admin)<br>
Consulta de usuarios (solo admin)<br>
Crud departamentos, municipios, puestos de votaciones (solo admin) <br>
Creacion de datos de votante (usuario lider) <br>

```

## Modelo de base de datos
```
Se uso el modelo de datos proporcionado a excepción de la entidad capitanes

```

## Clone the project
```
git clone <url project>
```
## enter folder
```
cd <project folder>
```

## Run the project

### Install the project
```
pip install pipenv (Si no se encuentra instalado)
pipenv install (para instalar dependencias en archivo Pipfile)
```
### Execute de enviroment
```
pipenv shell
```
luego
```
python manage.py runserver
```
### No hay motor de base de datos. Para este caso se uso el archivo sqlite que provee django
